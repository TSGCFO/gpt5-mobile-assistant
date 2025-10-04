<!-- Source: https://passlib.readthedocs.io/en/stable/install.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/narr/overview.html "Library Overview")
- [previous](https://passlib.readthedocs.io/en/stable/narr/index.html "Walkthrough & Tutorials")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

# Installation [¶](https://passlib.readthedocs.io/en/stable/install.html\#installation "Permalink to this headline")

## Supported Platforms [¶](https://passlib.readthedocs.io/en/stable/install.html\#supported-platforms "Permalink to this headline")

Passlib requires Python 2 (>= 2.6) or Python 3 (>= 3.3).
It is known to work with the following Python implementations:

Warning

**Passlib 1.8 will drop support for Python 2.x, 3.3, and 3.4**;
and will require Python >= 3.5. The 1.7 series will be the
last to support Python 2. (See [issue 119](https://foss.heptapod.net/python-libs/passlib/issues/119) for rationale).

- CPython 2 – v2.6 or newer.
- CPython 3 – v3.3 or newer.
- PyPy – v2.0 or newer.
- PyPy3 – v5.3 or newer.
- Jython – v2.7 or newer.

Passlib should work with all operating systems and environments,
as it contains builtin fallbacks for almost all OS-dependant features.
Google App Engine is supported as well.

Changed in version 1.7: Support for Python 2.5, 3.0-3.2 was dropped.
Support for PyPy 1.x was dropped.

## Optional Libraries [¶](https://passlib.readthedocs.io/en/stable/install.html\#optional-libraries "Permalink to this headline")

- [bcrypt](https://pypi.python.org/pypi/bcrypt),
[py-bcrypt](https://pypi.python.org/pypi/py-bcrypt), or
[bcryptor](https://bitbucket.org/ares/bcryptor/overview)


> Warning
>
> Support for `py-bcrypt` and `bcryptor` will be dropped in Passlib 1.8,
> as these libraries are unmaintained.
>
> If any of these packages are installed, they will be used to provide
> support for the BCrypt hash algorithm.
> This is required if you want to handle BCrypt hashes,
> and your OS does not provide native BCrypt support
> via stdlib’s `crypt` (which includes pretty much all non-BSD systems).
>
> [bcrypt](https://pypi.python.org/pypi/bcrypt) is currently the recommended
> option – it’s actively maintained, and compatible with both CPython and PyPy.
>
> Use `pip install passlib[bcrypt]` to get the recommended bcrypt setup.

- [argon2\_cffi](https://pypi.python.org/pypi/argon2_cffi) (>= 18.2.0), or
[argon2pure](https://pypi.python.org/pypi/argon2pure) (>= 1.3)


> If any of these packages are installed, they will be used to provide
> support for the [`argon2`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#passlib.hash.argon2 "passlib.hash.argon2") hash algorithm.
> [argon2\_cffi](https://pypi.python.org/pypi/argon2_cffi) is currently the recommended
> option.
>
> Use `pip install passlib[argon2]` to get the recommended argon2 setup.

- [Cryptography](https://pypi.python.org/pypi/cryptography)


> If installed, will be used to enable encryption of TOTP secrets for storage
> (see [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#module-passlib.totp "passlib.totp: totp / two factor authentaction")).
>
> Use `pip install passlib[totp]` to get the recommended TOTP setup.

- [fastpbkdf2](https://pypi.python.org/pypi/fastpbkdf2)


> If installed, will be used to greatly speed up [`pbkdf2_hmac()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf2_hmac "passlib.crypto.digest.pbkdf2_hmac"),
> and any pbkdf2-based hashes.

- [SCrypt](https://pypi.python.org/pypi/scrypt) (>= 0.6)


> If installed, this will be used to provide support for the [`scrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#passlib.hash.scrypt "passlib.hash.scrypt")
> hash algorithm. If not installed, a MUCH slower builtin reference implementation will be used.


Changed in version 1.7: Added fastpbkdf2, cryptography, argon2\_cffi, argon2pure, and scrypt support.
Removed M2Crypto support.

## Installation Instructions [¶](https://passlib.readthedocs.io/en/stable/install.html\#installation-instructions "Permalink to this headline")

Caution

All PyPI releases are signed with the gpg key
[4D8592DF4CE1ED31](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x4D8592DF4CE1ED31).

To install from PyPi using **pip**:

```
pip install passlib

```

To install from the source using **setup.py**:

```
python setup.py install

```

## Testing [¶](https://passlib.readthedocs.io/en/stable/install.html\#testing "Permalink to this headline")

Passlib contains a comprehensive set of unittests (about 38% of the total code),
which provide nearly complete coverage, and verification of the hash
algorithms using multiple external sources (if detected at runtime).

All unit tests are contained within the `passlib.tests` subpackage,
and are designed to be run using the
[Nose](http://somethingaboutorange.com/mrl/projects/nose) unit testing library
(as well as the `unittest2` library under Python 2.6).

Once Passlib and Nose have been installed, the main suite of tests may be run using:

```
nosetests --tests passlib.tests

```

By default, this runs the main battery of tests, but omits some additional ones
(such as internal cross-checks, and mock-testing of features not provided natively by the host OS).
To run these tests as well, set the following environmental variable:

```
PASSLIB_TEST_MODE="full" nosetests --tests passlib.tests

```

To run a quick check to confirm just basic functionality, with a pared-down set of tests:

```
PASSLIB_TEST_MODE="quick" nosetests --tests passlib.tests

```

Tests may also be run via `setup.py test` or the included `tox.ini` file.
The `tox.ini` file is used to test passlib before each release,
and contains a number different environment setups.
These tests require [tox](https://pypi.python.org/pypi/tox) 2.5 or later.

## Building the Documentation [¶](https://passlib.readthedocs.io/en/stable/install.html\#building-the-documentation "Permalink to this headline")

The latest copy of this documentation should always be available
online at [https://passlib.readthedocs.io](https://passlib.readthedocs.io/).
If you wish to generate your own copy of the documentation,
you will need to:

1. Download the Passlib source, extract it, and `cd` into the source directory.
2. Install all the dependencies required via `pip install -e .[build_docs]`.
3. Run `python setup.py build_sphinx`.
4. Once Sphinx completes its run, point a web browser to the file at `SOURCE/build/sphinx/html/index.html`
to access the Passlib documentation in html format.

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
  - [Installation](https://passlib.readthedocs.io/en/stable/install.html#)
    - [Supported Platforms](https://passlib.readthedocs.io/en/stable/install.html#supported-platforms)
    - [Optional Libraries](https://passlib.readthedocs.io/en/stable/install.html#optional-libraries)
    - [Installation Instructions](https://passlib.readthedocs.io/en/stable/install.html#installation-instructions)
    - [Testing](https://passlib.readthedocs.io/en/stable/install.html#testing)
    - [Building the Documentation](https://passlib.readthedocs.io/en/stable/install.html#building-the-documentation)
  - [Library Overview](https://passlib.readthedocs.io/en/stable/narr/overview.html)
  - [New Application Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html)
  - [`PasswordHash` Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html)
  - [`CryptContext` Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html)
  - [`TOTP` Tutorial](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/narr/overview.html "Library Overview")
- [previous](https://passlib.readthedocs.io/en/stable/narr/index.html "Walkthrough & Tutorials")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/install.html)**[stable](https://passlib.readthedocs.io/en/stable/install.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/install.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)