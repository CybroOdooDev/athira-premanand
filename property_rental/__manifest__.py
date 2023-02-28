{
    'name': "Property Rental",
    'version': '16.0.1.0.0',
    'summary': """""",
    'description': """""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'management',
    'depends': ['property_sale', 'maintenance'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_cron_data.xml',
        'views/property_views.xml',
        'views/property_rental_views.xml',
        'views/wizard_maintenance.xml',
        'views/contacts_views.xml',
        'views/property_payment.xml',
        'views/res_configuration.xml',
        'views/follow_up.xml',
        'views/contract_views.xml',
        'templates/rental_view.xml',
        'reports/brouchure_temp.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'property_rental/static/src/js/follow_up.js',
            'property_rental/static/src/xml/follow_up_template.xml',
            'property_rental/static/src/css/style.scss'

        ],
        'web.assets_frontend': [
            'property_rental/static/js/property_website.js',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
