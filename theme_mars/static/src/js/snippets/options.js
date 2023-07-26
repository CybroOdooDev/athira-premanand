odoo.define('theme_mars.mars_pie_chart_options', function(require) {
    'use strict';
    // Import required modules
    const core = require('web.core');
    const utils = require('web.utils');
    const options = require('web_editor.snippets.options');
    // Define the pie chart snippets class
    options.registry.pieChartSnippets = options.Class.extend({
        // Initialize the class
        init: function() {
            this._super(...arguments);
            // Call the progressBarValue and _computeWidgetState methods
            this.progressBarValue();
            this._computeWidgetState();
        },
        // Set the progress bar value
        progressBarValue: function(previewMode, widgetValue, params) {
            let value = parseInt(widgetValue);
            value = utils.confine(value, 0, 100);
            // Find the progress bar and text elements and update their values
            const $progressBar = this.$target.find('.charts');
            const $progressBarText = this.$target.find('.percent');
            $progressBarText.text($progressBarText.text().replace(/[0-9]+%/, value + '%'));
            $progressBar.attr("data-percent", value);
        },
        // Compute the widget state
        _computeWidgetState: function(methodName, params) {
            switch (methodName) {
                case 'progressBarValue': {
                    return this.$target.find('.progress-bar').attr('data-percent') + '%';
                }
            }
            // Call the super method
            return this._super(...arguments);
        },
    });
    // Define the title type class
    options.registry.TitleType = options.Class.extend({
        // Initialize the class
        init: function() {
            this._super(...arguments);
            // Call the titleType and _computeWidgetState methods and log a message
            this.titleType();
            this._computeWidgetState();
        },
        // Set the title type
        titleType: function(previewMode, widgetValue, params) {
            // Update the title class based on the selected widget value
            if (widgetValue == "left") {
                this.$target.find('.title').removeClass('right_title');
                this.$target.find('.title').addClass('left_title');
                this.$target.toggleClass('left', widgetValue === "left");
            }
            if (widgetValue == 'right') {
                this.$target.find('.title').removeClass('left_title');
                this.$target.find('.title').addClass('right_title');
            }
            if (widgetValue == 'animation') {
                this.$target.find('.title').addClass('fade-in');
                this.$target.find('.title').removeClass('left_title');
                this.$target.find('.title').removeClass('right_title');
            }
            if (widgetValue == 'default') {
                this.$target.find('.title').removeClass('fade-in');
                this.$target.find('.title').removeClass('left_title');
                this.$target.find('.title').removeClass('right_title');
            }
        },
    });
});
