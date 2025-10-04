<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html "passlib.hash - Password Hashing Schemes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html "passlib.exc - Exceptions and warnings")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.ext.django`](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html\#module-passlib.ext.django "passlib.ext.django") \- Django Password Hashing Plugin [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html\#passlib-ext-django-django-password-hashing-plugin "Permalink to this headline")

Warning

This extension is a high maintenance, with an uncertain number of users.
The current plan is to split this out as a separate package concurrent
with Passlib 1.8, and then judge whether it should continue to be maintained
in it’s own right. See [issue 81](https://foss.heptapod.net/python-libs/passlib/issues/81).

This module contains a [Django](http://www.djangoproject.com/) plugin which
overrides all of Django’s password hashing functions, replacing them
with wrappers around a Passlib [CryptContext](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-reference) object
whose configuration is controlled from Django’s `settings`.
While this extension’s utility is diminished with the advent
of Django 1.4’s _hashers_ framework, this plugin still has a number
of uses:

- Make use of the new Django 1.4 [pbkdf2 & bcrypt formats](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html#django-1-4-hashes),
even under earlier Django releases.
- Allow your application to work with any password hash format
[supported](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) by Passlib, allowing you to import
existing hashes from other systems.
Common examples include SHA512-Crypt, PHPass, and BCrypt.
- Set different iterations / cost settings based on the type of user account,
and automatically update hashes that use weaker settings when the user
logs in.
- Mark any hash algorithms as deprecated, and automatically migrate to stronger
hashes when the user logs in.

Note

This plugin should be considered “release candidate” quality.
It works, and has good unittest coverage, but has seen only
limited real-world use. Please report any issues.
It has been tested with Django 1.8 - 3.1.

New in version 1.6.

Changed in version 1.7: Support for Django 1.0 - 1.7 was dropped; now requires Django 1.8 or newer.

Warning

As of Passlib 1.8, this module will require Django 2.2 or newer.

## Installation [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html\#installation "Permalink to this headline")

Installation is simple: once Passlib itself has been installed, just add
`"passlib.ext.django"` to Django’s `settings.INSTALLED_APPS`,
as soon as possible after `django.contrib.auth`.

Once installed, this plugin will automatically monkeypatch
Django to use a Passlib `CryptContext`
instance in place of the normal Django password authentication routines
(as an unfortunate side effect, this disables Django 1.4’s hashers framework entirely,
though the default configuration supports all the built-in Django 1.4 hashers).

## Configuration [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html\#configuration "Permalink to this headline")

While this plugin will function perfectly well without setting any configuration
options, you can customize it using the following options in Django’s `settings.py`:

`PASSLIB_CONFIG`

> This option specifies the CryptContext configuration options
> that will be used when the plugin is loaded.
>
> - Its value will usually be an INI-formatted string or a dictionary, containing
> options to be passed to [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext").
> - Alternately, it can be the name of any preset supported by
> [`get_preset_config()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#passlib.ext.django.utils.get_preset_config "passlib.ext.django.utils.get_preset_config"), such as
> `"passlib-default"` or `"django-default"`.
> - Finally, it can be the special string `"disabled"`, which will disable
> this plugin.
>
> At any point after this plugin has been loaded, you can serialize
> its current configuration to a string:
>
> ```
> >>> from passlib.ext.django.models import password_context
> >>> print password_context.to_string()
>
> ```
>
> This string can then be modified, and used as the new value
> of `PASSLIB_CONFIG`.
>
> Note
>
> It is _strongly_ recommended to use a configuration which will support
> the existing Django hashes. Dumping and then modifying one of the
> preset strings is a good starting point.

`PASSLIB_GET_CATEGORY`

> > By default, Passlib will assign users to one of three categories:
> > `"superuser"`, `"staff"`, or `None`; based on the attributes
> > of the `User` object. This allows `PASSLIB_CONFIG`
> > to have per-category policies, such as a larger number of iterations
> > for the superuser account.
> >
> > This option allows overriding the function which performs this mapping,
> > so that more fine-grained / alternate user categories can be used.
> > If specified, the function should have the call syntax
> > `get_category(user) -> category_string|None`.
>
> See also
>
> See [User Categories](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories) for more details.

`PASSLIB_CONTEXT`

> Deprecated since version 1.6: This is a deprecated alias for `PASSLIB_CONFIG`,
> used by the (undocumented) version of this plugin that was
> released with Passlib 1.5. It should not be used by new applications.

## Module Contents [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html\#module-passlib.ext.django.models "Permalink to this headline")

`passlib.ext.django.models.` `password_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#passlib.ext.django.models.password_context "Permalink to this definition")

The `CryptContext` instance that drives this plugin.
It can be imported and examined to inspect the current configuration,
changes made to it will immediately alter how Django hashes passwords.

(Do not replace the reference with another CryptContext, it will break things;
just update the context in-place).

`passlib.ext.django.models.` `context_changed`() [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#passlib.ext.django.models.context_changed "Permalink to this definition")

If the context is modified after loading, call this function to clear internal caches.

`passlib.ext.django.utils.` `get_preset_config`( _name_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#passlib.ext.django.utils.get_preset_config "Permalink to this definition")

Returns configuration string for one of the preset strings
supported by the `PASSLIB_CONFIG` setting.
Currently supported presets:

- `"passlib-default"` \- default config used by this release of passlib.
- `"django-default"` \- config matching currently installed django version.
- `"django-latest"` \- config matching newest django version (currently same as `"django-1.6"`).
- `"django-1.0"` \- config used by stock Django 1.0 - 1.3 installs
- `"django-1.4"` \- config used by stock Django 1.4 installs
- `"django-1.6"` \- config used by stock Django 1.6 installs

`passlib.ext.django.utils.` `PASSLIB_DEFAULT` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#passlib.ext.django.utils.PASSLIB_DEFAULT "Permalink to this definition")

This constant contains the default configuration for `PASSLIB_CONFIG`.
It provides the following features:

- uses [`django_pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html#passlib.hash.django_pbkdf2_sha256 "passlib.hash.django_pbkdf2_sha256") as the default algorithm.
- supports all of the Django 1.0-1.4 [hash formats](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html).
- additionally supports SHA512-Crypt, BCrypt, and PHPass.
- is configured to use a larger number of rounds for the superuser account.
- is configured to automatically migrate all Django 1.0 hashes
to use the default hash as soon as each user logs in.

As of Passlib 1.6, it contains the following string:

```
[passlib]

; list of schemes supported by configuration
; currently all django 1.4 hashes, django 1.0 hashes,
; and three common modular crypt format hashes.
schemes =
    django_pbkdf2_sha256, django_pbkdf2_sha1, django_bcrypt,
    django_salted_sha1, django_salted_md5, django_des_crypt, hex_md5,
    sha512_crypt, bcrypt, phpass

; default scheme to use for new hashes
default = django_pbkdf2_sha256

; hashes using these schemes will automatically be re-hashed
; when the user logs in (currently all django 1.0 hashes)
deprecated =
    django_pbkdf2_sha1, django_salted_sha1, django_salted_md5,
    django_des_crypt, hex_md5

; sets some common options, including minimum rounds for two primary hashes.
; if a hash has less than this number of rounds, it will be re-hashed.
all__vary_rounds = 0.05
sha512_crypt__min_rounds = 80000
django_pbkdf2_sha256__min_rounds = 10000

; set somewhat stronger iteration counts for ``User.is_staff``
staff__sha512_crypt__default_rounds = 100000
staff__django_pbkdf2_sha256__default_rounds = 12500

; and even stronger ones for ``User.is_superuser``
superuser__sha512_crypt__default_rounds = 120000
superuser__django_pbkdf2_sha256__default_rounds = 15000

```

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
  - [`passlib.ext.django` \- Django Password Hashing Plugin](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#)
    - [Installation](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#installation)
    - [Configuration](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#configuration)
    - [Module Contents](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#module-passlib.ext.django.models)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html "passlib.hash - Password Hashing Schemes")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html "passlib.exc - Exceptions and warnings")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.ext.django.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.ext.django.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)