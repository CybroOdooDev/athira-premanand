odoo.define('customize_signup.signup', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
publicWidget.registry.SignUpForm = publicWidget.Widget.extend({
    selector: '.oe_signup_form',
    events: {
        'click #info': '_extraInfo',
        'click #hide_info': '_hideInfo',
        'click .btn-primary':'_signupBtn',
    },
    /**
   * this method is used to store the information in the local storage
   */
    start: function(){
        if (localStorage.getItem('city')){
            this.$el.find('#city').val(localStorage.getItem('city'))
        }
        this.$el.find('#job_position').val(localStorage.getItem('job_position'))
        this.$el.find('#name').val(localStorage.getItem('name'))
        this.$el.find('#login').val(localStorage.getItem('login'))
        this.$el.find('#phone').val(localStorage.getItem('phone'))
        this.$el.find('#country').val(localStorage.getItem('country'))
//        this.$el.find('#file').val(localStorage.getItem('file'))
    },
    _signupBtn:function (){
        localStorage.setItem('city', this.$el.find('#city').val());
        localStorage.setItem('job_position', this.$el.find('#job_position').val());
        localStorage.setItem('name', this.$el.find('#name').val());
        localStorage.setItem('login', this.$el.find('#login').val());
        localStorage.setItem('phone', this.$el.find('#phone').val());
        localStorage.setItem('country', this.$el.find('#country').val());
//        localStorage.setItem('file', this.$el.find('#file').val());
    },
     /**
     * this method is used to show the extra information given in the
     *  signup form
     */
     _extraInfo: function () {
        this.$el.find("#data").toggle();
        if (info.style.display == 'none') {
            info.style.display = 'block';
        } else {
            info.style.display = 'none';
            hide_info.style.display = 'block';
        }
    },
    /**
     * this method is used to hide the extra information given in the
     *  signup form
     */
    _hideInfo: function () {
        this.$el.find("#data").toggle();
        if (hide_info.style.display == 'none') {
            hide_info.style.display = 'block';
        } else {
            hide_info.style.display = 'none';
            info.style.marginLeft= '-37px', info.style.display = 'block';
        }
    },
});
});
