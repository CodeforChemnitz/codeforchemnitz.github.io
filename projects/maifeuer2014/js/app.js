var map = L.map('map').fitBounds([[50.77525, 12.82581], [50.87391, 13.01717]]);

L.tileLayer('http://tiles.lyrk.org/ls/{z}/{x}/{y}?apikey=94931f083ee84f43b37e6d230515ab80', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Tiles by <a href="http://lyrk.de/">Lyrk</a>',
	id: 'examples.map-20v6611k'
}).addTo(map);

var fireIcon = L.icon({
	iconUrl: 'img/a.png',
	iconSize: [30, 70],
	iconAnchor: [15, 35],
	popupAnchor: [0, -35]
});


L.geoJson(fireplaces, {

	pointToLayer: function (feature, latlng) {
		return L.marker(latlng, {icon: fireIcon});
	},

	onEachFeature: function (feature, layer) {
		var popupContent = '<dl>';

		popupContent += '<dt>Ort</dt>';
		popupContent += '<dd>'+ feature.properties['Ort'] + '</dd>';
		popupContent += '<dt>Zeit</dt>';
		popupContent += '<dd>'+ feature.properties['Zeit'] + '</dd>';

		popupContent += '</dl>'

		layer.bindPopup(popupContent);
	}
}).addTo(map);
