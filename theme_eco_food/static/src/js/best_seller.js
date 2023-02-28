odoo.define('theme_eco_food.eco_food_best_seller', function(require){
    'use strict';

    var Animation = require('website.content.snippets.animation');
    var ajax = require('web.ajax');

    Animation.registry.get_best_seller = Animation.Class.extend({
        selector : '.best_seller',
        start: function(){
            var self = this;
            ajax.jsonRpc('/get_best_seller', 'call', {})
            .then(function (data) {
                if(data){
                    self.$target.empty().append(data);
                }
            });
        }
    });
});
