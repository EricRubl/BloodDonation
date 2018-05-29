import json

import requests


def markdown_file_to_html(md_file):
    try:
        path = 'static/Documentation/' + md_file + '.md'
        file_content = open(path, "r").read()
        params = {
            'text': file_content,
            'mode': 'gfm',
            'context': 'github/Japjappedulap'
        }
        req = requests.post('https://api.github.com/markdown', data=json.dumps(params))
        return req.text
    except Exception as e:
        return e


