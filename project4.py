#Problem #4

import time, os, webbrowser

class Construction():
    def __init__(self):
        webbrowser.open('https://www.youtube.com/watch?v=hl_9_q_uLF8', new=2, autoraise=True)

    def destructor(self):
        webbrowser.open('https://youtu.be/JwXohnAYyuc?t=22s', new=2, autoraise=True)


def main():
    print("Hit enter to Build and Destroy ")
    con = Construction()
    print("Built")
    print("In 15 seconds the next video will open. ")
    time.sleep(15.0)
    con.destructor()
    print("Destroyed")

main()