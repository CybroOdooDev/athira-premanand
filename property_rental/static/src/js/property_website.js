odoo.define('property.property_rental_view', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var PropertyView = require('property.property_view')
    publicWidget.registry.PropertyRental = PropertyView.extend({
        events: _.extend({}, PropertyView.prototype.events, {

        }),
        _changeView: function(ev){
            var action_id = $(ev.target).data('action')
            if (action_id == "3"){
                $('#property_rental_view').css('display', 'block')

            }else{
                $('#property_rental_view').css('display', 'none')
            }
        },
    })
})