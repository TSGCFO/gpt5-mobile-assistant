<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html "passlib.hash.cisco_type7 - Cisco “Type 7” hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html "passlib.hash.msdcc - Windows’ Domain Cached Credentials")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.msdcc2`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html\#passlib.hash.msdcc2 "passlib.hash.msdcc2") \- Windows’ Domain Cached Credentials v2 [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html\#passlib-hash-msdcc2-windows-domain-cached-credentials-v2 "Permalink to this headline")

New in version 1.6.

This class implements the DCC2 (Domain Cached Credentials version 2) hash, used
by Windows Vista and newer to cache and verify remote credentials when the relevant
server is unavailable. It is known by a number of other names,
including “mscache2” and “mscash2” (Microsoft CAched haSH). It replaces
the weaker [msdcc v1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html) hash used by previous releases
of Windows. Security wise it is not particularly weak, but due to its
use of the username as a salt, it should probably not be used for anything
but verifying existing cached credentials.
This class can be used directly as follows:

```
>>> from passlib.hash import msdcc2

>>> # hash password using specified username
>>> hash = msdcc2.hash("password", user="Administrator")
>>> hash
'4c253e4b65c007a8cd683ea57bc43c76'

>>> # verify correct password
>>> msdcc2.verify("password", hash, user="Administrator")
True
>>> # verify correct password w/ wrong username
>>> msdcc2.verify("password", hash, user="User")
False
>>> # verify incorrect password
>>> msdcc2.verify("letmein", hash, user="Administrator")
False

```

See also

- [password hash usage](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples) – for more usage examples
- [msdcc](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html) – the predecessor to this hash

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `msdcc2` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html#passlib.hash.msdcc2 "Permalink to this definition")

This class implements version 2 of Microsoft’s Domain Cached Credentials
password hash, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It has a fixed number of rounds, and uses the associated
username as the salt.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), [`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods
have the following extra keyword:

| Parameters: | **user** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>String containing name of user account this password is associated with.<br>This is required to properly calculate the hash.<br>This keyword is case-insensitive, and should contain just the username<br>(e.g. `Administrator`, not `SOMEDOMAIN\Administrator`). |

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html\#format-algorithm "Permalink to this headline")

Much like `lmhash`, `nthash`, and `msdcc`,
MS DCC v2 hashes consists of a 16 byte digest, usually encoded as 32
hexadecimal characters. An example hash (of `"password"` with the
account `"Administrator"`) is `4c253e4b65c007a8cd683ea57bc43c76`.

The digest is calculated as follows:

1. The password is encoded using `UTF-16-LE`.
2. The MD4 digest of step 1 is calculated.
(The result of this is identical to the [`nthash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.nthash "passlib.hash.nthash")
digest of the password).
3. The unicode username is converted to lowercase,
and encoded using `UTF-16-LE`.
This should be just the plain username (e.g. `User`
not `SOMEDOMAIN\\User`)
4. The username from step 3 is appended to the
digest from step 2; and the MD4 digest of the result
is calculated (The result of this is identical to the
[`msdcc`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html#passlib.hash.msdcc "passlib.hash.msdcc") digest).
5. [`PBKDF2-HMAC-SHA1`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf2_hmac "passlib.crypto.digest.pbkdf2_hmac") is then invoked,
using the result of step 4 as the secret, the username from step 3 as
the salt, 10240 rounds, and resulting in a 16 byte digest.
6. The result of step 5 is encoded into hexadecimal;
this is the DCC2 hash.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html\#security-issues "Permalink to this headline")

This hash is essentially [msdcc v1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html) with a fixed-round PBKDF2 function
wrapped around it. The number of rounds of PBKDF2 is currently
sufficient to make this a semi-reasonable way to store passwords,
but the use of the lowercase username as a salt, and the fact
that the rounds can’t be increased, means this hash is not particularly
future-proof, and should not be used for new applications.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html\#deviations "Permalink to this headline")

- Max Password Size

Windows appears to enforce a maximum password size,
but the actual value of this limit is unclear; sources
report it to be set at assorted values from 26 to 128 characters,
and it may in fact vary between Windows releases.
The one consistent piece of information is that
passwords above the limit are simply not allowed (rather
than truncated ala [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt")).
Because of this, Passlib does not currently enforce a size limit:
any hashes this class generates should be correct, provided Windows
is willing to accept a password of that size.


Footnotes

|     |     |
| --- | --- |
| \[1\] | Description of DCC v2 algorithm -<br>[http://openwall.info/wiki/john/MSCash2](http://openwall.info/wiki/john/MSCash2) |

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
    - [MS Windows Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ms-windows-hashes)
      - [`passlib.hash.lmhash` \- LanManager Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html)
      - [`passlib.hash.nthash` \- Windows’ NT-HASH](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html)
      - [`passlib.hash.msdcc` \- Windows’ Domain Cached Credentials](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html)
      - [`passlib.hash.msdcc2` \- Windows’ Domain Cached Credentials v2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html#security-issues)
        - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html#deviations)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html "passlib.hash.cisco_type7 - Cisco “Type 7” hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html "passlib.hash.msdcc - Windows’ Domain Cached Credentials")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.msdcc2.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.msdcc2.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)