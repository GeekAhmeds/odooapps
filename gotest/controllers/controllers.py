# -*- coding: utf-8 -*-
# from odoo import http


# class Gotest(http.Controller):
#     @http.route('/gotest/gotest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gotest/gotest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gotest.listing', {
#             'root': '/gotest/gotest',
#             'objects': http.request.env['gotest.gotest'].search([]),
#         })

#     @http.route('/gotest/gotest/objects/<model("gotest.gotest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gotest.object', {
#             'object': obj
#         })
