<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html "passlib.hash.md5_crypt - MD5 Crypt")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html "passlib.hash.sha512_crypt - SHA-512 Crypt")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.unix_disabled`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html\#passlib.hash.unix_disabled "passlib.hash.unix_disabled") \- Unix Disabled Account Helper [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html\#passlib-hash-unix-disabled-unix-disabled-account-helper "Permalink to this headline")

This class does not provide an encryption scheme,
but instead provides a helper for handling disabled
password fields as found in unix `/etc/shadow` files.
This class is mainly useful only for plugging into a
[`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instance.
It can be used directly as follows:

```
>>> from passlib.hash import unix_disabled

>>> # 'hashing' a password always results in "!" or "*"
>>> unix_disabled.hash("password")
'!'

>>> # verifying will fail for all passwords and hashes
>>> unix_disabled.verify("password", "!")
False
>>> unix_disabled.verify("letmein", "*NOPASSWORD*")
False

>>> # this class should identify all strings which aren't
>>> # valid Unix crypt() output, while leaving MCF hashes alone
>>> unix_disabled.identify('!')
True
>>> unix_disabled.identify('')
True
>>> unix_disabled.identify("$1$somehash")
False

```

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `unix_disabled` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_disabled "Permalink to this definition")

This class provides disabled password behavior for unix shadow files,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

This class does not implement a hash, but instead matches the “disabled account”
strings found in `/etc/shadow` on most Unix variants. “encrypting” a password
will simply return the disabled account marker. It will reject all passwords,
no matter the hash string. The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash")
method supports one optional keyword:

| Parameters: | **marker** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>Optional marker string which overrides the platform default<br>used to indicate a disabled account.<br>If not specified, this will default to `"*"` on BSD systems,<br>and use the Linux default `"!"` for all other platforms.<br>( `unix_disabled.default_marker` will contain the default value) |

New in version 1.6: This class was added as a replacement for the now-deprecated
[`unix_fallback`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_fallback "passlib.hash.unix_fallback") class, which had some undesirable features.

## Deprecated Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html\#deprecated-interface "Permalink to this headline")

_class_ `passlib.hash.` `unix_fallback` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_fallback "Permalink to this definition")

This class provides the fallback behavior for unix shadow files, and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

This class does not implement a hash, but instead provides fallback
behavior as found in /etc/shadow on most unix variants.
If used, should be the last scheme in the context.

- this class will positively identify all hash strings.
- for security, passwords will always hash to `!`.
- it rejects all passwords if the hash is NOT an empty string ( `!` or `*` are frequently used).
- by default it rejects all passwords if the hash is an empty string,
but if `enable_wildcard=True` is passed to verify(),
all passwords will be allowed through if the hash is an empty string.

Deprecated since version 1.6: This has been deprecated due to its “wildcard” feature,
and will be removed in Passlib 1.8. Use [`unix_disabled`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_disabled "passlib.hash.unix_disabled") instead.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html\#deviations "Permalink to this headline")

According to the Linux `shadow` man page, an empty string is treated
as a wildcard by Linux, allowing all passwords. For security purposes,
this behavior is NOT supported; empty strings are treated the same as `!` or `*`.

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
      - [Active Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#active-unix-hashes)
        - [`passlib.hash.bcrypt` \- BCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html)
        - [`passlib.hash.sha256_crypt` \- SHA-256 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html)
        - [`passlib.hash.sha512_crypt` \- SHA-512 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html)
        - [`passlib.hash.unix_disabled` \- Unix Disabled Account Helper](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#interface)
          - [Deprecated Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#deprecated-interface)
          - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#deviations)
      - [Deprecated Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#deprecated-unix-hashes)
      - [Archaic Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#archaic-unix-hashes)
    - [Other “Modular Crypt” Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-modular-crypt-hashes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html "passlib.hash.md5_crypt - MD5 Crypt")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html "passlib.hash.sha512_crypt - SHA-512 Crypt")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.unix_disabled.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.unix_disabled.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)