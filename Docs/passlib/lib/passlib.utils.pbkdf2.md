<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/other.html "Other Documentation")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html "passlib.utils.des - DES routines [deprecated]")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

# [`passlib.utils.pbkdf2`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html\#module-passlib.utils.pbkdf2 "passlib.utils.pbkdf2: PBKDF2 and related key derivation algorithms") \- PBKDF2 key derivation algorithm \[deprecated\] [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html\#module-passlib.utils.pbkdf2 "Permalink to this headline")

Warning

This module has been deprecated as of Passlib 1.7,
and will be removed in Passlib 2.0.
The functions in this module have been replaced by equivalent
(but not identical) functions in the [`passlib.crypto`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html#module-passlib.crypto "passlib.crypto: internal cryptographic helpers for implementing password hashes") module.

This module provides a couple of key derivation functions,
as well as supporting utilities.
Primarily, it offers [`pbkdf2()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#passlib.utils.pbkdf2.pbkdf2 "passlib.utils.pbkdf2.pbkdf2"),
which provides the ability to generate an arbitrary
length key using the PBKDF2 key derivation algorithm,
as specified in [rfc 2898](http://tools.ietf.org/html/rfc2898).
This function can be helpful in creating password hashes
using schemes which have been based around the pbkdf2 algorithm.

## PKCS\#5 Key Derivation Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html\#pkcs-5-key-derivation-functions "Permalink to this headline")

`passlib.utils.pbkdf2.` `pbkdf1`( _secret_, _salt_, _rounds_, _keylen=None_, _hash='sha1'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#passlib.utils.pbkdf2.pbkdf1 "Permalink to this definition")

pkcs#5 password-based key derivation v1.5

| Parameters: | - **secret** – passphrase to use to generate key<br>- **salt** – salt string to use when generating key<br>- **rounds** – number of rounds to use to generate key<br>- **keylen** – number of bytes to generate (if `None`, uses digest’s native size)<br>- **hash** – hash function to use. must be name of a hash recognized by hashlib. |
| Returns: | raw bytes of generated key |

Note

This algorithm has been deprecated, new code should use PBKDF2.
Among other limitations, `keylen` cannot be larger
than the digest size of the specified hash.

Deprecated since version 1.7: This has been relocated to [`passlib.crypto.digest.pbkdf1()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf1 "passlib.crypto.digest.pbkdf1"),
and this version will be removed in Passlib 2.0.
_Note the call signature has changed._

`passlib.utils.pbkdf2.` `pbkdf2`( _secret_, _salt_, _rounds_, _keylen=None_, _prf='hmac-sha1'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#passlib.utils.pbkdf2.pbkdf2 "Permalink to this definition")

pkcs#5 password-based key derivation v2.0

| Parameters: | - **secret** – passphrase to use to generate key<br>- **salt** – salt string to use when generating key<br>- **rounds** – number of rounds to use to generate key<br>- **keylen** – number of bytes to generate.<br>  if set to `None`, will use digest size of selected prf.<br>- **prf** – <br>  psuedo-random family to use for key strengthening.<br>  this must be a string starting with `"hmac-"`, followed by the name of a known digest.<br>  this defaults to `"hmac-sha1"` (the only prf explicitly listed in<br>  the PBKDF2 specification) |
| Returns: | raw bytes of generated key |

Deprecated since version 1.7: This has been deprecated in favor of [`passlib.crypto.digest.pbkdf2_hmac()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf2_hmac "passlib.crypto.digest.pbkdf2_hmac"),
and will be removed in Passlib 2.0. _Note the call signature has changed._

Note

The details of PBKDF1 and PBKDF2 are specified in [**RFC 2898**](https://tools.ietf.org/html/rfc2898.html).

## Helper Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html\#helper-functions "Permalink to this headline")

`passlib.utils.pbkdf2.` `norm_hash_name`( _name_, _format='hashlib'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#passlib.utils.pbkdf2.norm_hash_name "Permalink to this definition")

Normalize hash function name (convenience wrapper for `lookup_hash()`).

> | arg name: | Original hash function name.<br>This name can be a Python [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "(in Python v3.9)") digest name,<br>a SCRAM mechanism name, IANA assigned hash name, etc.<br>Case is ignored, and underscores are converted to hyphens. |
> | param format: | Naming convention to normalize to.<br>Possible values are:<br>- `"hashlib"` (the default) - normalizes name to be compatible<br>  with Python’s `hashlib`.<br>- `"iana"` \- normalizes name to IANA-assigned hash function name.<br>  For hashes which IANA hasn’t assigned a name for, this issues a warning,<br>  and then uses a heuristic to return a “best guess” name. |
> | returns: | Hash name, returned as native `str`. |

Deprecated since version 1.7: and will be removed in version 1.8, use passlib.crypto.digest.norm\_hash\_name instead.

`passlib.utils.pbkdf2.` `get_prf`( _name_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#passlib.utils.pbkdf2.get_prf "Permalink to this definition")

Lookup pseudo-random family (PRF) by name.

| Parameters: | **name** – <br>This must be the name of a recognized prf.<br>Currently this only recognizes names with the format<br>`hmac-digest`, where `digest`<br>is the name of a hash function such as<br>`md5`, `sha256`, etc.<br>todo: restore text about callables. |
| Raises: | - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if the name is not known<br>- [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if the name is not a callable or string |
| Returns: | a tuple of `(prf_func, digest_size)`, where:<br>- `prf_func` is a function implementing<br>  the specified PRF, and has the signature<br>  `prf_func(secret, message) -> digest`.<br>- `digest_size` is an integer indicating<br>  the number of bytes the function returns. |

Usage example:

```
>>> from passlib.utils.pbkdf2 import get_prf
>>> hmac_sha256, dsize = get_prf("hmac-sha256")
>>> hmac_sha256
<function hmac_sha256 at 0x1e37c80>
>>> dsize
32
>>> digest = hmac_sha256('password', 'message')

```

Deprecated since version 1.7: This function is deprecated, and will be removed in Passlib 2.0.
This only related replacement is `passlib.crypto.digest.compile_hmac()`.

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
  - [`passlib.hosts` \- OS Password Handling](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html)
  - [`passlib.ifc` – Password Hash Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html)
  - [`passlib.pwd` – Password generation helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html)
  - [`passlib.registry` \- Password Handler Registry](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html)
  - [`passlib.totp` – TOTP / Two Factor Authentication](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html)
  - [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html)
    - [Constants](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#constants)
    - [Unicode Helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#unicode-helpers)
    - [Bytes Helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#bytes-helpers)
    - [Encoding Helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#encoding-helpers)
    - [Randomness](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#randomness)
    - [Interface Tests](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#interface-tests)
    - [Submodules](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#submodules)
      - [`passlib.utils.handlers` \- Framework for writing password hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html)
      - [`passlib.utils.binary` \- Binary Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html)
      - [`passlib.utils.des` \- DES routines \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html)
      - [`passlib.utils.pbkdf2` \- PBKDF2 key derivation algorithm \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#)
        - [PKCS#5 Key Derivation Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#pkcs-5-key-derivation-functions)
        - [Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html#helper-functions)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/other.html "Other Documentation")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html "passlib.utils.des - DES routines [deprecated]")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.utils.pbkdf2.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.utils.pbkdf2.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)