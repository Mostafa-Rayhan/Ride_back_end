// function initMap() {
//         	var location = {lat: 23.777176, lng: 90.399452
//         	};
//         	var map = new google.maps.Map(document.getElementById("map"), {
//         		zoom: 4,
//         		Center: location
//         	});
        
        	
//                 var marker = new google.maps.Marker({
// 			position: location,
// 			map: map,
// 			});
// 		};


function initMap() {
	var options = {
		zoom: 4,
		lat: 23.777176, lng: 90.399452
	}

	var map = new 
	google.maps.Map(document.getElementById("map"), options);


        
	var marker = new google.maps.Marker({
		position: {lat: 23.746466,lng: 90.376015},
		map: map,
		});

		var infoWindow = new google.maps.infoWindow({
			content: '<h1>Dhanmondi</h1>'
		});
	}

	// var marker = new mapboxgl.Marker()
	// 	.setLngLat([23.746466, 90.376015])
	// 	.addTo(map);

	// const addMarker = () => {
    // const marker = new mapboxgl.Marker()
    //   marker.setLngLat([23.746466, 90.376015])
    //   marker.addTo(map);
	// }
	// map.on("load", addMarker)

  // // Set marker options.
  // const marker = new mapboxgl.Marker({
  //     color: "#ffffff",
  //     draggable: true
  // }).setLngLat([23.746466, 90.376015])
  //     .addTo(map);



  // const markerHeight = 50;
  // const markerRadius = 10;
  // const linearOffset = 25;
  // const popupOffsets = {
  // 'top': [0, 0],
  // 'top-left': [0, 0],
  // 'top-right': [0, 0],
  // 'bottom': [0, -markerHeight],
  // 'bottom-left': [linearOffset, (markerHeight - markerRadius + linearOffset) * -1],
  // 'bottom-right': [-linearOffset, (markerHeight - markerRadius + linearOffset) * -1],
  // 'left': [markerRadius, (markerHeight - markerRadius) * -1],
  // 'right': [-markerRadius, (markerHeight - markerRadius) * -1]
  // };
  // const popup = new mapboxgl.Popup({offset: popupOffsets, className: 'my-class'})
  // .setLngLat(e.lngLat)
  // .setHTML("<h1>Hello World!</h1>")
  // .setMaxWidth("300px")
  // .addTo(map);
}