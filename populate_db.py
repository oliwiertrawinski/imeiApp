import os
import logging
import csv
import json
import random
import pandas as pd
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ImeiChecker.settings')

import django

django.setup()
logging.basicConfig(level=logging.INFO)
fakegen = Faker()

from imeiApp.models import Imei_numbers, Phone_brands, User

from collections import OrderedDict

PATH_TO_SAMPLE_DATA = "utils/sample_data/"

MODEL_OBJECT_MAPPINGS = {
    "PHONE_BRANDS": Phone_brands,
    "IMEI_NUMBERS": Imei_numbers
}


def get_foreign_key_obj(kwargs):
    result = {}
    for key, value in kwargs.items():
        key: str
        if key.startswith("FK-"):
            _, table_name, column_name = key.split("-")
            table_object = MODEL_OBJECT_MAPPINGS[table_name]
            if len(value) > 0:
                fk_obj = table_object.objects.get(objectId=value)
                result[column_name] = fk_obj

        else:
            result[key] = value

    return result


def populate_users(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        # Create Fake mymap for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_password = fake_first_name + '1'
        # Create new User Entry
        user = User.objects.get_or_create(username=fake_first_name + '_' + fake_last_name,
                                          email=fake_email)[0]
        user.set_password(fake_password)
        user.save()


def create_superuser():
    username = 'testadmin'
    password = 'a1d2m3i4n5'
    email = 'admin@admin.com'
    user = User.objects.get_or_create(username=username,email=email, is_superuser=True,is_active=True,is_staff=True)[0]
    user.set_password(password)
    user.save()

def fill_db(path_to_sample_data=PATH_TO_SAMPLE_DATA):
    for file_name in os.listdir(path_to_sample_data):

        file_path = os.path.join(path_to_sample_data, file_name)
        table_name = file_name.split("-")[1].replace('.json', '')

        table_object = MODEL_OBJECT_MAPPINGS[table_name]
        table_data: pd.DataFrame = pd.read_json(file_path)

        columns = table_data.columns

        for _, row in table_data.iterrows():
            kwargs = dict(zip(columns, row))
            kwargs = get_foreign_key_obj(kwargs)
            table_object.objects.get_or_create(**kwargs)


# removeKeys()
# createImeiJsonFile(100)

# createImeiJsonFile(100)

if __name__ == '__main__':
    # uruchom 5 ponizsze linijki
    logging.info("Populating the databases...Please Wait")
    fill_db()
    create_superuser()
    populate_users(5)
    logging.info('Populating Complete')

    # removeKeys()
    # createImeiJsonFile(200 )
