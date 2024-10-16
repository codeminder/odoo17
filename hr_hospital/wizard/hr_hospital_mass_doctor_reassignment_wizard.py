
from odoo import models, fields, api


class MassDoctorReassignmentWizard(models.TransientModel):
    _name = 'hr_hospital.mass_doctor_reassignment_wizard'
    _description = 'Mass Reassignment of Personal Doctor'

    new_doctor_id = fields.Many2one(
        'hr_hospital.doctor', string='New Doctor', required=True)
    patient_ids = fields.Many2many(
        'hr_hospital.patient',
        string='Patients',
        relation='doctor_reassign_patient_rel',)

    @api.model
    def default_get(self, fields_list):
        """ Populate default values for the wizard fields. """
        res = super(
            MassDoctorReassignmentWizard, self).default_get(fields_list)
        if 'default_patient_ids' in self.env.context:
            default_patient_ids = self.env.context.get('default_patient_ids')
            res.update({'patient_ids': [(6, 0, default_patient_ids)]})
        return res

    def action_reassign_doctor(self):
        """ Reassign the selected doctor to the patients. """
        if self.patient_ids:
            self.patient_ids.write(
                {'doctor_id': self.new_doctor_id.id})
        return {'type': 'ir.actions.act_window_close'}
