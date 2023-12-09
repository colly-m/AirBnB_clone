#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
