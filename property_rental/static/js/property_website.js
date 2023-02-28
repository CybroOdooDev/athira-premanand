odoo.define('property.property_rental_view', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var PropertyView = require('property.property_view')
    var PropertyItemView = require('property.property_item_view');

    publicWidget.registry.PropertyRental = PropertyView.extend({
        events: _.extend({}, PropertyView.prototype.events, {

        }),
        _changeView: function(ev){
            var action_id = $(ev.target).data('action')
            if (action_id == "3"){
                $('#property-item').css('display', 'none')
                $('#property_rental_view').css('display', 'block')
            }else{
                $('#property_rental_view').css('display', 'none')
            }
        },
    })

    publicWidget.registry.PropertyItemSales = PropertyItemView.extend({
        events: _.extend({}, PropertyItemView.prototype.events, {
            'click .rentalReq': 'createRentReq',
            'click .sale_submit': '_submitSale',
        }),
        start: function(){
             var state = $('.property_item').data('state')
             var prop_id = $('.property_item').data('prop_id')
             console.log(state)
             if(state === 'for_rent'){
                   $('.requestBtn').append(`<button type="button"  style="width:auto;" class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#rentalModal" data-whatever="@mdo">Rental Request</button>`)

             }
             if(state === 'for sale'){
             $('.requestBtn').append(`<div class="row">
                <button type="button" class="btn btn-primary" style="width:auto;"  data-bs-toggle="modal" data-bs-target="#exampleModal" data-whatever="@mdo">Sale Request</button>
               </div>`)
        }
        },
        createRentReq: function(ev){
                var self = this;
        console.log("hhhhhhhhh", $(ev.target))
        var property_id = $(ev.target).data('prop_id');
        console.log(property_id)
        var from_date = $('#from_date').val();
        console.log(from_date,"from_date")
        rpc.query({
            route: `/property/rent/${property_id}`,
            params:{from_date: from_date}
            }).then(function(result){})
        },

        _submitSale: function(ev){
        var self = this;
        console.log("hhhhhhhhh", $(ev.target))
        var property_id = $(ev.target).data('property_id');
        console.log(property_id)
        var ask_price = parseFloat($(`#ask_price`).val());
        console.log(ask_price,"ask price")
                rpc.query({
                    route: `/property/sale/${property_id}`,
                    params:{ask_price: ask_price}
                }).then(function(result){
//                    $('#sale_button').click()
                })
    },
    })
})