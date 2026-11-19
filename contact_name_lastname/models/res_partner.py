from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    names = fields.Char(
        string='Names',
    )
    mother_surname = fields.Char(
        string='Mother Surname'
    )
    father_surname = fields.Char(
        string='Father Surname'
    )
