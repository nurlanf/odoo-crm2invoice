# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class testmodule(models.Model):
#     _name = 'testmodule.testmodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Account(models.Model):
    _inherit = 'account.invoice'

    crm_lead = fields.Many2one('crm.lead', string="Lead/Opportunity", readonly="True")