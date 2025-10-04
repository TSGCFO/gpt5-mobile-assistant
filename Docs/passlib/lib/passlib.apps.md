<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html "passlib.context - CryptContext Hash Manager")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html "passlib.apache - Apache Password Files")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.apps`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#module-passlib.apps "passlib.apps: hashing & verifying passwords used in sql servers and other applications") \- Helpers for various applications [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#module-passlib.apps "Permalink to this headline")

This module contains a number of preconfigured [CryptContext](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-reference) instances
that are provided by Passlib for easily handling the hash formats used by various applications.

## Usage Example [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#usage-example "Permalink to this headline")

The `CryptContext` class itself has a large number of features,
but to give an example of how to quickly use the instances in this module:

Each of the objects in this module can be imported directly:

```
>>> # as an example, this imports the custom_app_context object,
>>> # a helper to let new applications *quickly* add password hashing.
>>> from passlib.apps import custom_app_context

```

Hashing a password is simple (and salt generation is handled automatically):

```
>>> hash = custom_app_context.hash("toomanysecrets")
>>> hash
'$5$rounds=84740$fYChCy.52EzebF51$9bnJrmTf2FESI93hgIBFF4qAfysQcKoB0veiI0ZeYU4'

```

Verifying a password against an existing hash is just as quick:

```
>>> custom_app_context.verify("toomanysocks", hash)
False
>>> custom_app_context.verify("toomanysecrets", hash)
True

```

See also

the [CryptContext Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial)
and [CryptContext Reference](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-reference)
for more information about the CryptContext class.

## Django [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#django "Permalink to this headline")

The following objects provide pre-configured `CryptContext` instances
for handling [Django](http://www.djangoproject.com/)
password hashes, as used by Django’s `django.contrib.auth` module.
They recognize all the [builtin Django hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html)
supported by the particular Django version.

Note

These objects may not match the hashes in your database if a third-party
library has been used to patch Django to support alternate hash formats.
This includes the [django-bcrypt](http://pypi.python.org/pypi/django-bcrypt)
plugin, or Passlib’s builtin [`django extension`](https://passlib.readthedocs.io/en/stable/lib/passlib.ext.django.html#module-passlib.ext.django "passlib.ext.django").
As well, Django 1.4 introduced a very configurable “hashers” framework,
and individual deployments may support additional hashes and/or
have other defaults.

`passlib.apps.` `django10_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.django10_context "Permalink to this definition")

The object replicates the password hashing policy for Django 1.0-1.3.
It supports all the Django 1.0 hashes, and defaults to
[`django_salted_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html#passlib.hash.django_salted_sha1 "passlib.hash.django_salted_sha1").

New in version 1.6.

`passlib.apps.` `django14_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.django14_context "Permalink to this definition")

The object replicates the stock password hashing policy for Django 1.4.
It supports all the Django 1.0 & 1.4 hashes, and defaults to
[`django_pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html#passlib.hash.django_pbkdf2_sha256 "passlib.hash.django_pbkdf2_sha256"). It treats all
Django 1.0 hashes as deprecated.

New in version 1.6.

`passlib.apps.` `django16_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.django16_context "Permalink to this definition")

The object replicates the stock password hashing policy for Django 1.6.
It supports all the Django 1.0-1.6 hashes, and defaults to
[`django_pbkdf2_sha256`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.django_std.html#passlib.hash.django_pbkdf2_sha256 "passlib.hash.django_pbkdf2_sha256"). It treats all
Django 1.0 hashes as deprecated.

New in version 1.6.2.

`passlib.apps.` `django_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.django_context "Permalink to this definition")

This alias will always point to the latest preconfigured Django
context supported by Passlib, and as such should support
all historical hashes built into Django.

Changed in version 1.6.2: This now points to [`django16_context`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.django16_context "passlib.apps.django16_context").

## LDAP [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#ldap "Permalink to this headline")

Passlib provides two contexts related to ldap hashes:

`passlib.apps.` `ldap_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.ldap_context "Permalink to this definition")

This object provides a pre-configured `CryptContext` instance
for handling LDAPv2 password hashes. It recognizes all
the [standard ldap hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#standard-ldap-hashes).

It defaults to using the `{SSHA}` password hash.
For times when there should be another default, using code such as the following:

```
>>> from passlib.apps import ldap_context
>>> ldap_context = ldap_context.replace(default="ldap_salted_md5")

>>> # the new context object will now default to {SMD5}:
>>> ldap_context.hash("password")
'{SMD5}T9f89F591P3fFh1jz/YtW4aWD5s='

```

`passlib.apps.` `ldap_nocrypt_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.ldap_nocrypt_context "Permalink to this definition")

This object recognizes all the standard ldap schemes that `ldap_context`
does, _except_ for the `{CRYPT}`-based schemes.

## MySQL [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#mysql "Permalink to this headline")

This module provides two pre-configured `CryptContext` instances
for handling MySQL user passwords:

`passlib.apps.` `mysql_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.mysql_context "Permalink to this definition")

This object should recognize the new [`mysql41`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql41.html#passlib.hash.mysql41 "passlib.hash.mysql41") hashes,
as well as any legacy [`mysql323`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#passlib.hash.mysql323 "passlib.hash.mysql323") hashes.

It defaults to mysql41 when generating new hashes.

This should be used with MySQL version 4.1 and newer.

`passlib.apps.` `mysql3_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.mysql3_context "Permalink to this definition")

This object is for use with older MySQL deploys which only recognize
the [`mysql323`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.mysql323.html#passlib.hash.mysql323 "passlib.hash.mysql323") hash.

This should be used only with MySQL version 3.2.3 - 4.0.

## PHPass [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#phpass "Permalink to this headline")

[PHPass](http://www.openwall.com/phpass/) is a PHP password hashing library,
and hashes derived from it are found in a number of PHP applications.
It is found in a wide range of PHP applications, including Drupal and Wordpress.

`passlib.apps.` `phpass_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.phpass_context "Permalink to this definition")

This object following the standard PHPass logic:
it supports [`bcrypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt "passlib.hash.bcrypt"), [`bsdi_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bsdi_crypt.html#passlib.hash.bsdi_crypt "passlib.hash.bsdi_crypt"),
and implements an custom scheme called the “phpass portable hash” [`phpass`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html#passlib.hash.phpass "passlib.hash.phpass") as a fallback.

BCrypt is used as the default if support is available,
otherwise the Portable Hash will be used as the default.

Changed in version 1.5: Now uses Portable Hash as fallback if BCrypt isn’t available.
Previously used BSDI-Crypt as fallback
(per original PHPass implementation),
but it was decided PHPass is in fact more secure.

`passlib.apps.` `phpbb3_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.phpbb3_context "Permalink to this definition")

This object supports phpbb3 password hashes, which use a variant of [`phpass`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html#passlib.hash.phpass "passlib.hash.phpass").

## PostgreSQL [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#postgresql "Permalink to this headline")

`passlib.apps.` `postgres_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.postgres_context "Permalink to this definition")

This object should recognize password hashes stores in PostgreSQL’s `pg_shadow` table;
which are all assumed to follow the [`postgres_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.postgres_md5.html#passlib.hash.postgres_md5 "passlib.hash.postgres_md5") format.

Note that the username must be provided whenever hashing or verifying a postgres hash:

```
>>> from passlib.apps import postgres_context

>>> # hashing a password...
>>> postgres_context.hash("somepass", user="dbadmin")
'md578ed0f0ab2be0386645c1b74282917e7'

>>> # verifying a password...
>>> postgres_context.verify("somepass", 'md578ed0f0ab2be0386645c1b74282917e7', user="dbadmin")
True
>>> postgres_context.verify("wrongpass", 'md578ed0f0ab2be0386645c1b74282917e7', user="dbadmin")
False

>>> # forgetting the user will result in an error:
>>> postgres_context.hash("somepass")
Traceback (most recent call last):
    <traceback omitted>
TypeError: user must be unicode or bytes, not None

```

## Roundup [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#roundup "Permalink to this headline")

The [Roundup Issue Tracker](http://www.roundup-tracker.org/) has long
supported a series of different methods for encoding passwords.
The following contexts are available for reading Roundup password hash fields:

`passlib.apps.` `roundup10_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.roundup10_context "Permalink to this definition")

This object should recognize all password hashes used by Roundup 1.4.16 and earlier:
[`ldap_hex_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.ldap_hex_sha1 "passlib.hash.ldap_hex_sha1") (the default),
[`ldap_hex_md5`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.ldap_hex_md5 "passlib.hash.ldap_hex_md5"), [`ldap_des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_crypt.html#passlib.hash.ldap_des_crypt "passlib.hash.ldap_des_crypt"),
and [`roundup_plaintext`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_other.html#passlib.hash.roundup_plaintext "passlib.hash.roundup_plaintext").

`passlib.apps.` `roundup15_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.roundup15_context "Permalink to this definition")

Roundup 1.4.17 adds support for [`ldap_pbkdf2_sha1`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.ldap_pbkdf2_digest.html#passlib.hash.ldap_pbkdf2_sha1 "passlib.hash.ldap_pbkdf2_sha1")
as its preferred hash format.
This context supports all the [`roundup10_context`](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.roundup10_context "passlib.apps.roundup10_context") hashes,
but adds that hash as well (and uses it as the default).

`passlib.apps.` `roundup_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.roundup_context "Permalink to this definition")

this is an alias for the latest version-specific roundup context supported
by passlib, currently the `roundup15_context`.

## Custom Applications [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html\#custom-applications "Permalink to this headline")

`passlib.apps.` `custom_app_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#passlib.apps.custom_app_context "Permalink to this definition")

This `CryptContext` object is provided for new python applications
to quickly and easily add password hashing support.
It comes preconfigured with:

- Support for [`sha256_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html#passlib.hash.sha256_crypt "passlib.hash.sha256_crypt") and [`sha512_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha512_crypt.html#passlib.hash.sha512_crypt "passlib.hash.sha512_crypt")
- Defaults to SHA256-Crypt under 32 bit systems, SHA512-Crypt under 64 bit systems.
- Large number of `rounds`, for increased time-cost to hedge against attacks.

For applications which want to quickly add a password hash,
all they need to do is import and use this object, per the
[usage example](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#predefined-context-example) at the top of this page.

See also

The [New Application Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html) for additional details.

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
  - [`passlib.apache` \- Apache Password Files](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html)
  - [`passlib.apps` \- Helpers for various applications](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#)
    - [Usage Example](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#usage-example)
    - [Django](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#django)
    - [LDAP](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#ldap)
    - [MySQL](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#mysql)
    - [PHPass](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#phpass)
    - [PostgreSQL](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#postgresql)
    - [Roundup](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#roundup)
    - [Custom Applications](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html#custom-applications)
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
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html "passlib.context - CryptContext Hash Manager")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.apache.html "passlib.apache - Apache Password Files")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.apps.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.apps.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.apps.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)