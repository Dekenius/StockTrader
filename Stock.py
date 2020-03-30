import time

class Stock:
    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        # Change the value. Commit last value to history
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print 'Changelog for Stock object:'
        for k, v in self.history.items():
            print '%s\t %s' % (k, v)

    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank stock" when we unpickle.
        return self.history

    def __setstate__(self, state):
        # Make self.history = state and last_change and value undefined
        self.history = state
        self.value, self.last_change = None, None


    def __cmp__(self, other):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __round__(self, n=None):
        # not sure this one is necessary
        raise NotImplementedError


    def __add__(self, other):
        # for computing value of portfolio
        raise NotImplementedError

    def __str__(self):

        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        # when updating stock current price?
        raise NotImplementedError
