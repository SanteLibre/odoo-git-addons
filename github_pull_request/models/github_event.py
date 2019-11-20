# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class GithubEvent(models.Model):

    _name = "github.event"
    _description = "Github Event"

    payload = fields.Text()
