#!/usr/bin/python3
"""Test module for the console"""
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import sys
import re


class TestHBNBCommand(TestCase):
    """console test class"""

    def test_commands_without_class(self):
        expected_error = '** class name missing **\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

    def test_commands_with_wrong_class(self):
        expected_error = '** class doesn\'t exist **\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create NotAClass')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show NotAClass')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy NotAClass')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update NotAClas')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

    def test_commands_without_id(self):
        expected_error = '** instance id missing **\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Place')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User')
            output = f.getvalue()
            self.assertEqual(output, expected_error)

    def test_commands_with_unknown_id(self):
        expected_error = '** no instance found **\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 1234-abcd-5678-efgh-90ijkl')
            output = f.getvalue()
            self.assertEqual(output, expected_error)
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy Amenity 1234-abcd-5678-efgh-90ijkl')
            output = f.getvalue()
            self.assertEqual(output, expected_error)
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update City 1234-abcd-5678-efgh-90ijkl')
            output = f.getvalue()
            self.assertEqual(output, expected_error)
            self.assertEqual(output, expected_error)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show State 1234-abcd-5678-efgh-90ijkl')
            output = f.getvalue()
            self.assertEqual(output, expected_error)
            self.assertEqual(output, expected_error)

    def test_do_create(self):
        expected_print_fmt = '.{8}\-.{4}\-.{4}\-.{4}\-.{12}'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            output = f.getvalue()
            self.assertIsNotNone(output)
            self.assertRegex(output, expected_print_fmt)

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            obj_id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {obj_id}')
            output = f.getvalue()
            result = re.match('^\[BaseModel\] \(.{8}\-.{4}\-.{4}\-.{4}\-.{12}\) {.*}\n', output)
            self.assertIsNotNone(result)
        print(output)
