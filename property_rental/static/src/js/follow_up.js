odoo.define('client_act.follow_up', function (require) {
   'use strict';
   console.log('asdfghjk')
   var AbstractAction = require('web.AbstractAction');
   var core = require('web.core');
   var rpc = require('web.rpc');
   var QWeb = core.qweb;
   var FollowUp = AbstractAction.extend({
        template: 'SaleCust',
        events: {
            'click .import_sale': 'import_sale',
        },
       start: function() {
           var self = this;
           this.import_rent();
       },
        import_rent: function (e) {
        var self = this;
          rpc.query({
                model: 'res.partner',
                method: 'search_read',
                domain: [["is_rental", "=", true]],
                }).then(function(result) {
                    console.log(result,"sass")
                    result.forEach(element => {
                    $('.rentKanban').append(`
                    <div class="card col-md-6 col-lg-6 col-sm-12 ">
                        <div class="stat-widget-one" style="display: flex;">
                            <div class="stat-icon" style="green;">
                            <img id="renter_image" width="80px" src="data:image/png;base64,${element.avatar_1920}"/><b class="render_name">${element.display_name}</b>
                            </div>
                        </div>
                    </div>`)
//                    count += 1;
})
			})
		},

    });
 core.action_registry.add("follow_up", FollowUp);
   return FollowUp;
});