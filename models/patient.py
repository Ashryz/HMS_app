from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"
    _rec_name = "first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    age = fields.Integer(compute="compute_age", store=True)
    address = fields.Text()
    image = fields.Binary()
    cr_ratio = fields.Float()
    pcr = fields.Boolean()
    blood_type = fields.Selection([
        ('a_positive', 'A+'), ('a_negative', 'A-'),
        ('b_positive', 'B+'), ('b_negative', 'B-'),
        ('ab_positive', 'AB+'), ('ab_negative', 'AB-'),
        ('o_positive', 'O+'), ('o_negative', 'O-'),
    ])
    history = fields.Html()
    department_id = fields.Many2one('hms.department')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])

    @api.depends("birth_date")
    def compute_age(self):
        for rec in self:
            if rec.birth_date:

                rec.age = relativedelta(fields.Date.today(), rec.birth_date).years
            else:
                rec.age = 0
