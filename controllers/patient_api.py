import json

from odoo import http
from odoo.http import request


class PatientApi(http.Controller):

    @http.route('/test', methods=['GET'], type='http', auth='none', csrf=False)
    def test_connection(self):
        pass

    @http.route('/patient/<int:patient_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_patient(self, patient_id):
        res = request.env['hms.patient'].sudo().search([('id', '=', patient_id)])
        return {
            "id": res.id,
            "first_name": res.first_name,
            "last_name": res.last_name,
            "birth_date": res.birth_date,
        }

    @http.route('/patient', methods=['POST'], type='json', auth='none', csrf=False)
    def add_patient(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['hms.patient'].sudo().create(vals)
        return {
            "msg": "record created successfully ",
            "first_name": res.first_name,
            "last_name": res.last_name,
            "birth_date": res.birth_date,
        }
