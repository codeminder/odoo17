
from odoo import fields, models


class DoctorWeeklyScheduleWizard(models.TransientModel):
    _name = 'hr_hospital.doctor_weekly_schedule_wizard'
    _description = 'Doctor Weekly Schedule Wizard'

    doctor_id = fields.Many2one('hr_hospital.doctor', string="Doctor", required=True)
    week_type = fields.Selection([('even', 'Even Week'), ('odd', 'Odd Week')], string="Week Type", required=True)
    monday_start = fields.Float(string="Monday Start Time")
    monday_end = fields.Float(string="Monday End Time")
    tuesday_start = fields.Float(string="Tuesday Start Time")
    tuesday_end = fields.Float(string="Tuesday End Time")
    wednesday_start = fields.Float(string="Wednesday Start Time")
    wednesday_end = fields.Float(string="Wednesday End Time")
    thursday_start = fields.Float(string="Thursday Start Time")
    thursday_end = fields.Float(string="Thursday End Time")
    friday_start = fields.Float(string="Friday Start Time")
    friday_end = fields.Float(string="Friday End Time")
    saturday_start = fields.Float(string="Saturday Start Time")
    saturday_end = fields.Float(string="Saturday End Time")
    sunday_start = fields.Float(string="Sunday Start Time")
    sunday_end = fields.Float(string="Sunday End Time")

    def action_apply_schedule(self):
        self.ensure_one()

        # Перевіряємо існуючий розклад і видаляємо його
        self.env['hr_hospital.doctor_weekly_schedule'].search([
            ('doctor_id', '=', self.doctor_id.id),
            ('week_type', '=', self.week_type)
        ]).unlink()

        # Створюємо новий розклад
        schedule_vals = [
            {'day': 'monday', 'start_time': self.monday_start, 'end_time': self.monday_end},
            {'day': 'tuesday', 'start_time': self.tuesday_start, 'end_time': self.tuesday_end},
            {'day': 'wednesday', 'start_time': self.wednesday_start, 'end_time': self.wednesday_end},
            {'day': 'thursday', 'start_time': self.thursday_start, 'end_time': self.thursday_end},
            {'day': 'friday', 'start_time': self.friday_start, 'end_time': self.friday_end},
            {'day': 'saturday', 'start_time': self.saturday_start, 'end_time': self.saturday_end},
            {'day': 'sunday', 'start_time': self.sunday_start, 'end_time': self.sunday_end},
        ]

        for vals in schedule_vals:
            if vals['start_time'] and vals['end_time']:
                self.env['hr_hospital.doctor_weekly_schedule'].create({
                    'doctor_id': self.doctor_id.id,
                    'week_type': self.week_type,
                    'day': vals['day'],
                    'start_time': vals['start_time'],
                    'end_time': vals['end_time'],
                })

        return {'type': 'ir.actions.act_window_close'}
