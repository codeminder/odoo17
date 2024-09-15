from odoo import models, fields, api
from datetime import datetime, timedelta

class SickReportWizard(models.TransientModel):
    _name = 'hr_hospital.sick_report_wizard'
    _description = 'Wizard for Monthly Sick Report'

    year = fields.Selection([(str(y), str(y)) for y in range(2000, datetime.now().year + 1)],
                            string='Year', required=True, default=str(datetime.now().year))
    month = fields.Selection([
        ('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'),
        ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'),
        ('11', 'November'), ('12', 'December')], string='Month', required=True, default=str(datetime.now().month).zfill(2))

    def action_generate_report(self):
        """Generate the report based on selected year and month."""
        self.ensure_one()

        # Calculate the start and end dates for the selected month
        start_date = datetime.strptime(f'{self.year}-{self.month}-01', '%Y-%m-%d')
        end_date = (start_date.replace(day=28) + timedelta(days=4)).replace(day=1)

        # Remove existing report data
        self.env['hr_hospital.sick_report'].search([]).unlink()

        # Get the data for the report
        report_data = self.env['hr_hospital.diagnosis'].read_group(
            domain=[('diagnosis_date', '>=', start_date), ('diagnosis_date', '<', end_date)],
            fields=['sick_id'],
            groupby=['sick_id']
        )

        # Create report records
        for data in report_data:
            self.env['hr_hospital.sick_report'].create({
                'sick_id': data['sick_id'][0],
                'diagnosis_count': data['sick_id_count'],
            })

        # Return an action to open the report view
        return {
            'type': 'ir.actions.act_window',
            'name': 'Monthly Sick Report',
            'view_mode': 'tree',
            'res_model': 'hr_hospital.sick_report',
            'target': 'current',
        }