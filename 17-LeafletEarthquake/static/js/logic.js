var earthquakeURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";


d3.json(earthquakeURL,function (data){
	createFeatures(data.features);
});

function createFeatures(earthquakeData) {
	var earthquakes = L.geoJSON(earthquakeData,{
		onEachFeature: function(feature,layer){
			layer.bindPopup(`<h3>Magnitude:${feature.properties.mag}</h3>\
				<h3>Location:${feature.properties.place}</h3>\
				<hr><p>${new Date(feature.properties.time)}</p>`);
		},
		pointToLayer:function(feature,latlng){
			return new L.circle(latlng,{
				radius: getRadius(feature.properties.mag),
				fillColor: getColor(feature.properties.mag),
				fillOpacity:.9,
				stroke:false,
			})
		}
	});

	createMap(earthquakes);
}

function createMap(earthquakes) {
    var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

var dark = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
});

var street = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
});


var baseMaps = {
  Light: light,
  Dark: dark,
  Street: street
};

    

    var overlayMaps ={
    	"Earthquakes": earthquakes,
    	
    };

  	var myMap = L.map("map", {
  		center: [37.09, -95.71],
  		zoom: 2.5,
  		layers: [street, earthquakes]
  	});
    

  	

  	L.control.layers(baseMaps, overlayMaps, {
       
      }).addTo(myMap);




var legend = L.control({position: 'bottomright'});

legend.onAdd = function (myMap) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0,2,3,4,5,6]
        labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(myMap);
}


function getColor(d){
  return d > 6 ? "#ff0000":
  d  > 5 ? "#ff6600":
  d > 4 ? "#ffa500":
  d > 3 ? "#ffb37e":
  d > 2 ? "#ffff66":
           "#90ee90";
}

function getRadius(value){
  return value*25000
};