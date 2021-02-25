import random
import time
import os

words = """stroke score hallway care rubbish voucher acceptable agreement twist alarm chorus poll judicial absent ensure addition favor violation concern perfume forum grain
        compose breakdown sport spoil dare distributor frighten profession convince miserable fault view bay wreck cancer creation turkey hot sit constellation shed medal
        consciousness promote charismatic oven kid skeleton latest thread mutual porter pierce depend museum choice filter answer desert supply impact market winner switch
        listen expect lawyer ethnic dragon option method asylum exceed gossip accept strict belong seller pocket mature import forget appeal orange studio remind second linger
        review sodium flight record cheese theory clinic chorus export unique"""

word_list = list(words.split())

def countdown():
    for i in range (3, 0 , -1):
        print ("Test starts in : " + str(i))
        time.sleep(1)
        os.system("cls")

def test():
    score, wrong = 0, 0 #have to declare var here only as below when increment is made, python will create a local var for this block and if it was mentioned above, error will be raised as no local definition will be found
    start_time = time.time()
    seconds = 60
    while (1):
        current_time = time.time()
        elapsed_time = current_time - start_time
        if(elapsed_time > seconds):
            os.system("cls")
            print("Test has ended")
            print("WPMM: " + str(score)) #imp convert integers to string
            print("Wrong: " + str(wrong))
            x = input() # dummy input wait so that applicaion doesn't close abruptly
            break
        else:
            curr_word = random.choice(word_list)
            print(curr_word)
            user_input = str(input())
            if(curr_word == user_input):
                score += 1
            else:
                wrong += 1
            os.system("cls")

countdown()
test()
