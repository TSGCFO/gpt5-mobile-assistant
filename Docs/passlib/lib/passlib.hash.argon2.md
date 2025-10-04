<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html "passlib.hash.bcrypt_sha256 - BCrypt+SHA256")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.crypt16.html "passlib.hash.crypt16 - Crypt16")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.argon2`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#passlib.hash.argon2 "passlib.hash.argon2") \- Argon2 [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#passlib-hash-argon2-argon2 "Permalink to this headline")

New in version 1.7.

This hash provides support for the Argon2 [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#argon2-home) password hash.
Argon2(i) is a state of the art memory-hard password hash, and the
winner of the 2013 Password Hashing Competition [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#phc). It has seen active development
and analysis in subsequent years, and while young, and is intended to replace
[`pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha256 "passlib.hash.pbkdf2_sha256"), [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt"), and [`scrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#passlib.hash.scrypt "passlib.hash.scrypt").

It is one of the four hashes Passlib [recommends](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes)
for new applications. This class can be used directly as follows:

```
>>> from passlib.hash import argon2

>>> # generate new salt, hash password
>>> h = argon2.hash("password")
>>> h
'$argon2i$v=19$m=512,t=2,p=2$aI2R0hpDyLm3ltLa+1/rvQ$LqPKjd6n8yniKtAithoR7A'

>>> # the same, but with an explicit number of rounds
>>> argon2.using(rounds=4).hash("password")
'$argon2i$v=19$m=512,t=4,p=2$eM+ZMyYkpDRGaI3xXmuNcQ$c5DeJg3eb5dskVt1mDdxfw'

>>> # verify password
>>> argon2.verify("password", h)
True
>>> argon2.verify("wrong", h)
False

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `argon2` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#passlib.hash.argon2 "Permalink to this definition")

This class implements the Argon2 password hash [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#argon2-home), and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

Argon2 supports a variable-length salt, and variable time & memory cost,
and a number of other configurable parameters.

The `replace()` method accepts the following optional keywords:

| Parameters: | - **type** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Specify the type of argon2 hash to generate.<br>  Can be one of “ID”, “I”, “D”.<br>  <br>  This defaults to “ID” if supported by the backend, otherwise “I”.<br>  <br>- **salt** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – Optional salt string.<br>  If specified, the length must be between 0-1024 bytes.<br>  If not specified, one will be auto-generated (this is recommended).<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>- **rounds** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of rounds to use.<br>  This corresponds linearly to the amount of time hashing will take.<br>- **time\_cost** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – An alias for **rounds**, for compatibility with underlying argon2 library.<br>- **memory\_cost** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Defines the memory usage in kibibytes.<br>  This corresponds linearly to the amount of memory hashing will take.<br>- **parallelism** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Defines the parallelization factor.<br>  _NOTE: this will affect the resulting hash value._<br>- **digest\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Length of the digest in bytes.<br>- **max\_threads** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – <br>  Maximum number of threads that will be used.<br>  -1 means unlimited; otherwise hashing will use `min(parallelism, max_threads)` threads.<br>  <br>  <br>  <br>  Note<br>  <br>  <br>  <br>  This option is currently only honored by the argon2pure backend.<br>  <br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include `rounds`<br>  that are too small or too large, and `salt` strings that are too long. |

Changed in version 1.7.2: Added the “type” keyword, and support for type “D” and “ID” hashes.
(Prior versions could verify type “D” hashes, but not generate them).

Todo

- Support configurable threading limits.

### Argon2 Backends [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#argon2-backends "Permalink to this headline")

This class will use the first available of two possible backends:

1. [argon2\_cffi](https://pypi.python.org/pypi/argon2_cffi), if installed.
(this is the recommended option).
2. [argon2pure](https://pypi.python.org/pypi/argon2pure), if installed.

If no backends are available, `hash()` and `verify()`
will throw [`MissingBackendError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.MissingBackendError "passlib.exc.MissingBackendError") when they are invoked.
You can check which backend is in use by calling `argon2.get_backend()`.

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#format-algorithm "Permalink to this headline")

The Argon2 hash format is defined by the argon2 reference implementation.
It’s compatible with the [PHC Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#phc-format) and [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format),
and uses `$argon2i$`, `$argon2d$`, or `$argon2id$` as the identifying prefixes
for all its strings. An example hash (of `password`) is:

> `$argon2i$v=19$m=512,t=3,p=2$c29tZXNhbHQ$SqlVijFGiPG+935vDSGEsA`

This string has the format `$argon2X$v=V$m=M,t=T,p=P$salt$digest`, where:

- `X` is either `i`, `d`, or `id`; depending on the argon2 variant
( `i` in the example).
- `V` is an integer representing the argon2 revision.
the value (when rendered into hexidecimal) matches the argon2 version
(in the example, `v=19` corresponds to 0x13, or Argon2 v1.3).
- `M` is an integer representing the variable memory cost, in kibibytes
(512kib in the example).
- `T` is an integer representing the variable time cost, in linear iterations.
(3 in the example).
- `P` is a parallelization parameter, which controls how much of the hash calculation
is parallelization (2 in the example).
- `salt` \- this is the base64-encoded version of the raw salt bytes
passed into the Argon2 function ( `c29tZXNhbHQ` in the example).
- `digest` \- this is the base64-encoded version of the raw derived key
bytes returned from the Argon2 function. Argon2 supports a variable
checksum size, though the hashes in passlib will typically be 16 bytes, resulting in a
22 byte digest ( `SqlVijFGiPG+935vDSGEsA` in the example).

All integer values are encoded uses ascii decimal, with no leading zeros.
All byte strings are encoded using the standard base64 encoding, but without
any trailing padding (“=”) chars.

Note

The `v=version$` segment was added in Argon2 v1.3; older version Argon2 v1.0
hashes may not include this portion.

The Argon2 specification also supports an optional `,data=data` suffix
following `p=parallelism`; but this is not consistently or fully supported.

The algorithm used by all of these schemes is deliberately identical and simple:
The password is encoded into UTF-8 if not already encoded, and handed off to the Argon2 function.
A specified number of bytes (16 byte default in passlib) returned result are encoded as the checksum.

See [https://github.com/P-H-C/phc-winner-argon2](https://github.com/P-H-C/phc-winner-argon2) for the canonical description of the Argon2 hash.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#security-issues "Permalink to this headline")

Argon2 is relatively new compared to other password hash algorithms, having started life in 2013,
and thus may still harbor some undiscovered issues. That said, it’s one of _very_ few which were
designed explicitly with password hashing in mind; and draws strongly on the lessons of the algorithms
before it. As of the release of Passlib 1.7, it has no known major security issues.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html\#deviations "Permalink to this headline")

- This implementation currently encodes all unicode passwords using UTF-8 before hashing,
other implementations may vary, or offer a configurable encoding; though UTF-8 is assumed
to be the default.

Footnotes

|     |     |
| --- | --- |
| \[1\] | _( [1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#id1), [2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#id3))_ the Argon2 homepage -<br>[https://github.com/P-H-C/phc-winner-argon2](https://github.com/P-H-C/phc-winner-argon2) |

|     |     |
| --- | --- |
| [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#id2) | 2012 Password Hashing Competition -<br>[https://password-hashing.net/](https://password-hashing.net/) |

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
      - [Active Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#active-hashes)
        - [`passlib.hash.argon2` \- Argon2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#interface)
            - [Argon2 Backends](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#argon2-backends)
          - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#format-algorithm)
          - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#security-issues)
          - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#deviations)
        - [`passlib.hash.bcrypt_sha256` \- BCrypt+SHA256](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html)
        - [`passlib.hash.phpass` \- PHPass’ Portable Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html)
        - [`passlib.hash.pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html)
        - [`passlib.hash.scram` \- SCRAM Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html)
        - [`passlib.hash.scrypt` \- SCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html)
      - [Deprecated Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#deprecated-hashes)
    - [LDAP / RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-rfc2307-hashes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html "passlib.hash.bcrypt_sha256 - BCrypt+SHA256")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.crypt16.html "passlib.hash.crypt16 - Crypt16")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.argon2.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.argon2.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)