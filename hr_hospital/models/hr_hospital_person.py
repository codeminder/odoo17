
from odoo import api, models, fields


class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Person'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')]
    )

    display_name = fields.Char(compute="_compute_display_name", store=True)

    @api.depends('first_name', 'last_name')
    def _compute_display_name(self):
        """
        Compute the display name in the format [FirstName] [LastName].
        """
        for person in self:
            person.display_name = f"{person.first_name or ''} \
                {person.last_name or ''}".strip()
