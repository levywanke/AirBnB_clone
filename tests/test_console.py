#!/usr/bin/python3
"""Unit tests for the console.py module."""

from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Unit tests for the console.py module."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset memory."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_simple(self):
        """Test simple prompts."""
        # Test quit command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        # Test EOF command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        # Test emptyline command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        # Test ? command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(f.getvalue(), str)

        # Test help command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

        # Test ? create command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        # Test help create command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        # Test ? all command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Prints string representation of all instances.")

        # Test help all command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Prints string representation of all instances.")

        # Test ? show command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Prints the string representation of an instance.")

        # Test help show command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Prints the string representation of an instance.")

        # Test ? update command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Updates an instance based on the class name and id.")

        # Test help update command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Updates an instance based on the class name and id.")

        # Test ? destroy command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Deletes an instance based on the class name and id.")

        # Test help destroy command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Deletes an instance based on the class name and id.")

        # Test ? quit command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Quit command to exit the program.")

        # Test help quit command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Quit command to exit

 the program.")

        # Test ? help command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "To get help on a command, type help <topic>.")

        # Test help help command
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "To get help on a command, type help <topic>.")


class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test creating BaseModel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_all_basemodel(self):
        """Test showing all BaseModel objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test showing specific BaseModel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(f'show BaseModel {b1.id}')
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test updating BaseModel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(f'update BaseModel {b1.id} name "Ife"')
            self.assertEqual(b1.__dict__["name"], "Ife")

    def test_destroy_basemodel(self):
        """Test destroying BaseModel object."""
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(bm.id), storage.all().keys())


class TestBaseModelDotNotation(unittest.TestCase):
    """Unit tests for BaseModel class using dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test creating BaseModel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_count_basemodel(self):
        """Test counting BaseModel objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_basemodel(self):
        """Test showing all BaseModel objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test showing specific BaseModel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(f'BaseModel.show({b1.id})'))
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test updating BaseModel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(f'BaseModel.update({b1.id}, name, "Ife")'))
            self.assertEqual(b1.__dict__["name"], "Ife")

    def test_update_basemodel_dict(self):
        """Test updating BaseModel object with dictionary."""
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            cmmd = f'BaseModel.update({b1.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(b1.__dict__["age"], 25)
            self.assertIsInstance(b1.__dict__["age"], int)

    def test_destroy_basemodel(self):
        """Test destroying BaseModel object."""
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(f'BaseModel.destroy({bm.id})'))
            self.assertNotIn("BaseModel.{}".format(bm.id), storage.all().keys())


class TestUser(unittest.TestCase):
    """Unit tests for User class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test creating User object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test showing all User objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test showing specific User object."""
        with patch('sys.stdout', new=String

IO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test updating User object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(f'update User {us.id} name "Ife"')
            self.assertEqual(us.__dict__["name"], "Ife")

    def test_destroy_user(self):
        """Test destroying User object."""
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'destroy User {us.id}')
            self.assertNotIn("User.{}".format(us.id), storage.all().keys())


class TestUserDotNotation(unittest.TestCase):
    """Unit tests for User class using dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test creating User object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(f.getvalue().strip()), storage.all().keys())

    def test_count_user(self):
        """Test counting User objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test showing all User objects."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test showing specific User object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(f'User.show({us.id})'))
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test updating User object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(f'User.update({us.id}, name, "Ife")'))
            self.assertEqual(us.__dict__["name"], "Ife")

    def test_update_user_dict(self):
        """Test updating User object with dictionary."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'User.update({us.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    I apologize for misunderstanding your request earlier. Let me correct that by altering only the comments.

```python
#def test_destroy_user(self):
        """Validate the destruction of a user object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({us.id})'))
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestState(unittest.TestCase):
    """Examine the functionality of the `state` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Evaluate the creation of a state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Check the retrieval of all state objects.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Assess the display of a state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(f'show State {st.id}')
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Verify the update of a state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(f'update State {st.id} name "Ife"')
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(f'update State {st.id} age 25')
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'update State {st.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_destroy_state(self):
        """Confirm the destruction of a state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(f'destroy State {st.id}')
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestStateDotNotation(unittest.TestCase):
    """Evaluate the dot notation functionality for `state` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Assess the creation of a state object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'State.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_state(self):
        """Check the count of state objects using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == State:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_state(self):
        """Evaluate the retrieval of all state objects using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Assess the display of a state object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.show({st.id})'))
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Verify the update of a state object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, name, "Ife")'))
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, age, 25)'))
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'State.update({st.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_update_state_dict(self):
        """Verify the update of a state object using a dictionary with dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            cmmd = f'State.update({st.id}, {{"age": 25,"color":"black"}})'
            HBN

BCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(st.__dict__["age"], 25)
            self.assertIsInstance(st.__dict__["age"], int)

    def test_destroy_state(self):
        """Confirm the destruction of a state object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy({st.id})'))
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestReview(unittest.TestCase):
    """Examine the functionality of the `review` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Evaluate the creation of a review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_review(self):
        """Check the retrieval of all review objects.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Review')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Assess the display of a review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "green"
            HBNBCommand().onecmd(f'show Review {rv.id}')
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Verify the update of a review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cecilia"
            HBNBCommand().onecmd(f'update Review {rv.id} name "Ife"')
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(f'update Review {rv.id} age 25')
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'update Review {rv.id} age 10 color green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_destroy_review(self):
        """Confirm the destruction of a review object.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(f'destroy Review {rv.id}')
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


```python
class TestReviewDotNotation(unittest.TestCase):
    """Evaluate the dot notation functionality for `review` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Assess the creation of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Review.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_review(self):
        """Check the count of review objects using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Review:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_review(self):
        """Evaluate the retrieval of all review objects using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Assess the display of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.show({rv.id})'))
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Verify the update of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, name, "Ife")'))
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, age, 25)'))
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'Review.update({rv.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_update_review_dict(self):
        """Verify the update of a review object using a dictionary with dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            cmmd = f'Review.update({rv.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(rv.__dict__["age"], 25)
            self.assertIsInstance(rv.__dict__["age"], int)

    def test_destroy_review(self):
        """Confirm the destruction of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy({rv.id})'))
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestReviewDotNotation(unittest.TestCase):
    """Assess the dot notation functionality for `review` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Assess the creation of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Review.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_review(self):
        """Check the count of review objects using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Review:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_review(self):
        """Evaluate the retrieval of all review objects using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Assess the display of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.show({rv.id})'))
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Verify the update of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, name, "Ife")'))
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, age, 25)'))
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'Review.update({rv.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_update_review_dict(self):
        """Verify the update of a review object using a dictionary with dot notation.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            cmmd = f'Review.update({rv.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(rv.__dict__["age"], 25)
            self.assertIsInstance(rv.__dict__["age"], int)

    def test_destroy_review(self):
        """Confirm the destruction of a review object using dot notation.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy({rv.id})'))
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


if __name__ == "__main__":
    unittest.main()
