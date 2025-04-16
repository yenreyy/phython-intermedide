import random 
import time

def typing_speed_test():
    words = ["elephant","giraffe","chocolate","butterly","adventure"]
    word = random.choice(words)

    print("welcome to typing speed test")
    print(f"type the following word as fast you can: {word}")
    input("press enter to start...")

    start_time = time.time()
    user_input = input("type here:")
    end_time = time.time()
    if user_input == word:
        time_taken = round(end_time - start_time, 2)
        print(f"great job yoy took{time_taken} second.")
    else:
        print(f"oops you typed it incorrectly.the correct words was '{word}'.try again")

if __name__  == "__main__":
    typing_speed_test()
