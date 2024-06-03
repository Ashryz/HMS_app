from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"
    _rec_name = "first_name"

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
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
    history_ids = fields.One2many('hms.patient.history', 'patient_id')
    department_id = fields.Many2one('hms.department')
    doctor_ids = fields.Many2many('hms.doctor')
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

    def write(self, vals):
        res = super(Patient, self).write(vals)
        if 'state' in vals:
            for patient in self:
                self.env['hms.patient.history'].create({
                    'patient_id': patient.id,
                    'description': f'State changed to {patient.state}',
                    'date': fields.Datetime.now(),
                    'create_by': self.env.uid
                })
        return res

    @api.onchange('age')
    def check_age(self):
        for rec in self:
            if not rec.age:
                return {}
            elif rec.age < 30:
                rec.pcr = True
                return {
                    'warning': {
                        'title': 'Warning!',
                        'message': 'PCR checked automatically cause to age less than 30.'
                    }
                }
