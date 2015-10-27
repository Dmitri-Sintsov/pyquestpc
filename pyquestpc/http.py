import http.client, urllib.parse, json
from .sdv import dbg, get_nested


def build_url(fn):
    def wrapper(self, *args, **kwargs):
        if len(args) > 0:
            return fn(self, *args)
        path = kwargs['path']
        if 'query' in kwargs:
            path += '?' + urllib.parse.urlencode(kwargs['query'], doseq=True)
        fn_args = list(args)
        # dbg('fn_args original', fn_args)
        fn_args.append(path)
        # dbg('fn_args passed', fn_args)
        return fn(self, *fn_args)
    return wrapper


class Error(Exception):

    def __init__(self, status, data):
        self.status = status
        self.data = data

    def __str__(self):
        return repr({'status': self.status, 'data': self.data})


class Fetch(object):

    def __init__(self, host, port=80, timeout=60):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.conn = http.client.HTTPConnection(self.host, self.port, timeout=self.timeout)
        self.lastPath = None
        self.on_retry = lambda : None

    @build_url
    def get(self, path):
        # set_trace()
        self.lastPath = path
        attempts = 3
        while attempts > 0:
            try:
                self.conn.request('GET', self.lastPath)
                resp = self.conn.getresponse()
                if resp.status == 200:
                    break
                else:
                    raise Error(resp.status, ''.join([self.conn.host, self.lastPath]))
            except Exception as e:
                if attempts == 1:
                    raise e
                else:
                    self.conn.close()
                    self.conn = http.client.HTTPConnection(self.host, self.port, timeout=self.timeout)
                    self.on_retry()
            attempts -= 1
        return resp.read()

    @build_url
    def get_json(self, path):
        _str = self.get(path)
        return json.loads(_str.decode())
