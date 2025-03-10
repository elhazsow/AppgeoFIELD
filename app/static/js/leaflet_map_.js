
// var ee = ee;

//global variable
var map;
var elements;
// FeatureGroup is to store editable layers
var editItems = new L.FeatureGroup();




 // retrieve values for coloramp functions

 function getColor(d) {
  return d > 0.75 ? '#011301':
         d > 0.65 ?  '#012E01':
         d > 0.6 ?  '#056201':
         d > 0.4 ?  '#056201':
         d > 0.3  ? '#3E8601':
         d > 0.25  ?  '#66A000' :
         d > 0.1  ? '#FCD163' : 
                    '#DF923D';
}



////////////////////////////////////MutationObserver ///////Listening for change in the DOM /////////////////////////////

MutationObserver = window.MutationObserver || window.WebkitMutationObserver


const observer = new MutationObserver((mutations,observer) => {

  ndvi_add()
  // observer.disconnect()

});

observer.observe($('.container_chart')[0], {
  childList: true,
  // subtree: true

});

// set the style to the layer

function style(feature) {

  return {
      fillColor: getColor(feature.properties.superf_ha_field),
      weight: 1,
      opacity: 1,
      color: 'black',
      dashArray: '',
      fillOpacity: 0.9,
      className:String(feature.id),
       
  } ;
}





///////////////////////////////adding ndvi layer/////////////////////////////


var layer_ndvi;
// spinner add() and remove()
var spinner = document.getElementById('spinner')

function addspin(){
  spinner.classList.add('loader')
}

function removespin(){
  spinner.classList.remove('loader')
}


var ndvi_add =  function(){

  var tiles = JSON.parse(document.getElementById('tiles').textContent)
  var attr = JSON.parse(document.getElementById('attr').textContent)

  if(layer_ndvi){
   
    layer_ndvi.setUrl(tiles, noRedraw = false);
    
    return;
    
  }

  layer_ndvi = L.tileLayer(tiles,{
    'attribution':attr,
    pane:'ndvi'})

 
  map.layerscontrol.addOverlay(layer_ndvi, "Ndvi");
  layer_ndvi.addTo(map);
  
  // tiles=tiles.textContent
  // map.createPane('ndvi');
  // map.getPane('ndvi').style.zIndex = 450; 
};
  
  

//////////////////////////////////////////// adding layer control ////////////////////////////////////////////

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info noselect'); // create a div with a class "info" to hold the details
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h4>'+ (props ?
        '<b>' + props.nom + '</b></h4><br />' +'<b>Aire: </b>'+ props.superf_ha_field + ' ha <br />'+'<br />'+(props.arret_dec1 ?
        "<b>Arrêté n°:"+ props.arret_dec1 +'</b>':'Arrêté  : Non définit')
        : 'Hover over a polygon');
};



// highlight on hover
function highlightFeature(e) {
  var layer = e.target;
  info.update(layer.feature.properties);
  layer.setStyle({  //change the style
      weight: 6,
      color: '#DF923D',
      dashArray: '',
      fillOpacity: 0.3,
  });

  layer.bringToFront();
};

// reset the style of the layer


function resetHighlight(e) {

  info.update();
  elements.resetStyle(e.target)};


function zoomToFeature(e) {
  
  var layer = e.target;
  var id = layer.feature.id;
  //////////////
  addspin()
  ////////////////
  $.ajax({url: String(id), success: function(result){  //ajax request on the bokeh_chart view
    $(".container_chart").html(result);
  }});
  map.fitBounds(e.target.getBounds());
  ////////////////////////
  removespin()


  // console.log(map.getPanes())
  // ndvi_add()
  
};


function onEachFeature(feature, layer) {
layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
      click: zoomToFeature,
});
};



function draw() {
  
   // Ajouter les options de dessin
   var drawControl = new L.Control.Draw({
    position: 'bottomright',
    draw: {
        polygon: true,
        polyline: false,
        rectangle: false,
        circle: false,
        circlemarker:false,
        marker: false,
    },
    edit: {
        featureGroup: editItems,// Ajoute un groupe de calques pour l'édition
        edit: true, 
    }
  });
  
  map.addControl(drawControl);

  // Écouteur d'événements pour capturer les objets dessinés
  map.on('draw:created', function (e) {
  var layer = e.layer;
  var type = e.layerType; // Type d'objet (polygon, polyline, etc.)
  console.log('Un nouvel objet a été créé :', type);

  // Ajoute l'objet à la carte
  layer.addTo(editItems);
  editItems.addTo(map);
});
}

////////////////////////////////////////////fetching data from backend////////////////////////////////////////////

// async function load_poly() {
//   const poly_url = `/api/ZonesProtégées/`;

//   //?in_bbox={map.getBounds().toBBoxString()}

//   const response = await fetch(
//     poly_url
//   );
//   const geojson = await response.json();
//   return geojson;
// };

const data_geo = JSON.parse(document.getElementById('map_data').textContent);

// var data = await load_poly();








/////////////////////////////////////////////////////////

window.addEventListener("map:init" , function(e){
  // console.log(data)
  map = e.detail.map;
  map.createPane('ndvi');
  map.getPane('ndvi').style.zIndex = 450;
  elements = L.geoJson(JSON.parse(data_geo),
          {
          style: style,
          onEachFeature: onEachFeature
          });

  // layerscontrol(elements)
  
  
  map.fitBounds(elements.getBounds());
  
  map.layerscontrol.addOverlay(elements, "Zones Protégées du SENEGAL");
  elements.addTo(map);
  info.addTo(map);
  draw()
  // $(".leaflet-draw-toolbar").append("<form action='#' onsubmit='return false;'><input type='file' id='fileinput'><input type='button' id='btnLoad' value='Load' onclick='loadFile();'></form>")
});





 
////////////////////////////////////////////////////

 var observer_ = new MutationObserver(function (mutations, observer_) {
 
   $( ".list-lieux p" ).on( {mouseover: highlight_,
     mouseleave: resetHighlight_,
    //  click: zoomToFeature_
   });
  //  observer_.disconnect();
 });
 
 
 observer_.observe($('#list')[0], {
   subtree:true,
   childList:true,
 })




/////////////////////interactiveness/////////////////////////////////////////////////////////////////////


var highlight_ = function(e) {
  var el = $('.'+String(this.id))

  $('.'+String(this.id)).css({"stroke": "#DF923D", "stroke-width":"6", "fill-opacity": "0.7"});
}


var resetHighlight_ = function(){
  info.update();
  $('.'+String(this.id)).removeAttr("style");
}

// function zoomToFeature_() {
//   console.log("zoom")
//   var el= $('.'+String(this.id))
//   if ($('.'+String(this.id)).click()){
//     console.log("oui")
//   };


  // "fillColor": String(getColor(feature.properties.superf_ha_field)),
  // "stroke-width": "1",
  // "fill": "1",
  // "stroke": 'black',
  // "dashArray": '',
  // "fill-opacity": "0.9",
  // className:String(feature.id),});


  // FeatureGroup is to store editable layers

  // var drawnItems = new L.FeatureGroup();
  // map.addLayer(drawnItems);
  // var drawControl = new L.Control.Draw({
  // edit: { featureGroup: drawnItems
  // }
  // });
  // map.addControl(drawControl);
  

