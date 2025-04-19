# -*- coding: utf-8 -*-

{
    'name': 'Enterprise HRMS Biometric Device Integration',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Integrating Biometric Device With HR Attendance (Face + Thumb)',
    'description': 'This module integrates Odoo with the biometric device'
                   '(Model: ZKteco uFace 202)',
    'author': 'Salman Malik,Open HRMS',
    'company': 'NTF Group',
    'maintainer': 'Salman Malik',
    'website': "https://www.ntf-group.com",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'data/ir_cron_data.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/zk_machine_views.xml',
        'views/hr_attendance_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
