#!/usr/bin/python3
import cmd
""" CMD class """


class HBNBCommand(cmd.Cmd):
    """ command interpreter"""

    prompt = "(hbnb)"
    __classes = {
            "BaseModel"
            }
    def emptyline(self):
        """ No entry,+ Enter should do nothing"""
        pass

    def do_quit(self, arg):
        """ exit program """
        return True

    def do_EOF(self, arg):
        """ EOF, exit program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
