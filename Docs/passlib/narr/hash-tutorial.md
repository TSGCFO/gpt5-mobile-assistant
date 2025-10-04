<!-- Source: https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html "CryptContext Tutorial")
- [previous](https://passlib.readthedocs.io/en/stable/narr/quickstart.html "New Application Quickstart Guide")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

# [`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html\#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") Tutorial [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#passwordhash-tutorial "Permalink to this headline")

## Overview [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#overview "Permalink to this headline")

Passlib supports a large number of hash algorithms,
all of which can be imported from the [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") module.
While the exact options and behavior will vary between each algorithm,
all of the hashes provided by Passlib use the same interface,
defined by the [`passlib.ifc.PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") abstract class.

The `PasswordHash` class provides a generic interface for interacting
individually with the various hashing algorithms.
It offers methods and attributes for a number of use-cases,
which fall into three general categories:

> - Creating & verifying hashes
> - Examining the configuration of a hasher,
> and customizing the defaults.
> - Assorting supplementary methods.

See also

- [`passlib.ifc`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#module-passlib.ifc "passlib.ifc: abstract interfaces used by Passlib") – API reference of all the methods and attributes
of the `PasswordHash` class.
- [passlib.context.CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial) –
For working with multiple hash formats at once
(such a user account table with multiple existing hash formats).

## Hashing & Verifying [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#hashing-verifying "Permalink to this headline")

While all the hashers in [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") offer a range of methods and attributes,
the main activities applications will need to perform is hashing and verifying passwords.
This can be done with the [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") and [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods.

Caution

**Changed in 1.7:**

Prior releases used [`PasswordHash.encrypt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.encrypt "passlib.ifc.PasswordHash.encrypt") for hashing,
which has now been renamed to [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash").
A compatibility alias is present in 1.7, but will be removed in Passlib 2.0.

### Hashing [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#hashing "Permalink to this headline")

First, import the desired hash. The following example uses the [`pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha256 "passlib.hash.pbkdf2_sha256") class
(which derives from `PasswordHash`):

```
>>> # import the desired hasher
>>> from passlib.hash import pbkdf2_sha256

```

Use [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") to hash a password. This call takes care of unicode encoding,
picking default rounds values, and generating a random salt:

```
>>> hash = pbkdf2_sha256.hash("password")
>>> hash
'$pbkdf2-sha256$29000$9t7be09prfXee2/NOUeotQ$Y.RDnnq8vsezSZSKy1QNy6xhKPdoBIwc.0XDdRm9sJ8'

```

Note that since each call generates a new salt, the contents of the resulting
hash will differ between calls (despite using the same password as input):

```
>>> hash2 = pbkdf2_sha256.hash("password")
>>> hash2
'$pbkdf2-sha256$29000$V0rJeS.FcO4dw/h/D6E0Bg$FyLs7omUppxzXkARJQSl.ozcEOhgp3tNgNsKIAhKmp8'
                      ^^^^^^^^^^^^^^^^^^^^^^

```

### Verifying [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#verifying "Permalink to this headline")

Subsequently, you can call [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") to check user input
against an existing hash:

```
>>> pbkdf2_sha256.verify("password", hash)
True

>>> pbkdf2_sha256.verify("joshua", hash)
False

```

### Unicode & non-ASCII Characters [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#unicode-non-ascii-characters "Permalink to this headline")

_Sidenote regarding unicode passwords & non-ASCII characters:_

For the majority of hash algorithms and use-cases, passwords should
be provided as either `unicode` (or `utf-8`-encoded `bytes`).

One exception is legacy hashes that were generated
using a different character encoding. In this case, passwords should be
encoded using the correct encoding before they are passed to `verify()`;
otherwise users may not be able to log in successfully.

For proper internationalization, applications should also take care to ensure
unicode inputs are normalized to a single representation before hashing.
The [`passlib.utils.saslprep()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.html#passlib.utils.saslprep "passlib.utils.saslprep") function can be used for this purpose.

## Customizing the Configuration [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#customizing-the-configuration "Permalink to this headline")

### The using() Method [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#the-using-method "Permalink to this headline")

Each hasher contains a number of [informational attributes](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#informational-attributes).
many of which can be customized to change the properties of the hashes
generated by [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"). When you want to change the defaults,
you don’t have to modify the hasher class directly, or pass in the options to each call to `PasswordHash.hash()`.

Instead, all the hashes offer a [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method.
This is a powerful method which accepts most hash informational attributes,
as well as some other hash-specific configuration keywords; and returns
a subclass of the original hasher (or a object with an identical interface).
The returned object inherits the defaults settings from it’s parent,
but integrates any values you choose to override.

Caution

**Changed in 1.7:**

Prior releases required you to pass custom settings to each [`PasswordHash.encrypt()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.encrypt "passlib.ifc.PasswordHash.encrypt") call.
That usage pattern is deprecated, and will be removed in Passlib 2.0;
code should be switched to use [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using"), as shown below.

### Usage Example [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#usage-example "Permalink to this headline")

As an example, if the hasher you select supports a variable number of iterations
(such as [`pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha256 "passlib.hash.pbkdf2_sha256")), you can specify a custom value
using the `rounds` keyword.

Here, the default class uses 29000 rounds:

```
>>> from passlib.hash import pbkdf2_sha256

>>> pbkdf2_sha256.default_rounds
29000

>>> pbkdf2_sha256.hash("password")
'$pbkdf2-sha256$29000$V0rJeS.FcO4dw/h/D6E0Bg$FyLs7omUppxzXkARJQSl.ozcEOhgp3tNgNsKIAhKmp8'
                ^^^^^

```

But if we call [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using"), we can override this value:

```
>>> custom_pbkdf2 = pbkdf2_sha256.using(rounds=123456)
>>> custom_pbkdf2.default_rounds
123456

>>> custom_pbkdf2.hash("password")
'$pbkdf2-sha256$123456$QwjBmJPSOsf4HyNE6L239g$8m1pnP69EYeOiKKb5sNSiYw9M8pJMyeW.CSm0KKO.GI'
                ^^^^^^

```

### Other Keywords [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#other-keywords "Permalink to this headline")

While hashes frequently have additional keywords supported by using,
the basic set of settings you can customize can be found by inspecting
the [`PasswordHash.setting_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.setting_kwds "passlib.ifc.PasswordHash.setting_kwds") attribute:

```
>>> pbkdf2_sha256.settings_kwds
("salt", "salt_size", "rounds")

```

For instance, the following generates pbkdf2 hashes with a 32-byte salt
instead of the default 16:

```
>>> pbkdf2_sha256.using(salt_size=8).hash("password")
'$pbkdf2-sha256$29000$tPZ.r5UyZgyhNEaI8Z5z7r1X6p1zTknJ.T/nHINwbq0$RlM49Qf5qRraHx.L7gq3hKIKSMLttrG1zWmWXyfXqc8'
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

This method is also used internally by the [CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial)
class it order to create a custom hasher configured based on the CryptContext policy
it was provided.

See also

- [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") – API reference

## Context Keywords [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#context-keywords "Permalink to this headline")

While the [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") example above works for most hashes,
a small number of algorithms require you provide external data
(such as a username) every time a hash is calculated.

An example of this is the [`oracle10`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.oracle10.html#passlib.hash.oracle10 "passlib.hash.oracle10") hash,
where hashing requires a username:

```
>>> from passlib.hash import oracle10
>>> hash = oracle10.hash("secret", user="admin")
'B858CE295C95193F'

```

The difference between this and specifying something like a rounds setting
(see [Customizing the Configuration](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hash-configuring) above) is that a configuration option
only needs to be specified once, and is then encoded into the hash string itself…
Whereas a context keyword represents something that isn’t stored in the hash string,
and needs to be specified every time you call [`PasswordHash.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash") **or** [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify"):

```
>>> oracle10.verify("secret", hash, user="admin")
True

```

In this example, if either the username OR password is wrong,
verify() will fail:

```
>>> oracle10.verify("secret", hash, user="wronguser")
False

>>> oracle10.verify("wrongpassword", hash, user="admin")
False

```

Forgetting to include a context keywords when it’s required will cause a TypeError:

```
>>> hash = oracle10.hash("password")
Traceback (most recent call last):
    <traceback omitted>
TypeError: user must be unicode or bytes, not None

```

Whether a hash requires external parameters (such as `user`)
can be determined from its documentation page; but also programmatically from
its [`PasswordHash.context_kwds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.context_kwds "passlib.ifc.PasswordHash.context_kwds") attribute:

```
>>> oracle10.context_kwds
("user",)

>>> pbkdf2_sha256.context_kwds
()

```

## Identifying Hashes [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#identifying-hashes "Permalink to this headline")

One of the rarer use-cases is the need to identify whether a string
recognizably belongs to a given hasher class. This can be important
in some cases, because attempting to call [`PasswordHash.verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify")
with another algorithm’s hash will result in a ValueError:

```
>>> from passlib.hash import pbkdf2_sha256, md5_crypt

>>> other_hash = md5_crypt.hash("password")

>>> pbkdf2_sha256.verify("password", other_hash)
Traceback (most recent call last):
    <traceback omitted>
ValueError: not a valid pbkdf2_sha256 hash

```

This can be prevented by using the identify method,
which determines whether a hash belongs to a given algorithm:

```
>>> hash = pbkdf2_sha256.hash("password")
>>> pbkdf2_sha256.identify(hash)
True

>>> pbkdf2_sha256.identify(other_hash)
False

```

See also

In most cases where an application needs to
distinguish between multiple hash formats, it will be more useful to switch to
a [CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial) object, which automatically handles this
and many similar tasks.

Todo

Document usage of [`PasswordHash.needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.needs_update "passlib.ifc.PasswordHash.needs_update"),
and how it ties into [`PasswordHash.using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using").

## Choosing the right rounds value [¶](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html\#choosing-the-right-rounds-value "Permalink to this headline")

For hash algorithms with a variable time-cost,
Passlib’s [`PasswordHash.default_rounds`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.default_rounds "passlib.ifc.PasswordHash.default_rounds") values attempt to be secure enough for
the average [\[1\]](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#avgsys) system. But the “right” value for a given hash
is dependant on the server, its cpu, its expected load, and its users.
Since larger values mean increased work for an attacker…

**The right `rounds` value for a given hash & server should be the largest**
**possible value that doesn’t cause intolerable delay for your users.**

For most public facing services, you can generally have signin
take upwards of 250ms - 400ms before users start getting annoyed.
For superuser accounts, it should take as much time as the admin can stand
(usually ~4x more delay than a regular account).

Passlib’s `default_rounds` values are retuned periodically,
starting with a rough estimate of what an “average” system is capable of,
and then setting all `hash.default_rounds` values to take ~300ms on such a system.
However, some older algorithms (e.g. [`bsdi_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bsdi_crypt.html#passlib.hash.bsdi_crypt "passlib.hash.bsdi_crypt")) are weak enough that
a tradeoff must be made, choosing “more secure but intolerably slow” over “fast but unacceptably insecure”.

For this reason, it is strongly recommended to not use a value much lower than Passlib’s default,
and to use one of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes), as one of their chief qualifying
features is the mere _existence_ of rounds values which take a short enough amount of time,
and yet are still considered secure.

Todo

Expand this section into a full document, including
information from the following posts:

- [http://stackoverflow.com/questions/13545677/python-passlib-what-is-the-best-value-for-rounds](http://stackoverflow.com/questions/13545677/python-passlib-what-is-the-best-value-for-rounds)
- [http://stackoverflow.com/questions/11829602/pbkdf2-and-hash-comparison](http://stackoverflow.com/questions/11829602/pbkdf2-and-hash-comparison)

As well as maybe JS-interactive calculation helper.

|     |     |
| --- | --- |
| [\[1\]](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#id1) | For Passlib 1.6.3, all hashes were retuned to take ~300ms on a<br>system with a 3.0 ghz 64 bit CPU. |

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
  - [Installation](https://passlib.readthedocs.io/en/stable/install.html)
  - [Library Overview](https://passlib.readthedocs.io/en/stable/narr/overview.html)
  - [New Application Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html)
  - [`PasswordHash` Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#)
    - [Overview](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#overview)
    - [Hashing & Verifying](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hashing-verifying)
      - [Hashing](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#hashing)
      - [Verifying](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#verifying)
      - [Unicode & non-ASCII Characters](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#unicode-non-ascii-characters)
    - [Customizing the Configuration](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#customizing-the-configuration)
      - [The using() Method](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#the-using-method)
      - [Usage Example](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#usage-example)
      - [Other Keywords](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#other-keywords)
    - [Context Keywords](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#context-keywords)
    - [Identifying Hashes](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#identifying-hashes)
    - [Choosing the right rounds value](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#choosing-the-right-rounds-value)
  - [`CryptContext` Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html)
  - [`TOTP` Tutorial](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html "CryptContext Tutorial")
- [previous](https://passlib.readthedocs.io/en/stable/narr/quickstart.html "New Application Quickstart Guide")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/narr/hash-tutorial.html)**[stable](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/narr/hash-tutorial.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)