import time
from Tab import *
from Debug import *

class TimeMonitor:
  """A docstring"""

  timeData = {}

  def report():
      print('\n------- Timing summary ------\n')
      maxLen = 0
      for k in TimeMonitor.timeData.keys():
          if len(k) > maxLen: maxLen = len(k)

      f = '%{}s %12.5g'.format(maxLen+4)
      for k,v in TimeMonitor.timeData.items():
          print(f % (k,v))
      print('\n-----------------------------')

class Timer:
  def __init__(self, name):
      if name not in TimeMonitor.timeData:
          TimeMonitor.timeData[name] = 0.0
      self.name = name
      self.start = time.time()

  def __del__(self):
      total = time.time() - self.start
      TimeMonitor.timeData[self.name] += total

  def walltime(self):
      return TimeMonitor.timeData[self.name]



# ------ Test & demo



def f1(verb=0):
  timer = Timer('f1')
  tab = Tab()
  tab1 = Tab()
  Debug.msg1(verb, tab, 'In f1')

  for x in range(4):
      time.sleep(0.3)
      Debug.msg2(verb, tab1, 'x=%g' % x)

  Debug.msg1(verb, tab, 'Calling f2')
  f2(verb)

def f2(verb=0):
  timer = Timer('f2')
  tab = Tab()
  time.sleep(0.1)
  Debug.msg1(verb, tab, 'In f2')


def main():
  tab = Tab()
  timer = Timer('main')

  verb = 3
  Debug.msg1(verb, tab, 'starting test')
  f1(verb)
  Debug.msg1(verb, tab, 'done test')

if __name__=='__main__':
  main()
  TimeMonitor.report()
