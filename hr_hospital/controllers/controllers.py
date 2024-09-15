# from odoo import http


# class GresDfosfa(http.Controller):
#     @http.route('/gres_dfosfa/gres_dfosfa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gres_dfosfa/gres_dfosfa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gres_dfosfa.listing', {
#             'root': '/gres_dfosfa/gres_dfosfa',
#             'objects': http.request.env[
#                 'gres_dfosfa.gres_dfosfa'
#                 ].search([]),
#         })

#     @http.route('/gres_dfosfa/gres_dfosfa/objects/ \
#         <model("gres_dfosfa.gres_dfosfa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gres_dfosfa.object', {
#             'object': obj
#         })
