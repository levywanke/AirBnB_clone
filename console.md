# Constructing the Console
This scrapbook serves as our organizational tool as we develop the AirBnB command line interpreter.

## [cmd](https://docs.python.org/3.8/library/cmd.html#module-cmd) — Supporting Line-Oriented Command Interpreters

The `Cmd` class offers a straightforward framework for crafting line-oriented command interpreters. These prove invaluable for creating test harnesses, administrative utilities, and prototypes that may later evolve into more sophisticated interfaces.

A `Cmd` instance or subclass instance serves as a foundation for a line-oriented interpreter framework. While there's little reason to instantiate `Cmd` directly, it proves beneficial as a superclass for a custom interpreter class you define, enabling inheritance of `Cmd`'s methods and encapsulating action methods.

## Crucial Concepts 🎓
- Cmd.cmdloop(intro=None):
  - Iteratively prompts for input, accepts input, parses an initial prefix from the input, and dispatches it to action methods, providing the remaining line as an argument.
  - All `Cmd` subclasses inherit a pre-defined `do_help()`. This method, when called with an argument 'bar', triggers the corresponding method `help_bar()`. If absent, it prints the docstring of `do_bar()`, if available. Without arguments, `do_help()` lists all available help topics (commands with corresponding `help_*()` methods or commands with docstrings) and also lists any undocumented commands.
  - This method continues execution until the `postcmd()` method returns a `true` value. The `stop` argument passed to `postcmd()` is the return value from the command’s corresponding `do_*()` method.
- End-of-file on input is signaled by the string 'EOF'.
- An interpreter instance recognizes a command name `foo` only if it possesses a method `do_foo()`. As a special case, a line beginning with '?' is routed to the `do_help()` method. Another special case involves a line beginning with '!', dispatched to the `do_shell()` method (if defined).
- Implement `do_EOF()` to handle errors gracefully.
- Override default behavior of `empty line + return` by implementing `emptyline()`.
