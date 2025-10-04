<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html "passlib.totp – TOTP / Two Factor Authentication")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html "passlib.pwd – Password generation helpers")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.registry`](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html\#module-passlib.registry "passlib.registry: registry for tracking password hash handlers.") \- Password Handler Registry [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html\#module-passlib.registry "Permalink to this headline")

This module contains the code Passlib uses to track all password hash handlers
that it knows about. While custom handlers can be used directly within an application,
or even handed to a `CryptContext`; it is frequently useful to register
them globally within a process and then refer to them by name.
This module provides facilities for that, as well as programmatically
querying Passlib to detect what algorithms are available.

Warning

This module is primarily used as an internal support module.
Its interface has not been finalized yet, and may be changed somewhat
between major releases of Passlib, as the internal code is cleaned up
and simplified.

Applications should access hashes through the [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") module
where possible (new ones may also be registered by writing to that module).

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html\#interface "Permalink to this headline")

`passlib.registry.` `get_crypt_handler`( _name_\[, _default_\]) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.get_crypt_handler "Permalink to this definition")

return handler for specified password hash scheme.

this method looks up a handler for the specified scheme.
if the handler is not already loaded,
it checks if the location is known, and loads it first.

| Parameters: | - **name** – name of handler to return<br>- **default** – optional default value to return if no handler with specified name is found. |
| Raises: | [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.9)") – if no handler matching that name is found, and no default specified, a KeyError will be raised. |
| Returns: | handler attached to name, or default value (if specified). |

`passlib.registry.` `list_crypt_handlers`( _loaded\_only=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.list_crypt_handlers "Permalink to this definition")

return sorted list of all known crypt handler names.

| Parameters: | **loaded\_only** – if `True`, only returns names of handlers which have actually been loaded. |
| Returns: | list of names of all known handlers |

`passlib.registry.` `register_crypt_handler_path`( _name_, _path_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.register_crypt_handler_path "Permalink to this definition")

register location to lazy-load handler when requested.

custom hashes may be registered via [`register_crypt_handler()`](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.register_crypt_handler "passlib.registry.register_crypt_handler"),
or they may be registered by this function,
which will delay actually importing and loading the handler
until a call to [`get_crypt_handler()`](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.get_crypt_handler "passlib.registry.get_crypt_handler") is made for the specified name.

| Parameters: | - **name** – name of handler<br>- **path** – module import path |

the specified module path should contain a password hash handler
called `name`, or the path may contain a colon,
specifying the module and module attribute to use.
for example, the following would cause `get_handler("myhash")` to look
for a class named `myhash` within the `myapp.helpers` module:

```
>>> from passlib.registry import registry_crypt_handler_path
>>> registry_crypt_handler_path("myhash", "myapp.helpers")

```

…while this form would cause `get_handler("myhash")` to look
for a class name `MyHash` within the `myapp.helpers` module:

```
>>> from passlib.registry import registry_crypt_handler_path
>>> registry_crypt_handler_path("myhash", "myapp.helpers:MyHash")

```

`passlib.registry.` `register_crypt_handler`( _handler_, _force=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.register_crypt_handler "Permalink to this definition")

register password hash handler.

this method immediately registers a handler with the internal passlib registry,
so that it will be returned by [`get_crypt_handler()`](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#passlib.registry.get_crypt_handler "passlib.registry.get_crypt_handler") when requested.

| Parameters: | - **handler** – the password hash handler to register<br>- **force** – force override of existing handler (defaults to False)<br>- **\_attr** – \[internal kwd\] if specified, ensures `handler.name`<br>  matches this value, or raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if the specified object does not appear to be a valid handler.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if the specified object’s name (or other required attributes)<br>  contain invalid values.<br>- [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.9)") – if a (different) handler was already registered with<br>  the same name, and `force=True` was not specified. |

Note

All password hashes registered with passlib
can be imported by name from the [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") module.
This is true not just of the built-in hashes,
but for any hash registered with the registration functions
in this module.

## Usage [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html\#usage "Permalink to this headline")

Example showing how to use `registry_crypt_handler_path()`:

```
>>> # register the location of a handler without loading it
>>> from passlib.registry import register_crypt_handler_path
>>> register_crypt_handler_path("myhash", "myapp.support.hashes")

>>> # even before being loaded, its name will show up as available
>>> from passlib.registry import list_crypt_handlers
>>> 'myhash' in list_crypt_handlers()
True
>>> 'myhash' in list_crypt_handlers(loaded_only=True)
False

>>> # when the name "myhash" is next referenced,
>>> # the class "myhash" will be imported from the module "myapp.support.hashes"
>>> from passlib.context import CryptContext
>>> cc = CryptContext(schemes=["myhash"]) #<-- this will cause autoimport

```

Example showing how to load a hash by name:

```
>>> from passlib.registry import get_crypt_handler
>>> get_crypt_handler("sha512_crypt")
<class 'passlib.handlers.sha2_crypt.sha512_crypt'>

>>> get_crypt_handler("missing_hash")
KeyError: "no crypt handler found for algorithm: 'missing_hash'"

>>> get_crypt_handler("missing_hash", None)
None

```

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
  - [`passlib.apache` \- Apache Password Files](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html)
  - [`passlib.apps` \- Helpers for various applications](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html)
  - [`passlib.context` \- CryptContext Hash Manager](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html)
  - [`passlib.crypto` \- Cryptographic Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html)
  - [`passlib.exc` \- Exceptions and warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html)
  - [`passlib.ext.django` \- Django Password Hashing Plugin](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html)
  - [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html)
  - [`passlib.hosts` \- OS Password Handling](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html)
  - [`passlib.ifc` – Password Hash Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html)
  - [`passlib.pwd` – Password generation helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html)
  - [`passlib.registry` \- Password Handler Registry](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#)
    - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#interface)
    - [Usage](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#usage)
  - [`passlib.totp` – TOTP / Two Factor Authentication](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html)
  - [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html "passlib.totp – TOTP / Two Factor Authentication")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html "passlib.pwd – Password generation helpers")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.registry.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.registry.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)