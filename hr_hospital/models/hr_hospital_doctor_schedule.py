from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DoctorSchedule(models.Model):
    _name = 'hr_hospital.doctor.schedule'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)
    appointment_time = fields.Float(string='Appointment Time', required=True, help="Time in 24-hour format (e.g., 14.5 for 2:30 PM)")

    # Constraint to ensure unique time slots for the same doctor on the same day
    _sql_constraints = [
        ('unique_schedule', 'unique(doctor_id, appointment_date, appointment_time)',
         'A doctor cannot have two appointments at the same time on the same day.'),
    ]

    @api.constrains('appointment_time')
    def _check_appointment_time(self):
        """Ensure the appointment time is within a valid range (0.0 - 24.0)."""
        for record in self:
            if record.appointment_time < 0.0 or record.appointment_time >= 24.0:
                raise ValidationError("Appointment time must be between 0.0 (midnight) and 24.0.")
