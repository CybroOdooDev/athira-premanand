{
    'name': "Property Management",
    'version': '16.0.1.0.0',
    'summary': """""",
    'description': """""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'management',
    'depends': ['base', 'mail', 'website', 'base_geolocalize'],
    'data': [
        'views/menu.xml',
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/website_menu.xml',
        'views/property_property.xml',
        'views/portal.xml',
        'views/owners_property_template.xml',
        'views/property_type.xml',
        'views/property_facilities.xml',
        'views/property_tags.xml',
        'views/nearby_connectivity.xml',
        'views/neighbours_data.xml',
        'views/search_panel.xml',
        'templates/property.xml',
        'reports/property_brochure.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'property_management/static/src/js/property_website.js',
            'property_management/static/src/js/property_item.js',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
