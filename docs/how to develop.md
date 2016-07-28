# How to develop

This page describes gemini development process and contains general guidelines and information on how to contribute to the project.

## General contribute guidelines

- Any non-trivial change must contain tests.
- All the functions and methods must contain Sphinx docstrings which are used to generate the API documentation.
- If you are adding a new feature, make sure to add a corresponding documentation.

## Code style guide

- We follow [PEP8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/).
- Use 4 spaces for a tab
- Use 79 characters in a line
- Make sure edited file doesn't contain any trailing whitespace

## Code conventions

This section describes some general code conventions you should follow when writing a gemini code.

### 1. Import ordering

Please organize imports in the following order:

&ensp;1. Standard library imports  
&ensp;2. Third-party library imports  
&ensp;3. Local library (gemini) imports  

Each section should be separated with a blank line. For example:

    import sys
    import base64

    import xmltodict
    from libcloud.compute.drivers.libvirt_driver import LibvirtNodeDriver

    from gemini.compute.types import *
    from gemini import app

### 2. Function and method ordering

Functions in a module and methods on a class should be organized in the following order:

&ensp;1. “Public” functions / methods  
&ensp;2. "Private" functions / methods (methods prefixed with an underscore)  &ensp;3. "Internal" methods (methods prefixed and suffixed with a double underscore)  

For example:

    class Unicorn(object):
    def __init__(self, name='fluffy'):
        self._name = name

    def make_a_rainbow(self):
        pass

    def _get_rainbow_colors(self):
        pass

    def __eq__(self, other):
        return self.name == other.name

Methods on a driver class should be organized in the following order:

&ensp;1. Methods which are part of the standard API  
&ensp;2. Extension methods  
&ensp;3. "Private" methods (methods prefixed with an underscore)  
&ensp;4. "Internal" methods (methods prefixed and suffixed with a double underscore)

Methods which perform a similar functionality should be grouped together and defined one after another.

For example:

    class MyDriver(object):
        def __init__(self):
            pass

        def list_nodes(self):
            pass

        def list_images(self):
            pass

        def create_node(self):
            pass

        def reboot_node(self):
            pass

        def ex_create_image(self):
            pass

        def _to_nodes(self):
            pass

        def _to_node(self):
            pass

        def _to_images(self):
            pass

        def _to_image(self):
            pass

Methods should be ordered this way for the consistency reasons and to make reading and following the generated API documentation easier.

### 3. Prefer keyword over regular arguments

For better readability and understanding of the code, prefer keyword over regular arguments.

Good:

`some_method(public_ips=public_ips, private_ips=private_ips)`

Bad:

`some_method(public_ips, private_ips)`

### 4. Don't abuse **kwargs

You should always explicitly declare arguments in a function or a method signature and only use `**kwargs` and `*args` respectively when there is a valid use case for it.

Using `**kwargs` in many contexts is against Python's "explicit is better than implicit" mantra and makes it for a bad and a confusing API. On top of that, it makes many useful things such as programmatic API introspection hard or impossible.

A use case when it might be valid to use `**kwargs` is a decorator.

Good:

    def my_method(self, name, description=None, public_ips=None):
        pass

Bad:

    def my_method(self, name, **kwargs):
        description = kwargs.get('description', None)
        public_ips = kwargs.get('public_ips', None)

### 5. When returning a dictionary, document its structure

Dynamic nature of Python can be very nice and useful, but if (ab)use it in a wrong way it can also make it hard for the API consumer to understand what is going on and what kind of values are being returned.

If you have a function or a method which returns a dictionary, make sure to explicitly document in the docstring which keys the returned dictionary contains.

### 6. Prefer to use "is not None" when checking if a variable is provided or defined

When checking if a variable is provided or defined, prefer to use `if foo is not None` instead of `if foo`.

If you use `if foo` approach, it's easy to make a mistake when a valid value can also be falsy (e.g. a number 0).

For example:

    class SomeClass(object):
    def some_method(self, domain=None):
        params = {}

        if domain is not None:
            params['Domain'] = domain

## Docstring conventions

For documenting the API we use Sphinx and reStructuredText syntax. Docstring conventions to which you should adhere to are described below.

- Docstrings should always be used to describe the purpose of methods, functions, classes, and modules.
- Method docstring should describe all the normal and keyword arguments. You should describe all the available arguments even if you use `*args` and `**kwargs`.
- All parameters must be documented using `:param p:` or `:keyword p:` and `:type p:` annotation.
- `:param p: ...` - A description of the parameter `p` for a function or method.
- `:keyword p: ...` - A description of the keyword parameter `p`.
- `:type p: ...` The expected type of the parameter `p`.
- Return values must be documented using `:return:` and `:rtype` annotation.
- `:return: ...` A description of return value for a function or method.
- `:rtype: ...` The type of the return value for a function or method.
- Required keyword arguments must contain `(required)` notation in description. For example: `:keyword image: OS Image to boot on node. (required)`
- Multiple types are separated with `or` For example: ``:type auth: :class:`.NodeAuthSSHKey` or :class:`.NodeAuthPassword` ``
- For a description of the container types use the following notation: `<container_type> of <objects_type>`. For example: ``:rtype: `list` of :class:`Node` ``

For more information and examples, please refer to the following links:

- Sphinx Documentation - <http://sphinx-doc.org/markup/desc.html#info-field-lists>
