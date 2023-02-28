odoo.define('theme_eco_food.eco_food_featured_products', function(require){
    'use strict';

    var Animation = require('website.content.snippets.animation');
    var ajax = require('web.ajax');

    Animation.registry.get_featured_products = Animation.Class.extend({
        selector : '.featured_product',
        start: function(){
            var self = this;
            ajax.jsonRpc('/get_featured_products', 'call', {})
            .then(function (data) {
                if(data){
                    self.$target.empty().append(data);
                    self.product_carousel();
                }
            });
        },
        product_carousel: function (autoplay=false, items=8, slider_timing=5000) {
        var self= this;
            $("#demo_carousel").owlCarousel(
                {
                    items: 1,
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
                    responsiveClass: true,
                }
            );
        },
    });
});