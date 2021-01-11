
# Object for tab management in output.
class Tab:
    tabsize = 2
    depth = 0

    # Increase the tab depth upon constructing a new object
    def __init__(self):
        self.depth = Tab.depth
        Tab.depth += Tab.tabsize


    # The string representation is the specified number of spaces
    def __str__(self):
        return ' ' * (Tab.tabsize*self.depth)

    # Upon deletion of an object, decrement the tab depth
    def __del__(self):
        Tab.depth -= Tab.tabsize

# ------ Test & demo

if __name__=='__main__':

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
