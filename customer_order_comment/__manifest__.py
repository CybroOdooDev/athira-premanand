# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
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
    'name': 'Customer Order Comment',
    'version': '16.0.1.0.0',
    'summary': """This module helps you to add customer rating and comments through website.""",
    'description': """This module manages customer rating and comments.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'category': 'website',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'sale', 'website', 'website_sale'],
    'data': [
                'views/customer_comment.xml',
                'views/website_settings.xml',
                'views/confirmation.xml',
    ],
    'assets': {
        'web.assets_frontend': [
                        'customer_order_comment/static/src/js/review_and_rating.js',
                        'customer_order_comment/static/src/css/style.css',
            ],
    },

    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
