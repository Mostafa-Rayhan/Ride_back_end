
mapboxgl.accessToken =
  "pk.eyJ1IjoicmF5aGFuNTciLCJhIjoiY2tyMTc2bDhyMXpleDJ2dDk5cjlkdWwzNyJ9.wdlQcx9--Q-Mldi_9mPj1g"

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
  enableHighAccuracy: true
})

function successLocation(position) {
  setupMap([position.coords.longitude, position.coords.latitude])
}

function errorLocation() { 
  setupMap([23.777176, 90.399452])
}

function setupMap(center) {
  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: center,
    zoom: 15
  })

  const nav = new mapboxgl.NavigationControl()
  map.addControl(nav)

  var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken
  })

  map.addControl(directions, "top-left")

  map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    trackUserLocation: true,
    showUserHeading: true
  }));
  const addMarker = () => {
    const marker = new mapboxgl.Marker()
      marker.setLngLat([23.746466, 90.376015])
      marker.addTo(map);
  }
  map.on("load", addMarker)

  // // Set marker options.
  // const marker = new mapboxgl.Marker({
  //     color: "#ffffff",
  //     draggable: true
  // }).setLngLat([23.746466, 90.376015])
  //     .addTo(map);


  //
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
  // popup.setLngLat(e.lngLat)
  // popup.setHTML("<h1>Hello World!</h1>")
  // popup.setMaxWidth("300px")
  // popup.addTo(map);
}