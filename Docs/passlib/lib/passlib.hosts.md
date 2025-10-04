<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html "passlib.ifc – Password Hash Interface")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html "passlib.hash.plaintext - Plaintext")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.hosts`](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html\#module-passlib.hosts "passlib.hosts: hashing & verifying operating system passwords") \- OS Password Handling [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html\#module-passlib.hosts "Permalink to this headline")

This module provides some preconfigured [CryptContext](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-reference)
instances for hashing & verifying password hashes tied to user accounts of various operating systems.
While (most) of the objects are available cross-platform,
their use is oriented primarily towards Linux and BSD variants.

See also

for Microsoft Windows, see the list of [MS Windows Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#windows-hashes)
in [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib").

## Usage Example [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html\#usage-example "Permalink to this headline")

The `CryptContext` class itself has a large number of features,
but to give an example of how to quickly use the instances in this module:

Each of the objects in this module can be imported directly:

```
>>> # as an example, this imports the linux_context object,
>>> # which is configured to recognized most hashes found in Linux /etc/shadow files.
>>> from passlib.apps import linux_context

```

Hashing a password is simple (and salt generation is handled automatically):

```
>>> hash = linux_context.hash("toomanysecrets")
>>> hash
'$5$rounds=84740$fYChCy.52EzebF51$9bnJrmTf2FESI93hgIBFF4qAfysQcKoB0veiI0ZeYU4'

```

Verifying a password against an existing hash is just as quick:

```
>>> linux_context.verify("toomanysocks", hash)
False
>>> linux_context.verify("toomanysecrets", hash)
True

```

You can also identify hashes::

```
>>> linux_context.identify(hash)
'sha512_crypt'

```

Or encrypt using a specific algorithm::

```
>>> linux_context.schemes()
('sha512_crypt', 'sha256_crypt', 'md5_crypt', 'des_crypt', 'unix_disabled')
>>> linux_context.hash("password", scheme="des_crypt")
'2fmLLcoHXuQdI'
>>> linux_context.identify('2fmLLcoHXuQdI')
'des_crypt'

```

See also

the [CryptContext Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-tutorial)
and [CryptContext Reference](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-reference)
for more information about the CryptContext class.

## Unix Password Hashes [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html\#unix-password-hashes "Permalink to this headline")

Passlib provides a number of pre-configured `CryptContext` instances
which can identify and manipulate all the formats used by Linux and BSD.
See the [modular crypt identifier list](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#mcf-identifiers) for a complete
list of which hashes are supported by which operating system.

### Predefined Contexts [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html\#predefined-contexts "Permalink to this headline")

Passlib provides `CryptContext` instances
for the following Unix variants:

`passlib.hosts.` `linux_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#passlib.hosts.linux_context "Permalink to this definition")

context instance which recognizes hashes used
by the majority of Linux distributions.
encryption defaults to `sha512_crypt`.

`passlib.hosts.` `freebsd_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#passlib.hosts.freebsd_context "Permalink to this definition")

context instance which recognizes all hashes used by FreeBSD 8.
encryption defaults to `bcrypt`.

`passlib.hosts.` `netbsd_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#passlib.hosts.netbsd_context "Permalink to this definition")

context instance which recognizes all hashes used by NetBSD.
encryption defaults to `bcrypt`.

`passlib.hosts.` `openbsd_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#passlib.hosts.openbsd_context "Permalink to this definition")

context instance which recognizes all hashes used by OpenBSD.
encryption defaults to `bcrypt`.

Note

All of the above contexts include the [`unix_disabled`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.unix_disabled.html#passlib.hash.unix_disabled "passlib.hash.unix_disabled") handler
as a final fallback. This special handler treats all strings as invalid passwords,
particularly the common strings `!` and `*` which are used to indicate
that an account has been disabled [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#shadow).

### Current Host OS [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html\#current-host-os "Permalink to this headline")

`passlib.hosts.` `host_context` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#passlib.hosts.host_context "Permalink to this definition")

| Platform: | Unix |

This [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") instance should detect and support
all the algorithms the native OS `crypt()` offers.
The main differences between this object and `crypt()`:

- this object provides introspection about _which_ schemes
are available on a given system (via `host_context.schemes()`).
- it defaults to the strongest algorithm available,
automatically configured to an appropriate strength
for hashing new passwords.
- whereas `crypt()` typically defaults to using
[`des_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html#passlib.hash.des_crypt "passlib.hash.des_crypt"); and provides little introspection.

As an example, this can be used in conjunction with stdlib’s `spwd` module
to verify user passwords on the local system:

```
>>> # NOTE/WARNING: this example requires running as root on most systems.
>>> import spwd, os
>>> from passlib.hosts import host_context
>>> hash = spwd.getspnam(os.environ['USER']).sp_pwd
>>> host_context.verify("toomanysecrets", hash)
True

```

Changed in version 1.4: This object is only available on systems where the stdlib `crypt` module is present.
In version 1.3 and earlier, it was available on non-Unix systems, though it did nothing useful.

Footnotes

|     |     |
| --- | --- |
| [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#id1) | Man page for Linux /etc/shadow - [http://linux.die.net/man/5/shadow](http://linux.die.net/man/5/shadow) |

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
  - [`passlib.hosts` \- OS Password Handling](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#)
    - [Usage Example](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#usage-example)
    - [Unix Password Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#unix-password-hashes)
      - [Predefined Contexts](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#predefined-contexts)
      - [Current Host OS](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html#current-host-os)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html "passlib.ifc – Password Hash Interface")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.plaintext.html "passlib.hash.plaintext - Plaintext")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hosts.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hosts.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hosts.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)