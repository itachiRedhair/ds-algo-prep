class Rank:
    RESPONDER = 0
    MANAGER = 1
    DIRECTOR = 2


class Call:
    __rank = 0

    def __init__(self, caller):
        self.caller = caller
        self.__rank = Rank.RESPONDER

    def set_handler(self, employee):
        handler = employee

    def reply(self):
        pass


class Employee:
    __current_call = None

    def __init__(self):
        pass

    def receive_call(self):
        pass

    def is_free(self):
        pass


class Director(Employee):
    def __init__(self):
        self.rank = Rank.DIRECTOR

class Responder(Employee):
    def __init__(self):
        self.rank = Rank.RESPONDER

class Manager(Employee):
    def __init__(self):
        self.rank = Rank.MANAGER


class CallHandler:
    __LEVEL = 3
    __NUM_RESPONDENTS = 10
    __NUM_MANAGERS = 4
    __NUM_DIRECTORS = 2

    # List of employees by levels
    employee_levels = []

    call_queues = []

    def __init__(self):
        pass

    def get_handler_for_call(self, call):
        pass

    def dispatch_call_by_caller(self, caller):
        call = Call(caller)
        dispatch_call_by_call(call)

    def dispatch_call_by_call(self, call):
        employee = self.get_handler_for_call(call)

        if employee:
            employee.recieve_call(call)
        else:
            call.reply("Please wait for free employee to reply")
            self.call_queues[call.get_rank().get_value()].append(call)
