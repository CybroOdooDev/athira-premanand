/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";

import { patch } from "@web/core/utils/patch";

import session from "web.session";

const { onWillStart } = owl;

patch(NavBar.prototype, 'web_notification/static/src/js/navbar.js', {
    setup(){
        this._super.apply();
        onWillStart(() => {
            this.notification = session.user_messages
        })
    }
})
