# -*- coding: utf-8 -*-
{
    "name": "Hospital Management",
    "summary": """
        The module to automate using of hospital HR
        for appointment adoctor to patient""",
    "author": "Roman Rabotin",
    "website": "https://github.com/codeminder/odoo17/tree/17.0",
    "category": "Human Resources",
    "version": "17.0.0.0.0",
    'license': 'GPL-2',
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/doctor_views.xml",
        "views/patient_views.xml",
        "views/sick_views.xml",
        "views/appointment_views.xml",
        "views/hr_hospital_menu.xml",
        "data/sick_data.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "data/demo_data.xml",
    ],
    'installable': True,
    'application': True,
}
