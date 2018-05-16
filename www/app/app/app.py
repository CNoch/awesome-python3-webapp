import logging
import asyncio,os
import json,time
from datetime import datetime
from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>')

#@asyncio.coroutine

def main():
	pass

if __name__ == '__main__':
	main()
