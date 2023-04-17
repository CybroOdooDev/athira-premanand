{
    'name': 'Contract Management',
    'version': '16.0.1.0.0',
    'summary': """Calculates average landed costs of products.""",
    'description': """Calculates average landed costs of products.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'product'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/position.xml',
        'views/contract.xml',
        'views/partner.xml',
        'views/team_leader.xml',
        'views/approval_teams.xml',
        'wizard/wizard.xml',
        'views/return_reason.xml',
        'views/menu.xml',

    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'price': 29,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
