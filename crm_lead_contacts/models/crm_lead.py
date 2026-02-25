from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_ids = fields.One2many(
        comodel_name="res.partner",
        compute="_compute_contact_ids",
        string="Contacts",
    )

    @api.depends("partner_id")
    def _compute_contact_ids(self):
        for lead in self:
            if not lead.partner_id:
                lead.contact_ids = False
            else:
                contacts = self.env["res.partner"].search([
                    ("parent_id", "=", lead.partner_id.id),
                    ("company_type", "=", "person"),
                    ("type", "=", "contact"),
                ])
                lead.contact_ids = contacts
