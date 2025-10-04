<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html "passlib.hash.plaintext - Plaintext")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.grub_pbkdf2_sha512.html "passlib.hash.grub_pbkdf2_sha512 - Grub’s PBKDF2 Hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# `passlib.hash.hex_digest` \- Generic Hexadecimal Digests [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html\#passlib-hash-hex-digest-generic-hexadecimal-digests "Permalink to this headline")

Danger

Using a single round of any cryptographic hash
(especially without a salt) is so insecure
that it’s barely better than plaintext.
Do not use these schemes in new applications.

Some existing applications store passwords by storing them using
hexadecimal-encoded message digests, such as MD5 or SHA1.
Such schemes are _extremely_ vulnerable to pre-computed brute-force attacks,
and should not be used in new applications. However, for the sake
of backwards compatibility when converting existing applications,
Passlib provides wrappers for few of the common hashes.
These classes all wrap the underlying hashlib implementations,
and can be used directly as follows:

```
>>> from passlib.hash import hex_sha1 as hex_sha1

>>> # hash password
>>> h = hex_sha1.hash("password")
>>> h
'5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'

>>> # verify correct password
>>> hex_sha1.verify("password", h)
True

>>> # verify incorrect password
>>> hex_sha1.verify("secret", h)
False

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `hex_md4` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#passlib.hash.hex_md4 "Permalink to this definition")_class_ `passlib.hash.` `hex_md5` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#passlib.hash.hex_md5 "Permalink to this definition")_class_ `passlib.hash.` `hex_sha1` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#passlib.hash.hex_sha1 "Permalink to this definition")_class_ `passlib.hash.` `hex_sha256` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#passlib.hash.hex_sha256 "Permalink to this definition")_class_ `passlib.hash.` `hex_sha512` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#passlib.hash.hex_sha512 "Permalink to this definition")

Each of these classes implements a plain hexadecimal encoded
message digest, using the relevant digest function from `hashlib`,
and following the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

They support no settings or other keywords.

Note

Oracle VirtualBox’s **VBoxManager internalcommands passwordhash** command
uses [`hex_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#passlib.hash.hex_sha256 "passlib.hash.hex_sha256").

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html\#format-algorithm "Permalink to this headline")

All of these classes just report the result of the specified digest,
encoded as a series of lowercase hexadecimal characters;
though upper case is accepted as input.

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
      - [`passlib.hash.hex_digest` \- Generic Hexadecimal Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html#format-algorithm)
      - [`passlib.hash.plaintext` \- Plaintext](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html "passlib.hash.plaintext - Plaintext")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.grub_pbkdf2_sha512.html "passlib.hash.grub_pbkdf2_sha512 - Grub’s PBKDF2 Hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.hex_digests.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.hex_digests.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)