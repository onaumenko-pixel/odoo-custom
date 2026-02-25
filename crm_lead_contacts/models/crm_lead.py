from odoo import models, fields, _

class CrmLead(models.Model):
    _inherit = "crm.lead"

    # показываем контакты компании (дочерние контакты партнера)
    contact_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Contacts",
        related="partner_id.child_ids",
        readonly=True,
    )

    def action_add_company_contact(self):
        self.ensure_one()
        if not self.partner_id:
            return False

        return {
            "type": "ir.actions.act_window",
            "name": _("Create Contact"),
            "res_model": "res.partner",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_parent_id": self.partner_id.id,   # привязка к компании
                "default_type": "contact",                 # контактное лицо
                "default_company_type": "person",          # физ. лицо
            },
        }
