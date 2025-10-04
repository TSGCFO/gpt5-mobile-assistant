<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html "passlib.utils.des - DES routines [deprecated]")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html "passlib.utils.handlers - Framework for writing password hashes")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

# [`passlib.utils.binary`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#module-passlib.utils.binary "passlib.utils.binary: internal helpers for binary data") \- Binary Helper Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#module-passlib.utils.binary "Permalink to this headline")

Warning

This module is primarily used as an internal support module.
Its interface has not been finalized yet, and may be changed somewhat
between major releases of Passlib, as the internal code is cleaned up
and simplified.

## Constants [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#constants "Permalink to this headline")

`passlib.utils.binary.` `BASE64_CHARS` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.BASE64_CHARS "Permalink to this definition")

Character map used by standard MIME-compatible Base64 encoding scheme.

`passlib.utils.binary.` `HASH64_CHARS` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.HASH64_CHARS "Permalink to this definition")

Base64 character map used by a number of hash formats;
the ordering is wildly different from the standard base64 character map.

This encoding system appears to have originated with
[`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt"), but is used by
[`md5_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html#passlib.hash.md5_crypt "passlib.hash.md5_crypt"), [`sha256_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html#passlib.hash.sha256_crypt "passlib.hash.sha256_crypt"),
and others. Within Passlib, this encoding is referred as the “hash64” encoding,
to distinguish it from normal base64 and others.

`passlib.utils.binary.` `BCRYPT_CHARS` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.BCRYPT_CHARS "Permalink to this definition")

Base64 character map used by [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt").
The ordering is wildly different from both the standard base64 character map,
and the common hash64 character map.

## Base64 Encoding [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#base64-encoding "Permalink to this headline")

### Base64Engine Class [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#base64engine-class "Permalink to this headline")

Passlib has to deal with a number of different Base64 encodings,
with varying endianness, as well as wildly different character <-> value
mappings. This is all encapsulated in the [`Base64Engine`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine "passlib.utils.binary.Base64Engine") class,
which provides common encoding actions for an arbitrary base64-style encoding
scheme. There are also a couple of predefined instances which are commonly
used by the hashes in Passlib.

_class_ `passlib.utils.binary.` `Base64Engine`( _charmap_, _big=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine "Permalink to this definition")

Provides routines for encoding/decoding base64 data using
arbitrary character mappings, selectable endianness, etc.

| Parameters: | - **charmap** – A string of 64 unique characters,<br>  which will be used to encode successive 6-bit chunks of data.<br>  A character’s position within the string should correspond<br>  to its 6-bit value.<br>- **big** – Whether the encoding should be big-endian (default False). |

Note

This class does not currently handle base64’s padding characters
in any way what so ever.

#### Raw Bytes <-> Encoded Bytes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#passlib.utils.binary.Base64Engine-raw-bytes-encoded-bytes "Permalink to this headline")

The following methods convert between raw bytes,
and strings encoded using the engine’s specific base64 variant:

`encode_bytes`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.encode_bytes "Permalink to this definition")

encode bytes to base64 string.

| Parameters: | **source** – byte string to encode. |
| Returns: | byte string containing encoded data. |

`decode_bytes`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.decode_bytes "Permalink to this definition")

decode bytes from base64 string.

| Parameters: | **source** – byte string to decode. |
| Returns: | byte string containing decoded data. |

`encode_transposed_bytes`( _source_, _offsets_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.encode_transposed_bytes "Permalink to this definition")

encode byte string, first transposing source using offset list

`decode_transposed_bytes`( _source_, _offsets_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.decode_transposed_bytes "Permalink to this definition")

decode byte string, then reverse transposition described by offset list

#### Integers <-> Encoded Bytes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#passlib.utils.binary.Base64Engine-integers-encoded-bytes "Permalink to this headline")

The following methods allow encoding and decoding
unsigned integers to and from the engine’s specific base64 variant.
Endianess is determined by the engine’s `big` constructor keyword.

`encode_int6`( _value_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.encode_int6 "Permalink to this definition")

encodes 6-bit integer -> single hash64 character

`decode_int6`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.decode_int6 "Permalink to this definition")

decode single character -> 6 bit integer

`encode_int12`( _value_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.encode_int12 "Permalink to this definition")

encodes 12-bit integer -> 2 char string

`decode_int12`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.decode_int12 "Permalink to this definition")

decodes 2 char string -> 12-bit integer

`encode_int24`( _value_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.encode_int24 "Permalink to this definition")

encodes 24-bit integer -> 4 char string

`decode_int24`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.decode_int24 "Permalink to this definition")

decodes 4 char string -> 24-bit integer

`encode_int64`( _value_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.encode_int64 "Permalink to this definition")

encode 64-bit integer -> 11 char hash64 string

this format is used primarily by des-crypt & variants to encode
the DES output value used as a checksum.

`decode_int64`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.decode_int64 "Permalink to this definition")

decode 11 char base64 string -> 64-bit integer

this format is used primarily by des-crypt & variants to encode
the DES output value used as a checksum.

#### Informational Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#passlib.utils.binary.Base64Engine-informational-attributes "Permalink to this headline")

`charmap` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.charmap "Permalink to this definition")

unicode string containing list of characters used in encoding;
position in string matches 6bit value of character.

`bytemap` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.bytemap "Permalink to this definition")

bytes version of [`charmap`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.charmap "passlib.utils.binary.Base64Engine.charmap")

`big` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine.big "Permalink to this definition")

boolean flag indicating this using big-endian encoding.

### Predefined Instances [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#predefined-instances "Permalink to this headline")

`passlib.utils.binary.` `h64` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.h64 "Permalink to this definition")

Predefined instance of [`Base64Engine`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine "passlib.utils.binary.Base64Engine") which uses
the `HASH64_CHARS` character map and little-endian encoding.
(see [`HASH64_CHARS`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.HASH64_CHARS "passlib.utils.binary.HASH64_CHARS") for more details).

`passlib.utils.binary.` `h64big` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.h64big "Permalink to this definition")

Predefined variant of [`h64`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.h64 "passlib.utils.binary.h64") which uses big-endian encoding.
This is mainly used by [`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt").

Changed in version 1.6: Previous versions of Passlib contained
a module named `passlib.utils.h64`; As of Passlib 1.6 this
was replaced by the the `h64` and `h64big` instances of
the [`Base64Engine`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.Base64Engine "passlib.utils.binary.Base64Engine") class;
the interface remains mostly unchanged.

### Other [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html\#other "Permalink to this headline")

`passlib.utils.binary.` `ab64_encode`( _data_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.ab64_encode "Permalink to this definition")

encode using shortened base64 format which omits padding & whitespace.
uses custom `./` altchars.

it is primarily used by Passlib’s custom pbkdf2 hashes.

`passlib.utils.binary.` `ab64_decode`( _data_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.ab64_decode "Permalink to this definition")

decode from shortened base64 format which omits padding & whitespace.
uses custom `./` altchars, but supports decoding normal `+/` altchars as well.

it is primarily used by Passlib’s custom pbkdf2 hashes.

`passlib.utils.binary.` `b64s_encode`( _data_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.b64s_encode "Permalink to this definition")

encode using shortened base64 format which omits padding & whitespace.
uses default `+/` altchars.

`passlib.utils.binary.` `b64s_decode`( _data_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.b64s_decode "Permalink to this definition")

decode from shortened base64 format which omits padding & whitespace.
uses default `+/` altchars.

`passlib.utils.binary.` `b32encode`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.b32encode "Permalink to this definition")

wrapper around [`base64.b32encode()`](https://docs.python.org/3/library/base64.html#base64.b32encode "(in Python v3.9)") which strips padding,
and returns a native string.

`passlib.utils.binary.` `b32decode`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.b32decode "Permalink to this definition")

wrapper around [`base64.b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "(in Python v3.9)")
which handles common mistyped chars.
padding optional, ignored if present.

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
      - [`passlib.utils.binary` \- Binary Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#)
        - [Constants](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#constants)
        - [Base64 Encoding](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#base64-encoding)
          - [Base64Engine Class](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#base64engine-class)
          - [Predefined Instances](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#predefined-instances)
          - [Other](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#other)
      - [`passlib.utils.des` \- DES routines \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html)
      - [`passlib.utils.pbkdf2` \- PBKDF2 key derivation algorithm \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html "passlib.utils.des - DES routines [deprecated]")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html "passlib.utils.handlers - Framework for writing password hashes")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.utils.binary.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.utils.binary.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)