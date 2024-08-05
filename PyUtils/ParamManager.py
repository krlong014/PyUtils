# ============================================================================
#
# Functions to manage dictionaries of parameters
#
# Katharine Long
# Department of Mathematics and Statistics
# Texas Tech University
# katharine.long@ttu.edu
# ============================================================================

from abc import ABC, abstractmethod

def validateKeys(inputDict, knownKeys):
  '''
  Check a dictionary's keys against a container of known keys.
    * inputDict -- the dictionary to be checked
    * knownKeys -- container of known keys
  This function will return a set containing the keys appearing in the 
  input dictionary but not in the set of known keys.
  '''

  unknownKeys = set()

  for k in inputDict.keys():
    if k not in knownKeys:
      unknownKeys.add(k)

  return unknownKeys


def getDefaultParams(spec):
  '''
  Given a parameter specification dictionary 
  {'paramKey' : (paramType, defaultValue, validation), etc}
  extract the default values to make a dictionary
  {'paramKey' : defaultValue}.
  '''
  rtn = {}
  for k,v in spec.items():
    rtn[k] = v[1]

  return rtn

def validateParam(paramSpec, userParams, key):

  # Give up if the key isn't found in the specifications list
  try:
    spec = paramSpec[key]
  except KeyError:
    raise RuntimeError('Key [{}] not found in parameter spec {}'.format(
      key, paramSpec)
    )
  
  # Check that the parameter specification has three entries. 
  if len(spec) != 3:
    raise RuntimeError('Parameter specification for key=[{}] has length {}, '\
                       'expected 3. Specification is {}'.format(
                         key, len(p), p
                       ))
  
  
  # Now see if the user has specified the parameter. If so, use it. Otherwise,
  # use the default value given in the specification. 
  if key in userParams:
    val = userParams[key]
  else:
    val = spec[1] 
  
  # Now do validation
  param_type = spec[0]
  param_check = spec[2]

  # Type check
  if not isinstance(val, param_type):
    raise TypeError('Parameter key=[{}], value=[{}] expected to get '\
                       'type [{}], found type=[{}]'.format(key,val,
                                                      param_type,type(val)))
  
  # Predicate check (for example, positivity)
  if param_check != None and not param_check(val):
    raise ValueError('Parameter key=[{}], value=[{}] has invalid value: {}'\
                       .format(key,val,param_check.failure_msg(val)))

  # The parameter's type and value check out, so return the value
  return val


class ParamCheck(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def __call__(self, x):
    pass

  def failure_msg(self, x):
    return 'value {} failed parameter check {}.'.format(x, self)
  
class IsPositive(ParamCheck):
  def __init__(self):
    super(ParamCheck, self).__init__()

  def __call__(self, x):
    return x > 0
  
  def failure_msg(self, x):
    return 'value {} expected to be positive.'.format(x)

  
class IsNonNegative(ParamCheck):
  def __init__(self):
    super(ParamCheck, self).__init__()

  def __call__(self, x):
    return x >= 0
  
  def failure_msg(self, x):
    return 'value {} expected to be non-negative.'.format(x)


class IsOneOf(ParamCheck):
  def __init__(self, s):
    super(ParamCheck, self).__init__()
    self._s = s

  def __call__(self, x):
    return x in self._s
  
  def failure_msg(self, x):
    return 'value {} expected to be in set {}.'.format(x, self._s)

class IsCallable(ParamCheck):
  def __init__(self):
    pass

  def __call__(self, x):
    return callable(x)
  
  def failure_msg(self, x):
    return 'value {} expected to be callable.'.format(x)




# --------- Example

if __name__=='__main__':

  spec = {
    'n' : (int, 10, IsPositive()),
    'method' : (str, 'CG', IsOneOf({'CG', 'GMRES', 'BICGSTAB'})),
    'tau' : (float, 0.0001, IsPositive()),
    'verb' : (int, 0, IsNonNegative())
  }
   
  user = {
    'tau' : 0.005,
    'n' : 1.5,
    'method' : 'QMR'
  }  

  print('\ndefaults = ', spec)
  print('\nuser = ', user)
  
  err_caught = False

  try:
    n = validateParam(spec, user, 'n')
  except TypeError as err:
    print('Correctly detected type error {}'.format(err))
    err_caught = True

  if not err_caught:
    print('FAILED to detect type error in parameter n')

  err_caught = False
  try:
    n = validateParam(spec, user, 'method')
  except ValueError as err:
    print('Correctly detected value error {}'.format(err))
    err_caught = True

  if not err_caught:
    print('FAILED to detect value error in parameter method')

  err_caught = False
  try:
    tau = validateParam(spec, user, 'tau')
  except Exception as ex:
    print('FAILURE! Exception detected when parsing param tau')
  print('tau = ', tau)
  
  err_caught = False
  try:
    verb = validateParam(spec, user, 'verb')
    print('verb  p= ', verb)
  except Exception as ex:
    print('FAILURE! Exception detected when parsing param verb')
    print('Details: {}'.format(ex))

 