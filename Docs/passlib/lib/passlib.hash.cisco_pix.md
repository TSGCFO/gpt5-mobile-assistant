<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html "passlib.hash.cisco_asa - Cisco ASA MD5 hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html "passlib.hash.cisco_type7 - Cisco “Type 7” hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.cisco_pix`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#passlib.hash.cisco_pix "passlib.hash.cisco_pix") \- Cisco PIX MD5 hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#passlib-hash-cisco-pix-cisco-pix-md5-hash "Permalink to this headline")

Danger

**This algorithm is not considered secure by modern standards.**
It should only be used when verifying existing hashes,
or when interacting with applications that require this format.
For new code, see the list of [recommended hashes](https://passlib.readthedocs.io/en/stable/narr/quickstart.html#recommended-hashes).

New in version 1.6.

## Overview [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#overview "Permalink to this headline")

Todo

**Caveat Emptor**

Passlib’s implementations of [`cisco_pix`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_pix "passlib.hash.cisco_pix") and [`cisco_asa`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_asa "passlib.hash.cisco_asa") both need verification.
For those with access to Cisco PIX and ASA systems, verifying Passlib’s reference vectors
would be a great help (see [issue 51](https://foss.heptapod.net/python-libs/passlib/issues/51)). In the mean time, there are no guarantees
that passlib correctly replicates the official implementation.

Changed in version 1.7.1: A number of [bugs](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib-asa96-bug) were fixed after expanding
the reference vectors, and testing against an ASA 9.6 system.

The [`cisco_asa`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_asa "passlib.hash.cisco_asa") class implements the “encrypted” password hash algorithm commonly found on Cisco
ASA systems. The companion [`cisco_pix`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_pix "passlib.hash.cisco_pix") class
implements the older variant found on Cisco PIX.
Aside from internal differences, and slightly different limitations,
the two hashes have the same format, and in some cases the same output.

These classes can be used directly to generate or verify a hash for a specific
user. Specifying the user account name is required for this hash:

```
>>> from passlib.hash import cisco_asa

>>> # hash password using specified username
>>> hash = cisco_asa.hash("password", user="user")
>>> hash
'A5XOy94YKDPXCo7U'

>>> # verify correct password
>>> cisco_asa.verify("password", hash, user="user")
True

>>> # verify correct password w/ wrong username
>>> cisco_asa.verify("password", hash, user="other")
False

>>> # verify incorrect password
>>> cisco_asa.verify("letmein", hash, user="user")
False

```

The main “enable” password can be hashes / verified just by omitting
the `user` parameter, or setting `user=""`:

```
>>> # hash password without associated user account
>>> hash2 = cisco_asa.hash("password")
>>> hash2
'NuLKvvWGg.x9HEKO'

>>> # verify password without associated user account
>>> cisco_asa.verify("password", hash2)
True

```

See also

the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)

## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#interface "Permalink to this headline")

_class_ `passlib.hash.` `cisco_pix` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_pix "Permalink to this definition")

This class implements the password hash used by older Cisco PIX firewalls,
and follows the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).
It does a single round of hashing, and relies on the username
as the salt.

This class only allows passwords <= 16 bytes, anything larger
will result in a [`PasswordSizeError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordSizeError "passlib.exc.PasswordSizeError") if passed to `hash()`,
and be silently rejected if passed to `verify()`.

The [`hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.hash "passlib.ifc.PasswordHash.hash"),
[`genhash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.genhash "passlib.ifc.PasswordHash.genhash"), and
[`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.verify "passlib.ifc.PasswordHash.verify") methods
all support the following extra keyword:

| Parameters: | **user** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>String containing name of user account this password is associated with.<br>This is _required_ in order to correctly hash passwords associated<br>with a user account on the Cisco device, as it is used to salt<br>the hash.<br>Conversely, this _must_ be omitted or set to `""` in order to correctly<br>hash passwords which don’t have an associated user account<br>(such as the “enable” password). |

New in version 1.6.

Changed in version 1.7.1: Passwords > 16 bytes are now rejected / throw error instead of being silently truncated,
to match Cisco behavior. A number of [bugs](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib-asa96-bug) were fixed
which caused prior releases to generate unverifiable hashes in certain cases.

_class_ `passlib.hash.` `cisco_asa` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_asa "Permalink to this definition")

This class implements the password hash used by Cisco ASA/PIX 7.0 and newer (2005).
Aside from a different internal algorithm, it’s use and format is identical
to the older [`cisco_pix`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib.hash.cisco_pix "passlib.hash.cisco_pix") class.

For passwords less than 13 characters, this should be identical to `cisco_pix`,
but will generate a different hash for most larger inputs
(See the [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#format-algorithm) section for the details).

This class only allows passwords <= 32 bytes, anything larger
will result in a [`PasswordSizeError`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasswordSizeError "passlib.exc.PasswordSizeError") if passed to `hash()`,
and be silently rejected if passed to `verify()`.

New in version 1.7.

Changed in version 1.7.1: Passwords > 32 bytes are now rejected / throw error instead of being silently truncated,
to match Cisco behavior. A number of [bugs](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#passlib-asa96-bug) were fixed
which caused prior releases to generate unverifiable hashes in certain cases.

Note

These hash algorithms have a context-sensitive peculiarity.
They take in an optional username to salt the hash,
but have specific restrictions…

- The username _must_ be provided in order to correctly hash passwords
associated with a user account on the Cisco device.
- Conversely, the username _must not_ be provided (or must be set to `""`)
in order to correctly hash passwords which don’t have an associated user
account (such as the “enable” password).

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#format-algorithm "Permalink to this headline")

Cisco PIX & ASA hashes consist of a 12 byte digest, encoded as a 16 character
[`HASH64`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.h64 "passlib.utils.binary.h64")-encoded string. An example
hash (of `"password"`, with user `""`) is `"NuLKvvWGg.x9HEKO"`.

The PIX / ASA digests are calculated as follows:

1. The password is encoded using `UTF-8` (though entering non-ASCII
characters is subject to interface-specific issues, and may lead
to problems such as double-encoding).

If the result is greater than 16 bytes (for PIX), or 32 bytes (for ASA),
the password is not allowed – it will be rejected when set,
and simplify not verify during authentication.

2. If the hash is associated with a user account,
append the first four bytes of the user account name
to the end of the password. If the hash is NOT associated
with a user account (e.g. it’s the “enable” password),
this step should be omitted.

If the user account is 1-3 bytes, it is repeated until all 4 bytes are filled
up (e.g. “usr” becomes “usru”).

For `cisco_asa`,
this step is omitted if the password is 28 bytes or more.

3. The password+user string is truncated, or right-padded with NULLs,
until it’s 16 bytes in size.

For `cisco_asa`,
if the password+user string is 16 or more bytes,
a padding size of 32 is used instead.

4. Run the result of step 3 through MD5.

5. Discard every 4th byte of the 16-byte MD5 hash, starting
with the 4th byte.

6. Encode the 12-byte result using [`HASH64`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.h64 "passlib.utils.binary.h64").


Changed in version 1.7.1: Updated to reflect current understanding of the algorithm.

## Security Issues [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#security-issues "Permalink to this headline")

This algorithm is not suitable for _any_ use besides manipulating existing
Cisco PIX hashes, due to the following flaws:

- Its use of the username as a salt value (and only the first four characters
at that), means that common usernames (e.g. `admin`, `cisco`) will occur
more frequently as salts, weakening the effectiveness of the salt in
foiling pre-computed tables.
- Its truncation of the `password+user` combination to 16 characters
additionally limits the keyspace, and the effectiveness of the username
as a salt; making pre-computed and brute force attacks much more feasible.
- Since the keyspace of `password+user` is still a subset of ascii characters,
existing MD5 lookup tables have an increased chance of being able to
reverse common hashes.
- Its simplicity, and the weakness of MD5, makes high-speed brute force attacks
much more feasible.
- Furthermore, it discards of 1/4 of MD5’s already small 16 byte digest,
making collisions much more likely.

## Deviations [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html\#deviations "Permalink to this headline")

This implementation tries to adhere to the canonical Cisco implementation,
but without an official specification, there may be other unknown deviations.
The following are known issues:

- Unicode Policy:

ASA documentation [\[4\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#charset) indicates it uses UTF-8 encoding,
and Passlib does as well. However, some ASA interfaces
have issues such as: ASDM may double-encode unicode characters,
and SSH connections may drop non-ASCII characters entirely.

- How usernames are added is not entirely pinned down. Under ASA, 3-character
usernames have their last character repeated to make a string of length 4.
It is currently assumed that a similar repetition would be applied to
usernames of 1-2 characters, and that this applies to PIX as well;
though neither assumption has been confirmed.

- **Passlib 1.7.1 Bugfix**: Prior releases of Passlib had a number of issues
with their implementation of the PIX & ASA algorithms. As of 1.7.1,
the reference vectors were greatly expanded, and then tested against
an ASA 9.6 system. This revealed a number of errors in passlib’s implementation,
which under the following conditions would create hashes that were
unverifiable on a Cisco system:


  - PIX and ASA: Usernames containing 1-3 characters were not appended correctly (step 2, above).
  - ASA omits the user entirely (step 2, above) for passwords with >= 28 characters,
    not >= 27. Non-enable passwords of exactly 27 characters were previous hashed
    incorrectly.
  - ASA’s padding size decision (step 3, above) is made after the user
    has been appended, not before. This caused prior releases to
    incorrectly hash non-enable passwords of length 13-15.

Anyone relying on cisco\_asa or cisco\_pix should upgrade to Passlib 1.7.1 or newer
to avoid these issues.

Footnotes

|     |     |
| --- | --- |
| \[1\] | Description of PIX algorithm -<br>[http://www.perlmonks.org/index.pl?node\_id=797623](http://www.perlmonks.org/index.pl?node_id=797623) |

|     |     |
| --- | --- |
| \[2\] | Message threads hinting at how username is handled -<br>[http://www.openwall.com/lists/john-users/2010/02/02/7](http://www.openwall.com/lists/john-users/2010/02/02/7),<br>[www.freerainbowtables.com/phpBB3/viewtopic.php?f=2&t=1441](https://passlib.readthedocs.io/en/stable/lib/www.freerainbowtables.com/phpBB3/viewtopic.php?f=2&t=1441) |

|     |     |
| --- | --- |
| \[3\] | Partial description of ASA algorithm -<br>[https://github.com/stekershaw/asa-password-encrypt/blob/master/README.md](https://github.com/stekershaw/asa-password-encrypt/blob/master/README.md) |

|     |     |
| --- | --- |
| [\[4\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#id1) | Character set used by ASA 8.4 -<br>[http://www.cisco.com/c/en/us/td/docs/security/asa/asa84/configuration/guide/asa\_84\_cli\_config/ref\_cli.html#Supported\_Character\_Sets](http://www.cisco.com/c/en/us/td/docs/security/asa/asa84/configuration/guide/asa_84_cli_config/ref_cli.html#Supported_Character_Sets) |

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
    - [Overview](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#overview)
    - [Unix Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#unix-hashes)
    - [Other “Modular Crypt” Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-modular-crypt-hashes)
    - [LDAP / RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-rfc2307-hashes)
    - [SQL Database Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#sql-database-hashes)
    - [MS Windows Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ms-windows-hashes)
    - [Cisco Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#cisco-hashes)
      - [`passlib.hash.cisco_type7` \- Cisco “Type 7” hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html)
      - [`passlib.hash.cisco_pix` \- Cisco PIX MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#)
        - [Overview](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#overview)
        - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#interface)
        - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#format-algorithm)
        - [Security Issues](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#security-issues)
        - [Deviations](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html#deviations)
      - [`passlib.hash.cisco_asa` \- Cisco ASA MD5 hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html)
    - [Other Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-hashes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html "passlib.hash.cisco_asa - Cisco ASA MD5 hash")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html "passlib.hash.cisco_type7 - Cisco “Type 7” hash")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.cisco_pix.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.cisco_pix.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)