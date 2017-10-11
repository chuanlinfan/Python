import traceback

try:
  xxx
except Exception, e:
  traceback.print_exc()
  print str(e)
  sys.exit(1)
