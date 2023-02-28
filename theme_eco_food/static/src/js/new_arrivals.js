odoo.define('theme_eco_food.new_arrivals', function(require){
    'use strict';
    var Animation = require('website.content.snippets.animation');
    var ajax = require('web.ajax');

    Animation.registry.new_products = Animation.Class.extend({
        selector : '.new_arrivals',
        start: function(){
            var self = this;
            ajax.jsonRpc('/eco_food_new_arrivals', 'call', {})
            .then(function (data) {
                if(data){
                    console.log("Data:  ",data);
                    self.$target.empty().append(data);
                    self.product_carousel();
                }
            });
        },
    product_carousel: function (autoplay=false, items=5, slider_timing=5000) {
    var self= this;
    console.log($("#demo_new"))
         $("#demo_new").owlCarousel(
               {
                    items: 5,
                    loop: true,
                    margin: 30,
                    stagePadding: 30,
                    smartSpeed: 450,
                    autoplay: true,
                    autoPlaySpeed: 1000,
                    autoPlayTimeout: 1000,
                    autoplayHoverPause: true,
                    dots: false,
                    nav: true,
               }
            );
        },
});
});