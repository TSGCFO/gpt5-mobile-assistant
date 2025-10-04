<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html "passlib.hash.mysql41 - MySQL 4.1 password hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2005.html "passlib.hash.mssql2005 - MS SQL 2005 password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.mysql323`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html\#passlib.hash.mysql323 "passlib.hash.mysql323") \- MySQL 3.2.3 password hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html\#passlib-hash-mysql323-mysql-3-2-3-password-hash "Permalink to this headline")

Danger

**This algorithm is not considered secure by modern standards.**
It should only be used when verifying existing hashes,
or when interacting with applications that require this format.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

This class implements the first of MySQL’s password hash functions,
used to store its user account passwords. Introduced in MySQL 3.2.3
under the function `PASSWORD()`, this function was renamed
to `OLD_PASSWORD()` under MySQL 4.1, when a newer password
hash algorithm was introduced (see [`mysql41`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html#passlib.hash.mysql41 "passlib.hash.mysql41")).
Users will most likely find the frontends provided by [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications")
to be more useful than accessing this class directly.
That aside, this class can be used as follows:

```
>>> from passlib.hash import mysql323

>>> # hash password
>>> mysql323.hash("password")
'5d2e19393cc5ef67'

>>> # verify correct password
>>> mysql323.verify("password", '5d2e19393cc5ef67')
True
>>> mysql323.verify("secret", '5d2e19393cc5ef67')
False

```

See also

- [password hash usage](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples) – for more usage examples
- [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications") – for a list of predefined [mysql contexts](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#mysql-contexts).

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `mysql323` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#passlib.hash.mysql323 "Permalink to this definition")

This class implements the MySQL 3.2.3 password hash, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It has no salt and a single fixed round.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") methods accept no optional keywords.

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html\#format-algorithm "Permalink to this headline")

A mysql-323 password hash consists of 16 hexadecimal digits,
directly encoding the 64 bit checksum. MySQL always uses
lower-case letters, and so does Passlib
(though Passlib will recognize upper case letters as well).

The algorithm used is extremely simplistic, for details,
see the source implementation in the footnotes [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#f1).

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html\#security-issues "Permalink to this headline")

Lacking any sort of salt, ignoring all whitespace,
and having a simplistic algorithm that amounts to little more than a checksum,
this is not secure, and should not be used for _any_ purpose
but verifying existing MySQL 3.2.3 - 4.0 password hashes.

Footnotes

|     |     |
| --- | --- |
| [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#id1) | Source of implementation used by Passlib -<br>[http://djangosnippets.org/snippets/1508/](http://djangosnippets.org/snippets/1508/) |

|     |     |
| --- | --- |
| \[2\] | Mysql document describing transition -<br>[http://dev.mysql.com/doc/refman/4.1/en/password-hashing.html](http://dev.mysql.com/doc/refman/4.1/en/password-hashing.html) |

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
    - [Overview](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#overview)
    - [Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#unix-hashes)
    - [Other “Modular Crypt” Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-modular-crypt-hashes)
    - [LDAP / RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-rfc2307-hashes)
    - [SQL Database Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#sql-database-hashes)
      - [`passlib.hash.mssql2000` \- MS SQL 2000 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2000.html)
      - [`passlib.hash.mssql2005` \- MS SQL 2005 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2005.html)
      - [`passlib.hash.mysql323` \- MySQL 3.2.3 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#security-issues)
      - [`passlib.hash.mysql41` \- MySQL 4.1 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html)
      - [`passlib.hash.postgres_md5` \- PostgreSQL MD5 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html)
      - [`passlib.hash.oracle10` \- Oracle 10g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html)
      - [`passlib.hash.oracle11` \- Oracle 11g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html)
    - [MS Windows Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ms-windows-hashes)
    - [Cisco Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#cisco-hashes)
    - [Other Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-hashes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html "passlib.hash.mysql41 - MySQL 4.1 password hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2005.html "passlib.hash.mssql2005 - MS SQL 2005 password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.mysql323.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.mysql323.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)