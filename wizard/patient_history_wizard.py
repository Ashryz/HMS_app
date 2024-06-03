from odoo import fields, models, api


class PatientHistory(models.TransientModel):
    _name = 'hms.patient.history'
    _description = "Patient History Wizard"

    patient_id = fields.Many2one('hms.patient', readonly=True)
    create_by = fields.Many2one('res.users', default=lambda self: self.env.user, readonly=True)
    date = fields.Datetime(default=fields.Datetime.now, readonly=True)
    description = fields.Text(required=True)

