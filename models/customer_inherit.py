from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomerInherit(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains("email")
    def check_duplicat_email(self):
        for rec in self:
            if rec.related_patient_id and rec.related_patient_id.email == rec.email:
                raise ValidationError('Email already exists in the patient model.')
