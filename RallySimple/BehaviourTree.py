class Atomic():
    """
    Abstract implementation of an atomic action
    """
    def __init__(self, func):
        self.func = func

    def run(self):
        #print self.func.__name__
        return self.func()


class Task(object):
    """ Abstract Task implementation
    """

    def __init__(self):
        super(Task,self).__init__()

    def __init__(self,*children):
        self._children = []
        for child in children:
            self._children.append(child)

    def run(self):
        pass

class Selector(Task):
    """   Selector Implementation   """

    def run(self):
        for c in self._children:
            if c.run() :
                return True
        return False


class Sequence(Task):
    """   Sequence Implementation   """

    def run(self):
        for c in self._children :
            if not c.run() :
                return False
        return True