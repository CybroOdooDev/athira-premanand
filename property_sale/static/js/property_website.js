odoo.define('property.property_sales_view', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var PropertyView = require('property.property_view');
    var PropertyItemView = require('property.property_item_view');

    publicWidget.registry.PropertySales = PropertyView.extend({
        events: _.extend({}, PropertyView.prototype.events, {
        }),
        _changeView: function(ev){
            var action_id = $(ev.target).data('action')
            if (action_id == "2"){
                $('#property-item').css('display', 'none')
                $('#property_sales_view').css('display', 'block')
            }else{
                $('#property_sales_view').css('display', 'none')
            }
        },
        fetchPropertyItem : function(ev){
            $('#property-item').css('display', 'block')
            $('#property_sales_view').css('display', 'none')
            var self = this;
            var record_id = $(ev.target.closest('.o_property_item')).data('property_id')
            rpc.query({
                route: `/property/${record_id}`,
                params: {}
            }).then(function (result){
                console.log(result)
                if(result[0].measure){var measure = result[0].measure.replace(/[^a-zA-Z ]/g, "")}
                $('.property_item').html(`<div class="row bg-white">
                                        <div class="col-md-4">
                                            <img id="property-image" src="data:image/png;base64,${result[0].image}" style="width: -webkit-fill-available;"/>
                                        </div>

                                        <div class="col-md-8 introduction">
                                            <div class="row">
                                                <h2 class="my-0" style="text-transform: capitalize;">
                                                    ${result[0].name}-${result[0].type_id_base}
                                                </h2><br/><div class="col-sm-4 m-2"> Address: </div>
                                                <div class="col m-2">${result[0].street}<br/>${result[0].street2}<br/>
                                                ${result[0].city} ${result[0].state_id[1]} ${result[0].zip} </br>${result[0].country_id[1]}</div>
                                            </div>
                                        </div>
                                        <section id="details" style="page-break-inside: auto;" class="mt32">
                                            <div class="row">
                                                <div class="col-sm-4 m-2" style="font-size: 1.5rem;"> Measure: </div>
                                                <div class="col m-2" style="font-size: 1.5rem;text-transform: capitalize;">${result[0].measure_value} ${measure}</div>
                                            </div>

                                        </section>

                                    </div>`)
                if (result[0].unit_price)   {
                        $('.introduction').append(`<div class="row"><div class="col-sm-4 m-2"> Price: </div>
                                                     <div class="col m-2">${result[0].unit_price}/-</div></div>`)
                }
            })
        },
    })

    publicWidget.registry.PropertyItemSales = PropertyItemView.extend({
        events: _.extend({}, PropertyView.prototype.events, {
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