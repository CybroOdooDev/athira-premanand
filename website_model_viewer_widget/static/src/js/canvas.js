odoo.define('website_model_viewer_widget.canvas', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    publicWidget.registry.image3D = publicWidget.Widget.extend({
        selector: '#wrapper-el',
        start: function(){
            this.value = this.$el.find('input').val()
            var self = this;

        rpc.query({
            route: '/product/3d',
            params: {
                    product_id: this.value}
            }).then(function(data) {
                 console.log(data,"data")
                 if (data['3D_model'] != false){
                    var val = `data:model/gltf-binary;base64, ${data['3D_model']}`;
                    self.view3D = new View3D('#wrapper-el', {
                        src: val
                    });
                 }else{
                    var val = `/model_viewer_widget/static/src/assets/3d.glb`;
                    self.view3D = new View3D('#wrapper-el', {
                        src: val
                    });
                 }
            });
        }

//    selector: '.view3d-selector',
//    events: {
//        'click .3d_view':'_3dBtn',
//    },
//
//     _3dBtn:function (){
////        $("#data").toggle();
//
//         (view3d-canvas.style.display == 'none')
//
//         },


    });
});
