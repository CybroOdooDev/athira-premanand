odoo.define('property.property_auction_view', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var PropertyView = require('property.property_view')
    publicWidget.registry.PropertyAuction = PropertyView.extend({
        events: _.extend({}, PropertyView.prototype.events, {
            'click .auction_submit': '_submitAuction',
        }),
        _changeView: function(ev){
            var action_id = $(ev.target).data('action')
            if (action_id == "1"){
                $('#property_auction_view').css('display', 'block')
                $(ev.target).addClass('active')
                var self = this
                var product_id = parseInt($(ev.target).data('prod_id'))
                rpc.query({
                    route: `/property/auction/`,
                }).then(function(result){
                    $('.auction_cards').html(result)
                })
            }else{
                $('#property_auction_view').css('display', 'none')
            }
        },
        _submitAuction: function(ev){
            var self = this;
            var property_id = $(ev.target).data('id');
            var bid_amount = parseFloat($(`#property-${property_id}`).val());
            var last_bid = parseFloat($(`#last-bid-${property_id}`).text());
            var bid_start = parseFloat($(`#bid-start-${property_id}`).text());
            var toast = $('.toast')
            if (bid_amount && last_bid  && bid_start){
                if(bid_amount < last_bid && bid_amount < bid_start){
                    toast.addClass('show');
                }
                else{
                    rpc.query({
                        route: `/property/auction/${property_id}/bid`,
                        params:{bid_amount: bid_amount}
                    }).then(function(result){
                        $('#auction_button').click()
                    })
                }
            }else{
                toast.addClass('show');
            }
        },
    })
})