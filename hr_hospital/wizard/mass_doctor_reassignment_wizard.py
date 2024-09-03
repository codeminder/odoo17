# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class MassDoctorReassignmentWizard(models.TransientModel):
    _name = 'hr_hospital.mass_doctor_reassignment_wizard'
    _description = 'Mass Reassignment of Personal Doctor'

    new_doctor_id = fields.Many2one('hr_hospital.doctor', string='New Doctor', required=True)

    def action_reassign_doctor(self):
        """Reassign the selected patients to a new personal doctor."""
        patient_ids = self.env.context.get('active_ids', [])
        if not patient_ids:
            raise UserError("No patients selected.")
        
        # Reassign the doctor
        patients = self.env['hr_hospital.patient'].browse(patient_ids)
        for patient in patients:
            
            patient.doctor_id = self.new_doctor_id.id

            # Create a history record for the change
            self.env['hr_hospital.doctor_change_history'].create({
                'patient_id': patient.id,
                'doctor_id': self.new_doctor_id.id,
                'change_date': fields.Datetime.now(),
            })
