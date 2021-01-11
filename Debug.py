

class Debug:

    @classmethod
    def msg1(cls, verb, *args):
        if verb>=1:
            Debug.write(args)

    @classmethod
    def msg2(cls, verb, *args):
        if verb>=2:
            Debug.write(args)

    @classmethod
    def msg3(cls, verb, *args):
        if verb>=3:
            Debug.write(args)

    @classmethod
    def msg4(cls, verb, *args):
        if verb>=4:
            Debug.write(args)

    @classmethod
    def write(cls, args):
        for a in args:
            print(a, end='')
        print('')

if __name__=='__main__':

  def func(verb):

    Debug.msg1(verb, 'verb=%s, message 1' % verb)
    Debug.msg2(verb, 'verb=%s, message 2' % verb)
    Debug.msg3(verb, 'verb=%s, message 3' % verb)
    Debug.msg4(verb, 'verb=%s, message 4' % verb)

  for i in range(1,5):
    func(i)
