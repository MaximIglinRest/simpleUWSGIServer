def hello(environ: dict, start_response):
    """Handler for WSGI-server"""
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    print("Type of environ:", type(environ), "- Словарь с мета инфой!")
    print(type(start_response))
    yield 'Привет! Ты запустил тестовый WSGI-сервер.'.encode("utf-8")