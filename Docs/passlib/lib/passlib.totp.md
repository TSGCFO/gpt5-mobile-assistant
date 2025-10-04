<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html "passlib.utils - Helper Functions")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html "passlib.registry - Password Handler Registry")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.totp`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#module-passlib.totp "passlib.totp: totp / two factor authentaction") – TOTP / Two Factor Authentication [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#passlib-totp-totp-two-factor-authentication "Permalink to this headline")

New in version 1.7.

## Overview [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#overview "Permalink to this headline")

The `passlib.totp` module provides a number of classes for implementing
two-factor authentication (2FA) using the TOTP [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#totpspec) specification.
This page provides a reference to all the classes and methods in this module.

Passlib’s TOTP support is centered around the [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") class. There are also
some additional helpers, including the [`AppWallet`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet "passlib.totp.AppWallet") class, which
helps to securely encrypt TOTP keys for storage.

See also

- [TOTP Tutorial](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-tutorial) –
Overview of this module and walkthrough of how to use it.

## TOTP Class [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#totp-class "Permalink to this headline")

_class_ `passlib.totp.` `TOTP`( _key=None_, _format="base32"_, _\*_, _new=False_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "Permalink to this definition")

Helper for generating and verifying TOTP codes.

Given a secret key and set of configuration options, this object
offers methods for token generation, token validation, and serialization.
It can also be used to track important persistent TOTP state,
such as the last counter used.

This class accepts the following options
(only **key** and **format** may be specified as positional arguments).

| Parameters: | - **key** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  The secret key to use. By default, should be encoded as<br>  a base32 string (see **format** for other encodings).<br>  <br>  Exactly one of **key** or `new=True` must be specified.<br>  <br>- **format** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – The encoding used by the **key** parameter. May be one of:<br>  `"base32"` (base32-encoded string),<br>  `"hex"` (hexadecimal string), or `"raw"` (raw bytes).<br>  Defaults to `"base32"`.<br>- **new** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  If `True`, a new key will be generated using [`random.SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "(in Python v3.9)").<br>  <br>  Exactly one `new=True` or **key** must be specified.<br>  <br>- **label** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – Label to associate with this token when generating a URI.<br>  Displayed to user by most OTP client applications (e.g. Google Authenticator),<br>  and typically has format such as `"John Smith"` or `"jsmith@webservice.example.org"`.<br>  Defaults to `None`.<br>  See [`to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri") for details.<br>- **issuer** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – String identifying the token issuer (e.g. the domain name of your service).<br>  Used internally by some OTP client applications (e.g. Google Authenticator) to distinguish entries<br>  which otherwise have the same label.<br>  Optional but strongly recommended if you’re rendering to a URI.<br>  Defaults to `None`.<br>  See [`to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri") for details.<br>- **size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – <br>  Number of bytes when generating new keys. Defaults to size of hash algorithm (e.g. 20 for SHA1).<br>  <br>  <br>  <br>  Warning<br>  <br>  <br>  <br>  Overriding the default values for `digits`, `period`, or `alg` may<br>  cause problems with some OTP client programs (such as Google Authenticator),<br>  which may have these defaults hardcoded.<br>  <br>- **digits** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – <br>  The number of digits in the generated / accepted tokens. Defaults to `6`.<br>  Must be in range \[6 .. 10\].<br>  <br>  <br>  <br>  Caution<br>  <br>  <br>  <br>  Due to a limitation of the HOTP algorithm, the 10th digit can only take on values 0 .. 2,<br>  and thus offers very little extra security.<br>  <br>- **alg** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – Name of hash algorithm to use. Defaults to `"sha1"`.<br>  `"sha256"` and `"sha512"` are also accepted, per [**RFC 6238**](https://tools.ietf.org/html/rfc6238.html).<br>- **period** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – The time-step period to use, in integer seconds. Defaults to `30`. |

See below for all the `TOTP` methods & attributes…

## Alternate Constructors [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#alternate-constructors "Permalink to this headline")

There are a few alternate class constructors offered.
These range from simple convenience wrappers such as [`TOTP.new()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.new "passlib.totp.TOTP.new"),
to deserialization methods such as [`TOTP.from_source()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_source "passlib.totp.TOTP.from_source").

_classmethod_ `TOTP.` `new`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.new "Permalink to this definition")

convenience alias for creating new TOTP key, same as `TOTP(new=True)`

_classmethod_ `TOTP.` `from_source`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_source "Permalink to this definition")

Load / create a TOTP object from a serialized source.
This acts as a wrapper for the various deserialization methods:

- TOTP URIs are handed off to [`from_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_uri "passlib.totp.TOTP.from_uri")
- Any other strings are handed off to [`from_json()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_json "passlib.totp.TOTP.from_json")
- Dicts are handed off to [`from_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_dict "passlib.totp.TOTP.from_dict")

| Parameters: | **source** – Serialized TOTP object. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>If the key has been encrypted, but the application secret isn’t available;<br>or if the string cannot be recognized, parsed, or decoded.<br>See [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using") for how to configure application secrets. |
| Returns: | a [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") instance. |

_classmethod_ `TOTP.` `from_uri`( _uri_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_uri "Permalink to this definition")

create an OTP instance from a URI (such as returned by [`to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri")).

| Returns: | [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") instance. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if the uri cannot be parsed or contains errors. |

See also

[Configuring Clients](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-configuring-clients) tutorial for a usage example

_classmethod_ `TOTP.` `from_json`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_json "Permalink to this definition")

Load / create an OTP object from a serialized json string
(as generated by [`to_json()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_json "passlib.totp.TOTP.to_json")).

| Parameters: | **json** – Serialized output from [`to_json()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_json "passlib.totp.TOTP.to_json"), as unicode or ascii bytes. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>If the key has been encrypted, but the application secret isn’t available;<br>or if the string cannot be recognized, parsed, or decoded.<br>See [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using") for how to configure application secrets. |
| Returns: | a [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") instance. |

See also

[Storing TOTP instances](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-storing-instances) tutorial for a usage example

_classmethod_ `TOTP.` `from_dict`( _source_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_dict "Permalink to this definition")

Load / create a TOTP object from a dictionary
(as generated by [`to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_dict "passlib.totp.TOTP.to_dict"))

| Parameters: | **source** – dict containing serialized TOTP key & configuration. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>If the key has been encrypted, but the application secret isn’t available;<br>or if the dict cannot be recognized, parsed, or decoded.<br>See [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using") for how to configure application secrets. |
| Returns: | A [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") instance. |

See also

[Storing TOTP instances](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-storing-instances) tutorial for a usage example

## Factory Creation [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#factory-creation "Permalink to this headline")

One powerful method offered by the TOTP class is [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using").
This method allows you to quickly create TOTP subclasses with preconfigured defaults,
for configuration application secrets and setting default TOTP behavior
for your application:

_classmethod_ `TOTP.` `using`( _digits=None_, _alg=None_, _period=None_, _issuer=None_, _wallet=None_, _now=None_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "Permalink to this definition")

Dynamically create subtype of `TOTP` class
which has the specified defaults set.

| Parameters: | **digits, alg, period, issuer**:<br>All these options are the same as in the [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") constructor,<br>and the resulting class will use any values you specify here<br>as the default for all TOTP instances it creates. |
| Parameters: | - **wallet** – Optional [`AppWallet`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet "passlib.totp.AppWallet") that will be used for encrypting/decrypting keys.<br>- **secrets\_path** **,** **encrypt\_cost** ( _secrets_ _,_) – If specified, these options will be passed to the [`AppWallet`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet "passlib.totp.AppWallet") constructor,<br>  allowing you to directly specify the secret keys that should be used<br>  to encrypt & decrypt stored keys. |
| Returns: | subclass of `TOTP`. |

This method is useful for creating a TOTP class configured
to use your application’s secrets for encrypting & decrypting
keys, as well as create new keys using it’s desired configuration defaults.

As an example:

```
>>> # your application can create a custom class when it initializes
>>> from passlib.totp import TOTP, generate_secret
>>> TotpFactory = TOTP.using(secrets={"1": generate_secret()})

>>> # subsequent TOTP objects created from this factory
>>> # will use the specified secrets to encrypt their keys...
>>> totp = TotpFactory.new()
>>> totp.to_dict()
{'enckey': {'c': 14,
  'k': 'H77SYXWORDPGVOQTFRR2HFUB3C45XXI7',
  's': 'G5DOQPIHIBUM2OOHHADQ',
  't': '1',
  'v': 1},
 'type': 'totp',
 'v': 1}

```

See also

[Creating TOTP Instances](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-creation) and [Storing TOTP instances](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-storing-instances) tutorials for a usage example

## Basic Attributes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#basic-attributes "Permalink to this headline")

All the TOTP objects offer the following attributes,
which correspond to the constructor options above.
Most of this information will be serialized by [`TOTP.to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri") and [`TOTP.to_json()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_json "passlib.totp.TOTP.to_json"):

`TOTP.` `key` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.key "Permalink to this definition")

secret key as raw bytes

`TOTP.` `hex_key` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.hex_key "Permalink to this definition")

secret key encoded as hexadecimal string

`TOTP.` `base32_key` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.base32_key "Permalink to this definition")

secret key encoded as base32 string

`TOTP.` `label` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.label "Permalink to this definition")

default label for [`to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri")

`TOTP.` `issuer` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.issuer "Permalink to this definition")

default issuer for [`to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri")

`TOTP.` `digits` _= 6_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.digits "Permalink to this definition")

number of digits in the generated tokens.

`TOTP.` `alg` _= 'sha1'_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.alg "Permalink to this definition")

name of hash algorithm in use (e.g. `"sha1"`)

`TOTP.` `period` _= 30_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.period "Permalink to this definition")

number of seconds per counter step.
_(TOTP uses an internal time-derived counter which_
_increments by 1 every_ `period` _seconds)_.

`TOTP.` `changed` _= False_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.changed "Permalink to this definition")

Flag set by deserialization methods to indicate the object needs to be re-serialized.
This can be for a number of reasons – encoded using deprecated format,
or encrypted using a deprecated key or too few rounds.

## Token Generation [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#token-generation "Permalink to this headline")

Token generation is generally useful client-side, and for generating
values to test your server implementation.
There is one main generation method:

`TOTP.` `generate`( _time=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.generate "Permalink to this definition")

Generate token for specified time
(uses current time if none specified).

| Parameters: | **time** – Can be `None`, a `datetime`,<br>or class:!float / `int` unix epoch timestamp.<br>If `None` (the default), uses current system time.<br>Naive datetimes are treated as UTC. |
| Returns: | A [`TotpToken`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken "passlib.totp.TotpToken") instance, which can be treated<br>as a sequence of `(token, expire_time)` – see that class<br>for more details. |

Usage example:

```
>>> # generate a new token, wrapped in a TotpToken instance...
>>> otp = TOTP('s3jdvb7qd2r7jpxx')
>>> otp.generate(1419622739)
<TotpToken token='897212' expire_time=1419622740>

>>> # when you just need the token...
>>> otp.generate(1419622739).token
'897212'

```

Warning

Tokens should be displayed as strings, as
they may contain leading zeros which will get stripped if they are
first converted to an `int`.

### TotpToken [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#totptoken "Permalink to this headline")

The `TOTP.generate()` method returns instances of the following class,
which offers up detailed information about the generated token:

_class_ `passlib.totp.` `TotpToken` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken "Permalink to this definition")

Object returned by [`TOTP.generate()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.generate "passlib.totp.TOTP.generate").
It can be treated as a sequence of `(token, expire_time)`,
or accessed via the following attributes:

`token` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken.token "Permalink to this definition")

Token as decimal-encoded ascii string.

`expire_time` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken.expire_time "Permalink to this definition")

Timestamp marking end of period when token is valid

`counter` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken.counter "Permalink to this definition")

HOTP counter value used to generate token (derived from time)

`remaining` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken.remaining "Permalink to this definition")

number of (float) seconds before token expires

`valid` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpToken.valid "Permalink to this definition")

whether token is still valid

## Token Matching / Verification [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#token-matching-verification "Permalink to this headline")

Matching user-provided tokens is the main operation when implementing server-side TOTP support.
Passlib offers one main method: `TOTP.match()`, as well as a convenience wrapper `TOTP.verify()`:

`TOTP.` `match`( _token_, _time=None_, _window=30_, _skew=0_, _last\_counter=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.match "Permalink to this definition")

Match TOTP token against specified timestamp.
Searches within a window before & after the provided time,
in order to account for transmission delay and small amounts of skew in the client’s clock.

| Parameters: | - **token** – Token to validate.<br>  may be integer or string (whitespace and hyphens are ignored).<br>- **time** – Unix epoch timestamp, can be any of `float`, `int`, or `datetime`.<br>  if `None` (the default), uses current system time.<br>  _this should correspond to the time the token was received from the client_.<br>- **window** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – How far backward and forward in time to search for a match.<br>  Measured in seconds. Defaults to `30`. Typically only useful if set<br>  to multiples of [`period`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.period "passlib.totp.TOTP.period").<br>- **skew** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – <br>  Adjust timestamp by specified value, to account for excessive<br>  client clock skew. Measured in seconds. Defaults to `0`.<br>  <br>  Negative skew (the common case) indicates transmission delay,<br>  and/or that the client clock is running behind the server.<br>  <br>  Positive skew indicates the client clock is running ahead of the server<br>  (and by enough that it cancels out any negative skew added by<br>  the transmission delay).<br>  <br>  You should ensure the server clock uses a reliable time source such as NTP,<br>  so that only the client clock’s inaccuracy needs to be accounted for.<br>  <br>  This is an advanced parameter that should usually be left at `0`;<br>  The **window** parameter is usually enough to account<br>  for any observed transmission delay.<br>  <br>- **last\_counter** – <br>  Optional value of last counter value that was successfully used.<br>  If specified, verify will never search earlier counters,<br>  no matter how large the window is.<br>  <br>  Useful when client has previously authenticated,<br>  and thus should never provide a token older than previously<br>  verified value. |
| Raises: | [**TokenError**](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.TokenError "passlib.exc.TokenError") – If the token is malformed, fails to match, or has already been used. |
| Returns TotpMatch: |
|  | Returns a [`TotpMatch`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch "passlib.totp.TotpMatch") instance on successful match.<br>Can be treated as tuple of `(counter, time)`.<br>Raises error if token is malformed / can’t be verified. |

Usage example:

```
>>> totp = TOTP('s3jdvb7qd2r7jpxx')

>>> # valid token for this time period
>>> totp.match('897212', 1419622729)
<TotpMatch counter=47320757 time=1419622729 cache_seconds=60>

>>> # token from counter step 30 sec ago (within allowed window)
>>> totp.match('000492', 1419622729)
<TotpMatch counter=47320756 time=1419622729 cache_seconds=60>

>>> # invalid token -- token from 60 sec ago (outside of window)
>>> totp.match('760389', 1419622729)
Traceback:
    ...
InvalidTokenError: Token did not match

```

_classmethod_ `TOTP.` `verify`( _token_, _source_, _\*\*kwds_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.verify "Permalink to this definition")

Convenience wrapper around [`TOTP.from_source()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_source "passlib.totp.TOTP.from_source") and [`TOTP.match()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.match "passlib.totp.TOTP.match").

This parses a TOTP key & configuration from the specified source,
and tries and match the token.
It’s designed to parallel the [`passlib.ifc.PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") method.

| Parameters: | - **token** – Token string to match.<br>- **source** – Serialized TOTP key.<br>  Can be anything accepted by [`TOTP.from_source()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_source "passlib.totp.TOTP.from_source").<br>- **\\\*\\\*kwds** – All additional keywords passed to [`TOTP.match()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.match "passlib.totp.TOTP.match"). |
| Returns: | A [`TotpMatch`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch "passlib.totp.TotpMatch") instance, or raises a `TokenError`. |

See also

[Verifying Tokens](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-verifying) tutorial for a usage example

### TotpMatch [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#totpmatch "Permalink to this headline")

If successful, the `TOTP.verify()` method returns instances of the following class,
which offers up detailed information about the matched token:

_class_ `passlib.totp.` `TotpMatch` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch "Permalink to this definition")

Object returned by [`TOTP.match()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.match "passlib.totp.TOTP.match") and [`TOTP.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.verify "passlib.totp.TOTP.verify") on a successful match.

It can be treated as a sequence of `(counter, time)`,
or accessed via the following attributes:

`counter` _= 0_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.counter "Permalink to this definition")

TOTP counter value which matched token.
(Best practice is to subsequently ignore tokens matching this counter
or earlier)

`time` _= 0_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.time "Permalink to this definition")

Timestamp when verification was performed.

`expected_counter` _= 0_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.expected_counter "Permalink to this definition")

Counter value expected for timestamp.

`skipped` _= 0_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.skipped "Permalink to this definition")

How many steps were skipped between expected and actual matched counter
value (may be positive, zero, or negative).

`expire_time` _= 0_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.expire_time "Permalink to this definition")

Timestamp marking end of period when token is valid

`cache_seconds` _= 60_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.cache_seconds "Permalink to this definition")

Number of seconds counter should be cached
before it’s guaranteed to have passed outside of verification window.

`cache_time` _= 0_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TotpMatch.cache_time "Permalink to this definition")

Timestamp marking when counter has passed outside of verification window.

This object will always have a `True` boolean value.

## Client Configuration Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#client-configuration-methods "Permalink to this headline")

Once a server has generated a new TOTP key & configuration,
it needs to be communicated to the user in order for them to store it
in a suitable TOTP client.

This can be done by displaying the key & configuration for the user
to hand-enter into their client, or by encoding TOTP object into a URI [\[3\]](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#uriformat).
These configuration URIs can subsequently be displayed as a QR code,
for easy transfer to many smartphone-based TOTP clients
(such as Authy or Google Authenticator).

`TOTP.` `to_uri`( _label=None_, _issuer=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "Permalink to this definition")

Serialize key and configuration into a URI, per
Google Auth’s [KeyUriFormat](http://code.google.com/p/google-authenticator/wiki/KeyUriFormat).

| Parameters: | - **label** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Label to associate with this token when generating a URI.<br>  Displayed to user by most OTP client applications (e.g. Google Authenticator),<br>  and typically has format such as `"John Smith"` or `"jsmith@webservice.example.org"`.<br>  <br>  Defaults to **label** constructor argument. Must be provided in one or the other location.<br>  May not contain `:`.<br>  <br>- **issuer** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  String identifying the token issuer (e.g. the domain or canonical name of your service).<br>  Optional but strongly recommended if you’re rendering to a URI.<br>  Used internally by some OTP client applications (e.g. Google Authenticator) to distinguish entries<br>  which otherwise have the same label.<br>  <br>  Defaults to **issuer** constructor argument, or `None`.<br>  May not contain `:`. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – <br>- if a label was not provided either as an argument, or in the constructor.<br>- if the label or issuer contains invalid characters. |
| Returns: | all the configuration information for this OTP token generator,<br>encoded into a URI. |

These URIs are frequently converted to a QRCode for transferring
to a TOTP client application such as Google Auth.
Usage example:

```
>>> from passlib.totp import TOTP
>>> tp = TOTP('s3jdvb7qd2r7jpxx')
>>> uri = tp.to_uri("user@example.org", "myservice.another-example.org")
>>> uri
'otpauth://totp/user@example.org?secret=S3JDVB7QD2R7JPXX&issuer=myservice.another-example.org'

```

Changed in version 1.7.2: This method now prepends the issuer URI label. This is recommended by the KeyURI
specification, for compatibility with older clients.

`TOTP.` `pretty_key`( _format='base32'_, _sep='-'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.pretty_key "Permalink to this definition")

pretty-print the secret key.

This is mainly useful for situations where the user cannot get the qrcode to work,
and must enter the key manually into their TOTP client. It tries to format
the key in a manner that is easier for humans to read.

| Parameters: | - **format** – format to output secret key. `"hex"` and `"base32"` are both accepted.<br>- **sep** – separator to insert to break up key visually.<br>  can be any of `"-"` (the default), `" "`, or `False` (no separator). |
| Returns: | key as native string. |

Usage example:

```
>>> t = TOTP('s3jdvb7qd2r7jpxx')
>>> t.pretty_key()
'S3JD-VB7Q-D2R7-JPXX'

```

See also

- The [`TOTP.from_source()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_source "passlib.totp.TOTP.from_source") and [`TOTP.from_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_uri "passlib.totp.TOTP.from_uri") constructors for decoding URIs.
- The [Configuring Clients](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-configuring-clients) tutorial for details
about these methods, and how to render URIs to a QR Code.

## Serialization Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#serialization-methods "Permalink to this headline")

The [`TOTP.to_uri()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_uri "passlib.totp.TOTP.to_uri") method is useful, but limited, because it requires
additional information (label & issuer), and lacks the ability to encrypt the key.
The [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP") provides the following methods for serializing TOTP objects
to internal storage. When application secrets are configured via [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using"),
these methods will automatically encrypt the resulting keys.

`TOTP.` `to_json`( _encrypt=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_json "Permalink to this definition")

Serialize configuration & internal state to a json string,
mainly useful for persisting client-specific state in a database.
All keywords passed to [`to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_dict "passlib.totp.TOTP.to_dict").

| Returns: | json string containing serializes configuration & state. |

`TOTP.` `to_dict`( _encrypt=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.to_dict "Permalink to this definition")

Serialize configuration & internal state to a dict,
mainly useful for persisting client-specific state in a database.

| Parameters: | **encrypt** – <br>Whether to output should be encrypted.<br>- `None` (the default) – uses encrypted key if application<br>  secrets are available, otherwise uses plaintext key.<br>- `True` – uses encrypted key, or raises TypeError<br>  if application secret wasn’t provided to OTP constructor.<br>- `False` – uses raw key. |
| Returns: | dictionary, containing basic (json serializable) datatypes. |

See also

- The [`TOTP.from_source()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_source "passlib.totp.TOTP.from_source") and [`TOTP.from_json()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.from_json "passlib.totp.TOTP.from_json") constructors for decoding
the results of these methods.
- The [Storing TOTP instances](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-storing-instances) tutorial for more details.

## Helper Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#helper-methods "Permalink to this headline")

While [`TOTP.generate()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.generate "passlib.totp.TOTP.generate"), [`TOTP.match()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.match "passlib.totp.TOTP.match"), and [`TOTP.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.verify "passlib.totp.TOTP.verify")
automatically handle normalizing tokens & time values, the following methods
are exposed in case they are useful in other contexts:

`TOTP.` `normalize_token`( _token_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.normalize_token "Permalink to this definition")

Normalize OTP token representation:
strips whitespace, converts integers to a zero-padded string,
validates token content & number of digits.

This is a hybrid method – it can be called at the class level,
as `TOTP.normalize_token()`, or the instance level as `TOTP().normalize_token()`.
It will normalize to the instance-specific number of [`digits`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.digits "passlib.totp.TOTP.digits"),
or use the class default.

| Parameters: | **token** – token as ascii bytes, unicode, or an integer. |
| Raises: | [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)") – if token has wrong number of digits, or contains non-numeric characters. |
| Returns: | token as `unicode` string, containing only digits 0-9. |

_classmethod_ `TOTP.` `normalize_time`( _time_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.normalize_time "Permalink to this definition")

Normalize time value to unix epoch seconds.

| Parameters: | **time** – Can be `None`, `datetime`,<br>or unix epoch timestamp as `float` or `int`.<br>If `None`, uses current system time.<br>Naive datetimes are treated as UTC. |
| Returns: | unix epoch timestamp as [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)"). |

## AppWallet [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#appwallet "Permalink to this headline")

The `AppWallet` class is used internally by the [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using") method
to store the application secrets provided for handling encrypted keys.
If needed, they can also be created and passed in directly.

_class_ `passlib.totp.` `AppWallet`( _secrets=None_, _default\_tag=None_, _encrypt\_cost=None_, _secrets\_path=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet "Permalink to this definition")

This class stores application-wide secrets that can be used
to encrypt & decrypt TOTP keys for storage.
It’s mostly an internal detail, applications usually just need
to pass `secrets` or `secrets_path` to [`TOTP.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP.using "passlib.totp.TOTP.using").

See also

[Storing TOTP instances](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-storing-instances) for more details on this workflow.

### Arguments [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#passlib.totp.AppWallet-arguments "Permalink to this headline")

| Parameters: | - **secrets** – <br>  Dict of application secrets to use when encrypting/decrypting<br>  stored TOTP keys. This should include a secret to use when encrypting<br>  new keys, but may contain additional older secrets to decrypt<br>  existing stored keys.<br>  <br>  The dict should map tags -> secrets, so that each secret is identified<br>  by a unique tag. This tag will be stored along with the encrypted<br>  key in order to determine which secret should be used for decryption.<br>  Tag should be string that starts with regex range `[a-z0-9]`,<br>  and the remaining characters must be in `[a-z0-9_.-]`.<br>  <br>  It is recommended to use something like a incremental counter<br>  (“1”, “2”, …), an ISO date (“2016-01-01”, “2016-05-16”, …), <br>  or a timestamp (“19803495”, “19813495”, …) when assigning tags.<br>  <br>  This mapping be provided in three formats:<br>  <br>  <br>  - A python dict mapping tag -> secret<br>  - A JSON-formatted string containing the dict<br>  - A multiline string with the format `"tag: value\ntag: value\n..."`<br>(This last format is mainly useful when loading from a text file via **secrets\_path**)<br>See also<br>[`generate_secret()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.generate_secret "passlib.totp.generate_secret") to create a secret with sufficient entropy<br>- **secrets\_path** – Alternately, callers can specify a separate file where the<br>  application-wide secrets are stored, using either of the string<br>  formats described in **secrets**.<br>- **default\_tag** – <br>  Specifies which tag in **secrets** should be used as the default<br>  for encrypting new keys. If omitted, the tags will be sorted,<br>  and the largest tag used as the default.<br>  <br>  if all tags are numeric, they will be sorted numerically;<br>  otherwise they will be sorted alphabetically.<br>  this permits tags to be assigned numerically,<br>  or e.g. using `YYYY-MM-DD` dates.<br>  <br>- **encrypt\_cost** – Optional time-cost factor for key encryption.<br>  This value corresponds to log2() of the number of PBKDF2<br>  rounds used. |

Warning

The application secret(s) should be stored in a secure location by
your application, and each secret should contain a large amount
of entropy (to prevent brute-force attacks if the encrypted keys
are leaked).

[`generate_secret()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.generate_secret "passlib.totp.generate_secret") is provided as a convenience helper
to generate a new application secret of suitable size.

Best practice is to load these values from a file via **secrets\_path**,
and then have your application give up permission to read this file
once it’s running.

### Public Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#passlib.totp.AppWallet-public-methods "Permalink to this headline")

`has_secrets` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet.has_secrets "Permalink to this definition")

whether at least one application secret is present

`default_tag` _= None_ [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet.default_tag "Permalink to this definition")

tag for default secret

### Semi-Private Methods [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#passlib.totp.AppWallet-semi-private-methods "Permalink to this headline")

The following methods are used internally by the [`TOTP`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.TOTP "passlib.totp.TOTP")
class in order to encrypt & decrypt keys using the provided application
secrets. They will generally not be publically useful, and may have their
API changed periodically.

`get_secret`( _tag_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet.get_secret "Permalink to this definition")

resolve a secret tag to the secret (as bytes).
throws a KeyError if not found.

`encrypt_key`( _key_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet.encrypt_key "Permalink to this definition")

Helper used to encrypt TOTP keys for storage.

| Parameters: | **key** – TOTP key to encrypt, as raw bytes. |
| Returns: | dict containing encrypted TOTP key & configuration parameters.<br>this format should be treated as opaque, and potentially subject<br>to change, though it is designed to be easily serialized/deserialized<br>(e.g. via JSON). |

Note

This function requires installation of the external
[cryptography](https://cryptography.io/) package.

To give some algorithm details: This function uses AES-256-CTR to encrypt
the provided data. It takes the application secret and randomly generated salt,
and uses PBKDF2-HMAC-SHA256 to combine them and generate the AES key & IV.

`decrypt_key`( _enckey_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet.decrypt_key "Permalink to this definition")

Helper used to decrypt TOTP keys from storage format.
Consults configured secrets to decrypt key.

| Parameters: | **source** – source object, as returned by [`encrypt_key()`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet.encrypt_key "passlib.totp.AppWallet.encrypt_key"). |
| Returns: | `(key, needs_recrypt)` –<br>**key** will be the decrypted key, as bytes.<br>**needs\_recrypt** will be a boolean flag indicating<br>whether encryption cost or default tag is too old,<br>and henace that key needs re-encrypting before storing. |

Note

This function requires installation of the external
[cryptography](https://cryptography.io/) package.

## Support Functions [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#support-functions "Permalink to this headline")

`passlib.totp.` `generate_secret`( _entropy=256_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.generate_secret "Permalink to this definition")

generate a random string suitable for use as an
[`AppWallet`](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#passlib.totp.AppWallet "passlib.totp.AppWallet") application secret.

| Parameters: | **entropy** – number of bits of entropy (controls size/complexity of password). |

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html\#deviations "Permalink to this headline")

- The TOTP Spec [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#totpspec) includes an param ( `T0`) providing an optional offset from the base time.
Passlib omits this parameter (fixing it at `0`), but so do pretty much all other TOTP implementations.

Footnotes

|     |     |
| --- | --- |
| \[1\] | _( [1](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#id1), [2](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#id4))_ TOTP Specification - [**RFC 6238**](https://tools.ietf.org/html/rfc6238.html) |

|     |     |
| --- | --- |
| \[2\] | HOTP Specification - [**RFC 4226**](https://tools.ietf.org/html/rfc4226.html) |

|     |     |
| --- | --- |
| [\[3\]](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#id2) | Google’s OTPAuth URI format -<br>[https://github.com/google/google-authenticator/wiki/Key-Uri-Format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format) |

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
  - [`passlib.totp` – TOTP / Two Factor Authentication](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#)
    - [Overview](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#overview)
    - [TOTP Class](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#totp-class)
    - [Alternate Constructors](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#alternate-constructors)
    - [Factory Creation](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#factory-creation)
    - [Basic Attributes](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#basic-attributes)
    - [Token Generation](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#token-generation)
      - [TotpToken](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#totptoken)
    - [Token Matching / Verification](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#token-matching-verification)
      - [TotpMatch](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#totpmatch)
    - [Client Configuration Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#client-configuration-methods)
    - [Serialization Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#serialization-methods)
    - [Helper Methods](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#helper-methods)
    - [AppWallet](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#appwallet)
    - [Support Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#support-functions)
    - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html#deviations)
  - [`passlib.utils` \- Helper Functions](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html "passlib.utils - Helper Functions")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html "passlib.registry - Password Handler Registry")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.totp.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.totp.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.totp.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)