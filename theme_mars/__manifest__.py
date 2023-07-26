# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Theme Mars',
    'version': '16.0.1.0.0',
    'category': 'Theme',
    'summary': 'Theme Mars is an attractive and modern Website theme',
    'description': 'Theme Mars is a new kind of Theme. '
                   'The theme is a very user-friendly and is suitable for '
                   'your website.',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'website', 'website_sale_comparison',
                'website_sale_comparison_wishlist', 'website_blog'],
    'data': [
        'security/ir.model.access.csv',
        'data/menu.xml',
        'data/portfolio.xml',
        'data/gallery.xml',
        'views/header_templates.xml',
        'views/footer_templates.xml',
        'views/layouts_templates.xml',
        'views/theme_about_templates.xml',
        'views/userlogin_templates.xml',
        'views/theme_shop_cart_templates.xml',
        'views/theme_shop_wishlist_templates.xml',
        'views/theme_shop_product_templates.xml',
        'views/theme_shop_sidebar_templates.xml',
        'views/product_sidebar_templates.xml',
        'views/theme_shop_loadmore_templates.xml',
        'views/shop_infinity_scroll_templates.xml',
        'views/theme_shop_columns_templates.xml',
        'views/mars_pager_templates.xml',
        'views/theme_cart_templates.xml',
        'views/theme_checkout_templates.xml',
        'views/theme_portfolio_templates.xml',
        'views/mars_portfolio_views.xml',
        'views/mars_portfolio_images_views.xml',
        'views/mars_portfolio_group_views.xml',
        'views/theme_gallery_templates.xml',
        'views/mars_gallery_views.xml',
        'views/theme_gallery_columns_templates.xml',
        'views/theme_gallery_loadmore_templates.xml',
        'views/theme_gallery_sidebar_templates.xml',
        'views/theme_gallery_category.xml',
        'views/theme_gallery_infinity_scroll_templates.xml',
        'views/theme_gallery_wide_templates.xml',
        'views/website_blog_views.xml',
        'views/dynamic_blog_templates.xml',
        'views/blog_sidebar_left_templates.xml',
        'views/blog_sidebar_right_templates.xml',
        'views/sidebar_left_sticky_templates.xml',
        'views/sidebar_right_sticky_templates.xml',
        'views/tags_templates.xml',
        'views/blogs_templates.xml',
        'views/page_404_templates.xml',
        'views/contact_templates.xml',
        'views/snippets/about_templates.xml',
        'views/snippets/client.xml',
        'views/snippets/team_templates.xml',
        'views/snippets/contact_bottom_map_templates.xml',
        'views/snippets/services_templates.xml',
        'views/snippets/banner_templates.xml',
        'views/snippets/thumbnail_templates.xml',
        'views/theme_snippet_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
            'https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.6/dist/jquery.fancybox.min.js',
            'https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.6/dist/jquery.fancybox.min.css',
            "theme_mars/static/src/css/style.css",
            "/theme_mars/static/src/css/owl.carousel.min.css",
            "/theme_mars/static/src/css/animate.min.css",
            "/theme_mars/static/src/js/jquery.appear.min.js",
            "/theme_mars/static/src/js/owl.carousel.js",
            "/theme_mars/static/src/js/index.js",
            "/theme_mars/static/src/js/jquery.easypiechart.min.js",
            "/theme_mars/static/src/js/custom.js",
            "/theme_mars/static/src/js/blog.js",
            "/theme_mars/static/src/js/recent_blog.js",
            "/theme_mars/static/src/js/wishlist.js",
        ],
        'website.assets_wysiwyg': [
            "/theme_mars/static/src/js/snippets/options.js",
        ]
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
