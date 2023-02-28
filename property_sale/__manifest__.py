{
    'name': "Property Sale",
    'version': '16.0.1.0.0',
    'summary': """""",
    'description': """""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Sales',
    'depends': ['base', 'mail', 'property_management', 'account', 'sale'],
    'data': [
        'views/property_sale.xml',
        'views/property_report.xml',
        'views/property_property.xml',
        'views/property_commission.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'wizards/property_sale_report.xml',
        'report/sale_report_template.xml',
        'views/property_customers_views.xml',
        'templates/sale_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'property_sale/static/js/property_website.js',
        ]
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
