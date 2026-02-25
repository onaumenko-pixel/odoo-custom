from odoo import models, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="lead_id",
        string="Contacts",
        domain=[
            ("company_type", "=", "person"),
            ("type", "=", "contact"),
        ],
    )
