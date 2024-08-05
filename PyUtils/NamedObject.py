# ============================================================================
#
# Class NamedObject is a base class for objects that have names and can report
# a short self-descripton. 
#
# Katharine Long
# Department of Mathematics and Statistics
# Texas Tech University
# katharine.long@ttu.edu
# ============================================================================

class NamedObject:
  '''NamedObject is a base class for objects with names.'''

  def __init__(self, name=''):
    '''Constructor.'''
    self._name = name

  def name(self):
    '''Return the name of the object.'''
    return self._name
  
  def description(self, verb : int):
    '''
    Describe this object with a level of detail indicated by the verbosity 
    argument. The default implementation simply returns the name. You'll
    probably want to override this. 

    Input:
      * verb -- an integer indicating how much information to provide. Higher
          means more. 

    Output:
      A descriptive string.
    '''

    return self.name()


