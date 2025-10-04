<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.atlassian_pbkdf2_sha1.html "passlib.hash.atlassian_pbkdf2_sha1 - Atlassian’s PBKDF2-based Hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html "passlib.hash.ldap_other - Non-Standard RFC2307 Hashes")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# `passlib.hash.ldap_pbkdf2_digest` \- Generic PBKDF2 Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html\#passlib-hash-ldap-pbkdf2-digest-generic-pbkdf2-hashes "Permalink to this headline")

Passlib provides three custom hash schemes based on the PBKDF2 [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#pbkdf2) algorithm
which are compatible with the [ldap hash format](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-hashes):
`ldap_pbkdf2_sha1`, `ldap_pbkdf2_sha256`, `ldap_pbkdf2_sha512`.
They feature variable length salts, variable rounds.

See also

These classes are simply wrappers around the [MCF-Compatible Simple PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html).

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `ldap_pbkdf2_sha1` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#passlib.hash.ldap_pbkdf2_sha1 "Permalink to this definition")

this is the same as [`pbkdf2_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha1 "passlib.hash.pbkdf2_sha1"), except that it
uses `{PBKDF2}` as its identifying prefix instead of `$pdkdf2$`.

_class_ `passlib.hash.` `ldap_pbkdf2_sha256` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#passlib.hash.ldap_pbkdf2_sha256 "Permalink to this definition")

this is the same as [`pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha256 "passlib.hash.pbkdf2_sha256"), except that it
uses `{PBKDF2-SHA256}` as its identifying prefix instead of `$pdkdf2-sha256$`.

_class_ `passlib.hash.` `ldap_pbkdf2_sha512` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#passlib.hash.ldap_pbkdf2_sha512 "Permalink to this definition")

this is the same as [`pbkdf2_sha512`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha512 "passlib.hash.pbkdf2_sha512"), except that it
uses `{PBKDF2-SHA512}` as its identifying prefix instead of `$pdkdf2-sha512$`.

Footnotes

|     |     |
| --- | --- |
| [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#id1) | The specification for the PBKDF2 algorithm - [http://tools.ietf.org/html/rfc2898#section-5.2](http://tools.ietf.org/html/rfc2898#section-5.2),<br>part of [**RFC 2898**](https://tools.ietf.org/html/rfc2898.html). |

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
        - [`passlib.hash.ldap_other` \- Non-Standard RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html)
        - [`passlib.hash.ldap_pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#interface)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.atlassian_pbkdf2_sha1.html "passlib.hash.atlassian_pbkdf2_sha1 - Atlassian’s PBKDF2-based Hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html "passlib.hash.ldap_other - Non-Standard RFC2307 Hashes")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.ldap_pbkdf2_digest.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.ldap_pbkdf2_digest.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)