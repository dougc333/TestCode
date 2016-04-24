#!/usr/bin/env python


import logging
from cm_api.api_client import ApiResource

LOG=logging.getLogger(__name__)

CM_HOST='r2341-d-us01.dssd.com'
CM_USER='admin'
CM_PASSWORD='admin'



class ImpalaQuery(object):
  """
  """
  def __init__(self):
    self._api=ApiResource(CM_HOST, username=CM_USER, password=CM_PASSWORD, False)

  try:
    opts, args - getopt.getopt(argv[1:],"hf:t") 
  except getopt.GetoptError, err:
    #print >>sys.stderr, err
    #return -1

  def query(self, query, from_time, to_time):
    return self._api_query_timeseries(query, from_time, to_time)

# end class Impala Query


def do_print(response):
    """
    """
    print response

def do_query(q, from_time, to_time):
  """
  """
  tsquery = TimeSeriesQuery()
  for response in tsquery.query(q, from_time, to_time):
    do_print(response)

def usage():
  """
  """

def setup_logging(level):
  """
  """
  logging.basicConfig()
  logging.getLogger().setLevel(level)


def main(argv):
  setup_logging(logging.INFO)
  
  from_time = None
  to_time=None
  
  try:
    opts,args=getopt.getopt(argv[1:], "hf:t")
  except getopt.GetoptError, err:
    print >> sys.stderr, err
    usage()
    return -1

  for option, val in opts:
    if option=='-h':
      usage()
      return -1
    elif option == '-f':
      try:
        print val
        from_time=datetime.strptime(val,"%Y-%m-%dT%H:%M"  
    

if __name__ == '__main__:
   sys.exit(main(sys.argv))
