from bottle import route,run, template



@route('/')
def test():
  return "test"

run(host='localhost', port=8080, debug=True)



