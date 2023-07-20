url = '<insert url here>'
db = '<insert db here>'

username = '<insert username here>'
password = '<insert password here>'

import xmlrpc.client
import json

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Odoo Server Version Info: ", common.version())

uid = common.authenticate(db, username, password, {})
print("User ID = ", uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})
print("Partner IDs = ",models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5}))

#Using ID 11800 as an existing sales order ID (replace with an actual ID that exists when testing
ids = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['id', '=', 11800]]])
[record] = models.execute_kw(db, uid, password, 'sale.order', 'read', [ids])
print((record))
