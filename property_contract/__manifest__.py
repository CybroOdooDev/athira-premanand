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
    'name': 'Property Contract',
    'version': '16.0.1.0.0',
    'summary': """Store Several Email Addresses, multiple Phone Numbers and Usernames for Partners.""",
    'description': """Store Several Email Addresses, multiple Phone Numbers and Usernames for Partners.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'mail', 'sale', 'property_management'],
    'data': [
                'security/ir.model.access.csv',
                'data/recurring_contract.xml',
                'views/contract.xml',
    ],

    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'price': 29,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
