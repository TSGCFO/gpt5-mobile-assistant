<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html "passlib.hash.ldap_crypt - LDAP crypt() Wrappers")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.dlitz_pbkdf2_sha1.html "passlib.hash.dlitz_pbkdf2_sha1 - Dwayne Litzenberger’s PBKDF2 hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# `passlib.hash.ldap_digest` \- RFC2307 Standard Digests [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#passlib-hash-ldap-digest-rfc2307-standard-digests "Permalink to this headline")

Passlib provides support for all the standard
LDAP hash formats specified by [**RFC 2307**](https://tools.ietf.org/html/rfc2307.html).
This includes `{MD5}`, `{SMD5}`, `{SHA}`, `{SSHA}`.
These schemes range from somewhat to very insecure,
and should not be used except when required.
These classes all wrap the underlying hashlib implementations,
and are can be used directly as follows:

```
>>> from passlib.hash import ldap_salted_md5 as lsm

>>> # hash password
>>> hash = lsm.hash("password")
>>> hash
'{SMD5}OqsUXNHIhHbznxrqHoIM+ZT8DmE='

>>> # verify password
>>> lms.verify("password", hash)
True
>>> lms.verify("secret", hash)
False

```

See also

- [password hash usage](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples) – for more usage examples
- [ldap\_{crypt}](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html) –
LDAP `{CRYPT}` wrappers for common Unix hash algorithms.
- [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications") – for a list of [premade ldap contexts](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#ldap-contexts).

## Plain Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#plain-hashes "Permalink to this headline")

Warning

These hashes should not be considered secure in any way,
as they are nothing but raw MD5 & SHA-1 digests,
which are extremely vulnerable to brute-force attacks.

_class_ `passlib.hash.` `ldap_md5` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_md5 "Permalink to this definition")

This class stores passwords using LDAP’s plain MD5 format, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") methods have no optional keywords.

_class_ `passlib.hash.` `ldap_sha1` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_sha1 "Permalink to this definition")

This class stores passwords using LDAP’s plain SHA1 format, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") methods have no optional keywords.

### Format [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#format "Permalink to this headline")

These hashes have the format `prefixchecksum`.

- `prefix` is `{MD5}` for ldap\_md5, and `{SHA}` for ldap\_sha1.
- `checksum` is the base64 encoding
of the raw message digest of the password,
using the appropriate digest algorithm.

An example ldap\_md5 hash (of `password`) is `{MD5}X03MO1qnZdYdgyfeuILPmQ==`.
An example ldap\_sha1 hash (of `password`) is `{SHA}W6ph5Mm5Pz8GgiULbPgzG37mj9g=`.

## Salted Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#salted-hashes "Permalink to this headline")

_class_ `passlib.hash.` `ldap_salted_md5` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_md5 "Permalink to this definition")

This class stores passwords using LDAP’s salted MD5 format, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a 4-16 byte salt.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – Optional salt string.<br>  If not specified, one will be autogenerated (this is recommended).<br>  If specified, it may be any 4-16 byte string.<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>  Defaults to 4 bytes for compatibility with the LDAP spec,<br>  but some systems use larger salts, and Passlib supports<br>  any value between 4-16.<br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include<br>  `salt` strings that are too long.<br>  <br>  <br>  <br>  New in version 1.6. |

Changed in version 1.6: This format now supports variable length salts, instead of a fix 4 bytes.

_class_ `passlib.hash.` `ldap_salted_sha1` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_sha1 "Permalink to this definition")

This class stores passwords using LDAP’s “Salted SHA1” format,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a 4-16 byte salt.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – Optional salt string.<br>  If not specified, one will be autogenerated (this is recommended).<br>  If specified, it may be any 4-16 byte string.<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>  Defaults to 4 bytes for compatibility with the LDAP spec,<br>  but some systems use larger salts, and Passlib supports<br>  any value between 4-16.<br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include<br>  `salt` strings that are too long.<br>  <br>  <br>  <br>  New in version 1.6. |

Changed in version 1.6: This format now supports variable length salts, instead of a fix 4 bytes.

_class_ `passlib.hash.` `ldap_salted_sha256` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_sha256 "Permalink to this definition")

This class stores passwords using LDAP’s “Salted SHA2-256” format,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a 4-16 byte salt.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – Optional salt string.<br>  If not specified, one will be autogenerated (this is recommended).<br>  If specified, it may be any 4-16 byte string.<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>  Defaults to 8 bytes for compatibility with the LDAP spec,<br>  but Passlib supports any value between 4-16.<br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include<br>  `salt` strings that are too long. |

New in version 1.7.3.

_class_ `passlib.hash.` `ldap_salted_sha512` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_sha512 "Permalink to this definition")

This class stores passwords using LDAP’s “Salted SHA2-512” format,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a 4-16 byte salt.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – Optional salt string.<br>  If not specified, one will be autogenerated (this is recommended).<br>  If specified, it may be any 4-16 byte string.<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>  Defaults to 8 bytes for compatibility with the LDAP spec,<br>  but Passlib supports any value between 4-16.<br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include<br>  `salt` strings that are too long. |

New in version 1.7.3.

These hashes have the format `prefixdata`.

- `prefix` is `{SMD5}` for ldap\_salted\_md5,
and `{SSHA}` for ldap\_salted\_sha1.
- `data` is the base64 encoding of `checksumsalt`;
and in turn `salt` is a multi-byte binary salt,
and `checksum` is the raw digest of the
the string `passwordsalt`,
using the appropriate digest algorithm.

### Format [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#id1 "Permalink to this headline")

An example hash (of `password`) is `{SMD5}jNoSMNY0cybfuBWiaGlFw3Mfi/U=`.
After decoding, this results in a raw salt string `s\x1f\x8b\xf5`,
and a raw MD5 checksum of `\x8c\xda\x120\xd64s&\xdf\xb8\x15\xa2hiE\xc3`.

An example hash (of `password`) is `{SSHA}pKqkNr1tq3wtQqk+UcPyA3HnA2NsU5NJ`.
After decoding, this results in a raw salt string `lS\x93I`,
and a raw SHA1 checksum of `\xa4\xaa\xa46\xbdm\xab|-B\xa9>Q\xc3\xf2\x03q\xe7\x03c`.

### Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#security-issues "Permalink to this headline")

The LDAP salted hashes should not be considered very secure.

- They use only a single round of digests with known collision
and pre-image attacks (SHA1 & MD5).
- They currently use only 32 bits of entropy in their salt,
which is only borderline sufficient to defeat rainbow tables,
and cannot (portably) be increased.
- The SHA2 salted hashes (SSHA256, SSHA512) are only marginally better.
they use the newer SHA2 hash; and 64 bits of entropy in their salt.

## Plaintext [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#plaintext "Permalink to this headline")

_class_ `passlib.hash.` `ldap_plaintext` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_plaintext "Permalink to this definition")

This class stores passwords in plaintext, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

This class acts much like the generic `passlib.hash.plaintext` handler,
except that it will identify a hash only if it does NOT begin with the `{XXX}` identifier prefix
used by RFC2307 passwords.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), [`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods all require the
following additional contextual keyword:

| Parameters: | **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>This controls the character encoding to use (defaults to `utf-8`).<br>This encoding will be used to encode `unicode` passwords<br>under Python 2, and decode `bytes` hashes under Python 3. |

Changed in version 1.6: The `encoding` keyword was added.

This handler does not hash passwords at all,
rather it encoded them into UTF-8.
The only difference between this class and [`plaintext`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html#passlib.hash.plaintext "passlib.hash.plaintext")
is that this class will NOT recognize any strings that use
the `{SCHEME}HASH` format.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html\#deviations "Permalink to this headline")

- The salt size for the salted digests appears to vary between applications.
While OpenLDAP is fixed at 4 bytes, some systems appear to use 8 or more.
As of 1.6, Passlib can accept and generate strings with salts between 4-16 bytes,
though various servers may differ in what they can handle.

Footnotes

|     |     |
| --- | --- |
| \[1\] | The manpage for **slappasswd** \- [http://gd.tuwien.ac.at/linuxcommand.org/man\_pages/slappasswd8.html](http://gd.tuwien.ac.at/linuxcommand.org/man_pages/slappasswd8.html). |

|     |     |
| --- | --- |
| \[2\] | The basic format for these hashes is laid out in RFC 2307 - [http://www.ietf.org/rfc/rfc2307.txt](http://www.ietf.org/rfc/rfc2307.txt) |

|     |     |
| --- | --- |
| \[3\] | OpenLDAP hash documentation - [http://www.openldap.org/doc/admin24/security.html](http://www.openldap.org/doc/admin24/security.html) |

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
      - [Standard LDAP Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#standard-ldap-schemes)
        - [`passlib.hash.ldap_digest` \- RFC2307 Standard Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#)
          - [Plain Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#plain-hashes)
            - [Format](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#format)
          - [Salted Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#salted-hashes)
            - [Format](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#id1)
            - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#security-issues)
          - [Plaintext](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#plaintext)
          - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#deviations)
        - [`passlib.hash.ldap_crypt` \- LDAP crypt() Wrappers](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html)
      - [Non-Standard LDAP Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#non-standard-ldap-schemes)
    - [SQL Database Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#sql-database-hashes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html "passlib.hash.ldap_crypt - LDAP crypt() Wrappers")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.dlitz_pbkdf2_sha1.html "passlib.hash.dlitz_pbkdf2_sha1 - Dwayne Litzenberger’s PBKDF2 hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.ldap_std.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.ldap_std.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)