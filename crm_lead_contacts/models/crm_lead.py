from odoo import models, fields, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_ids = fields.One2many(
        comodel_name="res.partner",
        related="partner_id.child_ids",
        string="Contacts",
        readonly=True,
    )

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
