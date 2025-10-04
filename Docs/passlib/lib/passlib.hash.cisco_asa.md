<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html "passlib.hash.django_digest - Django-specific Hashes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html "passlib.hash.cisco_pix - Cisco PIX MD5 hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.cisco_asa`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#passlib.hash.cisco_asa "passlib.hash.cisco_asa") \- Cisco ASA MD5 hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html\#passlib-hash-cisco-asa-cisco-asa-md5-hash "Permalink to this headline")

Danger

**This algorithm is not considered secure by modern standards.**
It should only be used when verifying existing hashes,
or when interacting with applications that require this format.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

New in version 1.7.

Todo

**Caveat Emptor**

Passlib’s implementations of [`cisco_pix`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_pix "passlib.hash.cisco_pix") and [`cisco_asa`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_asa "passlib.hash.cisco_asa") both need verification.
For those with access to Cisco PIX and ASA systems, verifying Passlib’s reference vectors
would be a great help (see [issue 51](https://foss.heptapod.net/python-libs/passlib/issues/51)). In the mean time, there are no guarantees
that passlib correctly replicates the official implementation.

Changed in version 1.7.1: A number of [bugs](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib-asa96-bug) were fixed after expanding
the reference vectors, and testing against an ASA 9.6 system.

The `cisco_asa` class provides support for Cisco ASA “encrypted” hash format.
This is a revision of the older `cisco_pix` hash;
and the usage and format is the same.

**See the** [cisco\_pix](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html) **documentation page**
for combined details of both these classes.

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
      - [`passlib.hash.cisco_type7` \- Cisco “Type 7” hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html)
      - [`passlib.hash.cisco_pix` \- Cisco PIX MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html)
      - [`passlib.hash.cisco_asa` \- Cisco ASA MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html#)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html "passlib.hash.django_digest - Django-specific Hashes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html "passlib.hash.cisco_pix - Cisco PIX MD5 hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.cisco_asa.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.cisco_asa.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)