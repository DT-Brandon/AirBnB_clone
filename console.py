#!/usr/bin/python3
"""HBNB Command interpreter module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class"""


    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exits the console"""
        print()
        return True

    def do_quit(self, line):
        """Quits the console"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
