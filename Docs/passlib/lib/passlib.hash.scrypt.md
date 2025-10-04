<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.apr_md5_crypt.html "passlib.hash.apr_md5_crypt - Apache’s MD5-Crypt variant")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html "passlib.hash.scram - SCRAM Hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.scrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html\#passlib.hash.scrypt "passlib.hash.scrypt") \- SCrypt [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html\#passlib-hash-scrypt-scrypt "Permalink to this headline")

New in version 1.7.

This is a custom hash scheme provided by Passlib which allows storing password hashes
generated using the SCrypt [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#scrypt-home) key derivation function, and is designed
as the of a new generation of “memory hard” functions.

Warning

Be careful when using this algorithm, as the memory and CPU requirements
needed to achieve adequate security are generally higher than acceptable for heavily used
production systems [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#scrypt-cost). This is because (unlike many password hashes), increasing
the rounds value of scrypt will increase the _memory_ required as well as the time.

Unless you know what you’re doing, **You probably want** [argon2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html) **instead.**

This class can be used directly as follows:

```
>>> from passlib.hash import scrypt

>>> # generate new salt, hash password
>>> h = scrypt.hash("password")
>>> h
'$scrypt$ln=16,r=8,p=1$aM15713r3Xsvxbi31lqr1Q$nFNh2CVHVjNldFVKDHDlm4CbdRSCdEBsjjJxD+iCs5E'

>>> # the same, but with an explicit number of rounds
>>> scrypt.using(rounds=8).hash("password")
'$scrypt$ln=8,r=8,p=1$WKs1xljLudd6z9kbY0wpJQ$yCR4iDZYDKv+iEJj6yHY0lv/epnfB6f/w1EbXrsJOuQ'

>>> # verify password
>>> scrypt.verify("password", h)
True
>>> scrypt.verify("wrong", h)
False

```

Note

It is strongly recommended that you install
[scrypt](https://pypi.python.org/pypi/scrypt)
when using this hash.

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `scrypt` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#passlib.hash.scrypt "Permalink to this definition")

This class implements an SCrypt-based password [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#scrypt-home) hash, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a variable-length salt, a variable number of rounds,
as well as some custom tuning parameters unique to scrypt (see below).

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – Optional salt string.<br>  If specified, the length must be between 0-1024 bytes.<br>  If not specified, one will be auto-generated (this is recommended).<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>  Defaults to 16 bytes, but can be any value between 0 and 1024.<br>- **rounds** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – <br>  Optional number of rounds to use.<br>  Defaults to 16, but must be within `range(1,32)`.<br>  <br>  <br>  <br>  Warning<br>  <br>  <br>  <br>  Unlike many hash algorithms, increasing the rounds value<br>  will increase both the time _and memory_ required to hash a password.<br>  <br>- **block\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional block size to pass to scrypt hash function (the `r` parameter).<br>  Useful for tuning scrypt to optimal performance for your CPU architecture.<br>  Defaults to 8.<br>- **parallelism** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional parallelism to pass to scrypt hash function (the `p` parameter).<br>  Defaults to 1.<br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include `rounds`<br>  that are too small or too large, and `salt` strings that are too long. |

Note

The underlying scrypt hash function has a number of limitations
on it’s parameter values, which forbids certain combinations of settings.
The requirements are:

- `linear_rounds = 2**<some positive integer>`
- `linear_rounds < 2**(16 * block_size)`
- `block_size * parallelism <= 2**30-1`

Todo

This class currently does not support configuring default values
for `block_size` or `parallelism` via a [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext")
configuration.

### Scrypt Backends [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html\#scrypt-backends "Permalink to this headline")

This class will use the first available of two possible backends:

1. Python stdlib’s [`hashlib.scrypt()`](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt "(in Python v3.9)") method (only present for Python 3.6+ and OpenSSL 1.1+)
2. The C-accelerated [scrypt](https://pypi.python.org/pypi/scrypt) package, if installed.
3. A pure-python implementation of SCrypt, built into Passlib.

Warning

If [`hashlib.scrypt()`](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt "(in Python v3.9)") is not present on your system, it is strongly recommended to install
the external scrypt package.
The pure-python backend is intended as a reference and last-resort implementation only;
it is 10-100x too slow to be usable in production at a secure `rounds` cost.

Changed in version 1.7.2: Added support for using stdlib’s [`hashlib.scrypt()`](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt "(in Python v3.9)")

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html\#format-algorithm "Permalink to this headline")

This Scrypt hash format is compatible with the [PHC Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#phc-format) and [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format),
and uses `$scrypt$` as the identifying prefix
for all its strings. An example hash (of `password`) is:

> `$scrypt$ln=16,r=8,p=1$aM15713r3Xsvxbi31lqr1Q$nFNh2CVHVjNldFVKDHDlm4CbdRSCdEBsjjJxD+iCs5E`

This string has the format `$scrypt$ln=logN,r=R,p=P$salt$checksum`, where:

- `logN` is the exponent for calculating SCRYPT’s cost parameter (N), encoded as a decimal digit,
(logN is 16 in the example, corresponding to n = 2\*\*16 = 65536).
- `R` is the value of SCRYPT’s block size parameter (r), encoded as a decimal digit,
(r is 8 in the example).
- `P` is the value of SCRYPT’s parallel count parameter (p), encoded as a decimal digit,
(p is 1 in the example).
- `salt` \- this base64 encoded salt bytes passed into the SCRYPT function
( `aM15713r3Xsvxbi31lqr1Q` in the example).
- `checksum` \- this is the base64 encoded derived key bytes returned from the SCRYPT function.
This hash currently always uses 32 bytes, resulting in a 43-character checksum.
( `nFNh2CVHVjNldFVKDHDlm4CbdRSCdEBsjjJxD+iCs5E` in the example).

All byte strings are encoded using the standard base64 encoding, but without
any trailing padding (“=”) chars. The password is encoded into UTF-8 if not already encoded,
and run throught the SCRYPT function; along with the salt, and the values of n, r, and p.
The first 32 bytes of the returned result are encoded as the checksum.

See [http://www.tarsnap.com/scrypt.html](http://www.tarsnap.com/scrypt.html) for the canonical description of the scrypt kdf.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html\#security-issues "Permalink to this headline")

[SCrypt](http://www.tarsnap.com/scrypt.html) is the first in a class of “memory-hard”
key derivation functions. Initially, it looked very promising as a replacement for BCrypt,
PBKDF2, and SHA512-Crypt. However, the fact that it’s `N` parameter controls both
time _and_ memory cost means the two cannot be varied completely independantly. This
eventually proved to be problematic, as `N` values required for even BCrypt levels of security
resulting in memory requirements that were unacceptable on most production systems.

See also

[`argon2`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html#passlib.hash.argon2 "passlib.hash.argon2"), a next generation memory-hard KDF designed as the
successor to SCrypt.

Footnotes

|     |     |
| --- | --- |
| \[1\] | _( [1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#id1), [2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#id3))_ the SCrypt KDF homepage -<br>[http://www.tarsnap.com/scrypt.html](http://www.tarsnap.com/scrypt.html) |

|     |     |
| --- | --- |
| [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#id2) | posts discussing security implications of scrypt’s tying memory cost to calculation time -<br>[http://blog.ircmaxell.com/2014/03/why-i-dont-recommend-scrypt.html](http://blog.ircmaxell.com/2014/03/why-i-dont-recommend-scrypt.html),<br>[http://security.stackexchange.com/questions/26245/is-bcrypt-better-than-scrypt](http://security.stackexchange.com/questions/26245/is-bcrypt-better-than-scrypt),<br>[http://security.stackexchange.com/questions/4781/do-any-security-experts-recommend-bcrypt-for-password-storage](http://security.stackexchange.com/questions/4781/do-any-security-experts-recommend-bcrypt-for-password-storage) |

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
        - [`passlib.hash.argon2` \- Argon2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html)
        - [`passlib.hash.bcrypt_sha256` \- BCrypt+SHA256](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html)
        - [`passlib.hash.phpass` \- PHPass’ Portable Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html)
        - [`passlib.hash.pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html)
        - [`passlib.hash.scram` \- SCRAM Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html)
        - [`passlib.hash.scrypt` \- SCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#interface)
            - [Scrypt Backends](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#scrypt-backends)
          - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#format-algorithm)
          - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html#security-issues)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.apr_md5_crypt.html "passlib.hash.apr_md5_crypt - Apache’s MD5-Crypt variant")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html "passlib.hash.scram - SCRAM Hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.scrypt.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.scrypt.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)