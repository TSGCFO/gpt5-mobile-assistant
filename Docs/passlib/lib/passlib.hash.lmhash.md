<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html "passlib.hash.nthash - Windows’ NT-HASH")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html "passlib.hash.oracle11 - Oracle 11g password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.lmhash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#passlib.hash.lmhash "passlib.hash.lmhash") \- LanManager Hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#passlib-hash-lmhash-lanmanager-hash "Permalink to this headline")

Danger

**This algorithm is not considered secure by modern standards.**
It should only be used when verifying existing hashes,
or when interacting with applications that require this format.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

New in version 1.6.

This class implements the LanManager Hash (aka _LanMan_ or _LM_ hash).
It was used by early versions of Microsoft Windows to store user passwords,
until it was supplanted (though not entirely replaced) by
the [nthash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html) algorithm in Windows NT.
It continues to crop up in production due to its integral role
in the legacy NTLM authentication protocol.
This class can be used directly as follows:

```
>>> from passlib.hash import lmhash

>>> # hash password
>>> h = lmhash.hash("password")
>>> h
'e52cac67419a9a224a3b108f3fa6cb6d'

>>> # verify correct password
>>> lmhash.verify("password", h)
True
>>> # verify incorrect password
>>> lmhash.verify("secret", h)
False

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `lmhash` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#passlib.hash.lmhash "Permalink to this definition")

This class implements the Lan Manager Password hash, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It has no salt and a single fixed round.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts a single
optional keyword:

| Parameters: | **truncate\_error** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>By default, this will silently truncate passwords larger than 14 bytes.<br>Setting `truncate_error=True` will cause [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash")<br>to raise a [`PasswordTruncateError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordTruncateError "passlib.exc.PasswordTruncateError") instead.<br>New in version 1.7. |

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods accept a single
optional keyword:

| Parameters: | **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – This specifies what character encoding LMHASH should use when<br>calculating digest. It defaults to `cp437`, the most<br>common encoding encountered. |

Note that while this class outputs digests in lower-case hexadecimal,
it will accept upper-case as well.

### Issues with Non-ASCII Characters [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#issues-with-non-ascii-characters "Permalink to this headline")

Passwords containing only `ascii` characters should hash and compare
correctly across all LMhash implementations. However, due to historical
issues, no two LMhash implementations handle non- `ascii` characters in quite
the same way. While Passlib makes every attempt to behave as close to correct
as possible, the meaning of “correct” is dependant on the software you are
interoperating with. If you think you will have passwords containing
non- `ascii` characters, please read the [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#deviations) section (below) for
details about the known interoperability issues. It’s a mess of codepages.

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#format-algorithm "Permalink to this headline")

A LM hash consists of 32 hexadecimal digits,
which encode the 16 byte digest. An example hash (of `password`) is
`e52cac67419a9a224a3b108f3fa6cb6d`.

The digest is calculated as follows:

1. First, the password should be converted to uppercase, and encoded
using the “OEM Codepage” of the Windows release that the host / target
server is running [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#cp).

For pure-ASCII passwords, this step can be performed
using the `us-ascii` encoding (as most OEM Codepages are ASCII-compatible).
However, for passwords with non-ASCII characters, this step is fraught
with compatibility issues and border cases (see [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#deviations) for details).

2. The password is then truncated to 14 bytes,
or the end NULL padded to 14 bytes; as appropriate.

3. The first 7 bytes of the truncated password from step 2 are used as a key
to DES encrypt the constant `KGS!@#$%`, resulting
in the first 8 bytes of the final digest.

4. Step 3 is repeated using the second 7 bytes of the password from step 2,
resulting in the second 8 bytes of the final digest.

5. The combined digests from 3 and 4 are then encoded to hexadecimal.


## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#security-issues "Permalink to this headline")

Due to a myriad of flaws, and the existence high-speed password cracking software
dedicated to LMHASH, this algorithm should be considered broken. The major flaws include:

- It has no salt, making hashes easily pre-computable.
- It limits the password to 14 characters, and converts the password to
uppercase before hashing, greatly reducing the keyspace.
- By breaking the password into two independent chunks,
they can be attacked independently and simultaneously.
- The independence of the chunks reveals significant information
about the original password: The second 8 bytes of the digest
are the same for all passwords < 8 bytes; and for passwords
of 8-9 characters, the second chunk can be broken _much_ faster,
revealing part of the password, and reducing the likely
keyspace for the first chunk.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html\#deviations "Permalink to this headline")

Passlib’s implementation differs from others in a few ways, all related to
the handling of non-ASCII characters.

- Unicode Policy:

Officially, unicode passwords should be encoded using the “OEM Codepage”
used [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#cp) by the specific release of Windows that the host or target server
is running. Common encodings include `cp437` (used by the English
edition of Windows XP), `cp580` (used by many Western European editions
of XP), and `cp866` (used by many Eastern European editions of XP).
Complicating matters further, some third-party implementations are known
to use encodings such as `latin-1` and `utf-8`, which cause
non-ASCII characters to hash in a manner incompatible with the canonical
MS Windows implementation.

Thus if an application wishes to provide support for non-ASCII passwords,
it must decide which encoding to use.

Passlib uses `cp437` as it’s default encoding for unicode strings.
However, if your database used a different encoding, you will need to either
first encode the passwords into bytes, or override the default encoding
via `lmhash.hash(secret, encoding="some-other-codec")`

All known encodings are `us-ascii`-compatible, so for ASCII passwords,
the default should be sufficient.

- Upper Case Conversion:



Note



Future releases of Passlib may change this behavior
as new information and code is integrated.



Once critical step in the LMHASH algorithm is converting the password
to upper case. While ASCII characters are uppercased as normal,
non-ASCII characters are converted in implementation-dependant ways:

Windows systems encode the password first, and then
convert it to uppercase using an codepage-specific table.
For the most part these tables seem to agree with the Unicode specification,
but there are some codepoints where they deviate (for example,
Unicode uppercases U+00B5 -> U+039C, but `cp437` leaves it unchanged [\[3\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#uc)).

In contrast, most third-party implementations (Passlib included)
perform the uppercase conversion first using the Unicode specification,
and then encode the password second; despite the non-ASCII border cases where the
resulting hash would not match the official Windows hash.


Footnotes

|     |     |
| --- | --- |
| \[1\] | Article used as reference for algorithm -<br>[http://www.linuxjournal.com/article/2717](http://www.linuxjournal.com/article/2717). |

|     |     |
| --- | --- |
| \[2\] | _( [1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#id1), [2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#id2))_ The OEM codepage used by specific Window XP (and earlier) releases<br>can be found at [http://msdn.microsoft.com/nl-nl/goglobal/cc563921%28en-us%29.aspx](http://msdn.microsoft.com/nl-nl/goglobal/cc563921%28en-us%29.aspx). |

|     |     |
| --- | --- |
| [\[3\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#id3) | Online discussion dealing with upper-case encoding issues -<br>[http://www.openwall.com/lists/john-dev/2011/08/01/2](http://www.openwall.com/lists/john-dev/2011/08/01/2). |

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
      - [`passlib.hash.lmhash` \- LanManager Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#interface)
          - [Issues with Non-ASCII Characters](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#issues-with-non-ascii-characters)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#security-issues)
        - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#deviations)
      - [`passlib.hash.nthash` \- Windows’ NT-HASH](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html "passlib.hash.nthash - Windows’ NT-HASH")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html "passlib.hash.oracle11 - Oracle 11g password hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.lmhash.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.lmhash.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)