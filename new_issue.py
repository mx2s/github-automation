import json
from urllib.request import Request, urlopen

config = json.loads(open('./config/config.json', 'r').read())

req = Request('https://api.github.com/repos/mxss/gitcom-api/issues/1')
req.add_header('Authorization', 'xxx')
content = urlopen(req).read()

print(content)
