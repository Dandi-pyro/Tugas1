from xmlrpc.server import SimpleXMLRPCServer #import server

from xmlrpc.server import SimpleXMLRPCRequestHandler #import Request Handler

class RequestHandler(SimpleXMLRPCRequestHandler):
     rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(("127.0.0.1", 8008),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(pow)

    def adder_function(x,y):
        return x + y # return Penjumlahan dari x dan y
    
    class MyFuncs:
        def mul(self, x, y):
            return x * y # Return pembagian dari x dan y
    
    server.register_instance(MyFuncs())

    def minus_function(x, y):
        return x - y # Return pembagian dari x dan y
    
    server.register_instance(minus_function, 'minus')

    def divide_function(x, y):
        return x / y # Return pembagian dari x dan y
    
    server.register_instance(divide_function, 'div')

    server.serve_forever()