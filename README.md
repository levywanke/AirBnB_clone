# AirBnB Clone - The Console
![bnb](https://github.com/levywanke/AirBnB_clone/assets/132353709/9d27396a-15d5-44f6-beb2-32802b2ba8fd)

## Project Overview

This project involves creating a command interpreter to manage AirBnB objects. It is the first step towards building a full web application, the AirBnB clone. The command interpreter enables you to create, update, retrieve, and destroy objects, laying the groundwork for future projects involving HTML/CSS templating, database storage, API, and frontend integration.

## Group Information

- **Team Members**: Levy Wanyonyi
- **Project Duration**: February 5, 2024, 6:00 AM to February 12, 2024, 6:00 AM
- **Manual QA Review**: February 13, 2024, 10:15 PM by Alvin Muhindi
- **Auto Review**: Conducted at the project deadline

## Project Performance

- **Manual QA Review**: 48.0/48 mandatory
- **Auto QA Review**: 188.5/302 mandatory & 151.45/233 optional
- **Overall Score**: 111.49%
  - **Mandatory**: 67.57%
  - **Optional**: 65.0%
  - **Contribution**: 100.0%

## Overall Comment

Great work! Keep it up!

## Concepts Covered

- **Python Packages**
- **AirBnB Clone**

## Background Context

Welcome to the AirBnB clone project! This first step is crucial as it will be used in subsequent projects, including HTML/CSS templating, database storage, API, and frontend integration.

### Command Interpreter

The command interpreter is a simple shell designed to manage AirBnB objects. It allows you to:

- Create new objects (e.g., User, Place)
- Retrieve objects from a file or database
- Perform operations on objects (e.g., count, compute stats)
- Update object attributes
- Destroy objects

## Resources

To complete this project, refer to the following resources:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [Python test cheatsheet](https://docs.python.org/3/library/unittest.html)

## Learning Objectives

By the end of this project, you should be able to:

- Create a Python package
- Develop a command interpreter using the `cmd` module
- Implement unit testing for large projects
- Serialize and deserialize classes
- Write and read JSON files
- Manage datetime in Python
- Understand UUIDs
- Use `*args` and `**kwargs`
- Handle named arguments in functions

## Requirements

### Python Scripts

- Use allowed editors: `vi`, `vim`, `emacs`
- Ensure all files end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Include a `README.md` file at the root of the project
- Follow `pycodestyle` guidelines
- Make all files executable
- Document all modules, classes, and functions

### Python Unit Tests

- Use allowed editors: `vi`, `vim`, `emacs`
- Ensure all files end with a new line
- Place test files in the `tests` directory
- Use the `unittest` module
- Name test files with the prefix `test_`
- Match the file organization in the `tests` folder to the project structure
- Execute tests with `python3 -m unittest discover tests`

## GitHub

- Use one repository per group
- Avoid cloning or forking the repository with the same name before the second deadline to prevent a 0% score

## Execution

### Interactive Mode

Run the console in interactive mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```

### Non-Interactive Mode

Run the console in non-interactive mode:
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

Run tests in non-interactive mode:
```sh
$ echo "python3 -m unittest discover tests" | bash
```

---

By following the guidelines and meeting the project requirements, this README.md file provides a comprehensive overview of the AirBnB clone project - The Console.
