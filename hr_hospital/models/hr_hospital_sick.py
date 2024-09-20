
from odoo import models, fields


class Sick(models.Model):
    _name = 'hr_hospital.sick'
    _description = 'Sick'
    _parent_name = "parent_id"  # Field used for hierarchy
    _parent_store = True  # Enable hierarchy storage
    _parent_order = 'name'
    _rec_name = 'name'  # Default field to show in Many2one fields

    name = fields.Char(string='Sickness Name', required=True)
    description = fields.Text()

    # Hierarchical fields
    parent_id = fields.Many2one('hr_hospital.sick',
                                string="Parent sick",
                                index=True, ondelete='cascade')
    child_ids = fields.One2many('hr_hospital.sick', 'parent_id',
                                string="Secondary sicks")

    # This field is required for hierarchical searching
    parent_path = fields.Char(index=True, unaccent=False)
