# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class todo_app(models.Model):
#     _name = 'todo_app.todo_app'
#     _description = 'todo_app.todo_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models,fields

class ToDo(models.Model):
	_name = "todo.app"
	_description = "Lista de tareas"

	name = fields.Char(string="Nombre")
	description = fields.Char(string="Descripcion")
	state = fields.Char(string="Estado")
	#title = fields.Char(string="titulo")
	#price = fields.Float(string="precio")
