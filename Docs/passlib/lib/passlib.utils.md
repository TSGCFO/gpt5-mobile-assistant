<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html "passlib.utils.handlers - Framework for writing password hashes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html "passlib.totp – TOTP / Two Factor Authentication")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.utils`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#module-passlib.utils "passlib.utils: internal helpers for implementing password hashes") \- Helper Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#module-passlib.utils "Permalink to this headline")

Warning

This module is primarily used as an internal support module.
Its interface has not been finalized yet, and may be changed somewhat
between major releases of Passlib, as the internal code is cleaned up
and simplified.

This module primarily contains utility functions used internally by Passlib.
However, end-user applications may find some of the functions useful,
in particular:

> - [`consteq()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.consteq "passlib.utils.consteq")
> - [`saslprep()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.saslprep "passlib.utils.saslprep")
> - [`generate_password()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.generate_password "passlib.utils.generate_password")

## Constants [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#constants "Permalink to this headline")

`passlib.utils.` `unix_crypt_schemes` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.unix_crypt_schemes "Permalink to this definition")

List of the names of all the hashes in [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib")
which are natively supported by `crypt()` on at least one operating
system.

For all hashes in this list, the expression
`passlib.hash.alg.has_backend("os_crypt")`
will return `True` if the host OS natively supports the hash.
This list is used by [`host_context`](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#passlib.hosts.host_context "passlib.hosts.host_context")
and [`ldap_context`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.ldap_context "passlib.apps.ldap_context") to determine
which hashes are supported by the host.

See also

[Identifiers & Platform Support](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#mcf-identifiers) for a table of which OSes are known to support which hashes.

## Unicode Helpers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#unicode-helpers "Permalink to this headline")

`passlib.utils.` `consteq`( _left_, _right_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.consteq "Permalink to this definition")

Check two strings/bytes for equality.

This is functionally equivalent to `left == right`,
but attempts to take constant time relative to the size of the righthand input.

The purpose of this function is to help prevent timing attacks
during digest comparisons: the standard `==` operator aborts
after the first mismatched character, causing its runtime to be
proportional to the longest prefix shared by the two inputs.
If an attacker is able to predict and control one of the two
inputs, repeated queries can be leveraged to reveal information about
the content of the second argument. To minimize this risk, `consteq()`
is designed to take `THETA(len(right))` time, regardless
of the contents of the two strings.
It is recommended that the attacker-controlled input
be passed in as the left-hand value.

Warning

This function is _not_ perfect. Various VM-dependant issues
(e.g. the VM’s integer object instantiation algorithm, internal unicode representation, etc),
may still cause the function’s run time to be affected by the inputs,
though in a less predictable manner.
_To minimize such risks, this function should not be passed_ `unicode` _inputs that might contain non-_ `ASCII` _characters_.

New in version 1.6.

Changed in version 1.7: This is an alias for stdlib’s [`hmac.compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "(in Python v3.9)") under Python 3.3 and up.

`passlib.utils.` `saslprep`( _source_, _param='value'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.saslprep "Permalink to this definition")

Normalizes unicode strings using SASLPrep stringprep profile.

The SASLPrep profile is defined in [**RFC 4013**](https://tools.ietf.org/html/rfc4013.html).
It provides a uniform scheme for normalizing unicode usernames
and passwords before performing byte-value sensitive operations
such as hashing. Among other things, it normalizes diacritic
representations, removes non-printing characters, and forbids
invalid characters such as `\n`. Properly internationalized
applications should run user passwords through this function
before hashing.

| Parameters: | - **source** – unicode string to normalize & validate<br>- **param** – Optional noun identifying source parameter in error messages<br>  (Defaults to the string `"value"`). This is mainly useful to make the caller’s error<br>  messages make more sense contextually. |
| Raises: | - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if any characters forbidden by the SASLPrep profile are encountered.<br>- [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if input is not `unicode` |
| Returns: | normalized unicode string |

Note

This function is not available under Jython,
as the Jython stdlib is missing the `stringprep` module
( [Jython issue 1758320](http://bugs.jython.org/issue1758320)).

New in version 1.6.

## Bytes Helpers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#bytes-helpers "Permalink to this headline")

`passlib.utils.` `xor_bytes`( _left_, _right_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.xor_bytes "Permalink to this definition")

Perform bitwise-xor of two byte strings (must be same size)

`passlib.utils.` `render_bytes`( _source_, _\*args_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.render_bytes "Permalink to this definition")

Peform `%` formating using bytes in a uniform manner across Python 2/3.

This function is motivated by the fact that
[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") instances do not support `%` or `{}` formatting under Python 3.
This function is an attempt to provide a replacement:
it converts everything to unicode (decoding bytes instances as `latin-1`),
performs the required formatting, then encodes the result to `latin-1`.

Calling `render_bytes(source, *args)` should function roughly the same as
`source % args` under Python 2.

Todo

python >= 3.5 added back limited support for bytes %,
can revisit when 3.3/3.4 is dropped.

`passlib.utils.` `int_to_bytes`( _value_, _count_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.int_to_bytes "Permalink to this definition")

encode integer as single big-endian byte string

`passlib.utils.` `bytes_to_int`( _value_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.bytes_to_int "Permalink to this definition")

decode byte string as single big-endian integer

## Encoding Helpers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#encoding-helpers "Permalink to this headline")

`passlib.utils.` `is_same_codec`( _left_, _right_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.is_same_codec "Permalink to this definition")

Check if two codec names are aliases for same codec

`passlib.utils.` `is_ascii_codec`( _codec_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.is_ascii_codec "Permalink to this definition")

Test if codec is compatible with 7-bit ascii (e.g. latin-1, utf-8; but not utf-16)

`passlib.utils.` `is_ascii_safe`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.is_ascii_safe "Permalink to this definition")

Check if string (bytes or unicode) contains only 7-bit ascii

`passlib.utils.` `to_bytes`( _source_, _encoding='utf-8'_, _param='value'_, _source\_encoding=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.to_bytes "Permalink to this definition")

Helper to normalize input to bytes.

| Parameters: | - **source** – Source bytes/unicode to process.<br>- **encoding** – Target encoding (defaults to `"utf-8"`).<br>- **param** – Optional name of variable/noun to reference when raising errors<br>- **source\_encoding** – If this is specified, and the source is bytes,<br>  the source will be transcoded from _source\_encoding_ to _encoding_<br>  (via unicode). |
| Raises: | [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if source is not unicode or bytes. |
| Returns: | - unicode strings will be encoded using _encoding_, and returned.<br>- if _source\_encoding_ is not specified, byte strings will be<br>  returned unchanged.<br>- if _source\_encoding_ is specified, byte strings will be transcoded<br>  to _encoding_. |

`passlib.utils.` `to_unicode`( _source_, _encoding='utf-8'_, _param='value'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.to_unicode "Permalink to this definition")

Helper to normalize input to unicode.

| Parameters: | - **source** – source bytes/unicode to process.<br>- **encoding** – encoding to use when decoding bytes instances.<br>- **param** – optional name of variable/noun to reference when raising errors. |
| Raises: | [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if source is not unicode or bytes. |
| Returns: | - returns unicode strings unchanged.<br>- returns bytes strings decoded using _encoding_ |

`passlib.utils.` `to_native_str`( _source_, _encoding='utf-8'_, _param='value'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.to_native_str "Permalink to this definition")

Take in unicode or bytes, return native string.

Python 2: encodes unicode using specified encoding, leaves bytes alone.
Python 3: leaves unicode alone, decodes bytes using specified encoding.

| Raises: | [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if source is not unicode or bytes. |
| Parameters: | - **source** – source unicode or bytes string.<br>- **encoding** – encoding to use when encoding unicode or decoding bytes.<br>  this defaults to `"utf-8"`.<br>- **param** – optional name of variable/noun to reference when raising errors. |
| Returns: | [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") instance |

## Randomness [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#randomness "Permalink to this headline")

`passlib.utils.` `rng` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.rng "Permalink to this definition")

The random number generator used by Passlib to generate
salt strings and other things which don’t require a
cryptographically strong source of randomness.

If [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "(in Python v3.9)") support is available,
this will be an instance of `random.SystemRandom`,
otherwise it will use the default python PRNG class,
seeded from various sources at startup.

`passlib.utils.` `getrandbytes`( _rng_, _count_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.getrandbytes "Permalink to this definition")

return byte-string containing _count_ number of randomly generated bytes, using specified rng

`passlib.utils.` `getrandstr`( _rng_, _charset_, _count_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.getrandstr "Permalink to this definition")

return string containing _count_ number of chars/bytes, whose elements are drawn from specified charset, using specified rng

`passlib.utils.` `generate_password`( _size=10_, _charset=<default charset>_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.generate_password "Permalink to this definition")

generate random password using given length & charset

> | param size: | size of password. |
> | param charset: | optional string specified set of characters to draw from.<br>the default charset contains all normal alphanumeric characters,<br>except for the characters `1IiLl0OoS5`, which were omitted<br>due to their visual similarity. |
> | returns: | `str` containing randomly generated password. |
>
> Note
>
> Using the default character set, on a OS with `SystemRandom` support,
> this function should generate passwords with 5.7 bits of entropy per character.

Deprecated since version 1.7: and will be removed in version 2.0, use passlib.pwd.genword() / passlib.pwd.genphrase() instead.

## Interface Tests [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#interface-tests "Permalink to this headline")

`passlib.utils.` `is_crypt_handler`( _obj_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.is_crypt_handler "Permalink to this definition")

check if object follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api)

`passlib.utils.` `is_crypt_context`( _obj_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.is_crypt_context "Permalink to this definition")

check if object appears to be a [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instance

`passlib.utils.` `has_rounds_info`( _handler_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.has_rounds_info "Permalink to this definition")

check if handler provides the optional [rounds information](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#rounds-attributes) attributes

`passlib.utils.` `has_salt_info`( _handler_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.has_salt_info "Permalink to this definition")

check if handler provides the optional [salt information](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#salt-attributes) attributes

## Submodules [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html\#submodules "Permalink to this headline")

There are also a few sub modules which provide additional utility functions:

- [`passlib.utils.handlers` \- Framework for writing password hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html)
- [`passlib.utils.binary` \- Binary Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html)
- [`passlib.utils.des` \- DES routines \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.des.html)
- [`passlib.utils.pbkdf2` \- PBKDF2 key derivation algorithm \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html)

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
  - [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#)
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
      - [`passlib.utils.pbkdf2` \- PBKDF2 key derivation algorithm \[deprecated\]](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.pbkdf2.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html "passlib.utils.handlers - Framework for writing password hashes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html "passlib.totp – TOTP / Two Factor Authentication")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.utils.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.utils.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)