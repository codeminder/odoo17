from odoo import fields, models


class DoctorWeeklySchedule(models.Model):
    _name = 'hr_hospital.doctor_weekly_schedule'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one('hr_hospital.doctor',
                                string="Doctor", required=True)
    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ], string="Day", required=True)
    week_type = fields.Selection([('even', 'Even Week'),
                                  ('odd', 'Odd Week')],
                                 string="Week Type",
                                 required=True)
    start_time = fields.Float(string="Start Time", required=True)
    end_time = fields.Float(string="End Time", required=True)

    _sql_constraints = [
        ('unique_schedule', 'UNIQUE(doctor_id, day, week_type)',
         'Doctor can only have one schedule for each day '
         'of a given week type.')
    ]
