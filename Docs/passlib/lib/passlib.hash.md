<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html "passlib.hash.bcrypt - BCrypt")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html "passlib.ext.django - Django Password Hashing Plugin")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") \- Password Hashing Schemes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#module-passlib.hash "Permalink to this headline")

## Overview [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#overview "Permalink to this headline")

The `passlib.hash` module contains all the password hash algorithms built into Passlib.
While each hash has its own options and output format,
they all inherit from the [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") base interface.
The following pages describe each hash in detail,
including its format, underlying algorithm, and known security issues.

Danger

**Many of the hash algorithms listed below are \*NOT\* secure.**

Passlib supports a wide array of hash algorithms, primarily to
support legacy data and systems.
If you want to choose a secure algorithm for a new application,
see the [Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html).

See also

[PasswordHash Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-tutorial) – for general usage examples

## Unix Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#unix-hashes "Permalink to this headline")

Aside from “archaic” schemes such as `des_crypt`,
most of the password hashes supported by modern Unix flavors
adhere to the [modular crypt format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format),
allowing them to be easily distinguished when used within the same file.
Variants of this format’s basic `$scheme$salt$digest` structure have also been adopted for use
by other applications and password hash schemes.

### Active Unix Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#active-unix-hashes "Permalink to this headline")

All the following schemes are actively in use by various Unix flavors to store user passwords
They all follow the modular crypt format.

- [`passlib.hash.bcrypt` \- BCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html)
- [`passlib.hash.sha256_crypt` \- SHA-256 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html)
- [`passlib.hash.sha512_crypt` \- SHA-512 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html)

Special note should be made of the following fallback helper,
which is not an actual hash scheme, but implements the “disabled account marker”
found in many Linux & BSD password files:

- [`passlib.hash.unix_disabled` \- Unix Disabled Account Helper](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html)

### Deprecated Unix Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#deprecated-unix-hashes "Permalink to this headline")

The following schemes are supported by various Unix systems
using the modular crypt format, but are no longer considered secure,
and have been deprecated in favor of the [Active Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#active-unix-hashes) (above).

- [`passlib.hash.bsd_nthash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.bsd_nthash "passlib.hash.bsd_nthash") \- FreeBSD’s MCF-compatible encoding of [nthash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html) digests

- [`passlib.hash.md5_crypt` \- MD5 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html)
- [`passlib.hash.sha1_crypt` \- SHA-1 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha1_crypt.html)
- [`passlib.hash.sun_md5_crypt` \- Sun MD5 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sun_md5_crypt.html)

### Archaic Unix Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#archaic-unix-hashes "Permalink to this headline")

The following schemes are supported by certain Unix systems,
but are considered particularly archaic: Not only do they predate
the modular crypt format, but they’re based on the outmoded DES block cipher,
and are woefully insecure:

- [`passlib.hash.des_crypt` \- DES Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html)
- [`passlib.hash.bsdi_crypt` \- BSDi Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bsdi_crypt.html)
- [`passlib.hash.bigcrypt` \- BigCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bigcrypt.html)
- [`passlib.hash.crypt16` \- Crypt16](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.crypt16.html)

## Other “Modular Crypt” Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#other-modular-crypt-hashes "Permalink to this headline")

The [modular crypt format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format) is a loose standard
for password hash strings which started life under the Unix operating system,
and is used by many of the Unix hashes (above). However, it’s
it’s basic `$scheme$hash` format has also been adopted by a number
of application-specific hash algorithms:

### Active Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#active-hashes "Permalink to this headline")

While most of these schemes are generally application-specific,
and are not natively supported by any Unix OS,
they can be used compatibly along side other modular crypt format hashes:

- [`passlib.hash.argon2` \- Argon2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html)
- [`passlib.hash.bcrypt_sha256` \- BCrypt+SHA256](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html)
- [`passlib.hash.phpass` \- PHPass’ Portable Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html)
- [`passlib.hash.pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html)
- [`passlib.hash.scram` \- SCRAM Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html)
- [`passlib.hash.scrypt` \- SCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html)

### Deprecated Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#deprecated-hashes "Permalink to this headline")

The following are some additional application-specific hashes which are still
occasionally seen, use the modular crypt format, but are rarely used or weak
enough that they have been deprecated:

- [`passlib.hash.apr_md5_crypt` \- Apache’s MD5-Crypt variant](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.apr_md5_crypt.html)
- [`passlib.hash.cta_pbkdf2_sha1` \- Cryptacular’s PBKDF2 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cta_pbkdf2_sha1.html)
- [`passlib.hash.dlitz_pbkdf2_sha1` \- Dwayne Litzenberger’s PBKDF2 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.dlitz_pbkdf2_sha1.html)

## LDAP / RFC2307 Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#ldap-rfc2307-hashes "Permalink to this headline")

All of the following hashes use a variant of the password hash format
used by LDAPv2. Originally specified in [**RFC 2307**](https://tools.ietf.org/html/rfc2307.html) and used by OpenLDAP [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#openldap),
the basic format `{SCHEME}HASH` has seen widespread adoption in a number of programs.

### Standard LDAP Schemes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#standard-ldap-schemes "Permalink to this headline")

The following schemes are explicitly defined by RFC 2307,
and are supported by OpenLDAP.

- [`passlib.hash.ldap_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_md5 "passlib.hash.ldap_md5") \- MD5 digest
- [`passlib.hash.ldap_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_sha1 "passlib.hash.ldap_sha1") \- SHA1 digest
- [`passlib.hash.ldap_salted_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_md5 "passlib.hash.ldap_salted_md5") \- salted MD5 digest
- [`passlib.hash.ldap_salted_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_sha1 "passlib.hash.ldap_salted_sha1") \- salted SHA1 digest
- [`passlib.hash.ldap_salted_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_sha256 "passlib.hash.ldap_salted_sha256") \- salted SHA256 digest
- [`passlib.hash.ldap_salted_sha512`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_salted_sha512 "passlib.hash.ldap_salted_sha512") \- salted SHA512 digest

- [`passlib.hash.ldap_crypt` \- LDAP crypt() Wrappers](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html)

- [`passlib.hash.ldap_plaintext`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_plaintext "passlib.hash.ldap_plaintext") \- LDAP-Aware Plaintext Handler

### Non-Standard LDAP Schemes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#non-standard-ldap-schemes "Permalink to this headline")

None of the following schemes are actually used by LDAP,
but follow the LDAP format:

- [`passlib.hash.ldap_hex_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.ldap_hex_md5 "passlib.hash.ldap_hex_md5") \- Hex-encoded MD5 Digest
- [`passlib.hash.ldap_hex_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.ldap_hex_sha1 "passlib.hash.ldap_hex_sha1") \- Hex-encoded SHA1 Digest

- [`passlib.hash.ldap_pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html)
- [`passlib.hash.atlassian_pbkdf2_sha1` \- Atlassian’s PBKDF2-based Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.atlassian_pbkdf2_sha1.html)
- [`passlib.hash.fshp` \- Fairly Secure Hashed Password](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.fshp.html)

- [`passlib.hash.roundup_plaintext`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.roundup_plaintext "passlib.hash.roundup_plaintext") \- Roundup-specific LDAP Plaintext Handler

## SQL Database Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#sql-database-hashes "Permalink to this headline")

The following schemes are used by various SQL databases
to encode their own user accounts.
These schemes have encoding and contextual requirements
not seen outside those specific contexts:

- [`passlib.hash.mssql2000` \- MS SQL 2000 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2000.html)
- [`passlib.hash.mssql2005` \- MS SQL 2005 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2005.html)
- [`passlib.hash.mysql323` \- MySQL 3.2.3 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html)
- [`passlib.hash.mysql41` \- MySQL 4.1 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html)
- [`passlib.hash.postgres_md5` \- PostgreSQL MD5 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html)
- [`passlib.hash.oracle10` \- Oracle 10g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html)
- [`passlib.hash.oracle11` \- Oracle 11g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html)

## MS Windows Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#ms-windows-hashes "Permalink to this headline")

The following hashes are used in various places by Microsoft Windows.
As they were designed for “internal” use, they generally contain
no identifying markers, identifying them is pretty much context-dependant.

- [`passlib.hash.lmhash` \- LanManager Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html)
- [`passlib.hash.nthash` \- Windows’ NT-HASH](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html)
- [`passlib.hash.msdcc` \- Windows’ Domain Cached Credentials](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html)
- [`passlib.hash.msdcc2` \- Windows’ Domain Cached Credentials v2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html)

## Cisco Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#cisco-hashes "Permalink to this headline")

**Cisco IOS**

The following hashes are used in various places on Cisco IOS, and
are usually referred to by a Cisco-assigned “type” code:

- [`passlib.hash.cisco_type7` \- Cisco “Type 7” hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html)

- [passlib.hash.md5\_crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html) – “Type 5” hashes are actually just the standard
Unix MD5-Crypt hash, the format is identical.
- [passlib.hash.cisco\_type7](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html) – “Type 7” isn’t actually a hash,
but a reversible encoding designed to obscure passwords from idle view.
- “Type 8” hashes are based on PBKDF2-HMAC-SHA256;
but not currently supported by passlib ( [issue 87](https://foss.heptapod.net/python-libs/passlib/issues/87)).
- “Type 9” hashes are based on scrypt;
but not currently supported by passlib ( [issue 87](https://foss.heptapod.net/python-libs/passlib/issues/87)).

**Cisco PIX & ASA**

Separately from this, Cisco PIX & ASA firewalls have their own hash formats,
generally identified by the “format” parameter in the `username user password hash format` config line
they occur in. The following are known & handled by passlib:

- [`passlib.hash.cisco_pix` \- Cisco PIX MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html)
- [`passlib.hash.cisco_asa` \- Cisco ASA MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html)

- [passlib.hash.cisco\_pix](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html) – PIX “encrypted” hashes
use a simple unsalted MD5-based algorithm.
- [passlib.hash.cisco\_asa](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html) – ASA “encrypted” hashes
use a similar algorithm to PIX, with some minor improvements.
- ASA “nt-encrypted” hashes
are the same as [`passlib.hash.nthash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.nthash "passlib.hash.nthash"),
except that they use base64 encoding rather than hexadecimal.
- ASA 9.5 added support for “pbkdf2” hashes
(based on PBKDF2-HMAC-SHA512); which aren’t currently supported
by passlib ( [issue 87](https://foss.heptapod.net/python-libs/passlib/issues/87)).

## Other Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html\#other-hashes "Permalink to this headline")

The following schemes are used in various contexts,
but have formats or uses which cannot be easily placed
in one of the above categories:

- [`passlib.hash.django_digest` \- Django-specific Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html)
- [`passlib.hash.grub_pbkdf2_sha512` \- Grub’s PBKDF2 Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.grub_pbkdf2_sha512.html)
- [`passlib.hash.hex_digest` \- Generic Hexadecimal Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html)
- [`passlib.hash.plaintext` \- Plaintext](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html)

Footnotes

|     |     |
| --- | --- |
| [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#id1) | OpenLDAP homepage - [http://www.openldap.org/](http://www.openldap.org/). |

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
  - [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#)
    - [Overview](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#overview)
    - [Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#unix-hashes)
      - [Active Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#active-unix-hashes)
        - [`passlib.hash.bcrypt` \- BCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html)
        - [`passlib.hash.sha256_crypt` \- SHA-256 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html)
        - [`passlib.hash.sha512_crypt` \- SHA-512 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html)
        - [`passlib.hash.unix_disabled` \- Unix Disabled Account Helper](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html)
      - [Deprecated Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#deprecated-unix-hashes)
        - [`passlib.hash.md5_crypt` \- MD5 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html)
        - [`passlib.hash.sha1_crypt` \- SHA-1 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha1_crypt.html)
        - [`passlib.hash.sun_md5_crypt` \- Sun MD5 Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sun_md5_crypt.html)
      - [Archaic Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#archaic-unix-hashes)
        - [`passlib.hash.des_crypt` \- DES Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html)
        - [`passlib.hash.bsdi_crypt` \- BSDi Crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bsdi_crypt.html)
        - [`passlib.hash.bigcrypt` \- BigCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bigcrypt.html)
        - [`passlib.hash.crypt16` \- Crypt16](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.crypt16.html)
    - [Other “Modular Crypt” Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-modular-crypt-hashes)
      - [Active Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#active-hashes)
        - [`passlib.hash.argon2` \- Argon2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html)
        - [`passlib.hash.bcrypt_sha256` \- BCrypt+SHA256](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html)
        - [`passlib.hash.phpass` \- PHPass’ Portable Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html)
        - [`passlib.hash.pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html)
        - [`passlib.hash.scram` \- SCRAM Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html)
        - [`passlib.hash.scrypt` \- SCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html)
      - [Deprecated Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#deprecated-hashes)
        - [`passlib.hash.apr_md5_crypt` \- Apache’s MD5-Crypt variant](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.apr_md5_crypt.html)
        - [`passlib.hash.cta_pbkdf2_sha1` \- Cryptacular’s PBKDF2 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cta_pbkdf2_sha1.html)
        - [`passlib.hash.dlitz_pbkdf2_sha1` \- Dwayne Litzenberger’s PBKDF2 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.dlitz_pbkdf2_sha1.html)
    - [LDAP / RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-rfc2307-hashes)
      - [Standard LDAP Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#standard-ldap-schemes)
        - [`passlib.hash.ldap_digest` \- RFC2307 Standard Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html)
        - [`passlib.hash.ldap_crypt` \- LDAP crypt() Wrappers](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html)
      - [Non-Standard LDAP Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#non-standard-ldap-schemes)
        - [`passlib.hash.ldap_other` \- Non-Standard RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html)
        - [`passlib.hash.ldap_pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html)
        - [`passlib.hash.atlassian_pbkdf2_sha1` \- Atlassian’s PBKDF2-based Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.atlassian_pbkdf2_sha1.html)
        - [`passlib.hash.fshp` \- Fairly Secure Hashed Password](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.fshp.html)
    - [SQL Database Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#sql-database-hashes)
      - [`passlib.hash.mssql2000` \- MS SQL 2000 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2000.html)
      - [`passlib.hash.mssql2005` \- MS SQL 2005 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mssql2005.html)
      - [`passlib.hash.mysql323` \- MySQL 3.2.3 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html)
      - [`passlib.hash.mysql41` \- MySQL 4.1 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html)
      - [`passlib.hash.postgres_md5` \- PostgreSQL MD5 password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html)
      - [`passlib.hash.oracle10` \- Oracle 10g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html)
      - [`passlib.hash.oracle11` \- Oracle 11g password hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle11.html)
    - [MS Windows Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ms-windows-hashes)
      - [`passlib.hash.lmhash` \- LanManager Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html)
      - [`passlib.hash.nthash` \- Windows’ NT-HASH](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html)
      - [`passlib.hash.msdcc` \- Windows’ Domain Cached Credentials](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc.html)
      - [`passlib.hash.msdcc2` \- Windows’ Domain Cached Credentials v2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.msdcc2.html)
    - [Cisco Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#cisco-hashes)
      - [`passlib.hash.cisco_type7` \- Cisco “Type 7” hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html)
      - [`passlib.hash.cisco_pix` \- Cisco PIX MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html)
      - [`passlib.hash.cisco_asa` \- Cisco ASA MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html)
    - [Other Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-hashes)
      - [`passlib.hash.django_digest` \- Django-specific Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html)
      - [`passlib.hash.grub_pbkdf2_sha512` \- Grub’s PBKDF2 Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.grub_pbkdf2_sha512.html)
      - [`passlib.hash.hex_digest` \- Generic Hexadecimal Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.hex_digests.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html "passlib.hash.bcrypt - BCrypt")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html "passlib.ext.django - Django Password Hashing Plugin")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)