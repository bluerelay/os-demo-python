from sanic import response

import apis


def test_get_messages(loop):
    messages = loop.run_until_complete(apis.get_messages(None))
    assert isinstance(messages, response.HTTPResponse)