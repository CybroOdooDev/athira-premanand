odoo.define('theme_mars.counter_options', function (require) {
'use strict';
console.log("gggggggg");
    const core = require('web.core');
    const utils = require('web.utils');

    const options = require('web_editor.snippets.options');
    const _t = core._t;
    options.registry.CounterSnippet = options.Class.extend({

//        selectDataAttribute: function (previewMode, widgetValue, params) {
//            console.log("qwerty");
            init: function () {
             console.log("qwertyfff");
            this._super(...arguments);
             this.selectDataAttribute()
              this._computeWidgetState()
},
selectDataAttribute: function (previewMode, widgetValue, params) {
            var val = parseInt(widgetValue);
            this.$target.attr("data-number", val);
        },
        _computeWidgetState: function (methodName, params) {
        switch (methodName) {
            case 'selectDataAttribute': {
                return this.$target.find('.counter').attr('data-number');
            }
        }
        return this._super(...arguments);
    },
    });
});

//odoo.define('theme_mars.progress_bar_options', function (require) {
//'use strict';
//
//const core = require('web.core');
//const utils = require('web.utils');
//const options = require('web_editor.snippets.options');
//
//const _t = core._t;
//
//options.registry.counter = options.Class.extend({
//
//    //--------------------------------------------------------------------------
//    // Options
//    //--------------------------------------------------------------------------
//
//    /**
//     * Changes the position of the progressbar text.
//     *
//     * @see this.selectClass for parameters
//     */
//    display: function (previewMode, widgetValue, params) {
//        // retro-compatibility
//
//        let $text = this.$target.find('.counter');
//        console.log
////        if (!$text.length) {
////            $text = $('<span/>').addClass('counter').html(_t('80% Development'));
////        }
////
////        if (widgetValue === 'inline') {
////            $text.appendTo(this.$target.find('.progress-bar'));
////        } else {
////            $text.insertBefore(this.$target.find('.progress'));
////        }
//    },
//    /**
//     * Sets the progress bar value.
//     *
//     * @see this.selectClass for parameters
//     * @see this.selectClass for parameters
//     */
//    progressBarValue: function (previewMode, widgetValue, params) {
//        let value = parseInt(widgetValue);
//        value = utils.confine(value, 0, 100);
//        const $progressBar = this.$target.find('.progress-bar');
//        const $progressBarText = this.$target.find('.counter');
//        // Target precisely the XX% not only XX to not replace wrong element
//        // eg 'Since 1978 we have completed 45%' <- don't replace 1978
//        $progressBarText.text($progressBarText.text().replace(/[0-9]+%/, value + '%'));
//        $progressBar.attr("aria-valuenow", value);
//        $progressBar.css("width", value + "%");
//    },
//
//    //--------------------------------------------------------------------------
//    // Private
//    //--------------------------------------------------------------------------
//
//    /**
//     * @override
//     */
////    _computeWidgetState: function (methodName, params) {
////        switch (methodName) {
////            case 'display': {
////                const isInline = this.$target.find('.s_progress_bar_text')
////                                        .parent('.progress-bar').length;
////                return isInline ? 'inline' : 'below';
////            }
////            case 'progressBarValue': {
////                return this.$target.find('.progress-bar').attr('aria-valuenow') + '%';
////            }
////        }
////        return this._super(...arguments);
////    },
//});
//});
