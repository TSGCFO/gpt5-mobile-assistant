<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html "passlib.exc - Exceptions and warnings")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html "passlib.crypto.digest - Hash & Related Helpers")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.crypto` \- Cryptographic Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html) »

# [`passlib.crypto.des`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html\#module-passlib.crypto.des "passlib.crypto.des: routines for performing DES encryption") \- DES routines [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html\#module-passlib.crypto.des "Permalink to this headline")

Changed in version 1.7: This module was relocated from `passlib.utils.des`;
the old location will be removed in Passlib 2.0.

Warning

NIST has declared DES to be “inadequate” for cryptographic purposes.
These routines, and the password hashes based on them,
should not be used in new applications.

This module contains routines for encrypting blocks of data using the DES algorithm.
Note that these functions do not support multi-block operation or decryption,
since they are designed primarily for use in password hash algorithms
(such as [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") and [`bsdi_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bsdi_crypt.html#passlib.hash.bsdi_crypt "passlib.hash.bsdi_crypt")).

`passlib.crypto.des.` `expand_des_key`( _key_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html#passlib.crypto.des.expand_des_key "Permalink to this definition")

convert DES from 7 bytes to 8 bytes (by inserting empty parity bits)

`passlib.crypto.des.` `des_encrypt_block`( _key_, _input_, _salt=0_, _rounds=1_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html#passlib.crypto.des.des_encrypt_block "Permalink to this definition")

encrypt single block of data using DES, operates on 8-byte strings.

| Parameters: | - **key** – DES key as 7 byte string, or 8 byte string with parity bits<br>  (parity bit values are ignored).<br>- **input** – plaintext block to encrypt, as 8 byte string.<br>- **salt** – Optional 24-bit integer used to mutate the base DES algorithm in a<br>  manner specific to [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") and its variants.<br>  The default value `0` provides the normal (unsalted) DES behavior.<br>  The salt functions as follows:<br>  if the `i`’th bit of `salt` is set,<br>  bits `i` and `i+24` are swapped in the DES E-box output.<br>- **rounds** – Optional number of rounds of to apply the DES key schedule.<br>  the default ( `rounds=1`) provides the normal DES behavior,<br>  but [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") and its variants use<br>  alternate rounds values. |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if any of the provided args are of the wrong type.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if any of the input blocks are the wrong size,<br>  or the salt/rounds values are out of range. |
| Returns: | resulting 8-byte ciphertext block. |

`passlib.crypto.des.` `des_encrypt_int_block`( _key_, _input_, _salt=0_, _rounds=1_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html#passlib.crypto.des.des_encrypt_int_block "Permalink to this definition")

encrypt single block of data using DES, operates on 64-bit integers.

this function is essentially the same as [`des_encrypt_block()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html#passlib.crypto.des.des_encrypt_block "passlib.crypto.des.des_encrypt_block"),
except that it operates on integers, and will NOT automatically
expand 56-bit keys if provided (since there’s no way to detect them).

| Parameters: | - **key** – DES key as 64-bit integer (the parity bits are ignored).<br>- **input** – input block as 64-bit integer<br>- **salt** – optional 24-bit integer used to mutate the base DES algorithm.<br>  defaults to `0` (no mutation applied).<br>- **rounds** – optional number of rounds of to apply the DES key schedule.<br>  defaults to `1`. |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if any of the provided args are of the wrong type.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if any of the input blocks are the wrong size,<br>  or the salt/rounds values are out of range. |
| Returns: | resulting ciphertext as 64-bit integer. |

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
    - [`passlib.crypto.digest` \- Hash & Related Helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html)
    - [`passlib.crypto.des` \- DES routines](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html#)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html "passlib.exc - Exceptions and warnings")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html "passlib.crypto.digest - Hash & Related Helpers")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.crypto` \- Cryptographic Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.crypto.des.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.crypto.des.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)