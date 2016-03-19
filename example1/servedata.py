from bottle import route,run, static_file

@route("/data.tsv")
def getdata():
  return static_file('data.tsv', root='/Users/dc/Downloads/TestD3/example1/')


run(host='localhost', port=8080, debug=True)

