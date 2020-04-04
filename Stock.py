import time
import pickle
import os

class Stock:
    def __init__(self, name, value, history={}):
        self.name = name
        self.value = value
        self.last_change = time.asctime()
        # if history == None:
        self.history = history
        # else:
        # self.history = history

    def change(self, new_value):
        # Change the value. Commit last value to history
        while self.last_change == time.asctime():
            pass
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print('Changelog for Stock object:')
        for k, v in self.history.items():
            print('%s\t %s' % (k, v))

    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank stock" when we unpickle.
        return self.history

    def __setstate__(self, state):
        # Make self.history = state and last_change and value undefined
        self.history = state
        self.value, self.last_change = None, None

    # def save(self):
    #     pass
    #
    # @staticmethod
    # def load():
    #

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

    def get_value(self):

        return self.value
