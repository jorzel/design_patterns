import time

class Producer(object):
    """ Relatively more 'resource-intensive' object """

    def produce(self):
        print('Producer is working hard')
    
    def meet(self):
        print('Producer has time to meet')


class Proxy(object):
    """ 
        Relatively less 'resource-intensive' object
        Creating Producer is expensive so Proxy
        is responsible for handling requests from Quest
    """

    def __init__(self):
        self.producer = None
        self.is_occupied = False
    
    def produce(self):
        if not self.is_occupied:
            self.producer = Producer()
            time.sleep(2)
            
            self.producer.meet()
        else:
            time.sleep(2)
            print('Producer is busy!')


proxy = Proxy()
proxy.produce()

proxy.is_occupied = True
proxy.produce()