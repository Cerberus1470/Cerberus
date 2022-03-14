import Loading


class SystemInfo:

    def __init__(self):
        return

    def __repr__(self):
        return "< This is a System Info class named " + self.__class__.__name__ + ">"

    @staticmethod
    def main(versions):
        print("\nSYSTEM INFO")
        print("Software: POCS (Python Operating Command System) Version %s" % (versions["main"]))
        print("Shell: Python IDLE Version 3.10")
        print("Applications installed: 6")
        print("Applications: Jokes, Notepad, Bagels, Tic-Tac-Toe, Task Manager, User Settings, and System Info")
        print("Jokes Version: %s" % versions["jokes"])
        print("Notepad Version: %s" % versions["notes"])
        print("Bagels Version: %s" % versions["bagels"])
        print("Tic-Tac-Toe Version: %s" % versions["tictactoe"])
        print("User Settings Version: %s" % versions["userset"])
        print("System Info Version: %s" % versions["sysinfo"])
        print("Press [ENTER] or [return] to return to the applications screen!")
        if input() == "debug":
            # here is the animation
            Loading.testing_hash()

        return

# SystemInfo.main({"main": 11.0, "jokes": 1.2, "notes": 1.3, "bagels": 1.12, "tictactoe": 1.10, "hangman": 1.8, "userset": 1.11, "sysinfo": 1.4})
