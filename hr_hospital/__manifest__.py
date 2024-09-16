{
    "name": "Hospital Management",
    "summary": """
        The module to automate using of hospital HR
        for appointment adoctor to patient""",
    "author": "Roman Rabotin",
    "website": "https://github.com/codeminder/odoo17/tree/17.0",
    "category": "Human Resources",
    "version": "17.0.0.1.3",
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/hr_hospital_doctor_views.xml",
        "wizard/hr_hospital_mass_doctor_reassignment_wizard_views.xml",
        "views/hr_hospital_patient_views.xml",
        "views/hr_hospital_contact_person_views.xml",
        "views/hr_hospital_sick_views.xml",
        "views/hr_hospital_appointment_views.xml",
        "views/hr_hospital_diagnosis_views.xml",
        "views/hr_hospital_menus.xml",
        "views/hr_hospital_doctor_change_history_views.xml",
        "data/hr_hospital_sick_data.xml",
        "views/hr_hospital_doctor_schedule_views.xml",
        "views/hr_hospital_sick_report_wizard_views.xml",
        "views/hr_hospital_sick_report_views.xml",
        "wizard/hr_hospital_appointment_reschedule_wizard_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "data/hr_hospital_doctor_demo.xml",
        'data/hr_hospital_patient_demo.xml',
        'data/hr_hospital_sick_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hr_hospital/static/src/js/diagnosis_form_controller.js',
        ],
    },
    'installable': True,
    'application': True,
}
