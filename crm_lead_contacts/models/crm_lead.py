from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    contact_ids = fields.One2many(
        'res.partner',
        'lead_id',
        string='Contact Persons'
    )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    lead_id = fields.Many2one(
        'crm.lead',
        string='Lead'
    )
