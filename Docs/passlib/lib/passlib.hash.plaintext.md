<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html "passlib.hosts - OS Password Handling")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html "passlib.hash.hex_digest - Generic Hexadecimal Digests")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.plaintext`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html\#passlib.hash.plaintext "passlib.hash.plaintext") \- Plaintext [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html\#passlib-hash-plaintext-plaintext "Permalink to this headline")

This class stores passwords in plaintext. This is, of course, ridiculously insecure;
it is provided for backwards compatibility when migrating
existing applications. _It should not be used_ for any other purpose.
This class should always be the last algorithm checked, as it will recognize all hashes.
It can be used directly as follows:

```
>>> from passlib.hash import plaintext as plaintext

>>> # "encrypt" password
>>> plaintext.hash("password")
'password'

>>> # verify password
>>> plaintext.verify("password", "password")
True
>>> plaintext.verify("secret", "password")
False

```

See also

- [password hash usage](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples) – for more usage examples
- [`ldap_plaintext`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_plaintext "passlib.hash.ldap_plaintext") – on LDAP systems,
this format is probably more appropriate for storing plaintext passwords.

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `plaintext` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html#passlib.hash.plaintext "Permalink to this definition")

This class stores passwords in plaintext, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), [`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods all require the
following additional contextual keyword:

| Parameters: | **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>This controls the character encoding to use (defaults to `utf-8`).<br>This encoding will be used to encode `unicode` passwords<br>under Python 2, and decode `bytes` hashes under Python 3. |

Changed in version 1.6: The `encoding` keyword was added.

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
    - [Other Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-hashes)
      - [`passlib.hash.django_digest` \- Django-specific Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html)
      - [`passlib.hash.grub_pbkdf2_sha512` \- Grub’s PBKDF2 Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.grub_pbkdf2_sha512.html)
      - [`passlib.hash.hex_digest` \- Generic Hexadecimal Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html)
      - [`passlib.hash.plaintext` \- Plaintext](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html#interface)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html "passlib.hosts - OS Password Handling")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html "passlib.hash.hex_digest - Generic Hexadecimal Digests")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.plaintext.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.plaintext.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)