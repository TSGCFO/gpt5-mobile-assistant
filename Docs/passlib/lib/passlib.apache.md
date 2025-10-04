<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html "passlib.apps - Helpers for various applications")
- [previous](https://passlib.readthedocs.io/en/stable/lib/index.html "API Reference")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.apache`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#module-passlib.apache "passlib.apache: reading/writing htpasswd & htdigest files") \- Apache Password Files [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#module-passlib.apache "Permalink to this headline")

This module provides utilities for reading and writing Apache’s
htpasswd and htdigest files; though the use of two helper classes.

Changed in version 1.6: The api for this module was updated to be more flexible,
and to have less ambiguous method names.
The old method and keyword names are deprecated, and
will be removed in Passlib 1.8.

Changed in version 1.7: These classes will now preserve blank lines and “#” comments when updating
htpasswd files; previous releases would throw a parse error.

## Htpasswd Files [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#htpasswd-files "Permalink to this headline")

The `HTpasswdFile` class allows managing of htpasswd files.
A quick summary of its usage:

```
>>> from passlib.apache import HtpasswdFile

>>> # when creating a new file, set to new=True, add entries, and save.
>>> ht = HtpasswdFile("test.htpasswd", new=True)
>>> ht.set_password("someuser", "really secret password")
>>> ht.save()

>>> # loading an existing file to update a password
>>> ht = HtpasswdFile("test.htpasswd")
>>> ht.set_password("someuser", "new secret password")
>>> ht.save()

>>> # examining file, verifying user's password
>>> ht = HtpasswdFile("test.htpasswd")
>>> ht.users()
[ "someuser" ]
>>> ht.check_password("someuser", "wrong password")
False
>>> ht.check_password("someuser", "new secret password")
True

>>> # making in-memory changes and exporting to string
>>> ht = HtpasswdFile()
>>> ht.set_password("someuser", "mypass")
>>> ht.set_password("someuser", "anotherpass")
>>> print ht.to_string()
someuser:$apr1$T4f7D9ly$EobZDROnHblCNPCtrgh5i/
anotheruser:$apr1$vBdPWvh1$GrhfbyGvN/7HalW5cS9XB1

```

Warning

`HtpasswdFile` currently defaults to using `apr_md5_crypt`,
as this is the only htpasswd hash guaranteed to be portable across operating systems.
However, for security reasons Passlib 1.7 will default to using the strongest algorithm
available on the host platform (e.g. `bcrypt` or `sha256_crypt`).
Applications that are relying on the old behavior should specify
`HtpasswdFile(default_scheme="portable")` (new in Passlib 1.6.3).

_class_ `passlib.apache.` `HtpasswdFile`( _path=None_, _new=False_, _autosave=False_, _..._) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile "Permalink to this definition")

class for reading & writing Htpasswd files.

The class constructor accepts the following arguments:

| Parameters: | - **path** ( _filepath_) – <br>  Specifies path to htpasswd file, use to implicitly load from and save to.<br>  <br>  This class has two modes of operation:<br>  <br>  <br>  1. It can be “bound” to a local file by passing a `path` to the class<br>     constructor. In this case it will load the contents of the file when<br>     created, and the [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load "passlib.apache.HtpasswdFile.load") and [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.save "passlib.apache.HtpasswdFile.save") methods will automatically<br>     load from and save to that file if they are called without arguments.<br>  2. Alternately, it can exist as an independant object, in which case<br>     [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load "passlib.apache.HtpasswdFile.load") and [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.save "passlib.apache.HtpasswdFile.save") will require an explicit path to be<br>     provided whenever they are called. As well, `autosave` behavior<br>     will not be available.<br>     This feature is new in Passlib 1.6, and is the default if no<br>     `path` value is provided to the constructor.<br>     <br>This is also exposed as a readonly instance attribute.<br>- **new** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  Normally, if _path_ is specified, [`HtpasswdFile`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile "passlib.apache.HtpasswdFile") will<br>  immediately load the contents of the file. However, when creating<br>  a new htpasswd file, applications can set `new=True` so that<br>  the existing file (if any) will not be loaded.<br>  <br>  <br>  <br>  New in version 1.6: This feature was previously enabled by setting `autoload=False`.<br>  That alias has been deprecated, and will be removed in Passlib 1.8<br>  <br>- **autosave** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  Normally, any changes made to an [`HtpasswdFile`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile "passlib.apache.HtpasswdFile") instance<br>  will not be saved until [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.save "passlib.apache.HtpasswdFile.save") is explicitly called. However,<br>  if `autosave=True` is specified, any changes made will be<br>  saved to disk immediately (assuming _path_ has been set).<br>  <br>  This is also exposed as a writeable instance attribute.<br>  <br>- **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Optionally specify character encoding used to read/write file<br>  and hash passwords. Defaults to `utf-8`, though `latin-1`<br>  is the only other commonly encountered encoding.<br>  <br>  This is also exposed as a readonly instance attribute.<br>  <br>- **default\_scheme** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Optionally specify default scheme to use when encoding new passwords.<br>  <br>  This can be any of the schemes with builtin Apache support,<br>  OR natively supported by the host OS’s [`crypt.crypt()`](https://docs.python.org/3/library/crypt.html#crypt.crypt "(in Python v3.9)") function.<br>  <br>  <br>  - Builtin schemes include `"bcrypt"` (apache 2.4+), ```"apr_md5_crypt"`,<br>    and ``"des_crypt"```.<br>  - Schemes commonly supported by Unix hosts<br>    include `"bcrypt"`, `"sha256_crypt"`, and `"des_crypt"`.<br>In order to not have to sort out what you should use,<br>passlib offers a number of aliases, that will resolve<br>to the most appropriate scheme based on your needs:<br>  - `"portable"`, `"portable_apache_24"` – pick scheme that’s portable across hosts<br>    running apache >= 2.4. **This will be the default as of Passlib 2.0**.<br>  - `"portable_apache_22"` – pick scheme that’s portable across hosts<br>    running apache >= 2.4. **This is the default up to Passlib 1.9**.<br>  - `"host"`, `"host_apache_24"` – pick strongest scheme supported byapache >= 2.4 and/or host OS.<br>  - `"host_apache_22"` – pick strongest scheme supported byapache >= 2.2 and/or host OS.<br>New in version 1.6: This keyword was previously named `default`. That alias<br>has been deprecated, and will be removed in Passlib 1.8.<br>Changed in version 1.6.3: Added support for `"bcrypt"`, `"sha256_crypt"`, and `"portable"` alias.<br>Changed in version 1.7: Added apache 2.4 semantics, and additional aliases.<br>- **context** ( [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext")) – <br>  `CryptContext` instance used to create<br>  and verify the hashes found in the htpasswd file.<br>  The default value is a pre-built context which supports all<br>  of the hashes officially allowed in an htpasswd file.<br>  <br>  This is also exposed as a readonly instance attribute.<br>  <br>  <br>  <br>  Warning<br>  <br>  <br>  <br>  This option may be used to add support for non-standard hash<br>  formats to an htpasswd file. However, the resulting file<br>  will probably not be usable by another application,<br>  and particularly not by Apache.<br>  <br>- **autoload** – <br>  Set to `False` to prevent the constructor from automatically<br>  loaded the file from disk.<br>  <br>  <br>  <br>  Deprecated since version 1.6: This has been replaced by the _new_ keyword.<br>  Instead of setting `autoload=False`, you should use<br>  `new=True`. Support for this keyword will be removed<br>  in Passlib 1.8.<br>  <br>- **default** – <br>  Change the default algorithm used to hash new passwords.<br>  <br>  <br>  <br>  Deprecated since version 1.6: This has been renamed to _default\_scheme_ for clarity.<br>  Support for this alias will be removed in Passlib 1.8. |

### Loading & Saving [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtpasswdFile-loading-saving "Permalink to this headline")

`load`( _path=None_, _force=True_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load "Permalink to this definition")

Load state from local file.
If no path is specified, attempts to load from `self.path`.

| Parameters: | - **path** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – local file to load from<br>- **force** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  if `force=False`, only load from `self.path` if file<br>  has changed since last load.<br>  <br>  <br>  <br>  Deprecated since version 1.6: This keyword will be removed in Passlib 1.8;<br>  Applications should use [`load_if_changed()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load_if_changed "passlib.apache.HtpasswdFile.load_if_changed") instead. |

`load_if_changed`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load_if_changed "Permalink to this definition")

Reload from `self.path` only if file has changed since last load

`load_string`( _data_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load_string "Permalink to this definition")

Load state from unicode or bytes string, replacing current state

`save`( _path=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.save "Permalink to this definition")

Save current state to file.
If no path is specified, attempts to save to `self.path`.

`to_string`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.to_string "Permalink to this definition")

Export current state as a string of bytes

### Inspection [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtpasswdFile-inspection "Permalink to this headline")

`users`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.users "Permalink to this definition")

Return list of all users in database

`check_password`( _user_, _password_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.check_password "Permalink to this definition")

Verify password for specified user.
If algorithm marked as deprecated by CryptContext, will automatically be re-hashed.

| Returns: | - `None` if user not found.<br>- `False` if user found, but password does not match.<br>- `True` if user found and password matches. |

Changed in version 1.6: This method was previously called `verify`, it was renamed
to prevent ambiguity with the `CryptContext` method.
The old alias is deprecated, and will be removed in Passlib 1.8.

`get_hash`( _user_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.get_hash "Permalink to this definition")

Return hash stored for user, or `None` if user not found.

Changed in version 1.6: This method was previously named `find`, it was renamed
for clarity. The old name is deprecated, and will be removed
in Passlib 1.8.

### Modification [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtpasswdFile-modification "Permalink to this headline")

`set_password`( _user_, _password_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.set_password "Permalink to this definition")

Set password for user; adds user if needed.

| Returns: | - `True` if existing user was updated.<br>- `False` if user account was added. |

Changed in version 1.6: This method was previously called `update`, it was renamed
to prevent ambiguity with the dictionary method.
The old alias is deprecated, and will be removed in Passlib 1.8.

`delete`( _user_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.delete "Permalink to this definition")

Delete user’s entry.

| Returns: | - `True` if user deleted.<br>- `False` if user not found. |

### Alternate Constructors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtpasswdFile-alternate-constructors "Permalink to this headline")

_classmethod_ `from_string`( _data_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.from_string "Permalink to this definition")

create new object from raw string.

| Parameters: | - **data** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – database to load, as single string.<br>- **\*\*kwds** – all other keywords are the same as in the class constructor |

### Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtpasswdFile-attributes "Permalink to this headline")

`path` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.path "Permalink to this definition")

Path to local file that will be used as the default
for all [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.load "passlib.apache.HtpasswdFile.load") and [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.save "passlib.apache.HtpasswdFile.save") operations.
May be written to, initialized by the _path_ constructor keyword.

`autosave` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile.autosave "Permalink to this definition")

Writeable flag indicating whether changes will be automatically
written to _path_.

### Errors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtpasswdFile-errors "Permalink to this headline")

| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – All of the methods in this class will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") if<br>any user name contains a forbidden character (one of `:\r\n\t\x00`),<br>or is longer than 255 characters. |

## Htdigest Files [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#htdigest-files "Permalink to this headline")

The `HtdigestFile` class allows management of htdigest files
in a similar fashion to [`HtpasswdFile`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtpasswdFile "passlib.apache.HtpasswdFile").

_class_ `passlib.apache.` `HtdigestFile`( _path_, _default\_realm=None_, _new=False_, _autosave=False_, _..._) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile "Permalink to this definition")

class for reading & writing Htdigest files.

The class constructor accepts the following arguments:

| Parameters: | - **path** ( _filepath_) – <br>  Specifies path to htdigest file, use to implicitly load from and save to.<br>  <br>  This class has two modes of operation:<br>  <br>  <br>  1. It can be “bound” to a local file by passing a `path` to the class<br>     constructor. In this case it will load the contents of the file when<br>     created, and the [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load "passlib.apache.HtdigestFile.load") and [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.save "passlib.apache.HtdigestFile.save") methods will automatically<br>     load from and save to that file if they are called without arguments.<br>  2. Alternately, it can exist as an independant object, in which case<br>     [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load "passlib.apache.HtdigestFile.load") and [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.save "passlib.apache.HtdigestFile.save") will require an explicit path to be<br>     provided whenever they are called. As well, `autosave` behavior<br>     will not be available.<br>     This feature is new in Passlib 1.6, and is the default if no<br>     `path` value is provided to the constructor.<br>     <br>This is also exposed as a readonly instance attribute.<br>- **default\_realm** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  If `default_realm` is set, all the [`HtdigestFile`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile "passlib.apache.HtdigestFile")<br>  methods that require a realm will use this value if one is not<br>  provided explicitly. If unset, they will raise an error stating<br>  that an explicit realm is required.<br>  <br>  This is also exposed as a writeable instance attribute.<br>  <br>  <br>  <br>  New in version 1.6.<br>  <br>- **new** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  Normally, if _path_ is specified, [`HtdigestFile`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile "passlib.apache.HtdigestFile") will<br>  immediately load the contents of the file. However, when creating<br>  a new htpasswd file, applications can set `new=True` so that<br>  the existing file (if any) will not be loaded.<br>  <br>  <br>  <br>  New in version 1.6: This feature was previously enabled by setting `autoload=False`.<br>  That alias has been deprecated, and will be removed in Passlib 1.8<br>  <br>- **autosave** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  Normally, any changes made to an [`HtdigestFile`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile "passlib.apache.HtdigestFile") instance<br>  will not be saved until [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.save "passlib.apache.HtdigestFile.save") is explicitly called. However,<br>  if `autosave=True` is specified, any changes made will be<br>  saved to disk immediately (assuming _path_ has been set).<br>  <br>  This is also exposed as a writeable instance attribute.<br>  <br>- **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Optionally specify character encoding used to read/write file<br>  and hash passwords. Defaults to `utf-8`, though `latin-1`<br>  is the only other commonly encountered encoding.<br>  <br>  This is also exposed as a readonly instance attribute.<br>  <br>- **autoload** – <br>  Set to `False` to prevent the constructor from automatically<br>  loaded the file from disk.<br>  <br>  <br>  <br>  Deprecated since version 1.6: This has been replaced by the _new_ keyword.<br>  Instead of setting `autoload=False`, you should use<br>  `new=True`. Support for this keyword will be removed<br>  in Passlib 1.8. |

### Loading & Saving [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtdigestFile-loading-saving "Permalink to this headline")

`load`( _path=None_, _force=True_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load "Permalink to this definition")

Load state from local file.
If no path is specified, attempts to load from `self.path`.

| Parameters: | - **path** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – local file to load from<br>- **force** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  if `force=False`, only load from `self.path` if file<br>  has changed since last load.<br>  <br>  <br>  <br>  Deprecated since version 1.6: This keyword will be removed in Passlib 1.8;<br>  Applications should use [`load_if_changed()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load_if_changed "passlib.apache.HtdigestFile.load_if_changed") instead. |

`load_if_changed`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load_if_changed "Permalink to this definition")

Reload from `self.path` only if file has changed since last load

`load_string`( _data_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load_string "Permalink to this definition")

Load state from unicode or bytes string, replacing current state

`save`( _path=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.save "Permalink to this definition")

Save current state to file.
If no path is specified, attempts to save to `self.path`.

`to_string`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.to_string "Permalink to this definition")

Export current state as a string of bytes

### Inspection [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtdigestFile-inspection "Permalink to this headline")

`realms`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.realms "Permalink to this definition")

Return list of all realms in database

`users`( _realm=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.users "Permalink to this definition")

Return list of all users in specified realm.

- uses `self.default_realm` if no realm explicitly provided.
- returns empty list if realm not found.

`check_password`( _user_, \[ _realm_, \] _password_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.check_password "Permalink to this definition")

Verify password for specified user + realm.

If `self.default_realm` has been set, this may be called
with the syntax `check_password(user, password)`,
otherwise it must be called with all three arguments:
`check_password(user, realm, password)`.

| Returns: | - `None` if user or realm not found.<br>- `False` if user found, but password does not match.<br>- `True` if user found and password matches. |

Changed in version 1.6: This method was previously called `verify`, it was renamed
to prevent ambiguity with the `CryptContext` method.
The old alias is deprecated, and will be removed in Passlib 1.8.

`get_hash`( _user_, _realm=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.get_hash "Permalink to this definition")

Return `htdigest` hash stored for user.

- uses `self.default_realm` if no realm explicitly provided.
- returns `None` if user or realm not found.

Changed in version 1.6: This method was previously named `find`, it was renamed
for clarity. The old name is deprecated, and will be removed
in Passlib 1.8.

### Modification [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtdigestFile-modification "Permalink to this headline")

`set_password`( _user_, \[ _realm_, \] _password_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.set_password "Permalink to this definition")

Set password for user; adds user & realm if needed.

If `self.default_realm` has been set, this may be called
with the syntax `set_password(user, password)`,
otherwise it must be called with all three arguments:
`set_password(user, realm, password)`.

| Returns: | - `True` if existing user was updated<br>- `False` if user account added. |

`delete`( _user_, _realm=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.delete "Permalink to this definition")

Delete user’s entry for specified realm.

if realm is not specified, uses `self.default_realm`.

| Returns: | - `True` if user deleted,<br>- `False` if user not found in realm. |

`delete_realm`( _realm_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.delete_realm "Permalink to this definition")

Delete all users for specified realm.

if realm is not specified, uses `self.default_realm`.

| Returns: | number of users deleted (0 if realm not found) |

### Alternate Constructors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtdigestFile-alternate-constructors "Permalink to this headline")

_classmethod_ `from_string`( _data_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.from_string "Permalink to this definition")

create new object from raw string.

| Parameters: | - **data** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – database to load, as single string.<br>- **\*\*kwds** – all other keywords are the same as in the class constructor |

### Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtdigestFile-attributes "Permalink to this headline")

`default_realm` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.default_realm "Permalink to this definition")

The default realm that will be used if one is not provided
to methods that require it. By default this is `None`,
in which case an explicit realm must be provided for every
method call. Can be written to.

`path` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.path "Permalink to this definition")

Path to local file that will be used as the default
for all [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.load "passlib.apache.HtdigestFile.load") and [`save()`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.save "passlib.apache.HtdigestFile.save") operations.
May be written to, initialized by the _path_ constructor keyword.

`autosave` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#passlib.apache.HtdigestFile.autosave "Permalink to this definition")

Writeable flag indicating whether changes will be automatically
written to _path_.

### Errors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html\#passlib.apache.HtdigestFile-errors "Permalink to this headline")

| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – All of the methods in this class will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") if<br>any user name or realm contains a forbidden character (one of `:\r\n\t\x00`),<br>or is longer than 255 characters. |

Footnotes

|     |     |
| --- | --- |
| \[1\] | Htpasswd Manual - [http://httpd.apache.org/docs/current/programs/htpasswd.html](http://httpd.apache.org/docs/current/programs/htpasswd.html) |

|     |     |
| --- | --- |
| \[2\] | Apache Auth Configuration - [http://httpd.apache.org/docs/current/howto/auth.html](http://httpd.apache.org/docs/current/howto/auth.html) |

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
  - [`passlib.apache` \- Apache Password Files](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#)
    - [Htpasswd Files](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#htpasswd-files)
    - [Htdigest Files](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#htdigest-files)
  - [`passlib.apps` \- Helpers for various applications](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html)
  - [`passlib.context` \- CryptContext Hash Manager](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html)
  - [`passlib.crypto` \- Cryptographic Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html)
  - [`passlib.exc` \- Exceptions and warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html)
  - [`passlib.ext.django` \- Django Password Hashing Plugin](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html)
  - [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html)
  - [`passlib.hosts` \- OS Password Handling](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html)
  - [`passlib.ifc` – Password Hash Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html)
  - [`passlib.pwd` – Password generation helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html)
  - [`passlib.registry` \- Password Handler Registry](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html "passlib.apps - Helpers for various applications")
- [previous](https://passlib.readthedocs.io/en/stable/lib/index.html "API Reference")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.apache.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.apache.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)