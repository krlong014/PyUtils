if __name__!='__main__':
  from . Tab import Tab
else:
  from Tab import Tab

def prettyPrintDict(d : dict, endWithComma=False):
  t0 = Tab()
  t1 = Tab()
  
  print('{}{{'.format(t0))
  keys = list(d)
  for i,k in enumerate(keys):
    v = d[k]
    if isinstance(v, dict):
      print('{}{}:'.format(t1,k))
      if i==len(keys)-1:      
        prettyPrintDict(v)
      else:
        prettyPrintDict(v, True)
    else:
      if i==len(keys)-1:      
        print('{}{} : {}'.format(t1, k, v))
      else:    
        print('{}{} : {},'.format(t1, k, v))
    
  t1.close()

  if endWithComma:
    print('{}}},'.format(t0))
  else:
    print('{}}},'.format(t0))

if __name__=='__main__':

  d = {
    1 : 3.14,
    'a' : 'bob',
    'p' : {'A':1,'B':2,'C':3},
    'q' : -3,
    'r' : 'fred'
  }

  prettyPrintDict(d)

