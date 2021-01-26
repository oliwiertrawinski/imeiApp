var tileLayer = new L.TileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',{
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
});

var map = new L.Map('map', {
  'center': [51.441767, 5.480247],
  'zoom': 12,
  'layers': [tileLayer]
});

var marker = L.marker([51.441767, 5.470247],{
  draggable: true
}).addTo(map);

marker.on('dragend', function (e) {
  document.getElementById('latitude').value = marker.getLatLng().lat;
  document.getElementById('longitude').value = marker.getLatLng().lng;
});