class SomeClass:
    def __init__(self):
        super().__init__()

    # This is a private func, cause it has __ in the beginning
    def __private_func(self):
        print("private func")


SomeClass().__private_func()
