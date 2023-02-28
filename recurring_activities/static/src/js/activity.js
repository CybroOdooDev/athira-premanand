/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { activity } from '@mail/js/activity';
import { useService } from "@web/core/utils/hooks";

import { getMessagingComponent } from '@mail/utils/messaging_component';
import { patch } from "@web/core/utils/patch";

import session from "web.session";

const { onWillStart } = owl;

patch(getMessagingComponent('ActivityMenuView').prototype, 'recurring_activities/static/src/js/activity.js', {

    async onActivityClick(){
       this.env.services.action.doAction({
            type: 'ir.actions.act_window',
            res_model: 'recurring.activity',
            view_mode: 'form',
            view_type: 'form',
            views: [[false, 'form']],
            target: 'new',

        })
    }
})
