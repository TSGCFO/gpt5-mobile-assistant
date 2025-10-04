<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.context.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html "passlib.crypto - Cryptographic Helper Functions")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html "passlib.apps - Helpers for various applications")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.context`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#module-passlib.context "passlib.context: CryptContext class, for managing multiple password hash schemes") \- CryptContext Hash Manager [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#passlib-context-cryptcontext-hash-manager "Permalink to this headline")

This page provides a complete reference of all the methods
and options supported by the `CryptContext` class
and helper utilities.

See also

- [CryptContext Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial) –
overview of this class and walkthrough of how to use it.

## The CryptContext Class [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#the-cryptcontext-class "Permalink to this headline")

_class_ `passlib.context.` `CryptContext`( _schemes=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "Permalink to this definition")

Helper for hashing passwords using different algorithms.

At its base, this is a proxy object that makes it easy to use
multiple [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") objects at the same time.
Instances of this class can be created by calling the constructor
with the appropriate keywords, or by using one of the alternate
constructors, which can load directly from a string or a local file.
Since this class has so many options and methods, they have been broken
out into subsections:

- [Constructor Keywords](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#constructor-keywords) – all the keywords this class accepts.

- [Context Options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#id1) – options affecting the Context itself.
- [Algorithm Options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#algorithm-options) – options controlling the wrapped hashes.

- [Primary Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#primary-methods) – the primary methods most applications need.
- [Hash Migration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#hash-migration) – methods for automatically replacing deprecated hashes.
- [Alternate Constructors](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#alternate-constructors) – creating instances from strings or files.
- [Changing the Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#changing-the-configuration) – altering the configuration of an existing context.
- [Examining the Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#examining-the-configuration) – programmatically examining the context’s settings.
- [Saving the Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#saving-the-configuration) – exporting the context’s current configuration.
- [Configuration Errors](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#configuration-errors) – overview of errors that may be thrown by `CryptContext` constructor

### Constructor Keywords [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#constructor-keywords "Permalink to this headline")

The [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") class accepts the following keywords,
all of which are optional.
The keywords are divided into two categories: [context options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#id1), which affect
the CryptContext itself; and [algorithm options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#algorithm-options), which place defaults
and limits on the algorithms used by the CryptContext.

#### Context Options [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#context-options "Permalink to this headline")

Options which directly affect the behavior of the CryptContext instance:

`schemes`

List of algorithms which the instance should support.

The most important option in the constructor,
This option controls what hashes can be used
by the [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash") method,
which hashes will be recognized by [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify "passlib.context.CryptContext.verify")
and [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.identify "passlib.context.CryptContext.identify"), and other effects
throughout the instance.
It should be a sequence of names,
drawn from the hashes in [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib").
Listing an unknown name will cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)").
You can use the [`schemes()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "passlib.context.CryptContext.schemes") method
to get a list of the currently configured algorithms.
As an example, the following creates a CryptContext instance
which supports the [`sha256_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html#passlib.hash.sha256_crypt "passlib.hash.sha256_crypt") and
[`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt") schemes:

```
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes=["sha256_crypt", "des_crypt"])
>>> myctx.schemes()
("sha256_crypt", "des_crypt")

```

Note

The order of the schemes is sometimes important,
as [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.identify "passlib.context.CryptContext.identify") will run
through the schemes from first to last until an algorithm
“claims” the hash. So plaintext algorithms and
the like should be listed at the end.

See also

the [Basic Usage](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-basic-example) example in the tutorial.

`default`

Specifies the name of the default scheme.

This option controls which of the configured
schemes will be used as the default when creating
new hashes. This parameter is optional; if omitted,
the first non-deprecated algorithm in `schemes` will be used.
You can use the [`default_scheme()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.default_scheme "passlib.context.CryptContext.default_scheme") method
to retrieve the name of the current default scheme.
As an example, the following demonstrates the effect
of this parameter on the [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash")
method:

```
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

>>> # hash() uses the first scheme
>>> myctx.default_scheme()
'sha256_crypt'
>>> myctx.hash("password")
'$5$rounds=80000$R5ZIZRTNPgbdcWq5$fT/Oeqq/apMa/0fbx8YheYWS6Z3XLTxCzEtutsk2cJ1'

>>> # but setting default causes the second scheme to be used.
>>> myctx.update(default="md5_crypt")
>>> myctx.default_scheme()
'md5_crypt'
>>> myctx.hash("password")
'$1$Rr0C.KI8$Kvciy8pqfL9BQ2CJzEzfZ/'

```

See also

the [Basic Usage](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-basic-example) example in the tutorial.

`deprecated`

List of algorithms which should be considered “deprecated”.

This has the same format as `schemes`, and should be
a subset of those algorithms. The main purpose of this
method is to flag schemes which need to be rehashed
when the user next logs in. This has no effect
on the [Primary Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#primary-methods); but if the special [Hash Migration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#hash-migration)
methods are passed a hash belonging to a deprecated scheme,
they will flag it as needed to be rehashed using
the `default` scheme.

This may also contain a single special value,
`["auto"]`, which will configure the CryptContext instance
to deprecate _all_ supported schemes except for the default scheme.

New in version 1.6: Added support for the `["auto"]` value.

See also

[Deprecation & Hash Migration](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-migration-example) in the tutorial

`truncate_error`

> By default, some algorithms will truncate large passwords
> (e.g. [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt") truncates ones larger than 72 bytes).
> Such hashes accept a `truncate_error=True` option to make them
> raise a [`PasswordTruncateError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordTruncateError "passlib.exc.PasswordTruncateError") instead.
>
> This can also be set at the CryptContext level,
> and will passed to all hashes that support it.
>
> New in version 1.7.

`min_verify_time`

> If specified, unsuccessful [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify "passlib.context.CryptContext.verify")
> calls will be penalized, and take at least this may
> seconds before the method returns. May be an integer
> or fractional number of seconds.
>
> Deprecated since version 1.6: This option has not proved very useful, is ignored by 1.7,
> and will be removed in version 1.8.
>
> Changed in version 1.7: Per deprecation roadmap above, this option is now ignored.

`harden_verify`

> Companion to `min_verify_time`, currently ignored.
>
> New in version 1.7.
>
> Deprecated since version 1.7.1: This option is ignored by 1.7.1, and will be removed in 1.8
> along with `min_verify_time`.

#### Algorithm Options [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#algorithm-options "Permalink to this headline")

All of the other options that can be passed to a [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext")
constructor affect individual hash algorithms.
All of the following keys have the form `scheme__key`,
where `scheme` is the name of one of the algorithms listed
in `schemes`, and `option` one of the parameters below:

`scheme__rounds`

> Set the number of rounds required for this scheme
> when generating new hashes (using [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash")).
> Existing hashes which have a different number of rounds will be marked
> as deprecated.
>
> This essentially sets `default_rounds`, `min_rounds`, and `max_rounds` all at once.
> If any of those options are also specified, they will override the value specified
> by `rounds`.
>
> New in version 1.7: Previous releases of Passlib treated this as an alias for `default_rounds`.

`scheme__default_rounds`

> Sets the default number of rounds to use with this scheme
> when generating new hashes (using [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash")).
>
> If not set, this will fall back to the an algorithm-specific
> [`default_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.default_rounds "passlib.ifc.PasswordHash.default_rounds").
> For hashes which do not support a rounds parameter, this option is ignored.
> As an example:
>
> ```
> >>> from passlib.context import CryptContext
>
> >>> # no explicit default_rounds set, so hash() uses sha256_crypt's default (80000)
> >>> myctx = CryptContext(["sha256_crypt"])
> >>> myctx.hash("fooey")
> '$5$rounds=80000$60Y7mpmAhUv6RDvj$AdseAOq6bKUZRDRTr/2QK1t38qm3P6sYeXhXKnBAmg0'
>            ^^^^^
>
> >>> # but if a default is specified, it will be used instead.
> >>> myctx = CryptContext(["sha256_crypt"], sha256_crypt__default_rounds=77123)
> >>> myctx.hash("fooey")
> '$5$rounds=77123$60Y7mpmAhUv6RDvj$AdseAOq6bKUZRDRTr/2QK1t38qm3P6sYeXhXKnBAmg0'
>            ^^^^^
>
> ```
>
> See also
>
> the [Using Default Settings](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-default-settings-example) example in the tutorial.

`scheme__vary_rounds`

> Deprecated since version 1.7: This option has been deprecated as of Passlib 1.7, and will be removed in Passlib 2.0.
> The (very minimal) security benefit it provides was judged to not be worth code complexity
> it requires.
>
> Instead of using a fixed rounds value (such as specified by
> `default_rounds`, above); this option will cause each call
> to [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash") to vary the default rounds value
> by some amount.
>
> This can be an integer value, in which case each call will use a rounds
> value within the range `default_rounds +/- vary_rounds`. It may
> also be a floating point value within the range 0.0 .. 1.0,
> in which case the range will be calculated as a proportion of the
> current default rounds ( `default_rounds +/- default_rounds*vary_rounds`).
> A typical setting is `0.1` to `0.2`.
>
> As an example of how this parameter operates:
>
> ```
> >>> # without vary_rounds set, hash() uses the same amount each time:
> >>> from passlib.context import CryptContext
> >>> myctx = CryptContext(schemes=["sha256_crypt"],
> ...                      sha256_crypt__default_rounds=80000)
> >>> myctx.hash("fooey")
> '$5$rounds=80000$60Y7mpmAhUv6RDvj$AdseAOq6bKUZRDRTr/2QK1t38qm3P6sYeXhXKnBAmg0'
> >>> myctx.hash("fooey")
> '$5$rounds=80000$60Y7mpmAhUv6RDvj$AdseAOq6bKUZRDRTr/2QK1t38qm3P6sYeXhXKnBAmg0'
>            ^^^^^
>
> >>> # but if vary_rounds is set, each one will be randomized
> >>> # (in this case, within the range 72000 .. 88000)
> >>> myctx = CryptContext(schemes=["sha256_crypt"],
> ...                      sha256_crypt__default_rounds=80000,
> ...                      sha256_crypt__vary_rounds=0.1)
> >>> myctx.hash("fooey")
> '$5$rounds=83966$bMpgQxN2hXo2kVr4$jL4Q3ov41UPgSbO7jYL0PdtsOg5koo4mCa.UEF3zan.'
> >>> myctx.hash("fooey")
> '$5$rounds=72109$43BBHC/hYPHzL69c$VYvVIdKn3Zdnvu0oJHVlo6rr0WjiMTGmlrZrrH.GxnA'
>            ^^^^^
>
> ```
>
> Note
>
> This is not a _needed_ security measure, but it lets some of the less-significant
> digits of the rounds value act as extra salt bits; and helps foil
> any attacks targeted at a specific number of rounds of a hash.

`scheme__min_rounds`,
`scheme__max_rounds`

> These options place a limit on the number of rounds allowed for a particular
> scheme.
>
> For one, they limit what values are allowed for `default_rounds`,
> and clip the effective range of the `vary_rounds` parameter.
> More importantly though, they proscribe a minimum strength for the hash,
> and any hashes which don’t have sufficient rounds will be flagged as
> needing rehashing by the [Hash Migration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#hash-migration) methods.
>
> Note
>
> These are configurable per-context limits.
> A warning will be issued if they exceed any hard limits
> set by the algorithm itself.
>
> See also
>
> the [Settings Rounds Limitations](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-min-rounds-example) example in the tutorial.

`scheme__other-option`

> Finally, any other options are assumed to correspond to one of the
> that algorithm’s `hash()` `settings`,
> such as setting a `salt_size`.
>
> See also
>
> the [Using Default Settings](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-default-settings-example) example in the tutorial.

#### Global Algorithm Options [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#global-algorithm-options "Permalink to this headline")

`all__option`

> The special scheme `all` permits you to set an option, and have
> it act as a global default for all the algorithms in the context.
> For instance, `all__vary_rounds=0.1` would set the `vary_rounds`
> option for all the schemes where it was not overridden with an
> explicit `scheme__vary_rounds` option.
>
> Deprecated since version 1.7: This special scheme is deprecated as of Passlib 1.7, and will be removed in Passlib 2.0.
> It’s only legitimate use was for `vary_rounds`, which is also being removed in Passlib 2.0.

#### User Categories [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#user-categories "Permalink to this headline")

`category__context__option`,
`category__scheme__option`

> Passing keys with this format to the [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") constructor
> allows you to specify conditional context and algorithm options,
> controlled by the `category` parameter supported by most CryptContext
> methods.
>
> These options are conditional because they only take effect if
> the `category` prefix of the option matches the value of the `category`
> parameter of the CryptContext method being invoked. In that case,
> they override any options specified without a category
> prefix (e.g. admin\_\_sha256\_crypt\_\_min\_rounds would override
> sha256\_crypt\_\_min\_rounds).
> The category prefix and the value passed into the `category` parameter
> can be any string the application wishes to use, the only constraint
> is that `None` indicates the default category.

_Motivation:_
Policy limits such as default rounds values and deprecated schemes
generally have to be set globally. However, it’s frequently desirable
to specify stronger options for certain accounts (such as admin accounts),
choosing to sacrifice longer hashing time for a more secure password.
The user categories system allows for this.
For example, a CryptContext could be set up as follows:

```
>>> # A context object can be set up as follows:
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes=["sha256_crypt"],
...                      sha256_crypt__default_rounds=77000,
...                      staff__sha256_crypt__default_rounds=88000)

>>> # In this case, calling hash() with ``category=None`` would result
>>> # in a hash that used 77000 sha256-crypt rounds:
>>> myctx.hash("password", category=None)
'$5$rounds=77000$sj3XI0AbKlEydAKt$BhFvyh4.IoxaUeNlW6rvQ.O0w8BtgLQMYorkCOMzf84'
           ^^^^^

>>> # But if the application passed in ``category="staff"`` when an administrative
>>> # account set their password, 88000 rounds would be used:
>>> myctx.hash("password", category="staff")
'$5$rounds=88000$w7XIdKfTI9.YLwmA$MIzGvs6NU1QOQuuDHhICLmDsdW/t94Bbdfxdh/6NJl7'
           ^^^^^

```

### Primary Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#primary-methods "Permalink to this headline")

The main interface to the CryptContext object deliberately mirrors
the [PasswordHash](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api) interface, since its central
purpose is to act as a container for multiple password hashes.
Most applications will only need to make use two methods in a CryptContext
instance:

`CryptContext.` `hash`( _secret_, _scheme=None_, _category=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "Permalink to this definition")

run secret through selected algorithm, returning resulting hash.

| Parameters: | - **secret** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – the password to hash.<br>- **scheme** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – <br>  Optional scheme to use. Scheme must be one of the ones<br>  configured for this context (see the<br>  [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) option).<br>  If no scheme is specified, the configured default<br>  will be used.<br>  <br>  <br>  <br>  Deprecated since version 1.7: Support for this keyword is deprecated, and will be removed in Passlib 2.0.<br>  <br>- **category** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – Optional [user category](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories).<br>  If specified, this will cause any category-specific defaults to<br>  be used when hashing the password (e.g. different default scheme,<br>  different default rounds values, etc).<br>- **\*\*kwds** – All other keyword options are passed to the selected algorithm’s<br>  [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") method. |
| Returns: | The secret as encoded by the specified algorithm and options.<br>The return value will always be a `str`. |
| Raises: | [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") **,** [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>- If any of the arguments have an invalid type or value.<br>  This includes any keywords passed to the underlying hash’s<br>  [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") method. |

See also

the [Basic Usage](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-basic-example) example in the tutorial

`CryptContext.` `encrypt`( _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.encrypt "Permalink to this definition")

Legacy alias for [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash").

Deprecated since version 1.7: This method was renamed to `hash()` in version 1.7.
This alias will be removed in version 2.0, and should only
be used for compatibility with Passlib 1.3 - 1.6.

`CryptContext.` `verify`( _secret_, _hash_, _scheme=None_, _category=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify "Permalink to this definition")

verify secret against an existing hash.

If no scheme is specified, this will attempt to identify
the scheme based on the contents of the provided hash
(limited to the schemes configured for this context).
It will then check whether the password verifies against the hash.

| Parameters: | - **secret** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – the secret to verify<br>- **hash** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – <br>  hash string to compare to<br>  <br>  if `None` is passed in, this will be treated as “never verifying”<br>  <br>- **scheme** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Optionally force context to use specific scheme.<br>  This is usually not needed, as most hashes can be unambiguously<br>  identified. Scheme must be one of the ones configured<br>  for this context<br>  (see the [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) option).<br>  <br>  <br>  <br>  Deprecated since version 1.7: Support for this keyword is deprecated, and will be removed in Passlib 2.0.<br>  <br>- **category** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – Optional [user category](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories) string.<br>  This is mainly used when generating new hashes, it has little<br>  effect when verifying; this keyword is mainly provided for symmetry.<br>- **\*\*kwds** – All additional keywords are passed to the appropriate handler,<br>  and should match its [`context_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "passlib.ifc.PasswordHash.context_kwds"). |
| Returns: | `True` if the password matched the hash, else `False`. |
| Raises: | - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>  - if the hash did not match any of the configured [`schemes()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "passlib.context.CryptContext.schemes").<br>  - if any of the arguments have an invalid value (this includes<br>    any keywords passed to the underlying hash’s<br>    [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") method).<br>- [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – <br>  - if any of the arguments have an invalid type (this includes<br>    any keywords passed to the underlying hash’s<br>    [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") method). |

See also

the [Basic Usage](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-basic-example) example in the tutorial

`CryptContext.` `identify`( _hash_, _category=None_, _resolve=False_, _required=False_, _unconfigured=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.identify "Permalink to this definition")

Attempt to identify which algorithm the hash belongs to.

Note that this will only consider the algorithms
currently configured for this context
(see the [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) option).
All registered algorithms will be checked, from first to last,
and whichever one positively identifies the hash first will be returned.

| Parameters: | - **hash** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – The hash string to test.<br>- **category** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – Optional [user category](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories).<br>  Ignored by this function, this parameter<br>  is provided for symmetry with the other methods.<br>- **resolve** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – If `True`, returns the hash handler itself,<br>  instead of the name of the hash.<br>- **required** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – If `True`, this will raise a ValueError if the hash<br>  cannot be identified, instead of returning `None`. |
| Returns: | The handler which first identifies the hash,<br>or `None` if none of the algorithms identify the hash. |

`CryptContext.` `dummy_verify`( _elapsed=0_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.dummy_verify "Permalink to this definition")

Helper that applications can call when user wasn’t found,
in order to simulate time it would take to hash a password.

Runs verify() against a dummy hash, to simulate verification
of a real account password.

| Parameters: | **elapsed** – <br>Deprecated since version 1.7.1: this option is ignored, and will be removed in passlib 1.8. |

New in version 1.7.

#### “crypt”-style methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#crypt-style-methods "Permalink to this headline")

Additionally, the main interface offers wrappers for the two Unix “crypt”
style methods provided by all the [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") objects:

`CryptContext.` `genhash`( _secret_, _config_, _scheme=None_, _category=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.genhash "Permalink to this definition")

Generate hash for the specified secret using another hash.

Deprecated since version 1.7: This method will be removed in version 2.0, and should only
be used for compatibility with Passlib 1.3 - 1.6.

`CryptContext.` `genconfig`( _scheme=None_, _category=None_, _\*\*settings_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.genconfig "Permalink to this definition")

Generate a config string for specified scheme.

Deprecated since version 1.7: This method will be removed in version 2.0, and should only
be used for compatibility with Passlib 1.3 - 1.6.

### Hash Migration [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#hash-migration "Permalink to this headline")

Applications which want to detect and regenerate deprecated
hashes will want to use one of the following methods:

`CryptContext.` `verify_and_update`( _secret_, _hash_, _scheme=None_, _category=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify_and_update "Permalink to this definition")

verify password and re-hash the password if needed, all in a single call.

This is a convenience method which takes care of all the following:
first it verifies the password ( [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify "passlib.context.CryptContext.verify")), if this is successfull
it checks if the hash needs updating ( [`needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.needs_update "passlib.context.CryptContext.needs_update")), and if so,
re-hashes the password ( [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash")), returning the replacement hash.
This series of steps is a very common task for applications
which wish to update deprecated hashes, and this call takes
care of all 3 steps efficiently.

| Parameters: | - **secret** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – the secret to verify<br>- **hash** – <br>  hash string to compare to.<br>  <br>  if `None` is passed in, this will be treated as “never verifying”<br>  <br>- **scheme** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Optionally force context to use specific scheme.<br>  This is usually not needed, as most hashes can be unambiguously<br>  identified. Scheme must be one of the ones configured<br>  for this context<br>  (see the [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) option).<br>  <br>  <br>  <br>  Deprecated since version 1.7: Support for this keyword is deprecated, and will be removed in Passlib 2.0.<br>  <br>- **category** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – Optional [user category](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories).<br>  If specified, this will cause any category-specific defaults to<br>  be used if the password has to be re-hashed.<br>- **\*\*kwds** – all additional keywords are passed to the appropriate handler,<br>  and should match that hash’s<br>  [`PasswordHash.context_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "passlib.ifc.PasswordHash.context_kwds"). |
| Returns: | This function returns a tuple containing two elements:<br>`(verified, replacement_hash)`. The first is a boolean<br>flag indicating whether the password verified,<br>and the second an optional replacement hash.<br>The tuple will always match one of the following 3 cases:<br>- `(False, None)` indicates the secret failed to verify.<br>- `(True, None)` indicates the secret verified correctly,<br>  and the hash does not need updating.<br>- `(True, str)` indicates the secret verified correctly,<br>  but the current hash needs to be updated. The `str`<br>  will be the freshly generated hash, to replace the old one. |
| Raises: | [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") **,** [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – For the same reasons as [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify "passlib.context.CryptContext.verify"). |

See also

the [Deprecation & Hash Migration](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-migration-example) example in the tutorial.

`CryptContext.` `needs_update`( _hash_, _scheme=None_, _category=None_, _secret=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.needs_update "Permalink to this definition")

Check if hash needs to be replaced for some reason,
in which case the secret should be re-hashed.

This function is the core of CryptContext’s support for hash migration:
This function takes in a hash string, and checks the scheme,
number of rounds, and other properties against the current policy.
It returns `True` if the hash is using a deprecated scheme,
or is otherwise outside of the bounds specified by the policy
(e.g. the number of rounds is lower than [min\_rounds](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-min-rounds-option)
configuration for that algorithm).
If so, the password should be re-hashed using [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash")
Otherwise, it will return `False`.

| Parameters: | - **hash** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – The hash string to examine.<br>- **scheme** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – <br>  Optional scheme to use. Scheme must be one of the ones<br>  configured for this context (see the<br>  [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) option).<br>  If no scheme is specified, it will be identified<br>  based on the value of _hash_.<br>  <br>  <br>  <br>  Deprecated since version 1.7: Support for this keyword is deprecated, and will be removed in Passlib 2.0.<br>  <br>- **category** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – Optional [user category](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories).<br>  If specified, this will cause any category-specific defaults to<br>  be used when determining if the hash needs to be updated<br>  (e.g. is below the minimum rounds).<br>- **secret** ( _unicode_ _,_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)") _, or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – <br>  Optional secret associated with the provided `hash`.<br>  This is not required, or even currently used for anything…<br>  it’s for forward-compatibility with any future<br>  update checks that might need this information.<br>  If provided, Passlib assumes the secret has already been<br>  verified successfully against the hash.<br>  <br>  <br>  <br>  New in version 1.6. |
| Returns: | `True` if hash should be replaced, otherwise `False`. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – If the hash did not match any of the configured [`schemes()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "passlib.context.CryptContext.schemes"). |

New in version 1.6: This method was previously named [`hash_needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash_needs_update "passlib.context.CryptContext.hash_needs_update").

See also

the [Deprecation & Hash Migration](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-migration-example) example in the tutorial.

`CryptContext.` `hash_needs_update`( _hash_, _scheme=None_, _category=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash_needs_update "Permalink to this definition")

Legacy alias for [`needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.needs_update "passlib.context.CryptContext.needs_update").

Deprecated since version 1.6: This method was renamed to `needs_update()` in version 1.6.
This alias will be removed in version 2.0, and should only
be used for compatibility with Passlib 1.3 - 1.5.

### Disabled Hash Managment [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#disabled-hash-managment "Permalink to this headline")

New in version 1.7.

It’s frequently useful to disable a user’s ability to login by
replacing their password hash with a standin that’s guaranteed
to never verify, against _any_ password. CryptContext offers
some convenience methods for this through the following API.

`CryptContext.` `disable`( _hash=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.disable "Permalink to this definition")

return a string to disable logins for user,
usually by returning a non-verifying string such as `"!"`.

| Parameters: | **hash** – Callers can optionally provide the account’s existing hash.<br>Some disabled handlers (such as `unix_disabled`)<br>will encode this into the returned value,<br>so that it can be recovered via [`enable()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.enable "passlib.context.CryptContext.enable"). |
| Raises: | [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.9)") – if this function is called w/o a disabled hasher<br>(such as [`unix_disabled`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_disabled "passlib.hash.unix_disabled")) included<br>in the list of schemes. |
| Returns: | hash string which will be recognized as valid by the context,<br>but is guaranteed to not validate against _any_ password. |

`CryptContext.` `enable`( _hash_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.enable "Permalink to this definition")

inverse of [`disable()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.disable "passlib.context.CryptContext.disable") –
attempts to recover original hash which was converted
by a `disable()` call into a disabled hash –
thus restoring the user’s original password.

| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if original hash not present, or if the disabled handler doesn’t<br>support encoding the original hash (e.g. `django_disabled`) |
| Returns: | the original hash. |

`CryptContext.` `is_enabled`( _hash_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.is_enabled "Permalink to this definition")

test if hash represents a usuable password –
i.e. does not represent an unusuable password such as `"!"`,
which is recognized by the [`unix_disabled`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_disabled "passlib.hash.unix_disabled") hash.

| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if the hash is not recognized<br>(typically solved by adding `unix_disabled` to the list of schemes). |

### Alternate Constructors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#alternate-constructors "Permalink to this headline")

In addition to the main class constructor, which accepts a configuration
as a set of keywords, there are the following alternate constructors:

_classmethod_ `CryptContext.` `from_string`( _source_, _section='passlib'_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "Permalink to this definition")

create new CryptContext instance from an INI-formatted string.

| Parameters: | - **source** ( _unicode_ _or_ [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – string containing INI-formatted content.<br>- **section** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – option name of section to read from, defaults to `"passlib"`.<br>- **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – optional encoding used when source is bytes, defaults to `"utf-8"`. |
| Returns: | new [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instance, configured based on the<br>parameters in the _source_ string. |

Usage example:

```
>>> from passlib.context import CryptContext
>>> context = CryptContext.from_string('''
... [passlib]
... schemes = sha256_crypt, des_crypt
... sha256_crypt__default_rounds = 30000
... ''')

```

New in version 1.6.

See also

[`to_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_string "passlib.context.CryptContext.to_string"), the inverse of this constructor.

_classmethod_ `CryptContext.` `from_path`( _path_, _section='passlib'_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_path "Permalink to this definition")

create new CryptContext instance from an INI-formatted file.

this functions exactly the same as [`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string"),
except that it loads from a local file.

| Parameters: | - **path** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – path to local file containing INI-formatted config.<br>- **section** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – option name of section to read from, defaults to `"passlib"`.<br>- **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – encoding used to load file, defaults to `"utf-8"`. |
| Returns: | new CryptContext instance, configured based on the parameters<br>stored in the file _path_. |

New in version 1.6.

See also

[`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string") for an equivalent usage example.

`CryptContext.` `copy`( _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.copy "Permalink to this definition")

Return copy of existing CryptContext instance.

This function returns a new CryptContext instance whose configuration
is exactly the same as the original, with the exception that any keywords
passed in will take precedence over the original settings.
As an example:

```
>>> from passlib.context import CryptContext

>>> # given an existing context...
>>> ctx1 = CryptContext(["sha256_crypt", "md5_crypt"])

>>> # copy can be used to make a clone, and update
>>> # some of the settings at the same time...
>>> ctx2 = custom_app_context.copy(default="md5_crypt")

>>> # and the original will be unaffected by the change
>>> ctx1.default_scheme()
"sha256_crypt"
>>> ctx2.default_scheme()
"md5_crypt"

```

New in version 1.6: This method was previously named `replace()`. That alias
has been deprecated, and will be removed in Passlib 1.8.

See also

[`update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "passlib.context.CryptContext.update")

### Changing the Configuration [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#changing-the-configuration "Permalink to this headline")

[`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") objects can have their configuration replaced or updated
on the fly, and from a variety of sources (keywords, strings, files).
This is done through three methods:

`CryptContext.` `update`( _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "Permalink to this definition")

Helper for quickly changing configuration.

This acts much like the `dict.update()` method:
it updates the context’s configuration,
replacing the original value(s) for the specified keys,
and preserving the rest.
It accepts any [keyword](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-options)
accepted by the `CryptContext` constructor.

New in version 1.6.

See also

[`copy()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.copy "passlib.context.CryptContext.copy")

`CryptContext.` `load`( _source_, _update=False_, _section='passlib'_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "Permalink to this definition")

Load new configuration into CryptContext, replacing existing config.

| Parameters: | - **source** – <br>  source of new configuration to load.<br>  this value can be a number of different types:<br>  <br>  - a `dict` object, or compatible Mapping<br>    <br>    > the key/value pairs will be interpreted the same<br>    > keywords for the [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") class constructor.<br>    <br>  - a `unicode` or `bytes` string<br>    <br>    > this will be interpreted as an INI-formatted file,<br>    > and appropriate key/value pairs will be loaded from<br>    > the specified _section_.<br>    <br>  - another `CryptContext` object.<br>    <br>    > this will export a snapshot of its configuration<br>    > using [`to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict").<br>- **update** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – By default, [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load") will replace the existing configuration<br>  entirely. If `update=True`, it will preserve any existing<br>  configuration options that are not overridden by the new source,<br>  much like the [`update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "passlib.context.CryptContext.update") method.<br>- **section** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – When parsing an INI-formatted string, [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load") will look for<br>  a section named `"passlib"`. This option allows an alternate<br>  section name to be used. Ignored when loading from a dictionary.<br>- **encoding** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Encoding to use when **source** is bytes.<br>  Defaults to `"utf-8"`. Ignored when loading from a dictionary.<br>  <br>  <br>  <br>  Deprecated since version 1.8: This keyword, and support for bytes input, will be dropped in Passlib 2.0 |
| Raises: | - [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.9)") – <br>  - If the source cannot be identified.<br>  - If an unknown / malformed keyword is encountered.<br>- [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – If an invalid keyword value is encountered. |

Note

If an error occurs during a `load()` call, the `CryptContext`
instance will be restored to the configuration it was in before
the `load()` call was made; this is to ensure it is
_never_ left in an inconsistent state due to a load error.

New in version 1.6.

`CryptContext.` `load_path`( _path_, _update=False_, _section='passlib'_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load_path "Permalink to this definition")

Load new configuration into CryptContext from a local file.

This function is a wrapper for [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load") which
loads a configuration string from the local file _path_,
instead of an in-memory source. Its behavior and options
are otherwise identical to `load()` when provided with
an INI-formatted string.

New in version 1.6.

### Examining the Configuration [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#examining-the-configuration "Permalink to this headline")

The CryptContext object also supports basic inspection of its
current configuration:

`CryptContext.` `schemes`( _resolve=False_, _category=None_, _unconfigured=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "Permalink to this definition")

return schemes loaded into this CryptContext instance.

| Parameters: | **resolve** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – if `True`, will return a tuple of [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash")<br>objects instead of their names. |
| Returns: | returns tuple of the schemes configured for this context<br>via the _schemes_ option. |

New in version 1.6: This was previously available as `CryptContext().policy.schemes()`

See also

the [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) option for usage example.

`CryptContext.` `default_scheme`( _category=None_, _resolve=False_, _unconfigured=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.default_scheme "Permalink to this definition")

return name of scheme that [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash") will use by default.

| Parameters: | - **resolve** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – if `True`, will return a [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash")<br>  object instead of the name.<br>- **category** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)") _or_ [_None_](https://docs.python.org/3/library/constants.html#None "(in Python v3.9)")) – Optional [user category](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories).<br>  If specified, this will return the catgory-specific default scheme instead. |
| Returns: | name of the default scheme. |

See also

the [default](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-default-option) option for usage example.

New in version 1.6.

Changed in version 1.7: This now returns a hasher configured with any CryptContext-specific
options (custom rounds settings, etc). Previously this returned
the base hasher from [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib").

`CryptContext.` `handler`( _scheme=None_, _category=None_, _unconfigured=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.handler "Permalink to this definition")

helper to resolve name of scheme -> [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") object used by scheme.

| Parameters: | - **scheme** – This should identify the scheme to lookup.<br>  If omitted or set to `None`, this will return the handler<br>  for the default scheme.<br>- **category** – If a user category is specified, and no scheme is provided,<br>  it will use the default for that category.<br>  Otherwise this parameter is ignored.<br>- **unconfigured** – By default, this returns a handler object whose .hash()<br>  and .needs\_update() methods will honor the configured<br>  provided by CryptContext. See `unconfigured=True`<br>  to get the underlying handler from before any context-specific<br>  configuration was applied. |
| Raises: | [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.9)") – If the scheme does not exist OR is not being used within this context. |
| Returns: | [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") object used to implement<br>the named scheme within this context (this will usually<br>be one of the objects from [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib")) |

New in version 1.6: This was previously available as `CryptContext().policy.get_handler()`

Changed in version 1.7: This now returns a hasher configured with any CryptContext-specific
options (custom rounds settings, etc). Previously this returned
the base hasher from [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib").

`CryptContext.` `context_kwds` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.context_kwds "Permalink to this definition")

return `set` containing union of all [contextual keywords](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#context-keywords)
supported by the handlers in this context.

New in version 1.6.6.

### Saving the Configuration [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#saving-the-configuration "Permalink to this headline")

More detailed inspection can be done by exporting the configuration
using one of the serialization methods:

`CryptContext.` `to_dict`( _resolve=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "Permalink to this definition")

Return current configuration as a dictionary.

| Parameters: | **resolve** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – if `True`, the `schemes` key will contain a list of<br>a [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") objects instead of just<br>their names. |

This method dumps the current configuration of the CryptContext
instance. The key/value pairs should be in the format accepted
by the `CryptContext` class constructor, in fact
`CryptContext(**myctx.to_dict())` will create an exact copy of `myctx`.
As an example:

```
>>> # you can dump the configuration of any crypt context...
>>> from passlib.apps import ldap_nocrypt_context
>>> ldap_nocrypt_context.to_dict()
{'schemes': ['ldap_salted_sha1',\
'ldap_salted_md5',\
'ldap_sha1',\
'ldap_md5',\
'ldap_plaintext']}

```

New in version 1.6: This was previously available as `CryptContext().policy.to_dict()`

See also

the [Loading & Saving a CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-serialization-example) example in the tutorial.

`CryptContext.` `to_string`( _section='passlib'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_string "Permalink to this definition")

serialize to INI format and return as unicode string.

| Parameters: | **section** – name of INI section to output, defaults to `"passlib"`. |
| Returns: | CryptContext configuration, serialized to a INI unicode string. |

This function acts exactly like [`to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict"), except that it
serializes all the contents into a single human-readable string,
which can be hand edited, and/or stored in a file. The
output of this method is accepted by [`from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string"),
[`from_path()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_path "passlib.context.CryptContext.from_path"), and [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load"). As an example:

```
>>> # you can dump the configuration of any crypt context...
>>> from passlib.apps import ldap_nocrypt_context
>>> print ldap_nocrypt_context.to_string()
[passlib]
schemes = ldap_salted_sha1, ldap_salted_md5, ldap_sha1, ldap_md5, ldap_plaintext

```

New in version 1.6: This was previously available as `CryptContext().policy.to_string()`

See also

the [Loading & Saving a CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-serialization-example) example in the tutorial.

### Configuration Errors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#configuration-errors "Permalink to this headline")

The following errors may be raised when creating a `CryptContext` instance
via any of its constructors, or when updating the configuration of an existing
instance:

| raises ValueError: |
|  | - If a configuration option contains an invalid value<br>  (e.g. `all__vary_rounds=-1`).<br>- If the configuration contains valid but incompatible options<br>  (e.g. listing a scheme as both [default](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-default-option)<br>  and [deprecated](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-deprecated-option)). |
| raises KeyError: |
|  | - If the configuration contains an unknown or forbidden option<br>  (e.g. `scheme__salt`).<br>- If the [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option),<br>  [default](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-default-option), or<br>  [deprecated](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-deprecated-option) options reference an unknown<br>  hash scheme (e.g. `schemes=['xxx']`) |
| raises TypeError: |
|  | - If a configuration value has the wrong type (e.g. `schemes=123`).<br>Note that this error shouldn’t occur when loading configurations<br>from a file/string (e.g. using [`CryptContext.from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string")). |

Additionally, a [`PasslibConfigWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibConfigWarning "passlib.exc.PasslibConfigWarning") may be issued
if any invalid-but-correctable values are encountered
(e.g. if `sha256_crypt__min_rounds` is set to less than
[`sha256_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html#passlib.hash.sha256_crypt "passlib.hash.sha256_crypt") ‘s minimum of 1000).

Changed in version 1.6: Previous releases used Python’s builtin [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "(in Python v3.9)") instead
of the more specific `passlib.exc.PasslibConfigWarning`.

## Other Helpers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#other-helpers "Permalink to this headline")

_class_ `passlib.context.` `LazyCryptContext`(\[ _schemes=None_, \] _\*\*kwds_\[, _onload=None_\]) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.LazyCryptContext "Permalink to this definition")

CryptContext subclass which doesn’t load handlers until needed.

This is a subclass of CryptContext which takes in a set of arguments
exactly like CryptContext, but won’t import any handlers
(or even parse its arguments) until
the first time one of its methods is accessed.

| Parameters: | - **schemes** – The first positional argument can be a list of schemes, or omitted,<br>  just like CryptContext.<br>- **onload** – <br>  If a callable is passed in via this keyword,<br>  it will be invoked at lazy-load time<br>  with the following signature:<br>  `onload(**kwds) -> kwds`;<br>  where `kwds` is all the additional kwds passed to LazyCryptContext.<br>  It should perform any additional deferred initialization,<br>  and return the final dict of options to be passed to CryptContext.<br>  <br>  <br>  <br>  New in version 1.6.<br>  <br>- **create\_policy** – <br>  <br>  <br>  Deprecated since version 1.6: This option will be removed in Passlib 1.8,<br>  applications should use `onload` instead.<br>  <br>- **kwds** – All additional keywords are passed to CryptContext;<br>  or to the _onload_ function (if provided). |

This is mainly used internally by modules such as [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications"),
which define a large number of contexts, but only a few of them will be needed
at any one time. Use of this class saves the memory needed to import
the specified handlers until the context instance is actually accessed.
As well, it allows constructing a context at _module-init_ time,
but using `onload()` to provide dynamic configuration
at _application-run_ time.

Note

This class is only useful if you’re referencing handler objects by name,
and don’t want them imported until runtime. If you want to have the config
validated before your application runs, or are passing in already-imported
handler instances, you should use [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instead.

New in version 1.4.

## The CryptPolicy Class (deprecated) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#the-cryptpolicy-class-deprecated "Permalink to this headline")

_class_ `passlib.context.` `CryptPolicy`( _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy "Permalink to this definition")

Deprecated since version 1.6: This class has been deprecated, and will be removed in Passlib 1.8.
All of its functionality has been rolled into [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext").

This class previously stored the configuration options for the
CryptContext class. In the interest of interface simplification,
all of this class’ functionality has been rolled into the CryptContext
class itself.
The documentation for this class is now focused on documenting how to
migrate to the new api. Additionally, where possible, the deprecation
warnings issued by the CryptPolicy methods will list the replacement call
that should be used.

### Constructors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#passlib.context.CryptPolicy-constructors "Permalink to this headline")

CryptPolicy objects can be constructed directly using any of
the keywords accepted by [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext"). Direct uses of the
`CryptPolicy` constructor should either pass the keywords
directly into the CryptContext constructor, or to [`CryptContext.update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "passlib.context.CryptContext.update")
if the policy object was being used to update an existing context object.

In addition to passing in keywords directly,
CryptPolicy objects can be constructed by the following methods:

_classmethod_ `from_path`( _path_, _section='passlib'_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.from_path "Permalink to this definition")

create a CryptPolicy instance from a local file.

Deprecated since version 1.6.

Creating a new CryptContext from a file, which was previously done via
`CryptContext(policy=CryptPolicy.from_path(path))`, can now be
done via `CryptContext.from_path(path)`.
See [`CryptContext.from_path()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_path "passlib.context.CryptContext.from_path") for details.

Updating an existing CryptContext from a file, which was previously done
`context.policy = CryptPolicy.from_path(path)`, can now be
done via `context.load_path(path)`.
See [`CryptContext.load_path()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load_path "passlib.context.CryptContext.load_path") for details.

_classmethod_ `from_string`( _source_, _section='passlib'_, _encoding='utf-8'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.from_string "Permalink to this definition")

create a CryptPolicy instance from a string.

Deprecated since version 1.6.

Creating a new CryptContext from a string, which was previously done via
`CryptContext(policy=CryptPolicy.from_string(data))`, can now be
done via `CryptContext.from_string(data)`.
See [`CryptContext.from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string") for details.

Updating an existing CryptContext from a string, which was previously done
`context.policy = CryptPolicy.from_string(data)`, can now be
done via `context.load(data)`.
See [`CryptContext.load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load") for details.

_classmethod_ `from_source`( _source_, _\_warn=True_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.from_source "Permalink to this definition")

create a CryptPolicy instance from some source.

this method autodetects the source type, and invokes
the appropriate constructor automatically. it attempts
to detect whether the source is a configuration string, a filepath,
a dictionary, or an existing CryptPolicy instance.

Deprecated since version 1.6.

Create a new CryptContext, which could previously be done via
`CryptContext(policy=CryptPolicy.from_source(source))`, should
now be done using an explicit method: the [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext")
constructor itself, [`CryptContext.from_path()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_path "passlib.context.CryptContext.from_path"),
or [`CryptContext.from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string").

Updating an existing CryptContext, which could previously be done via
`context.policy = CryptPolicy.from_source(source)`, should
now be done using an explicit method: [`CryptContext.update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "passlib.context.CryptContext.update"),
or [`CryptContext.load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load").

_classmethod_ `from_sources`( _sources_, _\_warn=True_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.from_sources "Permalink to this definition")

create a CryptPolicy instance by merging multiple sources.

each source is interpreted as by [`from_source()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.from_source "passlib.context.CryptPolicy.from_source"),
and the results are merged together.

Deprecated since version 1.6: Instead of using this method to merge multiple policies together,
a [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instance should be created, and then
the multiple sources merged together via [`CryptContext.load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load").

`replace`( _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.replace "Permalink to this definition")

create a new CryptPolicy, optionally updating parts of the
existing configuration.

Deprecated since version 1.6: Callers of this method should [`CryptContext.update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "passlib.context.CryptContext.update") or
[`CryptContext.copy()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.copy "passlib.context.CryptContext.copy") instead.

### Introspection [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#passlib.context.CryptPolicy-introspection "Permalink to this headline")

All of the informational methods provided by this class have been deprecated
by identical or similar methods in the [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") class:

`has_schemes`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.has_schemes "Permalink to this definition")

return True if policy defines _any_ schemes for use.

Deprecated since version 1.6: applications should use `bool(context.schemes())` instead.
see [`CryptContext.schemes()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "passlib.context.CryptContext.schemes").

`schemes`( _resolve=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.schemes "Permalink to this definition")

return list of schemes defined in policy.

Deprecated since version 1.6: applications should use [`CryptContext.schemes()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "passlib.context.CryptContext.schemes") instead.

`iter_handlers`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.iter_handlers "Permalink to this definition")

return iterator over handlers defined in policy.

Deprecated since version 1.6: applications should use `context.schemes(resolve=True))` instead.
see [`CryptContext.schemes()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.schemes "passlib.context.CryptContext.schemes").

`get_handler`( _name=None_, _category=None_, _required=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.get_handler "Permalink to this definition")

return handler as specified by name, or default handler.

Deprecated since version 1.6: applications should use [`CryptContext.handler()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.handler "passlib.context.CryptContext.handler") instead,
though note that the `required` keyword has been removed,
and the new method will always act as if `required=True`.

`get_options`( _name_, _category=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.get_options "Permalink to this definition")

return dictionary of options specific to a given handler.

Deprecated since version 1.6: this method has no direct replacement in the 1.6 api, as there
is not a clearly defined use-case. however, examining the output of
[`CryptContext.to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict") should serve as the closest alternative.

`handler_is_deprecated`( _name_, _category=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.handler_is_deprecated "Permalink to this definition")

check if handler has been deprecated by policy.

Deprecated since version 1.6: this method has no direct replacement in the 1.6 api, as there
is not a clearly defined use-case. however, examining the output of
[`CryptContext.to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict") should serve as the closest alternative.

`get_min_verify_time`( _category=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.get_min_verify_time "Permalink to this definition")

get min\_verify\_time setting for policy.

Deprecated since version 1.6: min\_verify\_time option will be removed entirely in passlib 1.8

Changed in version 1.7: this method now always returns the value automatically
calculated by `CryptContext.min_verify_time()`,
any value specified by policy is ignored.

### Exporting [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#passlib.context.CryptPolicy-exporting "Permalink to this headline")

`iter_config`( _ini=False_, _resolve=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.iter_config "Permalink to this definition")

iterate over key/value pairs representing the policy object.

Deprecated since version 1.6: applications should use [`CryptContext.to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict") instead.

`to_dict`( _resolve=False_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.to_dict "Permalink to this definition")

export policy object as dictionary of options.

Deprecated since version 1.6: applications should use [`CryptContext.to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict") instead.

`to_file`( _stream_, _section='passlib'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.to_file "Permalink to this definition")

export policy to file.

Deprecated since version 1.6: applications should use [`CryptContext.to_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_string "passlib.context.CryptContext.to_string") instead,
and then write the output to a file as desired.

`to_string`( _section='passlib'_, _encoding=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.to_string "Permalink to this definition")

export policy to file.

Deprecated since version 1.6: applications should use [`CryptContext.to_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_string "passlib.context.CryptContext.to_string") instead.

Note

CryptPolicy are immutable.
Use the [`replace()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptPolicy.replace "passlib.context.CryptPolicy.replace") method to mutate existing instances.

Deprecated since version 1.6.

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
  - [`passlib.apache` \- Apache Password Files](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html)
  - [`passlib.apps` \- Helpers for various applications](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html)
  - [`passlib.context` \- CryptContext Hash Manager](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#)
    - [The CryptContext Class](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#the-cryptcontext-class)
      - [Constructor Keywords](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#constructor-keywords)
        - [Context Options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-options)
        - [Algorithm Options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#algorithm-options)
        - [Global Algorithm Options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#global-algorithm-options)
        - [User Categories](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories)
      - [Primary Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#primary-methods)
        - [“crypt”-style methods](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#crypt-style-methods)
      - [Hash Migration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#hash-migration)
      - [Disabled Hash Managment](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#disabled-hash-managment)
      - [Alternate Constructors](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#alternate-constructors)
      - [Changing the Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#changing-the-configuration)
      - [Examining the Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#examining-the-configuration)
      - [Saving the Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#saving-the-configuration)
      - [Configuration Errors](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#configuration-errors)
    - [Other Helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#other-helpers)
    - [The CryptPolicy Class (deprecated)](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#the-cryptpolicy-class-deprecated)
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
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.html "passlib.crypto - Cryptographic Helper Functions")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html "passlib.apps - Helpers for various applications")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.context.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.context.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)