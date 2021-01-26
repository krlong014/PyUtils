'''! @ brief Tab management.'''

class Tab:
  '''! Tab is an object for managing tabbed output.

  @param tabsize -- width of tab (number of blank spaces)
  @param depth -- current tab depth
  '''

  tabsize = 2
  depth = 0

  # Increase the tab depth upon constructing a new object
  def __init__(self):
    '''When a Tab constructor is called, the tab depth is increased'''
    self.depth = Tab.depth
    Tab.depth += Tab.tabsize


  # The string representation is the specified number of spaces
  def __str__(self):
    '''Write a Tab to string.'''
    return ' ' * (Tab.tabsize*self.depth)

  # Upon deletion of an object, decrement the tab depth
  def __del__(self):
    '''Tab destructor. Upon deletion of an object, decrement the tab depth.'''
    Tab.depth -= Tab.tabsize

# ------ Test & demo

if __name__=='__main__':
  '''Example'''

  def f1():
    tab = Tab()
    tab1 = Tab()
    print(tab, 'In f1')

    for x in range(4):
      print(tab1, 'x=%g' % x)

    print(tab, 'Calling f2')
    f2()

  def f2():
    tab = Tab()
    print(tab, 'In f2')

  tab = Tab()
  print(tab, 'starting test')
  f1()
  print(tab, 'done test')
