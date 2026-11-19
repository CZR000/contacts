{
    'name': 'Contact Name Lastname',
    'version': '18.0.1.0.1',
    'author': 'AlexJimmy159',
    'maintainer': 'AlexJimmy159',
    'support': 'AlexJimmy159@gmail.com',
    'website': 'https://github.com/AlexJimmy159',
    'summary': 'Fields for the names, mother surname and father surname of the partner',
    'description': """
This module adds fields for the names, mother
surname and father surname of the partner.
""",
    'category': 'Extra Tools/Extra Tools',
    'depends': [
        # Odoo community
        'base',
    ],
    'data': [
        'views/res_partner_views.xml',
    ],
    'module_type': 'official',
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'Other proprietary',
}
