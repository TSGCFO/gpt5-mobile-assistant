<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html "passlib.hash.msdcc - Windows’ Domain Cached Credentials")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html "passlib.hash.lmhash - LanManager Hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.nthash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html\#passlib.hash.nthash "passlib.hash.nthash") \- Windows’ NT-HASH [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html\#passlib-hash-nthash-windows-nt-hash "Permalink to this headline")

Danger

**This algorithm is dangerously insecure by modern standards.**
It is trivially broken, and should not be used if at all possible.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

New in version 1.6.

This class implements the NT-HASH algorithm, used by Microsoft Windows NT
and successors to store user account passwords, supplanting
the much weaker [lmhash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html) algorithm.
This class can be used directly as follows:

```
>>> from passlib.hash import nthash

>>> # hash password
>>> h = nthash.hash("password")
>>> h
'8846f7eaee8fb117ad06bdd830b7586c'

>>> # verify password
>>> nthash.verify("password", h)
True
>>> nthash.verify("secret", h)
False

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `nthash` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.nthash "Permalink to this definition")

This class implements the NT Password hash, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It has no salt and a single fixed round.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") methods accept no optional keywords.

Note that while this class outputs lower-case hexadecimal digests,
it will accept upper-case digests as well.

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html\#format-algorithm "Permalink to this headline")

A nthash consists of 32 hexadecimal digits, which encode the digest.
An example hash (of `password`) is `8846f7eaee8fb117ad06bdd830b7586c`.

The digest is calculated by encoding the secret using `UTF-16-LE`,
taking the MD4 digest, and then encoding
that as hexadecimal.

## FreeBSD Variant [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html\#freebsd-variant "Permalink to this headline")

For cross-compatibility, FreeBSD’s `crypt()` supports storing
NTHASH digests in a manner compatible with the [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format),
to enable administrators to store user passwords in a manner compatible with
the SMB/CIFS protocol. This is accomplished by assigning NTHASH digests the
identifier `$3$`, and prepending the identifier to the normal (lowercase)
NTHASH digest. An example digest (of `password`) is
`$3$$8846f7eaee8fb117ad06bdd830b7586c` (note the doubled `$$`).

`passlib.hash.` `bsd_nthash` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.bsd_nthash "Permalink to this definition")

This object supports FreeBSD’s representation of NTHASH
(which is compatible with the [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format)),
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It has no salt and a single fixed round.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") methods accept no optional keywords.

Changed in version 1.6: This hash was named `nthash` under previous releases of Passlib.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html\#security-issues "Permalink to this headline")

This algorithm should be considered _completely_ broken:

- It has no salt.
- The MD4 message digest has been severely compromised by collision and
preimage attacks.
- Brute-force and pre-computed attacks exist targeting MD4 hashes in general,
and the encoding used by NTHASH in particular.

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
      - [`passlib.hash.nthash` \- Windows’ NT-HASH](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#format-algorithm)
        - [FreeBSD Variant](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#freebsd-variant)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#security-issues)
      - [`passlib.hash.msdcc` \- Windows’ Domain Cached Credentials](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html "passlib.hash.msdcc - Windows’ Domain Cached Credentials")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html "passlib.hash.lmhash - LanManager Hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.nthash.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.nthash.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)