from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    contact_ids = fields.One2many(
        'res.partner',
        related='partner_id.child_ids',
        string='Contacts',
        readonly=True
    )
