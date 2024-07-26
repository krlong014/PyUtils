
class XMLHeader:
    def __init__(self, tag):
        self.tag = tag
        self.attributes = {}

    def addAttribute(self, name, val):
        self.attributes[name]=str(val)

    def __str__(self):
        h = '<' + self.tag
        for k,v in self.attributes.items():
            h = '%s %s=\"%s\"' % (h, k, v)
        h = h + '>'
        return h

    def footer(self):
        return '</%s>' % self.tag

    def writeHeader(self, file):
        file.write(str(self) + '\n')

    def writeFooter(self, file):
        file.write(self.footer() + '\n')





if __name__=='__main__':

    import sys

    h = XMLHeader('Test')
    h.addAttribute('n', 32)
    h.addAttribute('color', 'blue')
    h.addAttribute('pi', 3.14)

    h.writeHeader(sys.stdout)
    sys.stdout.write('bob\n')
    h.writeFooter(sys.stdout)
