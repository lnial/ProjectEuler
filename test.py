import mtime

def foo():
  t = mtime.mtime()
  for i in range(1000000):
    pass
  t.end()
  t.tprint('s')

foo()


