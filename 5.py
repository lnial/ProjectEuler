import time

quotient = 10
flagEnd = 0
degug = TimePrintDebug()

while 1:
  quotient += 1
  count = 0

  degug.tb = datetime.datetime.now()
  degug.value = quotient


  for i in range(1, 21):
    if quotient % i == 0:
      count += 1
    if count == 20:
      flagEnd = 1
  if flagEnd == 1:
    break

print quotient


class TimePrintDebug()
  def __init__(self, time, ta, tb, value)
  #if init time, ta, tb
  ta = datetime.datetime.now()
  self.time = tb - ta
  if self.time >= 1:
    print self.value


#for i in range(1, 10):
  #print i



#quotient = 10
#flagEnd = 0
#while 1:
  #break
  #quotient += 1
  #for i in range(1, 11):
      #flagCount = 0
      #if quotient % i == 0:
          #flagCount += 1
          #if flagCount == 10:
            #flagEnd = 1
            #print quotient
  #if flagEnd == 1:
      #break

