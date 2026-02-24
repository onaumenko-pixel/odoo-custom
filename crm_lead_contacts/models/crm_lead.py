from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    contact_ids = fields.One2many(
        'res.partner',
        'parent_id',
        string='Contact Persons',
        domain=[('type', '=', 'contact')]
    )
