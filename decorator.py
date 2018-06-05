from functools import wraps
from datetime import datetime

def measure_time(function):

    @wraps(function)
    def decorator(*args, **kwargs):
        start = datetime.now()
        ret = function(*args, **kwargs)
        end = datetime.now()
        return "{} | Time elapsed: {}".format(ret, end - start)
    
    return decorator

@measure_time
def show_text(text):
    return text

print(show_text('Takie tam testy'))
print(show_text('Argumenty w dekoratorze i tyle'))
print(show_text.__name__)
