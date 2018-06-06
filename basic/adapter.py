class PolishSpeaker(object):
    def __init__(self):
        self.name = 'Polish'
    
    def speak_polish(self):
        return 'hej!'
    

class EnglishSpeaker(object):
    def __init__(self):
        self.name = 'English'
    
    def speak_english(self):
        return 'hello!'


class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        self._object = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


objects = []

polish = PolishSpeaker()
english = EnglishSpeaker()

objects.append(Adapter(polish, speak=polish.speak_polish))
objects.append(Adapter(english, speak=english.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))