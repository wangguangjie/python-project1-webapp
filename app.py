import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>AweSome</>')

@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)