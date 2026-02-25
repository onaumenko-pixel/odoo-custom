from odoo import models, fields, api, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_ids = fields.One2many(
        comodel_name="res.partner",
        compute="_compute_contact_ids",
        string="Contacts",
        readonly=True,
    )

    @api.depends("partner_id")
    def _compute_contact_ids(self):
        for lead in self:
            if not lead.partner_id:
                lead.contact_ids = [(6, 0, [])]
                continue

            contacts = self.env["res.partner"].search([
                ("parent_id", "=", lead.partner_id.id),
                ("company_type", "=", "person"),
                ("type", "=", "contact"),
            ], order="name")

            lead.contact_ids = [(6, 0, contacts.ids)]

    def action_add_company_contact(self):
        self.ensure_one()
        if not self.partner_id:
            return False

        partner_form = self.env.ref("base.view_partner_form")

        return {
            "type": "ir.actions.act_window",
            "name": _("Create Contact"),
            "res_model": "res.partner",
            "view_mode": "form",
            "views": [(partner_form.id, "form")],
            "target": "new",
            "context": {
                "default_parent_id": self.partner_id.id,
                "default_company_type": "person",
                "default_is_company": False,
                "default_type": "contact",
            },
        }
