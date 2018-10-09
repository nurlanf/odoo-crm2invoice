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

class CRM(models.Model):
    _inherit = 'crm.lead'

    x_crm_lead__account_invoice_count = fields.Integer(compute ='_results')

    @api.multi
    def _results(self):
    results = self.env['account.invoice'].read_group([('crm_lead', 'in', self.ids)], 'crm_lead', 'crm_lead')
    dic = {}
    for x in results: dic[x['crm_lead'][0]] = x['crm_lead_count']
    for record in self: record['x_crm_lead__account_invoice_count'] = dic.get(record.id, 0)
