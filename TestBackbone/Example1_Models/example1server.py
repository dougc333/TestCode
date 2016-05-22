from bottle import route,get,post,run,static_file, request


@route('/<filename:path>')
def server_static(filename):
  return static_file(filename,'/Users/dc/Downloads/TestBackbone/Example1_Models')

@get('/api/vehicles')
def foo():
  print "get to route /api/vehicles in function foo"
  vehicles=[ {"registrationNumber":1, "color": "red"},{"registrationNumber":2, "color":"blue"}]
  return dict(data=vehicles);

@post('/api/vehicles')
def postreq():
  print 'postrequest'
  print request.json
  return

run(host='localhost',port=8080, debug='True')

