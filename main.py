
import time
import Market
import Stock
import os
import pickle

def say_hi():
    print("hi")



def main():
    print("main started")

    # print('hello world')
    # sec = input('Let us wait for user input. Let me know how many seconds to sleep now.\n')
    # time.sleep(int(sec))
    # print('time passed')


    market = Market
    # print(market.__dir__())
    stock1 = Stock.Stock("APPL", 9)
    # print(stock1.get_value())
    # stock1
    todo = []
    # print(market.get_data())
    while(True):
        if len(todo) > 0:
            new_input = todo[0]
            todo = todo[1:]
            print(new_input)
        else:
            new_input = input("What do you want to do?\n")


        if new_input == 'end':
            print("goodbye")
            break
        elif new_input == 'many':
            todo += ["change", "change", "print"]
        elif new_input == 'change':
            print("increased by one")
            stock1.change(stock1.get_value() + 1)
        elif new_input == 'print':
            try:
                stock1
            except:
                print("stock1 doesn't exist")
            else:
                stock1.print_changes()
        # elif new_input == 'sethistory':
        #     stock1.history = {'foo': False, 'bar': True}
        elif new_input == 'pickle':
            # os.remove("data.pkl")
            jar = open('data.pkl', 'wb')
            pickle.dump(stock1, jar) # write the pickled data to the file jar
            jar.close()
            # del self
            # stock1.save()
            del stock1
        elif new_input == 'unpickle':
            print("loading")
            pkl_file = open('data.pkl', 'rb') # connect to the pickled data
            x = pickle.load(pkl_file) # load it into a variable
            print(x.history)
            print("wowee\n\n\n")
            stock1 = Stock.Stock("AMZ", 20, x.history)
            pkl_file.close()
            pass
            # stock1 = Stock.load()
        elif new_input == 'getvalue':
            try:
                stock1
            except:
                print("stock1 doesn't exist")
            else:
                print(stock1.get_value())
        else:
            print(new_input)
        print('\n')




# if __name__ == '__main__':
main()



