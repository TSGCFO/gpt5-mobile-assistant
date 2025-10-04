<!-- Source: https://passlib.readthedocs.io/en/stable/narr/overview.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/narr/quickstart.html "New Application Quickstart Guide")
- [previous](https://passlib.readthedocs.io/en/stable/install.html "Installation")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

# Library Overview [¶](https://passlib.readthedocs.io/en/stable/narr/overview.html\#library-overview "Permalink to this headline")

Passlib is a collection of routines for managing password hashes
such as found in unix “shadow” files, as returned by stdlib’s [`crypt.crypt()`](https://docs.python.org/3/library/crypt.html#crypt.crypt "(in Python v3.9)"),
as stored in mysql and postgres, and various other places.
Passlib’s contents can be roughly grouped into four categories:
password hashes, password contexts, two-factor authentication,
and other utility functions.

## Password Hashes [¶](https://passlib.readthedocs.io/en/stable/narr/overview.html\#password-hashes "Permalink to this headline")

All of the hashes supported by Passlib are implemented
as “hasher” classes which can be imported from the [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") module.
In turn, all of the hashers have a uniform interface,
which is documented in the [PasswordHash Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-tutorial).

_A word of warning:_ Some the hashes in this library are marked as “insecure”,
and are provided for historical purposes only. Still others are specialized in ways that are not generally useful.
If you are creating a new application and need to choose a password hash,
please read the [New Application Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html) first.

See also

- [PasswordHash Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-tutorial) – walkthrough of using a hasher class.
- [New Application Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html) – if you need to choose a hash.
- [`passlib.ifc`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#module-passlib.ifc "passlib.ifc: abstract interfaces used by Passlib") – PasswordHash API reference
- [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") – list of all hashes in Passlib.

## Password Contexts [¶](https://passlib.readthedocs.io/en/stable/narr/overview.html\#password-contexts "Permalink to this headline")

Mature applications frequently have to deal with tables of existing password hashes.
Over time, they have to support a number of tasks:

- Add support for new algorithms, and deprecate old ones.
- Raise the time-cost settings for existing algorithms as computing power increases.
- Perform rolling upgrades of existing hashes to comply with these changes.
- Eventually, these policies must be hardcoded in the source,
or time must be spent implementing a configuration language to encode them.

In these situations, loading and handling multiple hash algorithms becomes
complicated and tedious. The [`passlib.context`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#module-passlib.context "passlib.context: CryptContext class, for managing multiple password hash schemes") module provides a single class,
`CryptContext`, which attempts to solve all of these problems
(or at least relieve developers of most of the burden).

This class handles managing multiple password hash schemes,
deprecation & migration of old hashes, and supports a simple configuration
language that can be serialized to an INI file.

See also

- [CryptContext Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial) – walkthrough of the CryptContext class
- [`passlib.context`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#module-passlib.context "passlib.context: CryptContext class, for managing multiple password hash schemes") – API reference

## Two-Factor Authentication [¶](https://passlib.readthedocs.io/en/stable/narr/overview.html\#two-factor-authentication "Permalink to this headline")

While not strictly connected to password hashing, modern applications frequently
need to perform the related task of two-factor authentication. One of the most
common protocols for doing this is TOTP ( [**RFC 6238**](https://tools.ietf.org/html/rfc6238.html)).
To help get TOTP in place, the [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#module-passlib.totp "passlib.totp: totp / two factor authentaction") module provides a set of helper functions
for securely configuring, persisting, and verifying TOTP tokens.

See also

- [TOTP tutorial](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-tutorial) – walkthrough of setting up TOTP integration
- [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#module-passlib.totp "passlib.totp: totp / two factor authentaction") – API reference

## Application Helpers [¶](https://passlib.readthedocs.io/en/stable/narr/overview.html\#application-helpers "Permalink to this headline")

Passlib also provides a number of pre-configured `CryptContext` instances
in order to get users started quickly:

> - [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications") – contains pre-configured
> instances for managing hashes used by Postgres, Mysql, and LDAP, and others.
> - [`passlib.hosts`](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#module-passlib.hosts "passlib.hosts: hashing & verifying operating system passwords") – contains pre-configured
> instances for managing hashes as found in the /etc/shadow files
> on Linux and BSD systems.

Passlib also contains a couple of additional modules which provide
support for certain application-specific tasks:

> - [`passlib.apache`](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html#module-passlib.apache "passlib.apache: reading/writing htpasswd & htdigest files") – classes for managing htpasswd and htdigest files.
> - [`passlib.ext.django`](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#module-passlib.ext.django "passlib.ext.django") – Django plugin which monkeypatches support for (almost) any hash in Passlib.

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
  - [Installation](https://passlib.readthedocs.io/en/stable/install.html)
  - [Library Overview](https://passlib.readthedocs.io/en/stable/narr/overview.html#)
    - [Password Hashes](https://passlib.readthedocs.io/en/stable/narr/overview.html#password-hashes)
    - [Password Contexts](https://passlib.readthedocs.io/en/stable/narr/overview.html#password-contexts)
    - [Two-Factor Authentication](https://passlib.readthedocs.io/en/stable/narr/overview.html#two-factor-authentication)
    - [Application Helpers](https://passlib.readthedocs.io/en/stable/narr/overview.html#application-helpers)
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
- [next](https://passlib.readthedocs.io/en/stable/narr/quickstart.html "New Application Quickstart Guide")
- [previous](https://passlib.readthedocs.io/en/stable/install.html "Installation")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/narr/overview.html)**[stable](https://passlib.readthedocs.io/en/stable/narr/overview.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/narr/overview.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)