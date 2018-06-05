import copy

class Prototype(object):
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        if name in self._objects:
            del self._objects[name]
    
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Recruitment(object):
    def __init__(self):
        self.position = 'Software Developer'
        self.status = 'active'
    
    def __str__(self):
        return "{} | {}".format(self.position, self.status)

recruitment = Recruitment()

prototype = Prototype()
prototype.register_object('software_developer', recruitment)

recruitment2 = prototype.clone('software_developer', status='completed')
print recruitment
print recruitment2