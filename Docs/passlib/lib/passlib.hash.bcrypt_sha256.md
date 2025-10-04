<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html "passlib.hash.phpass - PHPass’ Portable Hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html "passlib.hash.argon2 - Argon2")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.bcrypt_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html\#passlib.hash.bcrypt_sha256 "passlib.hash.bcrypt_sha256") \- BCrypt+SHA256 [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html\#passlib-hash-bcrypt-sha256-bcrypt-sha256 "Permalink to this headline")

New in version 1.6.2.

BCrypt was developed to replace [`md5_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html#passlib.hash.md5_crypt "passlib.hash.md5_crypt") for BSD systems.
It uses a modified version of the Blowfish stream cipher.
It does, however, truncate passwords to 72 bytes, and some other minor quirks
(see [BCrypt Password Truncation](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#bcrypt-password-truncation) for details).
This class works around that issue by first running the password through HMAC-SHA2-256.
This class can be used directly as follows:

```
>>> from passlib.hash import bcrypt_sha256

>>> # generate new salt, hash password
>>> h = bcrypt_sha256.hash("password")
>>> h
'$bcrypt-sha256$v=2,t=2b,r=12$n79VH.0Q2TMWmt3Oqt9uku$Kq4Noyk3094Y2QlB8NdRT8SvGiI4ft2'

>>> # the same, but with an explicit number of rounds
>>> bcrypt_sha256.using(rounds=13).hash("password")
'$bcrypt-sha256$v=2,t=2b,r=13$AmytCA45b12VeVg0YdDT3.$IZTbbJKgJlD5IJoCWhuDUqYjnJwNPlO'

>>> # verify password
>>> bcrypt_sha256.verify("password", h)
True
>>> bcrypt_sha256.verify("wrong", h)
False

```

Note

It is strongly recommended that you install
[bcrypt](https://pypi.python.org/pypi/bcrypt)
when using this hash. See [passlib.hash.bcrypt - BCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html) for more details.

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `bcrypt_sha256` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html#passlib.hash.bcrypt_sha256 "Permalink to this definition")

This class implements a composition of BCrypt + HMAC\_SHA256,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a fixed-length salt, and a variable number of rounds.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") methods accept
all the same optional keywords as the base [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt") hash.

New in version 1.6.2.

Changed in version 1.7: Now defaults to `"2b"` bcrypt variant; though supports older hashes
generated using the `"2a"` bcrypt variant.

Changed in version 1.7.3: For increased security, updated to use HMAC-SHA256 instead of plain SHA256.
Now only supports the `"2b"` bcrypt variant. Hash format updated to “v=2”.

## Format [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html\#format "Permalink to this headline")

Bcrypt-SHA256 is compatible with the [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format), and uses `$bcrypt-sha256$` as the identifying prefix
for all it’s strings.
An example hash (of `password`) is:

> `$bcrypt-sha256$v=2,t=2b,r=12$n79VH.0Q2TMWmt3Oqt9uku$Kq4Noyk3094Y2QlB8NdRT8SvGiI4ft2`

Version 1 of this format had the format `$bcrypt-sha256$type,rounds$salt$digest`.
Passlib 1.7.3 introduced version 2 of this format, which changed the algorithm slightly (see below),
and adjusted the format to indicate a version: `$bcrypt-sha256$v=2,t=type,r=rounds$salt$digest`, where:

- `type` is the BCrypt variant in use (always `2b` under version 2; though `2a` was allowed under version 1).
- `rounds` is a cost parameter, encoded as decimal integer,
which determines the number of iterations used via `iterations=2**rounds` (rounds is 12 in the example).
- `salt` is a 22 character salt string, using the characters in the regexp range `[./A-Za-z0-9]` ( `n79VH.0Q2TMWmt3Oqt9uku` in the example).
- `digest` is a 31 character digest, using the same characters as the salt ( `Kq4Noyk3094Y2QlB8NdRT8SvGiI4ft2` in the example).

## Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html\#algorithm "Permalink to this headline")

The algorithm this hash uses is as follows:

- first the password is encoded to `UTF-8` if not already encoded.

- the next step is to hash the password before handing it off to bcrypt:


> - Under version 2 of this algorithm (the default as of passlib 1.7.3), the password is run
> through HMAC-SHA2-256, with the HMAC key set to the bcrypt salt (encoded as a 22 character ascii salt string).
> - Under the older version 1 of this algorithm, the password was instead run through plain SHA2-256.
>
> In either case, this generates a 32 byte digest.

- this hash is then encoded using base64, resulting in a 44-byte result
(including the trailing padding `=`). For the example `"password"` and the salt `"n79VH.0Q2TMWmt3Oqt9uku"`,
the output from this stage would be `b"7CwRr5rxo2JZcVmSDAi/2JPTkvkAdNy20Cz2LwYC0fw="` (for version 2).

- this base64 string is then passed on to the underlying bcrypt algorithm
as the new password to be hashed. See [passlib.hash.bcrypt - BCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html) for details
on it’s operation. For the example in the prior line, the resulting
bcrypt digest component would be `"Kq4Noyk3094Y2QlB8NdRT8SvGiI4ft2"`.


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
        - [`passlib.hash.bcrypt_sha256` \- BCrypt+SHA256](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html#)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html#interface)
          - [Format](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html#format)
          - [Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html#algorithm)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html "passlib.hash.phpass - PHPass’ Portable Hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html "passlib.hash.argon2 - Argon2")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.bcrypt_sha256.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.bcrypt_sha256.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)