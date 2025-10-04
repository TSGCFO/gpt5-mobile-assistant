<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html "passlib.hash.ldap_pbkdf2_digest - Generic PBKDF2 Hashes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html "passlib.hash.ldap_crypt - LDAP crypt() Wrappers")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# `passlib.hash.ldap_other` \- Non-Standard RFC2307 Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html\#passlib-hash-ldap-other-non-standard-rfc2307-hashes "Permalink to this headline")

This section as a catch-all for a number of password hash
formats supported by Passlib which use [**RFC 2307**](https://tools.ietf.org/html/rfc2307.html) style encoding,
but are not part of any standard.

See also

- [password hash usage](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples) –
for examples of how to use these classes via the common hash interface.
- [LDAP / RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-hashes) for a full list of RFC 2307 style hashes.

## Hexadecimal Digests [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html\#hexadecimal-digests "Permalink to this headline")

All of the digests specified in RFC 2307 use base64 encoding.
The following are non-standard versions which use hexadecimal
encoding, as is found in some applications.

_class_ `passlib.hash.` `ldap_hex_md5` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.ldap_hex_md5 "Permalink to this definition")

hexadecimal version of [`ldap_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_md5 "passlib.hash.ldap_md5"),
this is just the md5 digest of the password.

an example hash (of `password`) is `{MD5}5f4dcc3b5aa765d61d8327deb882cf99`.

_class_ `passlib.hash.` `ldap_hex_sha1` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.ldap_hex_sha1 "Permalink to this definition")

hexadecimal version of [`ldap_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_std.html#passlib.hash.ldap_sha1 "passlib.hash.ldap_sha1"),
this is just the sha1 digest of the password.

an example hash (of `password`) is `{SHA}5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8`.

## Other Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html\#other-hashes "Permalink to this headline")

_class_ `passlib.hash.` `roundup_plaintext` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.roundup_plaintext "Permalink to this definition")

RFC 2307 specifies plaintext passwords should be stored
without any identifying prefix.
This class implements an alternate method used by the Roundup Issue Tracker [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#roundup),
which (when storing plaintext passwords) uses the identifying prefix `{plaintext}`.

an example hash (of `password`) is `{plaintext}password`.

Footnotes

|     |     |
| --- | --- |
| [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#id1) | Roundup Issue Tracker homepage - [http://www.roundup-tracker.org](http://www.roundup-tracker.org/). |

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
      - [Standard LDAP Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#standard-ldap-schemes)
      - [Non-Standard LDAP Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#non-standard-ldap-schemes)
        - [`passlib.hash.ldap_other` \- Non-Standard RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#)
          - [Hexadecimal Digests](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#hexadecimal-digests)
          - [Other Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#other-hashes)
        - [`passlib.hash.ldap_pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html)
        - [`passlib.hash.atlassian_pbkdf2_sha1` \- Atlassian’s PBKDF2-based Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.atlassian_pbkdf2_sha1.html)
        - [`passlib.hash.fshp` \- Fairly Secure Hashed Password](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.fshp.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html "passlib.hash.ldap_pbkdf2_digest - Generic PBKDF2 Hashes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html "passlib.hash.ldap_crypt - LDAP crypt() Wrappers")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.ldap_other.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.ldap_other.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)