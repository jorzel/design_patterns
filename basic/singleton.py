
class Borg(object):
    """Borg class making attributes global"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):

    def __init__(self, **kwargs):
        super(Singleton, self).__init__()
        self._shared_state.update(kwargs)
    
    def __str__(self):
        return str(self._shared_state)


x = Singleton(**{'Bad Gateway': 400})
print x
y = Singleton(**{'Not Found': 404})
print y