
import time
import os


def install():
    print("install dependencies\n>1 Linux :3\n>2 Windows :(")

    inp = input(">")

    def do_it_yourself():
        print("so what the frick do you have...")
        time.sleep(1.5)
        print("you know what, just do it yourself <3")
        print("install pygame and re")

    if inp == "1":
        print("\n>1 pip\n>2 pacmen\n>3 dnf\n")
        inp = input(">")

        if inp == "1":
            os.system(f"sudo pip install pygame re")
        elif inp == "2":
            os.system(f"sudo pacman -S python-pygame")
        elif inp == "3":
            os.system(f"sudo dnf install python3-pygame")
        else:
            do_it_yourself()


    elif inp == "2":
        print("\n>1 pip\n")
        inp = input(">")

        if inp == "1" or inp == "":
            os.system(f"pip install pygame re")
        else:
            do_it_yourself()




install()
