from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.gis.geos import Point
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import  CreateUserForm
from .models import Imei_numbers, Phone_brands, Stolen_markers

import json
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required


from django.contrib.gis.db.models import PointField
from django.contrib.auth import get_user_model
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('imeiApp:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('imeiApp:login')

        context = {'form': form}
        return render(request, 'imeiApp/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('imeiApp:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('imeiApp:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'imeiApp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('imeiApp:home')

def home(request):
    return render(request, 'imeiApp/home.html')


def check_imei(request):
    #GETTING ALL USERS
    # User = get_user_model()
    # users = User.objects.all()
    # print(users)
    if request.method == 'POST':
        nr_imei = request.POST['imei']
        phone=None
        try:
            phone = Imei_numbers.objects.all().get(ImeiNumber=nr_imei).IdPhoneModel
        except Imei_numbers.DoesNotExist:
            print('Telefon o podanym nr imei nie istnieje')

        if phone is None:
            messages.success(request, 'There is no phone with this IMEI number')
            return HttpResponseRedirect(request.path_info)

        if  len(Stolen_markers.objects.filter(imei__ImeiNumber=nr_imei)) !=0:
            messages.success(request, 'This phone has been stolen!')


        return redirect('imeiApp:phone_details', model_id=phone.id )



    return render(request, 'imeiApp/check_imei.html')


def phone_details(request, model_id):
    phone = Phone_brands.objects.all().get(id=model_id)
    fields = phone._meta.get_fields()
    tuple_list = []

    for i in range(3, 30):
        field_name = fields[i].name
        field_content = getattr(phone, field_name)
        tuple_list.append((field_name, field_content))
    context = {'fields_tuple_list': tuple_list}
    return render(request, 'imeiApp/phone_details.html', context)


def phone_base(request):
    phones = Phone_brands.objects.all()

    context = {'phones':phones}

    return render(request, 'imeiApp/phone_base.html', context)



class MapStolenPhones(TemplateView):
    """Markers map view."""

    template_name = "imeiApp/map.html"

    def get_context_data(self, *args, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Stolen_markers.objects.all()))
        return context

@login_required
def report_stolen_phone(request):
    username = request.user.username
    if request.method == 'POST':
        nr_imei = request.POST['imei']
        phone = None
        try:
            phone = Imei_numbers.objects.all().get(ImeiNumber=nr_imei)
        except Imei_numbers.DoesNotExist:
            print('Telefon o podanym nr imei nie istnieje')

        if phone is None:
            messages.success(request, 'There is no phone with this IMEI number')
            return HttpResponseRedirect(request.path_info)
        if len(Stolen_markers.objects.filter(imei__ImeiNumber=nr_imei)) !=0:
            messages.success(request, 'Phone with this imei number has been already marked as stolen')
            return HttpResponseRedirect(request.path_info)
        try:
            latitude = float(request.POST.get('latitude', None))
            longitude = float(request.POST.get('longitude', None))
            location = Point(longitude, latitude)
        except:
            messages.success(request, 'Move marker to choose localisation on the map')
            return HttpResponseRedirect(request.path_info)

        Users = get_user_model()
        user = Users.objects.get(username=username)

        marker = Stolen_markers.objects.create(owner=user, imei=phone, location=location)
        marker.save()
        messages.success(request, 'Stolen phone has been reported')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'imeiApp/get_marker.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('imeiApp:home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'imeiApp/change_password.html', {
        'form': form
    })