__author__ = 'zdvitas'

from pprint import pprint
import xmlrpclib



server = xmlrpclib.Server("https://149.154.167.50/")

result = server.auth.checkPhone("79160159901")
print result
