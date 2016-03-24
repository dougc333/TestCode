from bottle import route,run,static_file,get,post


@route('/<filename>')
def server_static(filename):
  print "calling server_static"
  return static_file(filename,root='/Users/dc/Downloads/TestBackbone/Example1_Models')


@route('/testcourse',method='POST')
def testpost():
   print "calling testpost()"
   return "return from post function in server.py"


@post('/test')
def foo():
  print 'calling foo'
  return 'this is foo'


run(host='localhost', port=8080, debug=True)

