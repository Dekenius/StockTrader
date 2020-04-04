# from googlefinance import getQuotes
import json

class Market:

    # https://stackoverflow.com/questions/16125229/last-key-in-python-dictionary
    
    def __init__(self):
        # open files for stocks and sets them up
        answer = input("Do you want to update")


        raise NotImplementedError

    def __del__(self):
        # makes sure everything saved to files

        raise NotImplementedError

    # def __dir__(self) -> Iterable[str]:
    #     # for the user help method
    #     raise NotImplementedError

    def __contains__(self, item):
        # answer, does my database have this stock
        # or, answer,
        raise NotImplementedError

    def get_data(self):

        print(json.dumps(getQuotes('AAPL'), indent=2))
