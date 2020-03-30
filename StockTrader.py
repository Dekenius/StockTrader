
import time



def say_hi():
    print("hi")



def main():
    print("main run")

    # print('hello world')
    # sec = input('Let us wait for user input. Let me know how many seconds to sleep now.\n')
    # time.sleep(int(sec))
    # print('time passed')

    while(True):
        new_input = input("I parrot what you say.")
        if new_input == 'end':
            print("goodbye")
            break
        else:
            print(new_input)





if __name__ == '__main__':
    main()



