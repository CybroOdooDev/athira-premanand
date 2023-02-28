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
    'name': 'Duplicate Product BOM',
    'version': '16.0.1.0.0',
    'summary': """When you duplicate product it will also duplicate or copy BOM of the products so this odoo app
              reduce lots of hassel when you need to add large number of product to be add for Manufacturing module.""",
    'description': """When you duplicate product it will also duplicate or copy BOM of the products so this odoo app
                    reduce lots of hassel when you need to add large number of product to be add for Manufacturing
                     module.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'category': 'Manufacturing',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'sale', 'mrp'],
    'data': [
    ],

    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
