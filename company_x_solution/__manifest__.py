# company_x_solution/__manifest__.py

{
    'name': 'Company X Solution',
    'version': '1.0',
    'summary': 'Custom module for Company X B2B operations',
    'description': """
        This module includes features for managing B2B quotations, orders, payments, and deliveries.
    """,
    'author': 'Your Name',
    'depends': ['base', 'sales', 'purchase', 'report'],
    'data': [
        'data/security.xml',
        'views/dashboard_view.xml',
        'views/pivot_view.xml',
        'views/calendar_view.xml',
        'views/portal_view.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
