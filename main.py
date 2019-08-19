from http.server import BaseHTTPRequestHandler,HTTPServer
import json
import socketserver
import clipboard
import keyboard, func, sysevent, mouse


PORT_NUMBER = 2207

#todo: create 2 processes 1 for http and 1 for tsp socket
#This class will handles any incoming request from
#the browser((
# class myHandler(BaseHTTPRequestHandler):
#
#     #Handler for the GET requests
#     def do_GET(self):
#
#         act = func.qsGetStrByName(self.path, 'act')
#         data = func.qsGetStrByName(self.path, 'data')
#
#         if act in keyboard.VK_CODE:
#             keyboard.press(act)
#         elif act in mouse.EVENTS:
#             mouse.do(act, data)
#         elif act in sysevent.EVENTS:
#             sysevent.do(act)
#
#         self.send_response(200)
#         self.send_header('Content-type','text/html')
#         self.end_headers()
#         # Send the html message
#         self.wfile.write(bytes(act, 'UTF-8'))
#         return
#
# try:
#     #Create a web server and define the handler to manage the
#     #incoming request
#     server = HTTPServer(('', PORT_NUMBER), myHandler)
#     print ('Started httpserver on port ' , PORT_NUMBER)
#
#     #Wait forever for incoming htto requests
#     server.serve_forever()
#
# except KeyboardInterrupt:
#     print ('^C received, shutting down the web server')
#     server.socket.close()

# ----------- TCP Server -------------
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        req_str = self.data.decode("utf-8")
        req_dict = json.loads(req_str)
        print(req_dict)
        act = req_dict['act']
        val = req_dict['val']
        if 'data' in req_dict:
            data = req_dict['data']
        else:
            data = {}

        if act == 'press':
            if val in keyboard.VK_CODE:
                keyboard.press(val)
            elif val in keyboard.VK_CODE_SHIFT:
                keyboard.shiftPress(val)
        elif act == 'mouse':
            if val in mouse.EVENTS:
                mouse.do(val, data)
        elif act == 'system':
            if val in sysevent.EVENTS:
                sysevent.do(val)
        elif act == 'str':
            if val != "":
                clipboard.print_str(val)

        # if 'data' in req_dict:
        #     data = req_dict['data']
        # else:
        #     data = {}
        # if act in keyboard.VK_CODE:
        #     keyboard.press(act)
        # elif act in keyboard.VK_CODE_SHIFT:
        #     keyboard.shiftPress(act)
        # elif act in mouse.EVENTS:
        #     mouse.do(act, data)
        # elif act in sysevent.EVENTS:
        #     sysevent.do(act)

        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


try:
    HOST, PORT = "0.0.0.0", 2208
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print('Started tcp on port ', PORT)
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()