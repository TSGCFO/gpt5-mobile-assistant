<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html "passlib.pwd – Password generation helpers")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html "passlib.hosts - OS Password Handling")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.ifc`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#module-passlib.ifc "passlib.ifc: abstract interfaces used by Passlib") – Password Hash Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#passlib-ifc-password-hash-interface "Permalink to this headline")

## PasswordHash API [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#passwordhash-api "Permalink to this headline")

This module provides the `PasswordHash` abstract base class.
This class defines the common methods and attributes present
on all the hashes importable from the [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") module.
Additionally, the [`passlib.context.CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") class is deliberately
designed to parallel many of this interface’s methods.

See also

[PasswordHash Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-tutorial) – Overview of this interface and how to use it.

## Base Abstract Class [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#base-abstract-class "Permalink to this headline")

_class_ `passlib.ifc.` `PasswordHash` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "Permalink to this definition")

This class provides an abstract interface for an arbitrary password hasher.

Applications will generally not construct instances directly –
most of the operations are performed via classmethods, allowing
instances of a given class to be an internal detail used to implement
the various operations.

While `PasswordHash` offers a number of methods and attributes,
most applications will only need the two primary methods:

- [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") \- generate new salt, return hash of password.
- [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") \- verify password against existing hash.

Two additional support methods are also provided:

- [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") \- create subclass with customized configuration.
- [`PasswordHash.identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.identify "passlib.ifc.PasswordHash.identify") \- check if hash belongs to this algorithm.

Each hash algorithm also provides a number of [informational attributes](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#informational-attributes),
allowing programmatic inspection of its options and parameter limits.

See also

[PasswordHash Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-tutorial) – Overview of this interface and how to use it.

## Hashing & Verification Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#hashing-verification-methods "Permalink to this headline")

Most applications will only need to use two methods:
[`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") to generate new hashes, and [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify")
to check passwords against existing hashes.
These methods provide an easy interface for working with a password hash,
and abstract away details such as salt generation, hash normalization,
and hash comparison.

_classmethod_ `PasswordHash.` `hash`( _secret_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "Permalink to this definition")

Digest password using format-specific algorithm,
returning resulting hash string.

For most hashes supported by Passlib, the returned string will contain:
an algorithm identifier, a cost parameter, the salt string,
and finally the password digest itself.

| Parameters: | - **secret** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – string containing the password to encode.<br>- **\*\*kwds** – <br>  All additional keywords are algorithm-specific, and will be listed<br>  in that hash’s documentation; though many of the more common keywords<br>  are listed under [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds")<br>  and [`PasswordHash.context_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "passlib.ifc.PasswordHash.context_kwds").<br>  <br>  <br>  <br>  Deprecated since version 1.7: Passing [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds") such as `rounds` and `salt_size`<br>  directly into the [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") method is deprecated. Callers should instead<br>  use `handler.using(**settings).hash(secret)`. Support for the old method<br>  is is tentatively scheduled for removal in Passlib 2.0.<br>  <br>  <br>  <br>  Context keywords such as `user` should still be provided to `hash()`. |
| Returns: | Resulting password hash, encoded in an algorithm-specific format.<br>This will always be an instance of `str`<br>(i.e. `unicode` under Python 3, `ascii`-encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") under Python 2). |
| Raises: | - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>  - If a `kwd`’s value is invalid (e.g. if a `salt` string<br>    is too small, or a `rounds` value is out of range).<br>  - If `secret` contains characters forbidden by the hash algorithm<br>    (e.g. `des_crypt` forbids NULL characters).<br>- [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – <br>  - if `secret` is not `unicode` or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)").<br>  - if a `kwd` argument has an incorrect type.<br>  - if an algorithm-specific required `kwd` is not provided. |

Changed in version 1.6: Hashes now raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") if a required keyword is missing,
rather than [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") like in previous releases; in order
to conform with normal Python behavior.

Changed in version 1.6: Passlib is now much stricter about input validation: for example,
out-of-range `rounds` values now cause an error instead of being
clipped (though applications may set [relaxed=True](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#relaxed-keyword)
to restore the old behavior).

Changed in version 1.7: This method was renamed from [`encrypt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.encrypt "passlib.ifc.PasswordHash.encrypt").
Deprecated support for passing settings directly into `hash()`.

_classmethod_ `PasswordHash.` `encrypt`( _secret_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.encrypt "Permalink to this definition")

Legacy alias for [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash").

Deprecated since version 1.7: This method was renamed to `hash()` in version 1.7.
This alias will be removed in version 2.0, and should only
be used for compatibility with Passlib 1.3 - 1.6.

_classmethod_ `PasswordHash.` `verify`( _secret_, _hash_, _\*\*context\_kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "Permalink to this definition")

Verify a secret using an existing hash.

This checks if a secret matches against the one stored
inside the specified hash.

| Parameters: | - **secret** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – A string containing the password to check.<br>- **hash** – <br>  A string containing the hash to check against,<br>  such as returned by [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash").<br>  <br>  Hashes may be specified as `unicode` or<br>  `ascii`-encoded `bytes`.<br>  <br>- **\*\*kwds** – <br>  Very few hashes will have additional keywords.<br>  <br>  The ones that do typically require external contextual information<br>  in order to calculate the digest. For these hashes,<br>  the values must match the ones passed to the original<br>  [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") call when the hash was generated,<br>  or the password will not verify.<br>  <br>  These additional keywords are algorithm-specific, and will be listed<br>  in that hash’s documentation; though the more common keywords<br>  are listed under [`PasswordHash.context_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "passlib.ifc.PasswordHash.context_kwds").<br>  Examples of common keywords include `user`. |
| Returns: | `True` if the secret matches, otherwise `False`. |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – <br>  - if either `secret` or `hash` is not a unicode or bytes instance.<br>  - if the hash requires additional `kwds` which are not provided,<br>  - if a `kwd` argument has the wrong type.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>  - if `hash` does not match this algorithm’s format.<br>  - if the `secret` contains forbidden characters (see<br>    [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash")).<br>  - if a configuration/salt string generated by [`PasswordHash.genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig")<br>    is passed in as the value for `hash` (these strings look<br>    similar to a full hash, but typically lack the digest portion<br>    needed to verify a password). |

Changed in version 1.6: This function now raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") if `None` or a config string is provided
instead of a properly-formed hash; previous releases were inconsistent
in their handling of these two border cases.

See also

- [Hashing & Verifying](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-verifying) tutorial for a usage example

## Crypt Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#crypt-methods "Permalink to this headline")

Taken together, the [`PasswordHash.genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig") and [`PasswordHash.genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash")
are two tightly-coupled methods that mimic the standard Unix
“crypt” interface. The first method generates salt / configuration
strings from a set of settings, and the second hashes the password
using the provided configuration string.

See also

Most applications will find [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") much more useful,
as it combines the functionality of these two methods into one.

_classmethod_ `PasswordHash.` `genconfig`( _\*\*setting\_kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "Permalink to this definition")

Deprecated since version 1.7: As of 1.7, this method is deprecated, and slated for complete removal in Passlib 2.0.

For all known real-world uses, `.hash("", **settings)`
should provide equivalent functionality.

This deprecation may be reversed if a use-case presents itself in the mean time.

Returns a configuration string encoding settings for hash generation.

This function takes in all the same [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds")
as [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"), fills in suitable defaults,
and encodes the settings into a single “configuration” string,
suitable passing to [`PasswordHash.genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash").

| Parameters: | **\*\*kwds** – All additional keywords are algorithm-specific, and will be listed<br>in that hash’s documentation; though many of the more common keywords<br>are listed under [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds")<br>Examples of common keywords include `salt` and `rounds`. |
| Returns: | A configuration string (as `str`). |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") **,** [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – This function raises exceptions for the same<br>reasons as [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"). |

Changed in version 1.7: This should now always return a full hash string, even in cases
where previous releases would return a truncated “configuration only” string,
or `None`.

_classmethod_ `PasswordHash.` `genhash`( _secret_, _config_, _\*\*context\_kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "Permalink to this definition")

Encrypt secret using specified configuration string.

Deprecated since version 1.7: As of 1.7, this method is deprecated, and slated for complete removal in Passlib 2.0.

This deprecation may be reversed if a use-case presents itself in the mean time.

This takes in a password and a configuration string,
and returns a hash for that password.

| Parameters: | - **secret** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – string containing the password to be encrypted.<br>- **config** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – <br>  configuration string to use when hashing the secret.<br>  this can either be an existing hash that was previously<br>  returned by [`PasswordHash.genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), or a configuration string<br>  that was previously created by [`PasswordHash.genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig").<br>  <br>  <br>  <br>  Changed in version 1.7: `None` is no longer accepted for hashes which (prior to 1.7)<br>  lacked a configuration string format.<br>  <br>- **\*\*kwds** – <br>  Very few hashes will have additional keywords.<br>  <br>  The ones that do typically require external contextual information<br>  in order to calculate the digest. For these hashes,<br>  the values must match the ones passed to the original<br>  [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") call when the hash was generated,<br>  or the password will not verify.<br>  <br>  These additional keywords are algorithm-specific, and will be listed<br>  in that hash’s documentation; though the more common keywords<br>  are listed under : [`PasswordHash.context_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "passlib.ifc.PasswordHash.context_kwds").<br>  Examples of common keywords include `user`. |
| Returns: | Encoded hash matching specified secret, config, and kwds.<br>This will always be a native `str` instance. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") **,** [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – This function raises exceptions for the same<br>reasons as [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"). |

Warning

Traditionally, password verification using the “crypt” interface
was done by testing if `hash == genhash(password, hash)`.
This test is only reliable for a handful of algorithms,
as various hash representation issues may cause false results.
Applications are strongly urged to use [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") instead.

## Factory Creation [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#factory-creation "Permalink to this headline")

One powerful method offered by the `PasswordHash` class [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using").
This method allows you to quickly create subclasses of a specific hash,
providing it with preconfigured defaults specific to your application:

_classmethod_ `PasswordHash.` `using`( _relaxed=False_, _\*\*settings_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "Permalink to this definition")

This method takes in a set of algorithm-specific settings,
and returns a new handler object which uses the specified default settings instead.

| Parameters: | **\*\*settings** – All keywords are algorithm-specific, and will be listed<br>in that hash’s documentation; though many of the more common keywords<br>are listed under [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds").<br>Examples of common keywords include `rounds` and `salt_size`. |
| Returns: | A new object which adheres to `PasswordHash` api. |
| Raises: | - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>  - If a keywords’s value is invalid (e.g. if a `salt` string<br>    is too small, or a `rounds` value is out of range).<br>- [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – <br>  - if a `kwd` argument has an incorrect type. |

New in version 1.7.

See also

[Customizing the Configuration](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-configuring) tutorial for a usage example

## Hash Inspection Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#hash-inspection-methods "Permalink to this headline")

There are currently two hash inspection methods, [`PasswordHash.identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.identify "passlib.ifc.PasswordHash.identify")
and [`PasswordHash.needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.needs_update "passlib.ifc.PasswordHash.needs_update").

_classmethod_ `PasswordHash.` `identify`( _hash_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.identify "Permalink to this definition")

Quickly identify if a hash string belongs to this algorithm.

| Parameters: | **hash** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – the candidate hash string to check |
| Returns: | - `True` if the input is a configuration string or hash stringidentifiable as belonging to this scheme (even if it’s malformed).<br>- `False` if the input does not belong to this scheme. |
| Raises: | [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – if `hash` is not a unicode or bytes instance. |

Note

A small number of the hashes supported by Passlib lack a reliable
method of identification (e.g. [`lmhash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#passlib.hash.lmhash "passlib.hash.lmhash")
and [`nthash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.nthash.html#passlib.hash.nthash "passlib.hash.nthash") both consist of 32 hexadecimal characters,
with no distinguishing features). For such hashes, this method
may return false positives.

See also

If you are considering using this method to select from multiple
algorithms (e.g. in order to verify a password), you will be better served
by the [CryptContext](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-reference) class.

_classmethod_ `PasswordHash.` `needs_update`( _hash_, _secret=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.needs_update "Permalink to this definition")

check if hash’s configuration is outside desired bounds,
or contains some other internal option which requires
updating the password hash.

| Parameters: | - **hash** – hash string to examine<br>- **secret** – optional secret known to have verified against the provided hash.<br>  (this is used by some hashes to detect legacy algorithm mistakes). |
| Returns: | whether secret needs re-hashing. |

New in version 1.7.

## General Informational Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#general-informational-attributes "Permalink to this headline")

Each hash provides a handful of informational attributes, allowing
programs to dynamically adapt to the requirements of different
hash algorithms. The following attributes should be defined for all
the hashes in passlib:

`PasswordHash.` `name` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.name "Permalink to this definition")

Name uniquely identifying this hash.

For the hashes built into Passlib, this will always match
the location where it was imported from — `passlib.hash.name` —
though externally defined hashes may not adhere to this.

This should always be a `str` consisting of lowercase `a-z`,
the digits `0-9`, and the underscore character `_`.

`PasswordHash.` `setting_kwds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "Permalink to this definition")

Tuple listing the keywords supported by [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") control hash generation,
and which will be encoded into the resulting hash.

(These keywords will also be accepted by [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`PasswordHash.genconfig()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genconfig "passlib.ifc.PasswordHash.genconfig"),though that behavior is deprecated as of Passlib 1.7; and will be removed in Passlib 2.0).

This list commonly includes keywords for controlling salt generation,
adjusting time-cost parameters, etc. Most of these settings are optional,
and suitable defaults will be chosen if they are omitted (e.g. salts
will be autogenerated).

While the documentation for each hash should have a complete list of
the specific settings the hash uses, the following keywords should have
roughly the same behavior for all the hashes that support them:

`salt`

Specifies a fixed salt string to use, rather than randomly
generating one.

This option is supported by most of the hashes in Passlib,
though typically it isn’t used, as random generation of a salt
is usually the desired behavior.

Hashes typically require this to be a `unicode` or
`bytes` instance, with additional constraints
appropriate to the algorithm.

`salt_size`

> Most algorithms which support the `salt` setting will
> autogenerate a salt when none is provided. Most of those hashes
> will also offer this option, which allows the caller to specify
> the size of salt which should be generated. If omitted,
> the hash’s default salt size will be used.
>
> See also
>
> the [salt info](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#salt-attributes) attributes (below)

`rounds`

If present, this means the hash can vary the number
of internal rounds used in some part of its algorithm,
allowing the calculation to take a variable amount of processor
time, for increased security.

While this is almost always a non-negative integer,
additional constraints may be present for each algorithm
(such as the cost varying on a linear or logarithmic scale).

This value is typically omitted, in which case a default
value will be used. The defaults for all the hashes in Passlib
are periodically retuned to strike a balance between
security and responsiveness.

See also

the [rounds info](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#rounds-attributes) attributes (below)

`ident`

If present, the class supports multiple formats for encoding
the same hash. The class’s documentation will generally list
the allowed values, allowing alternate output formats to be selected.

Note that these values will typically correspond to different
revision of the hash algorithm itself, and they may not all
offer the same level of security.

`truncate_error`

> This will be present if and only if the hash truncates passwords
> larger than some limit (reported via it’s [`truncate_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.truncate_size "passlib.ifc.truncate_size") attribute).
> By default, they will silently truncate passwords above their limit.
> Setting `truncate_error=True` will cause [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash")
> to raise a [`PasswordTruncateError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordTruncateError "passlib.exc.PasswordTruncateError") instead.

`relaxed`

By default, passing an invalid value to [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using")
will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). However, if `relaxed=True`
then Passlib will attempt to correct the error and (if successful)
issue a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning") instead.
This warning may then be filtered if desired.
Correctable errors include (but are not limited to): `rounds`
and `salt_size` values that are too low or too high, `salt`
strings that are too large.

New in version 1.6.

`PasswordHash.` `context_kwds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "Permalink to this definition")

Tuple listing the keywords supported by [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"),
[`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify"), and [`PasswordHash.genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash").
These keywords are different from the settings kwds in that the context keywords
affect the hash, but are not encoded within it, and thus must be provided each time
the hash is calculated.

This list commonly includes a user account, http realm identifier,
etc. Most of these keywords are required by the hashes which support them,
as they are frequently used in place of an embedded salt parameter.

_Most hash algorithms in Passlib will have no context keywords._

While the documentation for each hash should have a complete list of
the specific context keywords the hash uses,
the following keywords should have roughly the same behavior
for all the hashes that support them:

`user`

> If present, the class requires a username be specified whenever
> performing a hash calculation (e.g.
> [`postgres_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#passlib.hash.postgres_md5 "passlib.hash.postgres_md5") and
> [`oracle10`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#passlib.hash.oracle10 "passlib.hash.oracle10")).

`encoding`

> Some hashes have poorly-defined or host-dependant unicode behavior,
> and properly hashing a non-ASCII password requires providing
> the correct encoding ( [`lmhash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html#passlib.hash.lmhash "passlib.hash.lmhash") is perhaps the worst offender).
> Hashes which provide this keyword will always expose
> their default encoding programmatically via the
> `PasswordHash.default_encoding` attribute.

`passlib.ifc.` `truncate_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.truncate_size "Permalink to this definition")

A positive integer, indicating the hash will truncate any passwords larger than this many bytes.
If `None` (the more common case), indicates the hash will use
the entire password provided.

Hashes which specify this setting will also support a `truncate_error`
flag via their [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method, to configure
how truncation is handled.

See also

[Customizing the Configuration](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-configuring) tutorial for a usage example

## Salt Information Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#salt-information-attributes "Permalink to this headline")

For schemes which support a salt string,
`"salt"` should be listed in their [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds"),
and the following attributes should be defined:

`PasswordHash.` `max_salt_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.max_salt_size "Permalink to this definition")

The maximum number of bytes/characters allowed in the salt.
Should either be a positive integer, or `None` (indicating
the algorithm has no effective upper limit).

`PasswordHash.` `min_salt_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.min_salt_size "Permalink to this definition")

The minimum number of bytes/characters required for the salt.
Must be an integer between 0 and [`PasswordHash.max_salt_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.max_salt_size "passlib.ifc.PasswordHash.max_salt_size").

`PasswordHash.` `default_salt_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.default_salt_size "Permalink to this definition")

The default salt size that will be used when generating a salt,
assuming `salt_size` is not set explicitly. This is typically
the same as [`max_salt_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.max_salt_size "passlib.ifc.PasswordHash.max_salt_size"),
or a sane default if `max_salt_size=None`.

`PasswordHash.` `salt_chars` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.salt_chars "Permalink to this definition")

A unicode string containing all the characters permitted
in a salt string.

For most [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format) hashes,
this is equal to [`passlib.utils.binary.HASH64_CHARS`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.HASH64_CHARS "passlib.utils.binary.HASH64_CHARS").
For the rare hashes where the `salt` parameter must be specified
in bytes, this will be a placeholder `bytes` object containing
all 256 possible byte values.

## Rounds Information Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#rounds-information-attributes "Permalink to this headline")

For schemes which support a variable time-cost parameter,
`"rounds"` should be listed in their [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds"),
and the following attributes should be defined:

`PasswordHash.` `max_rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.max_rounds "Permalink to this definition")

The maximum number of rounds the scheme allows.
Specifying a value beyond this will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)").
This will be either a positive integer, or `None` (indicating
the algorithm has no effective upper limit).

`PasswordHash.` `min_rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.min_rounds "Permalink to this definition")

The minimum number of rounds the scheme allows.
Specifying a value below this will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)").
Will always be an integer between 0 and [`PasswordHash.max_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.max_rounds "passlib.ifc.PasswordHash.max_rounds").

`PasswordHash.` `default_rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.default_rounds "Permalink to this definition")

The default number of rounds that will be used if none is explicitly
provided to [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash").
This will always be an integer between [`PasswordHash.min_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.min_rounds "passlib.ifc.PasswordHash.min_rounds")
and [`PasswordHash.max_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.max_rounds "passlib.ifc.PasswordHash.max_rounds").

`PasswordHash.` `rounds_cost` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.rounds_cost "Permalink to this definition")

While the cost parameter `rounds` is an integer, how it corresponds
to the amount of time taken can vary between hashes. This attribute
indicates the scale used by the hash:

- `"linear"` \- time taken scales linearly with rounds value
(e.g. [`sha512_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html#passlib.hash.sha512_crypt "passlib.hash.sha512_crypt"))
- `"log2"` \- time taken scales exponentially with rounds value
(e.g. [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt"))

Todo

document the additional [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") keywords
available for setting rounds limits.

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
  - [`passlib.ifc` – Password Hash Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#)
    - [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passwordhash-api)
    - [Base Abstract Class](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#base-abstract-class)
    - [Hashing & Verification Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#hashing-verification-methods)
    - [Crypt Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#crypt-methods)
    - [Factory Creation](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#factory-creation)
    - [Hash Inspection Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#hash-inspection-methods)
    - [General Informational Attributes](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#general-informational-attributes)
    - [Salt Information Attributes](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#salt-information-attributes)
    - [Rounds Information Attributes](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#rounds-information-attributes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html "passlib.pwd – Password generation helpers")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html "passlib.hosts - OS Password Handling")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.ifc.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.ifc.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)