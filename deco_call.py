#!/usr/local/python2.7/bin/python2.7
import re

class Route(object):
    def __init__(self):
        self.map = []
 
    def match(self, url):
        for r, f in self.map:
            m = r.match(url)
            if m:
                return f, m.groups()
                print 'ok'
        print 'WARNING :', url, 'not match any hanlder'
        return None, None
    def __call__(self, path):
        if not path.endswith('$'):
            path += '$' 
        re_path = re.compile(path)
        #def _(func):
        #    self.map.append((re_path, func))
        #    return func
        #return _
        #return True

class Handler(object):

    def __init__(self, request):
        p = urlparse(request.url)
        request.arguments = parse_qs(p.query, 1)
        self.request = request
        self.html = request.content

    def get_argument(self, name, default=None):
        result = self.request.arguments.get(name, None)
        if result is None:
            return default
        return result[0].encode('utf-8', 'ignore')

    def extract(self, begin, end):
        return extract(begin, end, self.html)

    def extract_all(self, begin, end):
        return extract_all(begin, end, self.html)

route = Route()

@route('/portal\.php')
class portal(Handler):
    def get(self):
        #for link in self.extract_all('<dt class="xs2"><a href="', '"'):
            pass

print route.map
