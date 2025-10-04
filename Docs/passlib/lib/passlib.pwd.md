<!-- Source: https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html "passlib.registry - Password Handler Registry")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html "passlib.ifc – Password Hash Interface")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

# [`passlib.pwd`](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html\#module-passlib.pwd "passlib.pwd: password generation helpers") – Password generation helpers [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html\#passlib-pwd-password-generation-helpers "Permalink to this headline")

New in version 1.7.

## Password Generation [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html\#password-generation "Permalink to this headline")

Warning

Before using these routines, make sure your system’s RNG entropy pool is
secure and full. Also make sure that `genword()` or `genphrase()`
is called with a sufficiently high `entropy` parameter
the intended purpose of the password.

`passlib.pwd.` `genword`( _entropy=None_, _length=None_, _charset="ascii\_62"_, _chars=None_, _returns=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#passlib.pwd.genword "Permalink to this definition")

Generate one or more random passwords.

This function uses `random.SystemRandom` to generate
one or more passwords using various character sets.
The complexity of the password can be specified
by size, or by the desired amount of entropy.

Usage Example:

```
>>> # generate a random alphanumeric string with 48 bits of entropy (the default)
>>> from passlib import pwd
>>> pwd.genword()
'DnBHvDjMK6'

>>> # generate a random hexadecimal string with 52 bits of entropy
>>> pwd.genword(entropy=52, charset="hex")
'310f1a7ac793f'

```

| Parameters: | - **entropy** – <br>  Strength of resulting password, measured in ‘guessing entropy’ bits.<br>  An appropriate **length** value will be calculated<br>  based on the requested entropy amount, and the size of the character set.<br>  <br>  This can be a positive integer, or one of the following preset<br>  strings: `"weak"` (24), `"fair"` (36),<br>  `"strong"` (48), and `"secure"` (56).<br>  <br>  If neither this or **length** is specified, **entropy** will default<br>  to `"strong"` (48).<br>  <br>- **length** – <br>  Size of resulting password, measured in characters.<br>  If omitted, the size is auto-calculated based on the **entropy** parameter.<br>  <br>  If both **entropy** and **length** are specified,<br>  the stronger value will be used.<br>  <br>- **returns** – <br>  Controls what this function returns:<br>  <br>  - If `None` (the default), this function will generate a single password.<br>  - If an integer, this function will return a list containing that many passwords.<br>  - If the `iter` constant, will return an iterator that yields passwords.<br>- **chars** – Optionally specify custom string of characters to use when randomly<br>  generating a password. This option cannot be combined with **charset**.<br>- **charset** – <br>  The predefined character set to draw from (if not specified by **chars**).<br>  There are currently four presets available:<br>  <br>  - `"ascii_62"` (the default) – all digits and ascii upper & lowercase letters.<br>    Provides ~5.95 entropy per character.<br>  - `"ascii_50"` – subset which excludes visually similar characters<br>    ( `1IiLl0Oo5S8B`). Provides ~5.64 entropy per character.<br>  - `"ascii_72"` – all digits and ascii upper & lowercase letters,<br>    as well as some punctuation. Provides ~6.17 entropy per character.<br>  - `"hex"` – Lower case hexadecimal. Providers 4 bits of entropy per character. |
| Returns: | `unicode` string containing randomly generated password;<br>or list of 1+ passwords if `returns=int` is specified. |

`passlib.pwd.` `genphrase`( _entropy=None_, _length=None_, _wordset="eff\_long"_, _words=None_, _sep=" "_, _returns=None_) [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#passlib.pwd.genphrase "Permalink to this definition")

Generate one or more random password / passphrases.

This function uses `random.SystemRandom` to generate
one or more passwords; it can be configured to generate
alphanumeric passwords, or full english phrases.
The complexity of the password can be specified
by size, or by the desired amount of entropy.

Usage Example:

```
>>> # generate random phrase with 48 bits of entropy
>>> from passlib import pwd
>>> pwd.genphrase()
'gangly robbing salt shove'

>>> # generate a random phrase with 52 bits of entropy
>>> # using a particular wordset
>>> pwd.genword(entropy=52, wordset="bip39")
'wheat dilemma reward rescue diary'

```

| Parameters: | - **entropy** – <br>  Strength of resulting password, measured in ‘guessing entropy’ bits.<br>  An appropriate **length** value will be calculated<br>  based on the requested entropy amount, and the size of the word set.<br>  <br>  This can be a positive integer, or one of the following preset<br>  strings: `"weak"` (24), `"fair"` (36),<br>  `"strong"` (48), and `"secure"` (56).<br>  <br>  If neither this or **length** is specified, **entropy** will default<br>  to `"strong"` (48).<br>  <br>- **length** – <br>  Length of resulting password, measured in words.<br>  If omitted, the size is auto-calculated based on the **entropy** parameter.<br>  <br>  If both **entropy** and **length** are specified,<br>  the stronger value will be used.<br>  <br>- **returns** – <br>  Controls what this function returns:<br>  <br>  - If `None` (the default), this function will generate a single password.<br>  - If an integer, this function will return a list containing that many passwords.<br>  - If the `iter` builtin, will return an iterator that yields passwords.<br>- **words** – Optionally specifies a list/set of words to use when randomly generating a passphrase.<br>  This option cannot be combined with **wordset**.<br>- **wordset** – <br>  The predefined word set to draw from (if not specified by **words**).<br>  There are currently four presets available:<br>  <br>  `"eff_long"` (the default)<br>  <br>  <br>  > Wordset containing 7776 english words of ~7 letters.<br>  > Constructed by the EFF, it offers ~12.9 bits of entropy per word.<br>  > <br>  > This wordset (and the other `"eff_"` wordsets)<br>  > were [created by the EFF](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)<br>  > to aid in generating passwords. See their announcement page<br>  > for more details about the design & properties of these wordsets.<br>  <br>  <br>  `"eff_short"`<br>  <br>  <br>  > Wordset containing 1296 english words of ~4.5 letters.<br>  > Constructed by the EFF, it offers ~10.3 bits of entropy per word.<br>  <br>  <br>  `"eff_prefixed"`<br>  <br>  <br>  > Wordset containing 1296 english words of ~8 letters,<br>  > selected so that they each have a unique 3-character prefix.<br>  > Constructed by the EFF, it offers ~10.3 bits of entropy per word.<br>  <br>  <br>  `"bip39"`<br>  <br>  <br>  > Wordset of 2048 english words of ~5 letters,<br>  > selected so that they each have a unique 4-character prefix.<br>  > Published as part of Bitcoin’s [BIP 39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt),<br>  > this wordset has exactly 11 bits of entropy per word.<br>  > <br>  > This list offers words that are typically shorter than `"eff_long"`<br>  > (at the cost of slightly less entropy); and much shorter than<br>  > `"eff_prefixed"` (at the cost of a longer unique prefix).<br>  <br>- **sep** – Optional separator to use when joining words.<br>  Defaults to `" "` (a space), but can be an empty string, a hyphen, etc. |
| Returns: | `unicode` string containing randomly generated passphrase;<br>or list of 1+ passphrases if `returns=int` is specified. |

## Predefined Symbol Sets [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html\#predefined-symbol-sets "Permalink to this headline")

The following predefined sets are used by the generation functions above,
but are exported by this module for general use:

`default_charsets`

Dictionary mapping charset name -> string of characters, used by [`genword()`](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#passlib.pwd.genword "passlib.pwd.genword").
See that function for a list of predefined charsets present in this dict.

`default_wordsets`

Dictionary mapping wordset name -> tuple of words, used by [`genphrase()`](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#passlib.pwd.genphrase "passlib.pwd.genphrase").
See that function for a list of predefined wordsets present in this dict.

(Note that this is actually a special object which will lazy-load
wordsets from disk on-demand)

## Password Strength Estimation [¶](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html\#password-strength-estimation "Permalink to this headline")

Passlib does not currently offer any password strength estimation routines.
However, the (javascript-based) [zxcvbn](https://github.com/dropbox/zxcvbn)
project is a _very_ good choice.

Though there are a few different python ports of ZXCVBN library, as of 2019-11-13,
[zxcvbn (@ pypi)](https://pypi.python.org/pypi/zxcvbn) is the most up-to-date,
and is endorsed by the upstream zxcvbn developers.

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
  - [`passlib.pwd` – Password generation helpers](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#)
    - [Password Generation](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#password-generation)
    - [Predefined Symbol Sets](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#predefined-symbol-sets)
    - [Password Strength Estimation](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html#password-strength-estimation)
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
- [next](https://passlib.readthedocs.io/en/stable/lib/passlib.registry.html "passlib.registry - Password Handler Registry")
- [previous](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html "passlib.ifc – Password Hash Interface")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/lib/passlib.pwd.html)**[stable](https://passlib.readthedocs.io/en/stable/lib/passlib.pwd.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/lib/passlib.pwd.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)