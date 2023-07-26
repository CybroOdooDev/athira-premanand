odoo.define('theme_mars.wishlist', function (require) {
"use strict";
var publicWidget = require('web.public.widget');
var wSaleUtils = require('website_sale.utils');
var VariantMixin = require('sale.VariantMixin');
  /**
     * Extends the ProductWishlist widget to include additional functionalities.
     */
publicWidget.registry.ProductWishlist.include({
     /**
     * Removes a wish from the wishlist.
     *
     */
    _removeWish: function (e, deferred_redirect) {
        var tr = $(e.currentTarget).parents('tr');
        var wish = tr.data('wish-id');
        var product = tr.data('product-id');
        var self = this;
        // Remove the wish via RPC call
        this._rpc({
            route: '/shop/wishlist/remove/' + wish,
        }).then(function () {
            $(tr).hide();
        });
         // Update the wishlistProductIDs array and the sessionStorage
        this.wishlistProductIDs = _.without(this.wishlistProductIDs, product);
        sessionStorage.setItem('website_sale_wishlist_product_ids', JSON.stringify(this.wishlistProductIDs));
        // If there are no more products in the wishlist, perform necessary actions
        if (this.wishlistProductIDs.length === 0) {
            if (deferred_redirect) {
                deferred_redirect.then(function () {
                    self._redirectNoWish();
                });
            }
            $('#o_comparelist_table').addClass('d-none')
            $('.shop_cart').removeClass('d-none')
        }
        this._updateWishlistView();
    },
})
});
