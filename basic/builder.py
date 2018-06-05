class Director(object):
    def __init__(self, builder):
        self._builder = builder
    
    def get_account(self):
        return self._builder.account

    def construct_account(self):
        self._builder.create_new_account()
        self._builder.add_status()
        self._builder.add_permission()


class Builder(object):
    def __init__(self):
        self.account = None
    
    def create_new_account(self):
        self.account = Account()


class StudentBuilder(Builder):
    def add_status(self):
        self.account.status = 'student'
    
    def add_permission(self):
        self.account.permission = 'user'

class StaffBuilder(Builder):
    def add_status(self):
        self.account.status = 'staff'
    
    def add_permission(self):
        self.account.permission = 'superuser'

class Account():
    def __init__(self):
        self.status = None
        self.permission = None

    def __str__(self):
        return "{} | {}".format(self.status, self.permission)


builders = [StudentBuilder(), StaffBuilder()]
for builder in builders:
    director = Director(builder)
    director.construct_account()
    account = director.get_account()
    print account
