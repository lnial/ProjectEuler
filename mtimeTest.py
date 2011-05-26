import mtime

def foo():
  t = mtime.mtime()
  for i in range(1000000):
    pass
  t.end()
  print t.s

  #print t.getTime()

foo()


