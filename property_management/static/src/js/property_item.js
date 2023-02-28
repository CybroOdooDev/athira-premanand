odoo.define('property.property_item_view', function (require) {
'use strict';
    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');

    publicWidget.registry.PropertyItemView = publicWidget.Widget.extend({
    templates: 'property_management.property_view_item',
    selector: '.property_container',
    events: {
            'click #loadMap': 'MapLoad'
    },
    MapLoad: function (e) {
            console.log("worked")
            $('#map-view').css('display', 'block')
            $('#loadMap').css('display', 'none')
            var lat = parseFloat(e.target.dataset.lat)
            var lng = parseFloat(e.target.dataset.lng)
            console.log(e)
            const location = { lat: lat, lng: lng };
            const map = new google.maps.Map(document.getElementById("map-view"),
            {
            zoom: 12,
            center: location,

            });
            const marker = new google.maps.Marker({
            position: location,
            map: map,
            });
    },
    });
    return publicWidget.registry.PropertyItemView ;
})
