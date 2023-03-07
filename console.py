#!/usr/bin/python3
"""HBNB Command interpreter module"""
import cmd
import string


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class"""

    prompt = '(hbnb) '
    errors = {
            'class_missing': '** class name missing **',
            'class_not_exist': '** class doesn\'t exist **',
            'id_missing': '** instance id missing **',
            'no_instance': '** no instance found **',
            'attribute_missing': '** attribute name missing **',
            'value_missing': '** value missing **'
            }
    classes = [
            'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
            ] # placeholder array for class list dict

    def do_EOF(self, line):
        """Exits the console"""
        print()
        return True

    def do_quit(self, line):
        """Quits the console"""
        return True

    def emptyline(self):
        """Do nothing on emptyline"""
        pass

    def parseline(self, line):
        """Parse command line"""
        for char in line:
            if char in list(string.punctuation) + [' ']:
                cmd_list = line.partition(char)
                return (cmd_list[0], ''.join(cmd_list[1:]).strip(), line)
        return (line, '', line)

    def do_create(self, line):
        """Creates a new instance and saves it to JSON file"""
        if not HBNBCommand.check_class(line):
            return
        print(f'{line} created')

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name"""
        if not HBNBCommand.check_class(line):
            return
        if not HBNBCommand.check_id(line):
            return
        print(storage.all()[f'{line.split()[1]}'])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        pass

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        pass

    def do_update(self, line):
        """Update an instance based on the class name and id
        by adding or updating attribute"""
        pass

    @classmethod
    def handle_errors(cls, error):
        """Handle all error message print outs"""
        print(cls.errors[error])

    @staticmethod
    def check_class(line):
        if not line:
            HBNBCommand.handle_errors('class_missing')
            return False
        if line.split()[0] not in HBNBCommand.classes:
            HBNBCommand.handle_errors('class_not_exist')
            return False
        return True

    @staticmethod
    def check_id(line):
        cls = line.split()[0]
        try:
            if f'{cls}.{line.split()[1]}' not in storage.all().keys():
                HBNBCommand.handle_errors('no_instance')
                return False
        except:
            HBNBCommand.handle_errors('id_missing')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
