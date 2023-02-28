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
       },
      import_sale: function (e) {
      var self = this;
      this.do_action({
                name: "Import Sale Order",
                type: 'ir.actions.act_window',
                res_model: 'sale.order.import.wizard',
                view_mode: 'form',
                views: [[false, 'form']],
                target: 'new',
            })
   },

});
 core.action_registry.add("follow_up", FollowUp);
   return FollowUp;
});