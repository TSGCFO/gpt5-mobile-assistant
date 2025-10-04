<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html "passlib.ext.django - Django Password Hashing Plugin")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html "passlib.crypto.des - DES routines")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.exc`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#module-passlib.exc "passlib.exc: exceptions & warnings raised by Passlib") \- Exceptions and warnings [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#module-passlib.exc "Permalink to this headline")

This module contains all the custom exceptions & warnings that
may be raised by Passlib.

## Exceptions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#exceptions "Permalink to this headline")

_exception_ `passlib.exc.` `MissingBackendError` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.MissingBackendError "Permalink to this definition")

Error raised if multi-backend handler has no available backends;
or if specifically requested backend is not available.

`MissingBackendError` derives
from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.9)"), since it usually indicates
lack of an external library or OS feature.
This is primarily raised by handlers which depend on
external libraries (which is currently just
[`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt")).

_exception_ `passlib.exc.` `InternalBackendError` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.InternalBackendError "Permalink to this definition")

Error raised if something unrecoverable goes wrong with backend call;
such as if `crypt.crypt()` returning a malformed hash.

New in version 1.7.3.

_exception_ `passlib.exc.` `PasswordValueError` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordValueError "Permalink to this definition")

Error raised if a password can’t be hashed / verified for various reasons.
This exception derives from the builtin `ValueError`.

May be thrown directly when password violates internal invariants of hasher
(e.g. some don’t support NULL characters). Hashers may also throw more specific subclasses,
such as `PasswordSizeError`.

New in version 1.7.3.

_exception_ `passlib.exc.` `PasswordSizeError`( _max\_size_, _msg=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordSizeError "Permalink to this definition")

Error raised if a password exceeds the maximum size allowed
by Passlib (by default, 4096 characters); or if password exceeds
a hash-specific size limitation.

This exception derives from [`PasswordValueError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordValueError "passlib.exc.PasswordValueError") (above).

Many password hash algorithms take proportionately larger amounts of time and/or
memory depending on the size of the password provided. This could present
a potential denial of service (DOS) situation if a maliciously large
password is provided to an application. Because of this, Passlib enforces
a maximum size limit, but one which should be _much_ larger
than any legitimate password. [`PasswordSizeError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordSizeError "passlib.exc.PasswordSizeError") derives
from `ValueError`.

Note

Applications wishing to use a different limit should set the
`PASSLIB_MAX_PASSWORD_SIZE` environmental variable before
Passlib is loaded. The value can be any large positive integer.

`max_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordSizeError.max_size "Permalink to this definition")

indicates the maximum allowed size.

New in version 1.6.

_exception_ `passlib.exc.` `PasswordTruncateError`( _cls_, _msg=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordTruncateError "Permalink to this definition")

Error raised if password would be truncated by hash.
This derives from [`PasswordSizeError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordSizeError "passlib.exc.PasswordSizeError") (above).

Hashers such as [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt") can be configured to raises
this error by setting `truncate_error=True`.

`max_size` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordTruncateError.max_size "Permalink to this definition")

indicates the maximum allowed size.

New in version 1.7.

_exception_ `passlib.exc.` `PasslibSecurityError` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibSecurityError "Permalink to this definition")

Error raised if critical security issue is detected
(e.g. an attempt is made to use a vulnerable version of a bcrypt backend).

New in version 1.6.3.

_exception_ `passlib.exc.` `UnknownHashError`( _message=None_, _value=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.UnknownHashError "Permalink to this definition")

Error raised by `lookup_hash` if hash name is not recognized.
This exception derives from `ValueError`.

As of version 1.7.3, this may also be raised if hash algorithm is known,
but has been disabled due to FIPS mode (message will include phrase “disabled for fips”).

As of version 1.7.4, this may be raised if a [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext")
is unable to identify the algorithm used by a password hash.

New in version 1.7.

Changed in version 1.7.4: altered call signature.

### TOTP Exceptions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#totp-exceptions "Permalink to this headline")

_exception_ `passlib.exc.` `TokenError`( _msg=None_, _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.TokenError "Permalink to this definition")

Base error raised by v:mod:passlib.totp when
a token can’t be parsed / isn’t valid / etc.
Derives from `ValueError`.

Usually one of the more specific subclasses below will be raised:

- [`MalformedTokenError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.MalformedTokenError "passlib.exc.MalformedTokenError") – invalid chars, too few digits
- [`InvalidTokenError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.InvalidTokenError "passlib.exc.InvalidTokenError") – no match found
- [`UsedTokenError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.UsedTokenError "passlib.exc.UsedTokenError") – match found, but token already used

New in version 1.7.

_exception_ `passlib.exc.` `MalformedTokenError`( _msg=None_, _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.MalformedTokenError "Permalink to this definition")

Error raised by [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#module-passlib.totp "passlib.totp: totp / two factor authentaction") when a token isn’t formatted correctly
(contains invalid characters, wrong number of digits, etc)

_exception_ `passlib.exc.` `InvalidTokenError`( _msg=None_, _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.InvalidTokenError "Permalink to this definition")

Error raised by [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#module-passlib.totp "passlib.totp: totp / two factor authentaction") when a token is formatted correctly,
but doesn’t match any tokens within valid range.

_exception_ `passlib.exc.` `UsedTokenError`( _\*args_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.UsedTokenError "Permalink to this definition")

Error raised by [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#module-passlib.totp "passlib.totp: totp / two factor authentaction") if a token is reused.
Derives from [`TokenError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.TokenError "passlib.exc.TokenError").

`expire_time` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.UsedTokenError.expire_time "Permalink to this definition")

optional value indicating when current counter period will end,
and a new token can be generated.

New in version 1.7.

## Warnings [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#warnings "Permalink to this headline")

_exception_ `passlib.exc.` `PasslibWarning` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibWarning "Permalink to this definition")

base class for Passlib’s user warnings,
derives from the builtin [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "(in Python v3.9)").

New in version 1.6.

### Minor Warnings [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#minor-warnings "Permalink to this headline")

_exception_ `passlib.exc.` `PasslibConfigWarning` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibConfigWarning "Permalink to this definition")

Warning issued when non-fatal issue is found related to the configuration
of a [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instance.

This occurs primarily in one of two cases:

- The CryptContext contains rounds limits which exceed the hard limits
imposed by the underlying algorithm.
- An explicit rounds value was provided which exceeds the limits
imposed by the CryptContext.

In both of these cases, the code will perform correctly & securely;
but the warning is issued as a sign the configuration may need updating.

New in version 1.6.

_exception_ `passlib.exc.` `PasslibHashWarning` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "Permalink to this definition")

Warning issued when non-fatal issue is found with parameters
or hash string passed to a passlib hash class.

This occurs primarily in one of two cases:

- A rounds value or other setting was explicitly provided which
exceeded the handler’s limits (and has been clamped
by the [relaxed](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#relaxed-keyword) flag).
- A malformed hash string was encountered which (while parsable)
should be re-encoded.

New in version 1.6.

### Critical Warnings [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html\#critical-warnings "Permalink to this headline")

_exception_ `passlib.exc.` `PasslibRuntimeWarning` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibRuntimeWarning "Permalink to this definition")

Warning issued when something unexpected happens during runtime.

The fact that it’s a warning instead of an error means Passlib
was able to correct for the issue, but that it’s anomalous enough
that the developers would love to hear under what conditions it occurred.

New in version 1.6.

_exception_ `passlib.exc.` `PasslibSecurityWarning` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibSecurityWarning "Permalink to this definition")

Special warning issued when Passlib encounters something
that might affect security.

New in version 1.6.

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
  - [`passlib.exc` \- Exceptions and warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#)
    - [Exceptions](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#exceptions)
      - [TOTP Exceptions](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#totp-exceptions)
    - [Warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#warnings)
      - [Minor Warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#minor-warnings)
      - [Critical Warnings](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#critical-warnings)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html "passlib.ext.django - Django Password Hashing Plugin")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.des.html "passlib.crypto.des - DES routines")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.exc.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.exc.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)