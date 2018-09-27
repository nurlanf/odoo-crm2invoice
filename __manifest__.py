# -*- coding: utf-8 -*-
##############################################################################
# Module name: CRM2Invoice for Odoo 11
# Required modules: Invoicing,CRM
# Authour: nurlanf@github
##############################################################################

{
    'name': 'crm2invoice',
    'version': '11.0.1.0.0',
    'summary': """CRM 2 Invoice addition""",
    'description': """CRM2Invoice""",
    'author': 'erpgo.az',
    'company': 'erpgo.az',
    'website': 'https://www.erpgo.az',
    'category': 'Industries',
    'depends': ['base', 'crm', 'account'],
    'license': 'AGPL-3',
    'data': [
	'views/crm2invoice.xml',
    ],
    'demo': [],
    'images': [''],
    'installable': True,
    'application': False,
    'auto_install': False,
}

