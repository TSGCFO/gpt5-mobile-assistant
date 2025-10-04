<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html "passlib.hash.scrypt - SCrypt")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html "passlib.hash.pbkdf2_digest - Generic PBKDF2 Hashes")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

# [`passlib.hash.scram`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html\#passlib.hash.scram "passlib.hash.scram") \- SCRAM Hash [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html\#passlib-hash-scram-scram-hash "Permalink to this headline")

New in version 1.6.

SCRAM is a password-based challenge response protocol defined by [**RFC 5802**](https://tools.ietf.org/html/rfc5802.html).
While Passlib does not provide an implementation of SCRAM, applications
which use SCRAM on the server side frequently need a way to store
user passwords in a secure format that can be used to authenticate users over
SCRAM.

To accomplish this, Passlib provides the following
[Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format)-compatible password hash scheme which uses the
`$scram$` identifier. This format encodes a salt, rounds settings, and one
or more [`pbkdf2_hmac()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.pbkdf2_hmac "passlib.crypto.digest.pbkdf2_hmac") digests… one digest for each
of the hash algorithms the server wishes to support over SCRAM.

Since this format is PBKDF2-based, it has equivalent security to
Passlib’s other [pbkdf2 hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html),
and can be used to authenticate users using either the normal [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api)
or the SCRAM-specific class methods documented below.

Note

If you aren’t working with the SCRAM protocol, you probably
don’t need to use this hash format.

## Usage [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html\#usage "Permalink to this headline")

This class can be used like any other Passlib hash, as follows:

```
>>> from passlib.hash import scram

>>> # generate new salt, hash password against default list of algorithms
>>> hash = scram.hash("password")
>>> hash
'$scram$6400$.Z/znnNOKWUsBaCU$sha-1=cRseQyJpnuPGn3e6d6u6JdJWk.0,sha-256=5G
cjEbRaUIIci1r6NAMdI9OPZbxl9S5CFR6la9CHXYc,sha-512=.DHbIm82ajXbFR196Y.9Ttbs
gzvGjbMeuWCtKve8TPjRMNoZK9EGyHQ6y0lW9OtWdHZrDZbBUhB9ou./VI2mlw'

>>> # same, but with an explicit number of rounds
>>> scram.using(rounds=8000).hash("password")
'$scram$8000$Y0zp/R/DeO89h/De$sha-1=eE8dq1f1P1hZm21lfzsr3CMbiEA,sha-256=Nf
kaDFMzn/yHr/HTv7KEFZqaONo6psRu5LBBFLEbZ.o,sha-512=XnGG11X.J2VGSG1qTbkR3FVr
9j5JwsnV5Fd094uuC.GtVDE087m8e7rGoiVEgXnduL48B2fPsUD9grBjURjkiA'

>>> # verify password
>>> scram.verify("password", hash)
True
>>> scram.verify("secret", hash)
False

```

See the generic [PasswordHash usage examples](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html#password-hash-examples)
for more details on how to use the common hash interface.

* * *

Additionally, this class provides a number of useful methods for SCRAM-specific actions:

- You can override the default list of digests, and/or the number of iterations:





```
>>> hash = scram.using(rounds=1000, algs="sha-1,sha-256,md5").hash("password")
>>> hash
'$scram$1000$RsgZo7T2/l8rBUBI$md5=iKsH555d3ctn795Za4S7bQ,sha-1=dRcE2AUjALLF
tX5DstdLCXZ9Afw,sha-256=WYE/LF7OntriUUdFXIrYE19OY2yL0N5qsQmdPNFn7JE'

```

- Given a scram hash, you can use a single call to extract all the information
the SCRAM needs to authenticate against a specific mechanism:





```
>>> # this returns (salt_bytes, rounds, digest_bytes)
>>> scram.extract_digest_info(hash, "sha-1")
('F\xc8\x19\xa3\xb4\xf6\xfe_+\x05@H',
1000,
'u\x17\x04\xd8\x05#\x00\xb2\xc5\xb5~C\xb2\xd7K\tv}\x01\xfc')

```

- Given a scram hash, you can extract the list of digest algorithms
it contains information for ( `sha-1` will always be present):





```
>>> scram.extract_digest_algs(hash)
["md5", "sha-1", "sha-256"]

```

- This class also provides a standalone helper which can calculate
the `SaltedPassword` portion of the SCRAM protocol, taking
care of the SASLPrep step as well:





```
>>> scram.derive_digest("password", b'\x01\x02\x03', 1000, "sha-1")
b'k\x086vg\xb3\xfciz\xb4\xb4\xe2JRZ\xaet\xe4`\xe7'

```


## Interface [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html\#interface "Permalink to this headline")

Note

This hash format is new in Passlib 1.6, and its SCRAM-specific API
may change in the next few releases, depending on user feedback.

_class_ `passlib.hash.` `scram` [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#passlib.hash.scram "Permalink to this definition")

This class provides a format for storing SCRAM passwords, and follows
the [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api).

It supports a variable-length salt, and a variable number of rounds.

The [`using()`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash.using "passlib.ifc.PasswordHash.using") method accepts the following optional keywords:

| Parameters: | - **salt** ( [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – Optional salt bytes.<br>  If specified, the length must be between 0-1024 bytes.<br>  If not specified, a 12 byte salt will be autogenerated<br>  (this is recommended).<br>- **salt\_size** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of bytes to use when autogenerating new salts.<br>  Defaults to 12 bytes, but can be any value between 0 and 1024.<br>- **rounds** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – Optional number of rounds to use.<br>  Defaults to 100000, but must be within `range(1,1<<32)`.<br>- **algs** ( _list of strings_) – <br>  Specify list of digest algorithms to use.<br>  <br>  By default each scram hash will contain digests for SHA-1,<br>  SHA-256, and SHA-512. This can be overridden by specify either be a<br>  list such as `["sha-1", "sha-256"]`, or a comma-separated string<br>  such as `"sha-1, sha-256"`. Names are case insensitive, and may<br>  use `hashlib` or [IANA](http://www.iana.org/assignments/hash-function-text-names)<br>  hash names.<br>  <br>- **relaxed** ( [_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.9)")) – <br>  By default, providing an invalid value for one of the other<br>  keywords will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.9)"). If `relaxed=True`,<br>  and the error can be corrected, a [`PasslibHashWarning`](https://passlib.readthedocs.io/en/stable/lib/passlib.exc.html#passlib.exc.PasslibHashWarning "passlib.exc.PasslibHashWarning")<br>  will be issued instead. Correctable errors include `rounds`<br>  that are too small or too large, and `salt` strings that are too long.<br>  <br>  <br>  <br>  New in version 1.6. |

In addition to the standard [PasswordHash API](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#password-hash-api) methods,
this class also provides the following methods for manipulating Passlib
scram hashes in ways useful for pluging into a SCRAM protocol stack:

_classmethod_ `extract_digest_info`( _hash_, _alg_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#passlib.hash.scram.extract_digest_info "Permalink to this definition")

return (salt, rounds, digest) for specific hash algorithm.

| Parameters: | - **hash** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – `scram` hash stored for desired user<br>- **alg** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – <br>  Name of digest algorithm (e.g. `"sha-1"`) requested by client.<br>  <br>  This value is run through [`norm_hash_name()`](https://passlib.readthedocs.io/en/stable/lib/passlib.crypto.digest.html#passlib.crypto.digest.norm_hash_name "passlib.crypto.digest.norm_hash_name"),<br>  so it is case-insensitive, and can be the raw SCRAM<br>  mechanism name (e.g. `"SCRAM-SHA-1"`), the IANA name,<br>  or the hashlib name. |
| Raises: | [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.9)") – If the hash does not contain an entry for the requested digest<br>algorithm. |
| Returns: | A tuple containing `(salt, rounds, digest)`,<br>where _digest_ matches the raw bytes returned by<br>SCRAM’s `Hi()` function for the stored password,<br>the provided _salt_, and the iteration count ( _rounds_).<br>_salt_ and _digest_ are both raw (unencoded) bytes. |

_classmethod_ `extract_digest_algs`( _hash_, _format='iana'_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#passlib.hash.scram.extract_digest_algs "Permalink to this definition")

Return names of all algorithms stored in a given hash.

| Parameters: | - **hash** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – The `scram` hash to parse<br>- **format** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – This changes the naming convention used by the<br>  returned algorithm names. By default the names<br>  are IANA-compatible; possible values are `"iana"` or `"hashlib"`. |
| Returns: | Returns a list of digest algorithms; e.g. `["sha-1"]` |

_classmethod_ `derive_digest`( _password_, _salt_, _rounds_, _alg_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#passlib.hash.scram.derive_digest "Permalink to this definition")

helper to create SaltedPassword digest for SCRAM.

This performs the step in the SCRAM protocol described as:

```
SaltedPassword  := Hi(Normalize(password), salt, i)

```

| Parameters: | - **password** ( _unicode_ _or_ _utf-8 bytes_) – password to run through digest<br>- **salt** ( [_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.9)")) – raw salt data<br>- **rounds** ( [_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.9)")) – number of iterations.<br>- **alg** ( [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.9)")) – name of digest to use (e.g. `"sha-1"`). |
| Returns: | raw bytes of `SaltedPassword` |

## Format & Algorithm [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html\#format-algorithm "Permalink to this headline")

An example scram hash (of the string `password`) is:

```
$scram$6400$.Z/znnNOKWUsBaCU$sha-1=cRseQyJpnuPGn3e6d6u6JdJWk.0,sha-256=5G
cjEbRaUIIci1r6NAMdI9OPZbxl9S5CFR6la9CHXYc,sha-512=.DHbIm82ajXbFR196Y.9Ttb
sgzvGjbMeuWCtKve8TPjRMNoZK9EGyHQ6y0lW9OtWdHZrDZbBUhB9ou./VI2mlw

```

An scram hash string has the format `$scram$rounds$salt$alg1=digest1,alg2=digest2,...`, where:

- `$scram$` is the prefix used to identify Passlib scram hashes,
following the [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html#modular-crypt-format)
- `rounds` is the number of decimal rounds to use (6400 in the example),
zero-padding not allowed. this value must be in `range(1, 2**32)`.
- `salt` is a base64 salt string ( `.Z/znnNOKWUsBaCU` in the example),
encoded using [`ab64_encode()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.ab64_encode "passlib.utils.binary.ab64_encode").
- `alg` is a lowercase IANA hash function name [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#hnames), which should
match the digest in the SCRAM mechanism name.
- `digest` is a base64 digest for the specific algorithm,
encoded using [`ab64_encode()`](https://passlib.readthedocs.io/en/stable/lib/passlib.utils.binary.html#passlib.utils.binary.ab64_encode "passlib.utils.binary.ab64_encode").
Digests for `sha-1`, `sha-256`, and `sha-512` are present in the example.
- There will always be one or more `alg=digest` pairs, separated by a
comma. Per the SCRAM specification, the algorithm `sha-1` should always be present.

There is also an alternate format ( `$scram$rounds$salt$alg,...`)
which is used to represent a configuration string that doesn’t contain
any digests. An example would be:

```
$scram$6400$.Z/znnNOKWUsBaCU$sha-1,sha-256,sha-512

```

The algorithm used to calculate each digest is:

```
pbkdf2(salsprep(password).encode("utf-8"), salt, rounds, alg_digest_size, "hmac-"+alg)

```

…as laid out in the SCRAM specification [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#scram). All digests
should verify against the same password, or the hash is considered malformed.

Note

This format is similar in spirit to the LDAP storage format for SCRAM hashes,
defined in [**RFC 5803**](https://tools.ietf.org/html/rfc5803.html), except that it encodes everything into a single
string, and does not have any storage requirements (outside of the ability
to store 512+ character ascii strings).

## Security [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html\#security "Permalink to this headline")

The security of this hash is only as strong as the weakest digest used
by this hash. Since the SCRAM [\[1\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#scram) protocol requires SHA1
always be supported, this will generally be the weakest link, since
the other digests will generally be stronger ones (e.g. SHA2-256).

None-the-less, since PBKDF2 is sufficiently collision-resistant
on its own, any pre-image weaknesses found in SHA1 should be mitigated
by the PBKDF2-HMAC-SHA1 wrapper; and should have no flaws outside of
brute-force attacks on PBKDF2-HMAC-SHA1.

Footnotes

|     |     |
| --- | --- |
| \[1\] | _( [1](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#id2), [2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#id3))_ The SCRAM protocol is laid out in [**RFC 5802**](https://tools.ietf.org/html/rfc5802.html). |

|     |     |
| --- | --- |
| [\[2\]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#id1) | The official list of IANA-assigned hash function names -<br>[http://www.iana.org/assignments/hash-function-text-names](http://www.iana.org/assignments/hash-function-text-names) |

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
      - [Active Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#active-hashes)
        - [`passlib.hash.argon2` \- Argon2](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.argon2.html)
        - [`passlib.hash.bcrypt_sha256` \- BCrypt+SHA256](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt_sha256.html)
        - [`passlib.hash.phpass` \- PHPass’ Portable Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html)
        - [`passlib.hash.pbkdf2_digest` \- Generic PBKDF2 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html)
        - [`passlib.hash.scram` \- SCRAM Hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#)
          - [Usage](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#usage)
          - [Interface](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#interface)
          - [Format & Algorithm](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#format-algorithm)
          - [Security](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html#security)
        - [`passlib.hash.scrypt` \- SCrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html)
      - [Deprecated Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#deprecated-hashes)
    - [LDAP / RFC2307 Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ldap-rfc2307-hashes)
    - [SQL Database Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#sql-database-hashes)
    - [MS Windows Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#ms-windows-hashes)
    - [Cisco Hashes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#cisco-hashes)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html "passlib.hash.scrypt - SCrypt")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html "passlib.hash.pbkdf2_digest - Generic PBKDF2 Hashes")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »
- [`passlib.hash` \- Password Hashing Schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.hash.scram.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scram.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.hash.scram.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)