import http.server, socketserver, threading, functools
def start(root='/tmp/w/video', port=8765):
    H=functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
    H.log_message=lambda *a: None
    socketserver.TCPServer.allow_reuse_address=True
    s=socketserver.ThreadingTCPServer(('127.0.0.1',port),H); s.daemon_threads=True
    threading.Thread(target=s.serve_forever,daemon=True).start(); return s
