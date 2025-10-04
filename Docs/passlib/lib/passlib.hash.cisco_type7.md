<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html "passlib.hash.cisco_pix - Cisco PIX MD5 hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html "passlib.hash.msdcc2 - Windows’ Domain Cached Credentials v2")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.cisco_type7`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html\#passlib.hash.cisco_type7 "passlib.hash.cisco_type7") \- Cisco “Type 7” hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html\#passlib-hash-cisco-type7-cisco-type-7-hash "Permalink to this headline")

Danger

This is not a hash, this is a reversible plaintext encoding.
**This format can be trivially decoded**.

New in version 1.6.

This class implements the “Type 7” password encoding used Cisco IOS.
This is not actually a true hash, but a reversible XOR Cipher encoding the plaintext
password. Type 7 strings are (and were designed to be) plaintext equivalent;
the goal was to protect from “over the shoulder” eavesdropping, and
little else. They can be trivially decoded.
This class can be used directly as follows:

```
>>> from passlib.hash import cisco_type7

>>> # encode password
>>> h = cisco_type7.hash("password")
>>> h
'044B0A151C36435C0D'

>>> # verify password
>>> cisco_type7.verify("password", h)
True
>>> pm.verify("letmein", h)
False

>>> # to demonstrate this is an encoding, not a real hash,
>>> # this class supports decoding the resulting string:
>>> cisco_type7.decode(h)
"password"

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

Note

This implementation should work correctly for most cases, but may not
fully implement some edge cases (see [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#deviations) below).
Please report any issues encountered.

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `cisco_type7` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#passlib.hash.cisco_type7 "Permalink to this definition")

This class implements the “Type 7” password encoding used by Cisco IOS,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).
It has a simple 4-5 bit salt, but is nonetheless a reversible encoding
instead of a real hash.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – This may be an optional salt integer drawn from `range(0,16)`.<br>  If omitted, one will be chosen at random.<br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include<br>  `salt` values that are out of range. |

Note that while this class outputs digests in upper-case hexadecimal,
it will accept lower-case as well.

This class also provides the following additional method:

_classmethod_ `decode`( _hash_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#passlib.hash.cisco_type7.decode "Permalink to this definition")

decode hash, returning original password.

| Parameters: | - **hash** – encoded password<br>- **encoding** – optional encoding to use (defaults to `UTF-8`). |
| Returns: | password as unicode |

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html\#format-algorithm "Permalink to this headline")

The Cisco Type 7 encoding consists of two decimal digits
(encoding the salt), followed a series of hexadecimal characters,
two for every byte in the encoded password.
An example encoding (of `"password"`) is `044B0A151C36435C0D`.
This has a salt/offset of 4 ( `04` in the example),
and encodes password via `4B0A151C36435C0D`.

Note

The following description may not be entirely correct with
respect to the official algorithm, see the [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#deviations) section for details.

The algorithm is a straightforward XOR Cipher:

1. The algorithm relies on the following `ascii`-encoded 53-byte
constant:





```
"dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87"

```

2. A integer salt should be generated from the range
0 .. 15. The first two characters of the encoded string are the
zero-padded decimal encoding of the salt.

3. The remaining characters of the encoded string are generated as follows:
For each byte in the password (starting with the 0th byte),
the `i`’th byte of the password is encoded as follows:


> 1. let `j=(i + salt) % 53`
> 2. XOR the `i`’th byte of the password with the `j`’th byte
> of the magic constant.
> 3. encode the resulting byte as uppercase hexadecimal,
> and append to the encoded string.


## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html\#deviations "Permalink to this headline")

This implementation differs from the official one in a few ways.
It may be updated as more information becomes available.

- Unicode Policy:

Type 7 encoding is primarily used with `ASCII` passwords,
how it handles other characters is not known.

In order to provide support for unicode strings, Passlib will encode unicode
passwords using `UTF-8` before running them through this algorithm. If a
different encoding is desired by an application, the password should be
encoded before handing it to Passlib.

- Magic Constant:

Other implementations contain a truncated 26-byte constant instead of the
53-byte constant listed above. However, it is likely those implementations
were merely incomplete, as they exhibit other issues as well after
the 26th byte is reached (throwing an error, truncating the password,
outputing garbage), and only worked for shorter passwords.

- Salt Range:

All known test vectors contain salt values in `range(0,16)`.
However, the algorithm itself should be able to handle any salt value
in `range(0,53)` (the size of the key). For maximum compatibility with
other implementations, Passlib will accept `range(0,53)`, but only
generate salts in `range(0,16)`.

- While this implementation handles all known test vectors,
and tries to make sense of the disparate implementations,
the actual algorithm has not been published by Cisco,
so there may be other unknown deviations.


Footnotes

|     |     |
| --- | --- |
| \[1\] | Description of Type 7 algorithm -<br>[http://pen-testing.sans.org/resources/papers/gcih/cisco-ios-type-7-password-vulnerability-100566](http://pen-testing.sans.org/resources/papers/gcih/cisco-ios-type-7-password-vulnerability-100566),<br>[http://wiki.nil.com/Deobfuscating\_Cisco\_IOS\_Passwords](http://wiki.nil.com/Deobfuscating_Cisco_IOS_Passwords) |

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
    - [Cisco Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#cisco-hashes)
      - [`passlib.hash.cisco_type7` \- Cisco “Type 7” hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#format-algorithm)
        - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html#deviations)
      - [`passlib.hash.cisco_pix` \- Cisco PIX MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html)
      - [`passlib.hash.cisco_asa` \- Cisco ASA MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html "passlib.hash.cisco_pix - Cisco PIX MD5 hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html "passlib.hash.msdcc2 - Windows’ Domain Cached Credentials v2")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.cisco_type7.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.cisco_type7.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)