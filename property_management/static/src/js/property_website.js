odoo.define('property.property_view', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');

    publicWidget.registry.PropertyView = publicWidget.Widget.extend({
        selector: 'div[id="property_container"]',
        events: {
            'click .property_action_buttons': '_changeView',
            'click .o_property_item': 'fetchPropertyItem',
            'click .loadMap': 'MapLoad',
        },
        _changeView : function(ev){
            var action_id = $(ev.target).data('action')
            $('.property_action_buttons').removeClass('active')
            if (action_id == "0"){
                $('#property_item_view').css('display', 'block')
                $(ev.target).addClass('active')
            }else{
                 $('#property_item_view').css('display', 'none')
            }
        },
        fetchPropertyItem : function(ev){
              var record_id = $(ev.target.closest('.o_property_item')).data('property_id')
              window.location='/property/'+record_id;
        },
    })

    publicWidget.registry.PropertyItemView = publicWidget.Widget.extend({
    templates: 'property_management.property_view_item',
    selector: '.property_container',
    events: {
            'click #loadMap': 'MapLoad'
    },
    MapLoad: function (e) {
            console.log("worked")
            $('#map-view').css('display', 'block')
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
    return publicWidget.registry.PropertyView ;
})
