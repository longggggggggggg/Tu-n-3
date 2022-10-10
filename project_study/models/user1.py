from odoo import api, fields, models, tools, _
class api (models.Model):
    _name="study1"
    name=fields.Char(string="study1")
    err=fields.Many2one('project.study',string='user')