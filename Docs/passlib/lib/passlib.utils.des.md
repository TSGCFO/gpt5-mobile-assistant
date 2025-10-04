<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html "passlib.utils.pbkdf2 - PBKDF2 key derivation algorithm [deprecated]")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html "passlib.utils.binary - Binary Helper Functions")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

# [`passlib.utils.des`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html\#module-passlib.utils.des "passlib.utils.des: routines for performing DES encryption") \- DES routines \[deprecated\] [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html\#module-passlib.utils.des "Permalink to this headline")

Warning

This module is deprecated as of Passlib 1.7:
It has been relocated to [`passlib.crypto.des`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html#module-passlib.crypto.des "passlib.crypto.des: routines for performing DES encryption");
and the aliases here will be removed in Passlib 2.0.

This module contains routines for encrypting blocks of data using the DES algorithm.
Note that these functions do not support multi-block operation or decryption,
since they are designed primarily for use in password hash algorithms
(such as [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") and [`bsdi_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bsdi_crypt.html#passlib.hash.bsdi_crypt "passlib.hash.bsdi_crypt")).

`passlib.utils.des.` `expand_des_key`( _key_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html#passlib.utils.des.expand_des_key "Permalink to this definition")

convert DES from 7 bytes to 8 bytes (by inserting empty parity bits)

Deprecated since version 1.7: and will be removed in version 1.8, use passlib.crypto.des.expand\_des\_key instead.

`passlib.utils.des.` `des_encrypt_block`( _key_, _input_, _salt=0_, _rounds=1_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html#passlib.utils.des.des_encrypt_block "Permalink to this definition")

encrypt single block of data using DES, operates on 8-byte strings.

> | arg key: | DES key as 7 byte string, or 8 byte string with parity bits<br>(parity bit values are ignored). |
> | arg input: | plaintext block to encrypt, as 8 byte string. |
> | arg salt: | Optional 24-bit integer used to mutate the base DES algorithm in a<br>manner specific to [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") and its variants.<br>The default value `0` provides the normal (unsalted) DES behavior.<br>The salt functions as follows:<br>if the `i`’th bit of `salt` is set,<br>bits `i` and `i+24` are swapped in the DES E-box output. |
> | arg rounds: | Optional number of rounds of to apply the DES key schedule.<br>the default ( `rounds=1`) provides the normal DES behavior,<br>but [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") and its variants use<br>alternate rounds values. |
> | raises TypeError: |
> |  | if any of the provided args are of the wrong type. |
> | raises ValueError: |
> |  | if any of the input blocks are the wrong size,<br>or the salt/rounds values are out of range. |
> | returns: | resulting 8-byte ciphertext block. |

Deprecated since version 1.7: and will be removed in version 1.8, use passlib.crypto.des.des\_encrypt\_block instead.

`passlib.utils.des.` `des_encrypt_int_block`( _key_, _input_, _salt=0_, _rounds=1_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html#passlib.utils.des.des_encrypt_int_block "Permalink to this definition")

encrypt single block of data using DES, operates on 64-bit integers.

> this function is essentially the same as [`des_encrypt_block()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html#passlib.utils.des.des_encrypt_block "passlib.utils.des.des_encrypt_block"),
> except that it operates on integers, and will NOT automatically
> expand 56-bit keys if provided (since there’s no way to detect them).
>
> | arg key: | DES key as 64-bit integer (the parity bits are ignored). |
> | arg input: | input block as 64-bit integer |
> | arg salt: | optional 24-bit integer used to mutate the base DES algorithm.<br>defaults to `0` (no mutation applied). |
> | arg rounds: | optional number of rounds of to apply the DES key schedule.<br>defaults to `1`. |
> | raises TypeError: |
> |  | if any of the provided args are of the wrong type. |
> | raises ValueError: |
> |  | if any of the input blocks are the wrong size,<br>or the salt/rounds values are out of range. |
> | returns: | resulting ciphertext as 64-bit integer. |

Deprecated since version 1.7: and will be removed in version 1.8, use passlib.crypto.des.des\_encrypt\_int\_block instead.

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
      - [`passlib.utils.des` \- DES routines \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html#)
      - [`passlib.utils.pbkdf2` \- PBKDF2 key derivation algorithm \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html "passlib.utils.pbkdf2 - PBKDF2 key derivation algorithm [deprecated]")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html "passlib.utils.binary - Binary Helper Functions")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.utils.des.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.utils.des.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)