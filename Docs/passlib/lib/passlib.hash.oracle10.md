<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html "passlib.hash.oracle11 - Oracle 11g password hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html "passlib.hash.postgres_md5 - PostgreSQL MD5 password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.oracle10`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html\#passlib.hash.oracle10 "passlib.hash.oracle10") \- Oracle 10g password hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html\#passlib-hash-oracle10-oracle-10g-password-hash "Permalink to this headline")

Danger

**This algorithm is dangerously insecure by modern standards.**
It is trivially broken, and should not be used if at all possible.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

This class implements the hash algorithm used by the Oracle Database up to
version 10g Rel.2. It was superseded by a newer algorithm in [`Oracle 11`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html#passlib.hash.oracle11 "passlib.hash.oracle11").
This class can be used directly as follows (note that this class requires
a username for all encrypt/verify operations):

```
>>> from passlib.hash import oracle10 as oracle10

>>> # hash password using specified username
>>> hash = oracle10.hash("password", user="username")
>>> hash
'872805F3F4C83365'

>>> # verify correct password
>>> oracle10.verify("password", hash, user="username")
True
>>> # verify correct password w/ wrong username
>>> oracle10.verify("password", hash, user="somebody")
False
>>> # verify incorrect password
>>> oracle10.verify("letmein", hash, user="username")
False

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

Warning

This implementation has not been compared
very carefully against the official implementation or reference documentation,
and its behavior may not match under various border cases.
_caveat emptor_.

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `oracle10` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#passlib.hash.oracle10 "Permalink to this definition")

This class implements the password hash used by Oracle up to version 10g, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It does a single round of hashing, and relies on the username as the salt.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), [`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods all require the
following additional contextual keywords:

| Parameters: | **user** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – name of oracle user account this password is associated with. |

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html\#format-algorithm "Permalink to this headline")

Oracle10 hashes all consist of a series of 16 hexadecimal digits,
representing the resulting checksum.
Oracle10 hashes can be formed by the following procedure:

1. Concatenate the username and password together.
2. Convert the result to upper case
3. Encoding the result in a multi-byte format [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#enc) such that ascii characters (eg: `USER`) are represented
with additional null bytes inserted (eg: `\x00U\x00S\x00E\x00R`).
4. Right-pad the result with null bytes, to bring the total size to an integer multiple of 8.
this is the final input string.
5. The input string is then encoded using DES in CBC mode.
The string `\x01\x23\x45\x67\x89\xAB\xCD\xEF` is used as the DES key,
and a block of null bytes is used as the CBC initialization vector.
All but the last block of ciphertext is discarded.
6. The input string is then run through DES-CBC a second time;
this time the last block of ciphertext from step 5 is used as the DES key,
a block of null bytes is still used as the CBC initialization vector.
All but the last block of ciphertext is discarded.
7. The last block of ciphertext of step 6 is converted
to a hexadecimal string, and returned as the checksum.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html\#security-issues "Permalink to this headline")

This algorithm it not suitable for _any_ use besides manipulating existing
Oracle10 account passwords, due to the following flaws [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#flaws):

- Its use of the username as a salt value means that common usernames
(e.g. `system`) will occur more frequently as salts,
weakening the effectiveness of the salt in foiling pre-computed tables.
- The fact that it is case insensitive, and simply concatenates the username
and password, greatly reduces the keyspace that must be searched by
brute-force or pre-computed attacks.
- Its simplicity, and decades of research on high-speed DES
implementations, makes efficient brute force attacks much more feasible.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html\#deviations "Permalink to this headline")

Passlib’s implementation of the Oracle10g hash may deviate from the official
implementation in unknown ways, as there is no official documentation.
There is only one known issue:

- Unicode Policy

Lack of testing (and test vectors) leaves it unclear
as to how Oracle 10g handles passwords containing non-7bit ascii.
In order to provide support for unicode strings,
Passlib will encode unicode passwords using `utf-16-be` [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#enc)
before running them through the Oracle10g algorithm.
This behavior may be altered in the future, if further testing
reveals another behavior is more in line with the official representation.
This note applies as well to any provided username,
as they are run through the same policy.


Footnotes

|     |     |
| --- | --- |
| \[1\] | _( [1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#id1), [2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#id3))_ The exact encoding used in step 3 of the algorithm is not clear from known references.<br>Passlib uses `utf-16-be`, as this is both compatible with existing test vectors,<br>and supports unicode input. |

|     |     |
| --- | --- |
| [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#id2) | Whitepaper analyzing flaws in this algorithm -<br>[http://www.isg.rhul.ac.uk/~ccid/publications/oracle\_passwd.pdf](http://www.isg.rhul.ac.uk/~ccid/publications/oracle_passwd.pdf). |

|     |     |
| --- | --- |
| \[3\] | Description of Oracle10g and Oracle11g algorithms -<br>[http://www.notesbit.com/index.php/scripts-oracle/oracle-11g-new-password-algorithm-is-revealed-by-seclistsorg/](http://www.notesbit.com/index.php/scripts-oracle/oracle-11g-new-password-algorithm-is-revealed-by-seclistsorg/). |

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
      - [`passlib.hash.postgres_md5` \- PostgreSQL MD5 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html)
      - [`passlib.hash.oracle10` \- Oracle 10g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#security-issues)
        - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#deviations)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html "passlib.hash.oracle11 - Oracle 11g password hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html "passlib.hash.postgres_md5 - PostgreSQL MD5 password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.oracle10.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.oracle10.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)