# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class inscription(models.Model):
    _name = 'inscription.management'
    _description = 'Gestion inscription'

    name = fields.Char(string='Name', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    date_inscription = fields.Datetime(string=' DateTime', default=fields.Datetime.now())
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    address = fields.Char(string='Address', required=True)
    cin = fields.Char(string='CIN', required=True)
    photo_identity = fields.Binary(string='Photo d’identity')
    ville = fields.Char(string='Ville', required=True)
    region = fields.Char(string='Region', required=True)
    country = fields.Char(string='Pays', required=True)
    status = fields.Selection(
        [('Nouveau', 'Nouveau'),
         ('En cours', 'En cours'),
         ('Termine', 'Termine'),
         ('Annule', 'Annule')],
        default='Nouveau')

    def action_confirm(self):
        self.status = 'En cours'

    def action_done(self):
        self.status = 'Termine'

    def action_cancel(self):
        self.status = 'Annulé'
