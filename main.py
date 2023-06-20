from wsgiref.simple_server import make_server


def application(environ, start_response):
    response_body = b"Hello, World!"
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]

    start_response(status, headers)
    return [response_body]


if __name__ == '__main__':
    httpd = make_server("", 8000, application)
    print("Running...")
    httpd.serve_forever()