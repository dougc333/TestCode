#!/usr/bin/python

from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer


class CORS(SimpleHTTPRequestHandler):
   def headers(self):
      self.send.header('Access-Control-Allow-Origin', '*')
      SimpleHTTPRequestHandler.headers(self)


if __name__=='__main)__':
  BaseHTTPServer.test(CORS, BaseHTTPServer.HTTPServer)

