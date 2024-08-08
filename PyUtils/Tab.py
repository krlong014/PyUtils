'''! @ brief Tab management.'''

import traceback as tb

class Tab:
  '''! Tab is an object for managing tabbed output.

  @param tabsize -- width of tab (number of blank spaces)
  @param depth -- current tab depth

  Katharine Long
  Department of Mathematics and Statistics
  Texas Tech University
  '''

  tabsize = 2
  depth = 0

  @classmethod
  def tablist(cls, n, live=True):
    rtn = []
    for i in range(n):
      if live:
        rtn.append(Tab())
      else:
        rtn.append('')

    return rtn
  

  # Increase the tab depth upon constructing a new object
  def __init__(self, n:int=1):
    '''When a Tab constructor is called, the tab depth is increased'''
    # print('Tab ctor: depth=', Tab.depth)
    # tb.print_stack(limit=4)
    self.n = n
    self.depth = Tab.depth
    self.open()
#    print('increasing tab depth to ', Tab.depth)


  # The string representation is the specified number of spaces
  def __str__(self):
    '''Write a Tab to string.'''
    return ' ' * self.depth
  
  # Increment the tab depth


  # Upon deletion of an object, decrement the tab depth
  def __del__(self):
    '''Tab destructor. Upon deletion of an object, decrement the tab depth.'''
    if self._in_scope:
      self.close()

  # Increment the tab depth
  def open(self):
    Tab.depth += self.n*Tab.tabsize
    self._in_scope = True

  # Use this to force an artificial closure of scope of the tab, This
  # is for use in loops and conditionals where Python does not close
  # scope at the end of the block
  def close(self):
    # print('Tab close: depth=', Tab.depth)
    # tb.print_stack(limit=4)
    Tab.depth -= self.n*Tab.tabsize
#    print('decreasing tab depth to ', Tab.depth) 
    self._in_scope = False


# ------ Test & demo

if __name__=='__main__':
  '''Example'''

  T = Tab.tablist(4)
  for t in T:
    print(t,'x')

  def f1():
    tab = Tab()
    tab1 = Tab()
    print(tab, 'In f1')

    print(tab1, 'Starting loop')
    for x in range(4):
      tab2 = Tab()
      print(tab2, 'x=%g' % x)
    tab2.close()

    print(tab1, 'Calling f2')
    f2()
    print(tab, 'Done f1')

  def f2():
    tab = Tab()
    print(tab, 'In f2')

    tab1 = Tab()
    tab2 = Tab()

    a = 1

    print(tab1, 'conditional 1')
    if a==1:
      print(tab2, 'true branch')
    else:
      print(tab2, 'false branch')

    print(tab1, 'conditional 2')
    if a==0:
      print(tab2, 'true branch')
    else:
      print(tab2, 'false branch')

    tab2.close()
    
    print(tab1, 'done conditional')
    print(tab, 'Done f2')


  tab = Tab()
  print(tab, 'starting test')
  f1()
  print(tab, 'done test')
