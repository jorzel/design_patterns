
class Employer(object):
    def __init__(self, name=None):
        self.name = name
    
class EmployerFactory(object):
    def get_employer(self):
        raise NotImplementedError('Abstract class Employer cannot create objects')

class Developer(Employer):
    def __str__(self):
        return 'developer {0}'.format(self.name)

class DeveloperFactory(object):
    def get_employer(self):
        return Developer('John')

class Manager(Employer):
    def __str__(self):
        return 'manager {0}'.format(self.name)

class ManagerFactory(EmployerFactory):
    def get_employer(self):
        return Manager('Helmut')
    

class Company(object):
    def __init__(self, employer_factory):
        self._employer_factory = employer_factory

    def show_employer(self):
        employer = self._employer_factory.get_employer()
        print employer

factory = DeveloperFactory()
company = Company(factory)
company.show_employer()