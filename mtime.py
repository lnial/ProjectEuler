import time
class mtime:
  def __init__(self):
    self.start = time.time()
    self.s = None
    #print 'start ....'

  def star(self):
    self.start = time.time()
  def end(self):
    self.end = time.time()
    #print '...end'
    self.process = self.end - self.start
    self.h = int(self.process / 3600)
    self.process -= self.h / 3600
    self.m = int(self.process / 60)
    self.process -= self.m / 60
    self.s = self.process
    #if unit == 'h':
      #print self.h
    #elif unit == 'm':
      #print self.m
    #elif unit == 's':
      #pass
      ##print self.s

