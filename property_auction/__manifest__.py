{
    'name': "Property Sale Auction",
    'version': '16.0.1.0.0',
    'summary': """""",
    'description': """""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Sales',
    'depends': ['property_sale'],
    'data': [
        'data/auction_sequence.xml',
        'security/ir.model.access.csv',
        'views/property_auction.xml',
        'templates/auction_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'property_auction/static/js/property_website.js',
        ]
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
