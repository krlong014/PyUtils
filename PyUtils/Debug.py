from PyUtils.Tab import Tab
import sys

class Debug:
  '''
  Debug is a class with static methods for runtime control of
  the level of diagnostic output.

  In all member functions, the parameters are:

  * verb -- the verbosity level, which determines whether or not a given message gets output.
  * *args -- message components to be output (can be one or more arguments)

  For example, the code fragment below will print the messages before and
  after the loop, but not the message within the loop. If verb is set to 2,
  the message within the loop will be printed as well.::

    verb=1
    Debug.msg1(verb, "About to run loop")
    val = 0
    for i in range(10):
      val = i+val
      Debug.msg2(verb, 'i=', i, ' value is ', val)
    Debug.msg1(verb, 'final val=', val)

  '''

  # By default, write to stdout
  outstream = sys.stdout

  @classmethod
  def msg1(cls, verb, *args):
    '''Write the arguments when verb >= 1.'''
    if verb>=1:
      Debug._write(args)

  @classmethod
  def msg2(cls, verb, *args):
    '''Write the arguments when verb >= 2.'''
    if verb>=2:
      Debug._write(args)

  @classmethod
  def msg3(cls, verb, *args):
    '''Write the arguments when verb >= 3.'''
    if verb>=3:
      Debug._write(args)

  @classmethod
  def msg4(cls, verb, *args):
    '''Write the arguments when verb >= 4.'''
    if verb>=4:
      Debug._write(args)

  @classmethod
  def _write(cls, args):
    for a in args:
      print(a, end='', file=Debug.outstream)
    print('', file=Debug.outstream)

if __name__=='__main__':

  t = Tab()
  def func(verb):
    tab = Tab()
    Debug.msg1(verb, tab, 'verb=%s, message 1' % verb)
    Debug.msg2(verb, tab, 'verb=%s, message 2' % verb)
    Debug.msg3(verb, tab, 'verb=%s, message 3' % verb)
    Debug.msg4(verb, tab, 'verb=%s, message 4' % verb)

  for i in range(1,5):
    print('i=', i)
    func(i)
