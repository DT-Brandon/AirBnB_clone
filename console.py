#!/usr/bin/python3
"""HBNB Command interpreter module"""
import cmd
import string
from models import storage
import re


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
        if '(' in line and ')' in line and '.' in line:
            cls, sep, line = line.partition('.')
            cmd, line = line.split('(')
            args = line.strip(')')
            if '{' in args and '}' in args:
                instance_id, sep, dict_arg = args.partition(',')
                instance_id = instance_id.strip('"')
                args = f'{instance_id} {dict_arg}'
            else:
                args = ' '.join([x.strip()
                                 for x in args.replace('"', '').split(',')])
            return (cmd, f'{cls} {args}', f'{cmd} {cls} {args}')
        for char in line:
            if char in list(string.punctuation) + [' ']:
                cmd_list = line.partition(char)
                return (cmd_list[0], ''.join(cmd_list[1:]).strip(), line)
        return (line, '', line)

    def do_create(self, line):
        """Creates a new instance and saves it to JSON file"""
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name"""
        if HBNBCommand.check_class(line) is None:
            return
        instance = HBNBCommand.check_id(line)
        if instance is None:
            return
        print(instance)

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return
        instance = HBNBCommand.check_id(line)
        if instance is None:
            return
        key = f'{cls.__name__}.{instance.id}'
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
based or not on the class name"""
        if line:
            cls = HBNBCommand.check_class(line)
            if cls is None:
                return
            all_instance = [str(obj) for obj in storage.all().values()
                            if obj.to_dict()['__class__'] == cls.__name__]
        else:
            all_instance = [str(obj) for obj in storage.all().values()]
        print(all_instance)

    def do_update(self, line):
        """Update an instance based on the class name and id
by adding or updating attribute"""
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return
        instance = HBNBCommand.check_id(line)
        if instance is None:
            return
        if '{' in line and '}' in line:
            if len(line.split()) < 3:
                HBNBCommand.handle_errors('value_missing')
                return
            dict_arg = re.search('{.*}', line).group(0)
            dict_arg = eval(dict_arg)
            for attr, value in dict_arg.items():
                value = storage.attributes()[attr](value)
                setattr(instance, attr, value)
        else:
            attr, value = HBNBCommand.check_attr(line)
            if attr is None or value is None:
                return
            value = value.strip('"')
            value = storage.attributes()[attr](value)
            setattr(instance, attr, value)
        instance.save()

    def do_count(self, line):
        """Number of instances in class"""
        cls = HBNBCommand.check_class(line)
        if cls is None:
            return
        print(len([obj for obj in storage.all().values()
                   if obj.to_dict()['__class__'] == cls.__name__]))

    @classmethod
    def handle_errors(cls, error):
        """Handle all error message print outs"""
        print(cls.errors[error])

    @staticmethod
    def check_class(line):
        """checks for class"""
        if not line:
            HBNBCommand.handle_errors('class_missing')
            return
        if line.split()[0] not in storage.classes().keys():
            HBNBCommand.handle_errors('class_not_exist')
            return
        return storage.classes()[line.split()[0]]

    @staticmethod
    def check_id(line):
        """check for instance id"""
        cls = line.split()[0]
        try:
            key = f'{cls}.{line.split()[1]}'
            if key is None or key not in storage.all().keys():
                HBNBCommand.handle_errors('no_instance')
                return
        except Exception:
            HBNBCommand.handle_errors('id_missing')
            return
        return storage.all()[key]

    @staticmethod
    def check_attr(line):
        """check for attribute and value"""
        if len(line.split()) < 3:
            HBNBCommand.handle_errors('attribute_missing')
            return None, None
        attr = line.split()[2]
        if len(line.split()) < 4:
            HBNBCommand.handle_errors('value_missing')
            return attr, None
        if '"' in line:
            value = line.split('"')[1]
            value = value.strip('"')
            print(value)
        else:
            value = line.split()[3]
        return (attr, value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
