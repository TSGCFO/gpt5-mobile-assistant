<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html "passlib.utils.binary - Binary Helper Functions")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html "passlib.utils - Helper Functions")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

# [`passlib.utils.handlers`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#module-passlib.utils.handlers "passlib.utils.handlers: framework for writing password hashes") \- Framework for writing password hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#module-passlib.utils.handlers "Permalink to this headline")

Warning

This module is primarily used as an internal support module.
Its interface has not been finalized yet, and may be changed somewhat
between major releases of Passlib, as the internal code is cleaned up
and simplified.

Todo

This module, and the instructions on how to write a custom handler,
definitely need to be rewritten for clarity. They are not yet
organized, and may leave out some important details.

## Implementing Custom Handlers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#implementing-custom-handlers "Permalink to this headline")

All that is required in order to write a custom handler that will work with
Passlib is to create an object (be it module, class, or object) that
exposes the functions and attributes required by the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).
For classes, Passlib does not make any requirements about what a class instance
should look like (if the implementation even uses them).

That said, most of the handlers built into Passlib are based around the [`GenericHandler`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler "passlib.utils.handlers.GenericHandler")
class, and its associated mixin classes. While deriving from this class is not required,
doing so will greatly reduce the amount of additional code that is needed for
all but the most convoluted password hash schemes.

Once a handler has been written, it may be used explicitly, passed into
a `CryptContext` constructor, or registered
globally with Passlib via the [`passlib.registry`](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html#module-passlib.registry "passlib.registry: registry for tracking password hash handlers.") module.

See also

[Testing Hash Handlers](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#testing-hash-handlers) for details about how to test
custom handlers against Passlib’s unittest suite.

## The GenericHandler Class [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#the-generichandler-class "Permalink to this headline")

### Design [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#design "Permalink to this headline")

Most of the handlers built into Passlib are based around the [`GenericHandler`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler "passlib.utils.handlers.GenericHandler")
class. This class is designed under the assumption that the common
workflow for hashes is some combination of the following:

1. parse hash into constituent parts - performed by [`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.from_string "passlib.utils.handlers.GenericHandler.from_string").
2. validate constituent parts - performed by `GenericHandler`’s constructor,
and the normalization functions such as [`_norm_checksum()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._norm_checksum "passlib.utils.handlers.GenericHandler._norm_checksum") and [`_norm_salt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt._norm_salt "passlib.utils.handlers.HasSalt._norm_salt")
which are provided by its related mixin classes.
3. calculate the raw checksum for a specific password - performed by [`_calc_checksum()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._calc_checksum "passlib.utils.handlers.GenericHandler._calc_checksum").
4. assemble hash, including new checksum, into a new string - performed by [`to_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.to_string "passlib.utils.handlers.GenericHandler.to_string").

With this in mind, `GenericHandler` provides implementations
of most of the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api) methods, eliminating the need
for almost all the boilerplate associated with writing a password hash.

In order to minimize the amount of unneeded features that must be loaded in, the `GenericHandler`
class itself contains only the parts which are needed by almost all handlers: parsing, rendering, and checksum validation.
Validation of all other parameters (such as salt, rounds, etc) is split out into separate
[mixin classes](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#generic-handler-mixins) which enhance `GenericHandler` with additional features.

### Usage [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#usage "Permalink to this headline")

In order to use `GenericHandler`, just subclass it, and then do the following:

> - fill out the `name` attribute with the name of your hash.
>
> - fill out the `setting_kwds` attribute with a tuple listing
> all the settings your hash accepts.
>
> - provide an implementation of the `from_string()` classmethod.
>
> this method should take in a potential hash string,
> parse it into components, and return an instance of the class
> which contains the parsed components. It should throw a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)")
> if no hash, or an invalid hash, is provided.
>
> - provide an implementation of the `to_string()` instance method.
>
> this method should render an instance of your handler class
> (such as returned by `from_string()`), returning
> a hash string.
>
> - provide an implementation of the `_calc_checksum()` instance method.
>
> this is the heart of the hash; this method should take in the password
> as the first argument, then generate and return the digest portion
> of the hash, according to the settings (such as salt, etc) stored
> in the parsed instance this method was called from.
>
> note that it should not return the full hash with identifiers, etc;
> that job should be performed by `to_string()`.

Some additional notes:

> - In addition to simply subclassing `GenericHandler`, most handlers
> will also benefit from adding in some of the mixin classes
> that are designed to add features to `GenericHandler`.
> See [GenericHandler Mixins](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#generic-handler-mixins) for more details.
> - Most implementations will want to alter/override the default [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.identify "passlib.utils.handlers.GenericHandler.identify") method.
> By default, it returns `True` for all hashes that [`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.from_string "passlib.utils.handlers.GenericHandler.from_string")
> can parse without raising a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"); which is reliable, but somewhat slow.
> For faster identification purposes, subclasses may fill in the [`ident`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.ident "passlib.utils.handlers.GenericHandler.ident") attribute
> with the hash’s identifying prefix, which [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.identify "passlib.utils.handlers.GenericHandler.identify") will then test for
> instead of calling [`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.from_string "passlib.utils.handlers.GenericHandler.from_string").
> For more complex situations, a custom implementation should be used;
> the [`HasManyIdents`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasManyIdents "passlib.utils.handlers.HasManyIdents") mixin may also be helpful.
> - This class does not support context kwds of any type,
> since that is a rare enough requirement inside passlib.

### Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#interface "Permalink to this headline")

_class_ `passlib.utils.handlers.` `GenericHandler`( _checksum=None_, _use\_defaults=False_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler "Permalink to this definition")

helper class for implementing hash handlers.

GenericHandler-derived classes will have (at least) the following
constructor options, though others may be added by mixins
and by the class itself:

| Parameters: | - **checksum** – this should contain the digest portion of a<br>  parsed hash (mainly provided when the constructor is called<br>  by [`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.from_string "passlib.utils.handlers.GenericHandler.from_string")).<br>  defaults to `None`.<br>- **use\_defaults** – <br>  If `False` (the default), a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") should be thrown<br>  if any settings required by the handler were not explicitly provided.<br>  <br>  If `True`, the handler should attempt to provide a default for any<br>  missing values. This means generate missing salts, fill in default<br>  cost parameters, etc.<br>  <br>  This is typically only set to `True` when the constructor<br>  is called by [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.hash "passlib.utils.handlers.GenericHandler.hash"), allowing user-provided values<br>  to be handled in a more permissive manner.<br>  <br>- **relaxed** – <br>  If `False` (the default), a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") should be thrown<br>  if any settings are out of bounds or otherwise invalid.<br>  <br>  If `True`, they should be corrected if possible, and a warning<br>  issue. If not possible, only then should an error be raised.<br>  (e.g. under `relaxed=True`, rounds values will be clamped<br>  to min/max rounds).<br>  <br>  This is mainly used when parsing the config strings of certain<br>  hashes, whose specifications implementations to be tolerant<br>  of incorrect values in salt strings. |

#### Class Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.GenericHandler-class-attributes "Permalink to this headline")

`ident` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.ident "Permalink to this definition")

\[optional\]
If this attribute is filled in, the default [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.identify "passlib.utils.handlers.GenericHandler.identify") method will use
it as a identifying prefix that can be used to recognize instances of this handler’s
hash. Filling this out is recommended for speed.

This should be a unicode str.

`_hash_regex` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._hash_regex "Permalink to this definition")

\[optional\]
If this attribute is filled in, the default [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.identify "passlib.utils.handlers.GenericHandler.identify") method
will use it to recognize instances of the hash. If [`ident`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.ident "passlib.utils.handlers.GenericHandler.ident")
is specified, this will be ignored.

This should be a unique regex object.

`checksum_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.checksum_size "Permalink to this definition")

\[optional\]
Specifies the number of characters that should be expected in the checksum string.
If omitted, no check will be performed.

`checksum_chars` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.checksum_chars "Permalink to this definition")

\[optional\]
A string listing all the characters allowed in the checksum string.
If omitted, no check will be performed.

This should be a unicode str.

`_stub_checksum` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._stub_checksum "Permalink to this definition")

Placeholder checksum that will be used by genconfig()
in lieu of actually generating a hash for the empty string.
This should be a string of the same datatype as [`checksum`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.checksum "passlib.utils.handlers.GenericHandler.checksum").

#### Instance Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.GenericHandler-instance-attributes "Permalink to this headline")

`checksum` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.checksum "Permalink to this definition")

The checksum string provided to the constructor (after passing it
through [`_norm_checksum()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._norm_checksum "passlib.utils.handlers.GenericHandler._norm_checksum")).

#### Required Subclass Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.GenericHandler-required-subclass-methods "Permalink to this headline")

The following methods must be provided by handler subclass:

_classmethod_ `from_string`( _hash_, _\*\*context_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.from_string "Permalink to this definition")

return parsed instance from hash/configuration string

| Parameters: | **\\\*\\\*context** – context keywords to pass to constructor (if applicable). |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if hash is incorrectly formatted |
| Returns: | hash parsed into components,<br>for formatting / calculating checksum. |

`to_string`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.to_string "Permalink to this definition")

render instance to hash or configuration string

| Returns: | hash string with salt & digest included.<br>should return native string type (ascii-bytes under python 2,<br>unicode under python 3) |

`_calc_checksum`( _secret_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._calc_checksum "Permalink to this definition")

given secret; calcuate and return encoded checksum portion of hash
string, taking config from object state

calc checksum implementations may assume secret is always
either unicode or bytes, checks are performed by verify/etc.

#### Default Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.GenericHandler-default-methods "Permalink to this headline")

The following methods have default implementations that should work for
most cases, though they may be overridden if the hash subclass needs to:

`_norm_checksum`( _checksum_, _relaxed=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler._norm_checksum "Permalink to this definition")

validates checksum keyword against class requirements,
returns normalized version of checksum.

_classmethod_ `genconfig`( _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.genconfig "Permalink to this definition")

compile settings into a configuration string for genhash()

Deprecated since version 1.7: As of 1.7, this method is deprecated, and slated for complete removal in Passlib 2.0.

For all known real-world uses, hashing a constant string
should provide equivalent functionality.

This deprecation may be reversed if a use-case presents itself in the mean time.

_classmethod_ `genhash`( _secret_, _config_, _\*\*context_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.genhash "Permalink to this definition")

generated hash for secret, using settings from config/hash string

Deprecated since version 1.7: As of 1.7, this method is deprecated, and slated for complete removal in Passlib 2.0.

This deprecation may be reversed if a use-case presents itself in the mean time.

_classmethod_ `identify`( _hash_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.identify "Permalink to this definition")

check if hash belongs to this scheme, returns True/False

_classmethod_ `hash`( _secret_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.hash "Permalink to this definition")

Hash secret, returning result.
Should handle generating salt, etc, and should return string
containing identifier, salt & other configuration, as well as digest.

| Parameters: | - **\\\*\\\*settings\_kwds** – <br>  Pass in settings to customize configuration of resulting hash.<br>  <br>  <br>  <br>  Deprecated since version 1.7: Starting with Passlib 1.7, callers should no longer pass settings keywords<br>  (e.g. `rounds` or `salt` directly to `hash()`); should use<br>  `.using(**settings).hash(secret)` construction instead.<br>  <br>  <br>  <br>  Support will be removed in Passlib 2.0.<br>  <br>- **\\\*\\\*context\_kwds** – Specific algorithms may require context-specific information (such as the user login). |

_classmethod_ `verify`( _secret_, _hash_, _\*\*context_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler.verify "Permalink to this definition")

verify secret against hash, returns True/False

### GenericHandler Mixins [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#generichandler-mixins "Permalink to this headline")

_class_ `passlib.utils.handlers.` `HasSalt`( _salt=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt "Permalink to this definition")

mixin for validating salts.

This [`GenericHandler`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler "passlib.utils.handlers.GenericHandler") mixin adds a `salt` keyword to the class constuctor;
any value provided is passed through the [`_norm_salt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt._norm_salt "passlib.utils.handlers.HasSalt._norm_salt") method,
which takes care of validating salt length and content,
as well as generating new salts if one it not provided.

| Parameters: | - **salt** – optional salt string<br>- **salt\_size** – optional size of salt (only used if no salt provided);<br>  defaults to [`default_salt_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.default_salt_size "passlib.utils.handlers.HasSalt.default_salt_size"). |

#### Class Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasSalt-class-attributes "Permalink to this headline")

In order for `_norm_salt()` to do its job, the following
attributes should be provided by the handler subclass:

`min_salt_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.min_salt_size "Permalink to this definition")

The minimum number of characters allowed in a salt string.
An [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") will be throw if the provided salt is too small.
Defaults to `0`.

`max_salt_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.max_salt_size "Permalink to this definition")

The maximum number of characters allowed in a salt string.
By default an [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") will be throw if the provided salt is
too large; but if `relaxed=True`, it will be clipped and a warning
issued instead. Defaults to `None`, for no maximum.

`default_salt_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.default_salt_size "Permalink to this definition")

\[required\]
If no salt is provided, this should specify the size of the salt
that will be generated by [`_generate_salt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt._generate_salt "passlib.utils.handlers.HasSalt._generate_salt"). By default
this will fall back to [`max_salt_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.max_salt_size "passlib.utils.handlers.HasSalt.max_salt_size").

`salt_chars` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.salt_chars "Permalink to this definition")

A string containing all the characters which are allowed in the salt
string. An [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") will be throw if any other characters
are encountered. May be set to `None` to skip this check (but see
in [`default_salt_chars`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.default_salt_chars "passlib.utils.handlers.HasSalt.default_salt_chars")).

`default_salt_chars` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.default_salt_chars "Permalink to this definition")

\[required\]
This attribute controls the set of characters use to generate
_new_ salt strings. By default, it mirrors [`salt_chars`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.salt_chars "passlib.utils.handlers.HasSalt.salt_chars").
If `salt_chars` is `None`, this attribute must be specified
in order to generate new salts. Aside from that purpose,
the main use of this attribute is for hashes which wish to generate
salts from a restricted subset of `salt_chars`; such as
accepting all characters, but only using a-z.

#### Instance Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasSalt-instance-attributes "Permalink to this headline")

`salt` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.salt "Permalink to this definition")

This instance attribute will be filled in with the salt provided
to the constructor (as adapted by [`_norm_salt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt._norm_salt "passlib.utils.handlers.HasSalt._norm_salt"))

#### Subclassable Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasSalt-subclassable-methods "Permalink to this headline")

_classmethod_ `_norm_salt`( _salt_, _relaxed=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt._norm_salt "Permalink to this definition")

helper to normalize & validate user-provided salt string

| Parameters: | **salt** – salt string |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – If salt not correct type.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>  - if salt contains chars that aren’t in [`salt_chars`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.salt_chars "passlib.utils.handlers.HasSalt.salt_chars").<br>  - if salt contains less than [`min_salt_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.min_salt_size "passlib.utils.handlers.HasSalt.min_salt_size") characters.<br>  - if `relaxed=False` and salt has more than [`max_salt_size`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt.max_salt_size "passlib.utils.handlers.HasSalt.max_salt_size")<br>    characters (if `relaxed=True`, the salt is truncated<br>    and a warning is issued instead). |
| Returns: | normalized salt |

_classmethod_ `_generate_salt`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasSalt._generate_salt "Permalink to this definition")

helper method for \_init\_salt(); generates a new random salt string.

_class_ `passlib.utils.handlers.` `HasRounds`( _rounds=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds "Permalink to this definition")

mixin for validating rounds parameter

This [`GenericHandler`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.GenericHandler "passlib.utils.handlers.GenericHandler") mixin adds a `rounds` keyword to the class
constuctor; any value provided is passed through the [`_norm_rounds()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds._norm_rounds "passlib.utils.handlers.HasRounds._norm_rounds")
method, which takes care of validating the number of rounds.

| Parameters: | **rounds** – optional number of rounds hash should use |

#### Class Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasRounds-class-attributes "Permalink to this headline")

In order for `_norm_rounds()` to do its job, the following
attributes must be provided by the handler subclass:

`min_rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.min_rounds "Permalink to this definition")

The minimum number of rounds allowed. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") will be
thrown if the rounds value is too small. Defaults to `0`.

`max_rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.max_rounds "Permalink to this definition")

The maximum number of rounds allowed. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") will be
thrown if the rounds value is larger than this. Defaults to `None`
which indicates no limit to the rounds value.

`default_rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.default_rounds "Permalink to this definition")

If no rounds value is provided to constructor, this value will be used.
If this is not specified, a rounds value _must_ be specified by the
application.

`rounds_cost` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.rounds_cost "Permalink to this definition")

\[required\]
The `rounds` parameter typically encodes a cpu-time cost
for calculating a hash. This should be set to `"linear"`
(the default) or `"log2"`, depending on how the rounds value relates
to the actual amount of time that will be required.

#### Class Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasRounds-class-methods "Permalink to this headline")

Todo

document using() and needs\_update() options

#### Instance Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasRounds-instance-attributes "Permalink to this headline")

`rounds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.rounds "Permalink to this definition")

This instance attribute will be filled in with the rounds value provided
to the constructor (as adapted by [`_norm_rounds()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds._norm_rounds "passlib.utils.handlers.HasRounds._norm_rounds"))

#### Subclassable Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasRounds-subclassable-methods "Permalink to this headline")

_classmethod_ `_norm_rounds`( _rounds_, _relaxed=False_, _param='rounds'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds._norm_rounds "Permalink to this definition")

helper for normalizing rounds value.

| Parameters: | - **rounds** – an integer cost parameter.<br>- **relaxed** – if `True` (the default), issues PasslibHashWarning is rounds are outside allowed range.<br>  if `False`, raises a ValueError instead.<br>- **param** – optional name of parameter to insert into error/warning messages. |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – <br>  - if `use_defaults=False` and no rounds is specified<br>  - if rounds is not an integer.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>  - if rounds is `None` and class does not specify a value for<br>    [`default_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.default_rounds "passlib.utils.handlers.HasRounds.default_rounds").<br>  - if `relaxed=False` and rounds is outside bounds of<br>    [`min_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.min_rounds "passlib.utils.handlers.HasRounds.min_rounds") and [`max_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRounds.max_rounds "passlib.utils.handlers.HasRounds.max_rounds") (if `relaxed=True`,<br>    the rounds value will be clamped, and a warning issued). |
| Returns: | normalized rounds value |

_class_ `passlib.utils.handlers.` `HasManyIdents`( _ident=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasManyIdents "Permalink to this definition")

mixin for hashes which use multiple prefix identifiers

For the hashes which may use multiple identifier prefixes,
this mixin adds an `ident` keyword to constructor.
Any value provided is passed through the `norm_idents()` method,
which takes care of validating the identifier,
as well as allowing aliases for easier specification
of the identifiers by the user.

Todo

document this class’s usage

#### Class Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasManyIdents-class-methods "Permalink to this headline")

Todo

document using() and needs\_update() options

_class_ `passlib.utils.handlers.` `HasManyBackends`( _checksum=None_, _use\_defaults=False_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasManyBackends "Permalink to this definition")

GenericHandler mixin which provides selecting from multiple backends.

Todo

finish documenting this class’s usage

For hashes which need to select from multiple backends,
depending on the host environment, this class
offers a way to specify alternate `_calc_checksum()` methods,
and will dynamically chose the best one at runtime.

Changed in version 1.7: This class now derives from `BackendMixin`, which abstracts
out a more generic framework for supporting multiple backends.
The public api ( `get_backend()`, `has_backend()`, `set_backend()`)
is roughly the same.

#### Private API (Subclass Hooks) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#passlib.utils.handlers.HasManyBackends-private-api-subclass-hooks "Permalink to this headline")

As of version 1.7, classes should implement `_load_backend_{name}()`, per
`BackendMixin`. This hook should invoke `_set_calc_checksum_backcend()`
to install it’s backend method.

Deprecated since version 1.7: The following api is deprecated, and will be removed in Passlib 2.0:

`_has_backend_{name}`

private class attribute checked by `has_backend()` to see if a
specific backend is available, it should be either `True`
or `False`. One of these should be provided by
the subclass for each backend listed in `backends`.

`_calc_checksum_{name}`

private class method that should implement `_calc_checksum()`
for a given backend. it will only be called if the backend has
been selected by `set_backend()`. One of these should be provided
by the subclass for each backend listed in `backends`.

_class_ `passlib.utils.handlers.` `HasRawSalt`( _salt=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRawSalt "Permalink to this definition")

mixin for classes which use decoded salt parameter

A variant of `HasSalt` which takes in decoded bytes instead of an encoded string.

Todo

document this class’s usage

_class_ `passlib.utils.handlers.` `HasRawChecksum`( _checksum=None_, _use\_defaults=False_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.HasRawChecksum "Permalink to this definition")

mixin for classes which work with decoded checksum bytes

Todo

document this class’s usage

### Examples [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#examples "Permalink to this headline")

Todo

Show some walk-through examples of how to use GenericHandler and its mixins

## The StaticHandler class [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#the-statichandler-class "Permalink to this headline")

_class_ `passlib.utils.handlers.` `StaticHandler`( _checksum=None_, _use\_defaults=False_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.StaticHandler "Permalink to this definition")

GenericHandler mixin for classes which have no settings.

This mixin assumes the entirety of the hash ise stored in the
`checksum` attribute; that the hash has no rounds, salt,
etc. This class provides the following:

- a default `genconfig()` that always returns None.
- a default `from_string()` and `to_string()`
that store the entire hash within `checksum`,
after optionally stripping a constant prefix.

All that is required by subclasses is an implementation of
the `_calc_checksum()` method.

Todo

Show some examples of how to use StaticHandler

## Other Constructors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#other-constructors "Permalink to this headline")

_class_ `passlib.utils.handlers.` `PrefixWrapper`( _name_, _wrapped_, _prefix=''_, _orig\_prefix=''_, _lazy=False_, _doc=None_, _ident=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.utils.handlers.PrefixWrapper "Permalink to this definition")

wraps another handler, adding a constant prefix.

instances of this class wrap another password hash handler,
altering the constant prefix that’s prepended to the wrapped
handlers’ hashes.

this is used mainly by the [ldap crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html) handlers;
such as [`ldap_md5_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html#passlib.hash.ldap_md5_crypt "passlib.hash.ldap_md5_crypt") which wraps [`md5_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html#passlib.hash.md5_crypt "passlib.hash.md5_crypt") and adds a `{CRYPT}` prefix.

usage:

```
myhandler = PrefixWrapper("myhandler", "md5_crypt", prefix="$mh$", orig_prefix="$1$")

```

| Parameters: | - **name** – name to assign to handler<br>- **wrapped** – handler object or name of registered handler<br>- **prefix** – identifying prefix to prepend to all hashes<br>- **orig\_prefix** – prefix to strip (defaults to ‘’).<br>- **lazy** – if True and wrapped handler is specified by name, don’t look it up until needed. |

## Testing Hash Handlers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#testing-hash-handlers "Permalink to this headline")

Within its unittests, Passlib provides the [`HandlerCase`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.tests.utils.HandlerCase "passlib.tests.utils.HandlerCase") class,
which can be subclassed to provide a unittest-compatible test class capable of
checking if a handler adheres to the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

### Usage [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#id2 "Permalink to this headline")

As an example of how to use `HandlerCase`,
the following is an annotated version
of the unittest for [`passlib.hash.des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt"):

```
from passlib.hash import des_crypt
from passlib.tests.utils import HandlerCase

# create a subclass for the handler...
class DesCryptTest(HandlerCase):
    "test des-crypt algorithm"

    # [required] - store the handler object itself in the handler attribute
    handler = des_crypt

    # [required] - this should be a list of (password, hash) pairs,
    #              which should all verify correctly using your handler.
    #              it is recommend include pairs which test all of the following:
    #
    #              * empty string & short strings for passwords
    #              * passwords with 2 byte unicode characters
    #              * hashes with varying salts, rounds, and other options
    known_correct_hashes = (
        # format: (password, hash)
        ('', 'OgAwTx2l6NADI'),
        (' ', '/Hk.VPuwQTXbc'),
        ('test', 'N1tQbOFcM5fpg'),
        ('Compl3X AlphaNu3meric', 'um.Wguz3eVCx2'),
        ('4lpHa N|_|M3r1K W/ Cur5Es: #$%(*)(*%#', 'sNYqfOyauIyic'),
        ('AlOtBsOl', 'cEpWz5IUCShqM'),
        (u'hell\u00D6', 'saykDgk3BPZ9E'),
        )

    # [optional] - if there are hashes which are similar in format
    #              to your handler, and you want to make sure :meth:`identify`
    #              does not return ``True`` for such hashes,
    #              list them here. otherwise this can be omitted.
    #
    known_unidentified_hashes = [\
        # bad char in otherwise correctly formatted hash\
        '!gAwTx2l6NADI',\
        ]

```

### Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html\#id3 "Permalink to this headline")

_class_ `passlib.tests.utils.` `HandlerCase` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#passlib.tests.utils.HandlerCase "Permalink to this definition")

base class for testing password hash handlers (esp passlib.utils.handlers subclasses)

In order to use this to test a handler,
create a subclass will all the appropriate attributes
filled as listed in the example below,
and run the subclass via unittest.

Todo

Document all of the options HandlerCase offers.

Note

This is subclass of [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.9)")
(or `unittest2.TestCase` if available).

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
      - [`passlib.utils.handlers` \- Framework for writing password hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#)
        - [Implementing Custom Handlers](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#implementing-custom-handlers)
        - [The GenericHandler Class](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#the-generichandler-class)
          - [Design](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#design)
          - [Usage](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#usage)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#interface)
          - [GenericHandler Mixins](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#generichandler-mixins)
          - [Examples](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#examples)
        - [The StaticHandler class](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#the-statichandler-class)
        - [Other Constructors](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#other-constructors)
        - [Testing Hash Handlers](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#testing-hash-handlers)
          - [Usage](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#id2)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html#id3)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html "passlib.utils.binary - Binary Helper Functions")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html "passlib.utils - Helper Functions")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.utils.handlers.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.handlers.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.utils.handlers.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)