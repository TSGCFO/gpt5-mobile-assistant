<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html "passlib.crypto.des - DES routines")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html "passlib.crypto - Cryptographic Helper Functions")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.crypto` \- Cryptographic Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html) »

# [`passlib.crypto.digest`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html\#module-passlib.crypto.digest "passlib.crypto.digest: Internal cryptographic helpers") \- Hash & Related Helpers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html\#module-passlib.crypto.digest "Permalink to this headline")

New in version 1.7.

This module provides various cryptographic support functions used by Passlib
to implement the various password hashes it provides, as well as paper over
some VM & version incompatibilities.

## Hash Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html\#hash-functions "Permalink to this headline")

`passlib.crypto.digest.` `norm_hash_name`( _name_, _format='hashlib'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.norm_hash_name "Permalink to this definition")

Normalize hash function name (convenience wrapper for [`lookup_hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.lookup_hash "passlib.crypto.digest.lookup_hash")).

| Parameters: | - **name** – <br>  Original hash function name.<br>  <br>  This name can be a Python [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "(in Python v3.9)") digest name,<br>  a SCRAM mechanism name, IANA assigned hash name, etc.<br>  Case is ignored, and underscores are converted to hyphens.<br>  <br>- **format** – <br>  Naming convention to normalize to.<br>  Possible values are:<br>  <br>  - `"hashlib"` (the default) - normalizes name to be compatible<br>    with Python’s `hashlib`.<br>  - `"iana"` \- normalizes name to IANA-assigned hash function name.<br>    For hashes which IANA hasn’t assigned a name for, this issues a warning,<br>    and then uses a heuristic to return a “best guess” name. |
| Returns: | Hash name, returned as native `str`. |

`passlib.crypto.digest.` `lookup_hash`( _digest_, _return\_unknown=False_, _required=True_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.lookup_hash "Permalink to this definition")

Returns a [`HashInfo`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo "passlib.crypto.digest.HashInfo") record containing information about a given hash function.
Can be used to look up a hash constructor by name, normalize hash name representation, etc.

| Parameters: | - **digest** – <br>  This can be any of:<br>  <br>  <br>  - A string containing a `hashlib` digest name (e.g. `"sha256"`),<br>  - A string containing an IANA-assigned hash name,<br>  - A digest constructor function (e.g. `hashlib.sha256`).<br>Case is ignored, underscores are converted to hyphens,<br>and various other cleanups are made.<br>- **required** – <br>  By default (True), this function will throw an [`UnknownHashError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.UnknownHashError "passlib.exc.UnknownHashError") if no hash constructor<br>  can be found, or if the hash is not actually available.<br>  <br>  If this flag is False, it will instead return a dummy `HashInfo` record<br>  which will defer throwing the error until it’s constructor function is called.<br>  This is mainly used by [`norm_hash_name()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.norm_hash_name "passlib.crypto.digest.norm_hash_name").<br>  <br>- **return\_unknown** – <br>  <br>  <br>  Deprecated since version 1.7.3: deprecated, and will be removed in passlib 2.0.<br>  this acts like inverse of **required**. |
| Returns HashInfo: |
|  | [`HashInfo`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo "passlib.crypto.digest.HashInfo") instance containing information about specified digest.<br>Multiple calls resolving to the same hash should always<br>return the same `HashInfo` instance. |

Note

`lookup_hash()` supports all hashes available directly in [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "(in Python v3.9)"),
as well as offered through [`hashlib.new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "(in Python v3.9)").
It will also fallback to passlib’s builtin MD4 implementation if one is not natively available.

_class_ `passlib.crypto.digest.` `HashInfo` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo "Permalink to this definition")

Record containing information about a given hash algorithm, as returned [`lookup_hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.lookup_hash "passlib.crypto.digest.lookup_hash").

This class exposes the following attributes:

`const` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.const "Permalink to this definition")

Hash constructor function (e.g. `hashlib.sha256()`)

`digest_size` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.digest_size "Permalink to this definition")

Hash’s digest size

`block_size` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.block_size "Permalink to this definition")

Hash’s block size

`name` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.name "Permalink to this definition")

Canonical / hashlib-compatible name (e.g. `"sha256"`).

`iana_name` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.iana_name "Permalink to this definition")

IANA assigned name (e.g. `"sha-256"`), may be `None` if unknown.

`aliases` _= ()_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.aliases "Permalink to this definition")

Tuple of other known aliases (may be empty)

`supported` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.HashInfo.supported "Permalink to this definition")

whether hash is available for use
(if False, constructor will throw UnknownHashError if called)

This object can also be treated a 3-element sequence
containing `(const, digest_size, block_size)`.

## PKCS\#5 Key Derivation Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html\#pkcs-5-key-derivation-functions "Permalink to this headline")

`passlib.crypto.digest.` `pbkdf1`( _digest_, _secret_, _salt_, _rounds_, _keylen=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf1 "Permalink to this definition")

pkcs#5 password-based key derivation v1.5

| Parameters: | - **digest** – digest name or constructor.<br>- **secret** – secret to use when generating the key.<br>  may be `bytes` or `unicode` (encoded using UTF-8).<br>- **salt** – salt string to use when generating key.<br>  may be `bytes` or `unicode` (encoded using UTF-8).<br>- **rounds** – number of rounds to use to generate key.<br>- **keylen** – number of bytes to generate (if omitted / `None`, uses digest’s native size) |
| Returns: | raw [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") of generated key |

Note

This algorithm has been deprecated, new code should use PBKDF2.
Among other limitations, `keylen` cannot be larger
than the digest size of the specified hash.

`passlib.crypto.digest.` `pbkdf2_hmac`( _digest_, _secret_, _salt_, _rounds_, _keylen=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf2_hmac "Permalink to this definition")

pkcs#5 password-based key derivation v2.0 using HMAC + arbitrary digest.

| Parameters: | - **digest** – digest name or constructor.<br>- **secret** – passphrase to use to generate key.<br>  may be `bytes` or `unicode` (encoded using UTF-8).<br>- **salt** – salt string to use when generating key.<br>  may be `bytes` or `unicode` (encoded using UTF-8).<br>- **rounds** – number of rounds to use to generate key.<br>- **keylen** – number of bytes to generate.<br>  if omitted / `None`, will use digest’s native output size. |
| Returns: | raw bytes of generated key |

Changed in version 1.7: This function will use the first available of the following backends:

- [fastpbk2](https://pypi.python.org/pypi/fastpbkdf2)
- [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac "(in Python v3.9)") (only available in py2 >= 2.7.8, and py3 >= 3.4)
- builtin pure-python backend

See [`passlib.crypto.digest.PBKDF2_BACKENDS`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.PBKDF2_BACKENDS "passlib.crypto.digest.PBKDF2_BACKENDS") to determine
which backend(s) are in use.

`passlib.crypto.digest.` `PBKDF2_BACKENDS` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.PBKDF2_BACKENDS "Permalink to this definition")

List of the pbkdf2 backends in use (listed in order of priority).

New in version 1.7.

Note

The details of PBKDF1 and PBKDF2 are specified in [**RFC 2898**](https://tools.ietf.org/html/rfc2898.html).

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
    - [`passlib.crypto.digest` \- Hash & Related Helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#)
      - [Hash Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#hash-functions)
      - [PKCS#5 Key Derivation Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#pkcs-5-key-derivation-functions)
    - [`passlib.crypto.des` \- DES routines](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html)
  - [`passlib.exc` \- Exceptions and warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html)
  - [`passlib.ext.django` \- Django Password Hashing Plugin](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html)
  - [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html "passlib.crypto.des - DES routines")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html "passlib.crypto - Cryptographic Helper Functions")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.crypto` \- Cryptographic Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.crypto.digest.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.crypto.digest.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)