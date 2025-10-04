<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html "passlib.hash.msdcc2 - Windows’ Domain Cached Credentials v2")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html "passlib.hash.nthash - Windows’ NT-HASH")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.msdcc`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html\#passlib.hash.msdcc "passlib.hash.msdcc") \- Windows’ Domain Cached Credentials [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html\#passlib-hash-msdcc-windows-domain-cached-credentials "Permalink to this headline")

Danger

**This algorithm is not considered secure by modern standards.**
It should only be used when verifying existing hashes,
or when interacting with applications that require this format.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

New in version 1.6.

This class implements the DCC (Domain Cached Credentials) hash, used
by Windows to cache and verify remote credentials when the relevant
server is unavailable. It is known by a number of other names,
including “mscache” and “mscash” (Microsoft CAched haSH). Security wise
it is not particularly strong, as it’s little more than [nthash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html)
salted with a username. It was replaced by [msdcc2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html)
in Windows Vista.
This class can be used directly as follows:

```
>>> from passlib.hash import msdcc

>>> # hash password using specified username
>>> hash = msdcc.hash("password", user="Administrator")
>>> hash
'25fd08fa89795ed54207e6e8442a6ca0'

>>> # verify correct password
>>> msdcc.verify("password", hash, user="Administrator")
True
>>> # verify correct password w/ wrong username
>>> msdcc.verify("password", hash, user="User")
False
>>> # verify incorrect password
>>> msdcc.verify("letmein", hash, user="Administrator")
False

```

See also

- [password hash usage](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples) – for more usage examples
- [msdcc2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html) – the successor to this hash

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `msdcc` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html#passlib.hash.msdcc "Permalink to this definition")

This class implements Microsoft’s Domain Cached Credentials password hash,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It has a fixed number of rounds, and uses the associated
username as the salt.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), [`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods
have the following optional keywords:

| Parameters: | **user** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>String containing name of user account this password is associated with.<br>This is required to properly calculate the hash.<br>This keyword is case-insensitive, and should contain just the username<br>(e.g. `Administrator`, not `SOMEDOMAIN\Administrator`). |

Note that while this class outputs lower-case hexadecimal digests,
it will accept upper-case digests as well.

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html\#format-algorithm "Permalink to this headline")

Much like `lmhash` and `nthash`, MS DCC hashes
consists of a 16 byte digest, usually encoded as 32 hexadecimal characters.
An example hash (of `"password"` with the account `"Administrator"`) is
`25fd08fa89795ed54207e6e8442a6ca0`.

The digest is calculated as follows:

1. The password is encoded using `UTF-16-LE`.
2. The MD4 digest of step 1 is calculated.
(The result of this step is identical to the [`nthash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.nthash "passlib.hash.nthash")
of the password).
3. The unicode username is converted to lowercase,
and encoded using `UTF-16-LE`.
This should be just the plain username (e.g. `User`
not `SOMEDOMAIN\\User`)
4. The username from step 3 is appended to the
digest from step 2; and the MD4 digest of the result
is calculated.
5. The result of step 4 is encoded into hexadecimal,
this is the DCC hash.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html\#security-issues "Permalink to this headline")

This algorithm is should not be used for any purpose besides
manipulating existing DCC v1 hashes, due to the following flaws:

- Its use of the username as a salt value (and lower-case at that),
means that common usernames (e.g. `Administrator`) will occur
more frequently as salts, weakening the effectiveness of the salt in
foiling pre-computed tables.
- The MD4 message digest has been severely compromised by collision and
preimage attacks.
- Efficient brute-force attacks on MD4 exist.

Footnotes

|     |     |
| --- | --- |
| \[1\] | Description of DCC v1 algorithm -<br>[http://openwall.info/wiki/john/MSCash](http://openwall.info/wiki/john/MSCash) |

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
      - [`passlib.hash.msdcc` \- Windows’ Domain Cached Credentials](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html#security-issues)
      - [`passlib.hash.msdcc2` \- Windows’ Domain Cached Credentials v2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html "passlib.hash.msdcc2 - Windows’ Domain Cached Credentials v2")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html "passlib.hash.nthash - Windows’ NT-HASH")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.msdcc.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.msdcc.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)