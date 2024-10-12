
from datetime import date
from odoo import api, models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'
    _inherit = 'hr_hospital.person'

    birth_date = fields.Date()
    age = fields.Integer(compute='_compute_age', store=True)
    passport_data = fields.Char()
    contact_person_id = fields.Many2one('hr_hospital.contact_person')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    doctor_id = fields.Many2one('hr_hospital.doctor')
    diagnosis_ids = fields.One2many('hr_hospital.diagnosis', 'patient_id')
    appointment_ids = fields.One2many('hr_hospital.appointment', 'patient_id')

    @api.depends('birth_date')
    def _compute_age(self):
        """Розраховує вік пацієнта на основі дати народження."""
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = (today.year - record.birth_date.year
                              - ((today.month, today.day)
                                 < (record.birth_date.month,
                                    record.birth_date.day)))
            else:
                record.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to handle batch creation properly."""
        # Ensure vals_list is a list (for batch processing)
        if not isinstance(vals_list, list):
            vals_list = [vals_list]

        records = super(Patient, self).create(vals_list)
        for record in records:
            if record.doctor_id:
                self.env['hr_hospital.doctor_change_history'].create({
                    'patient_id': record.id,
                    'doctor_id': record.doctor_id.id
                })
        return records

    def write(self, vals):
        res = super(Patient, self).write(vals)
        if 'doctor_id' in vals:
            for record in self:
                if record.doctor_id:
                    self.env['hr_hospital.doctor_change_history'].create({
                        'patient_id': record.id,
                        'doctor_id': record.doctor_id.id
                    })
        return res

    # Show history of appointment
    def action_show_appointments_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'History of appointment',
            'res_model': 'hr_hospital.appointment',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
        }

    # Show the history of sicks
    def action_show_diagnosis_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'History of diagnosis',
            'res_model': 'hr_hospital.diagnosis',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
        }

    # Show history of analyses
    def action_show_analyses_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'History of analyses',
            'res_model': 'hr_hospital.analysis',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
        }

    # Quick appointment to a doctor
    def action_quick_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quick appointment to a doctor',
            'res_model': 'hr_hospital.appointment',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_patient_id': self.id},
        }
