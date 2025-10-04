<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html "passlib.hash.oracle10 - Oracle 10g password hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html "passlib.hash.mysql41 - MySQL 4.1 password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.postgres_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html\#passlib.hash.postgres_md5 "passlib.hash.postgres_md5") \- PostgreSQL MD5 password hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html\#passlib-hash-postgres-md5-postgresql-md5-password-hash "Permalink to this headline")

Danger

**This algorithm is not considered secure by modern standards.**
It should only be used when verifying existing hashes,
or when interacting with applications that require this format.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

This class implements the md5-based hash algorithm used by PostgreSQL to store
its user account passwords. This scheme was introduced in PostgreSQL 7.2;
prior to this PostgreSQL stored its password in plain text.
Users will most likely find the frontend provided by [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications")
to be more useful than accessing this class directly.
That aside, this class can be used directly as follows:

```
>>> from passlib.hash import postgres_md5

>>> # hash password using specified username
>>> hash = postgres_md5.hash("password", user="username")
>>> hash
'md55a231fcdb710d73268c4f44283487ba2'

>>> # verify correct password
>>> postgres_md5.verify("password", hash, user="username")
True
>>> # verify correct password w/ wrong username
>>> postgres_md5.verify("password", hash, user="somebody")
False
>>> # verify incorrect password
>>> postgres_md5.verify("password", hash, user="username")
False

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `postgres_md5` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#passlib.hash.postgres_md5 "Permalink to this definition")

This class implements the Postgres MD5 Password hash, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It does a single round of hashing, and relies on the username as the salt.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), [`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods all require the
following additional contextual keywords:

| Parameters: | **user** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – name of postgres user account this password is associated with. |

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html\#format-algorithm "Permalink to this headline")

Postgres-MD5 hashes all have the format `md5checksum`,
where `checksum` is 32 hexadecimal digits, encoding a 128-bit checksum.
This checksum is the MD5 message digest of the password concatenated with the username.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html\#security-issues "Permalink to this headline")

This algorithm it not suitable for _any_ use besides manipulating existing
PostgreSQL account passwords, due to the following flaws:

- Its use of the username as a salt value means that common usernames
(e.g. `admin`, `root`, `postgres`) will occur more frequently as salts,
weakening the effectiveness of the salt in foiling pre-computed tables.
- Since the keyspace of `user+password` is still a subset of ascii characters,
existing MD5 lookup tables have an increased chance of being able to reverse common hashes.
- Its simplicity makes high-speed brute force attacks much more feasible [\[3\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#brute) .

Footnotes

|     |     |
| --- | --- |
| \[1\] | Discussion leading up to design of algorithm -<br>[http://archives.postgresql.org/pgsql-hackers/2001-06/msg00952.php](http://archives.postgresql.org/pgsql-hackers/2001-06/msg00952.php) |

|     |     |
| --- | --- |
| \[2\] | Message explaining postgres md5 hash algorithm -<br>[http://archives.postgresql.org/pgsql-php/2003-01/msg00021.php](http://archives.postgresql.org/pgsql-php/2003-01/msg00021.php) |

|     |     |
| --- | --- |
| [\[3\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#id1) | Blog post demonstrating brute-force attack [http://pentestmonkey.net/blog/cracking-postgres-hashes/](http://pentestmonkey.net/blog/cracking-postgres-hashes/). |

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
      - [`passlib.hash.mysql323` \- MySQL 3.2.3 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html)
      - [`passlib.hash.mysql41` \- MySQL 4.1 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html)
      - [`passlib.hash.postgres_md5` \- PostgreSQL MD5 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#security-issues)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html "passlib.hash.oracle10 - Oracle 10g password hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html "passlib.hash.mysql41 - MySQL 4.1 password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.postgres_md5.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.postgres_md5.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)