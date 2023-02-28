odoo.define('customize_signup.signup', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
publicWidget.registry.SignUpForm = publicWidget.Widget.extend({
    selector: '.oe_signup_form',
    events: {
        'click #info': '_extraInfo',
        'click #hide_info': '_hideInfo',
    },

     _extraInfo: function () {
        $("#data").toggle();

        if (info.style.display == 'none') {
            info.style.display = 'block';
        } else {
            info.style.display = 'none';
            hide_info.style.display = 'block';
        }
    },

    _hideInfo: function () {
        $("#data").toggle();

        if (hide_info.style.display == 'none') {
            hide_info.style.display = 'block';
        } else {
            hide_info.style.display = 'none';
            hide_info.style.display = 'none';
        }
    },
});
});
