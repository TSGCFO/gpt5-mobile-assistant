<!-- Source: https://passlib.readthedocs.io/en/stable/history/ancient.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/copyright.html "Copyrights & Licenses")
- [previous](https://passlib.readthedocs.io/en/stable/history/1.5.html "Passlib 1.5")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html) »
- [Release History](https://passlib.readthedocs.io/en/stable/history/index.html) »

# Passlib 1.4 & Earlier [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#passlib-1-4-earlier "Permalink to this headline")

## **1.4** (2011-05-04) [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#id1 "Permalink to this headline")

This release contains a large number of changes, both large and small.
It adds a number of PBKDF2-based schemes, better support
for LDAP-format hashes, improved documentation,
and faster load times. In detail…

### Hashes [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#hashes "Permalink to this headline")

> - added LDAP `{CRYPT}` support for all hashes
> known to be supported by OS crypt()
> - added 3 custom PBKDF2 schemes for general use,
> as well as 3 LDAP-compatible versions.
> - added support for Dwayne Litzenberger’s PBKDF2 scheme.
> - added support for Grub2’s PBKDF2 hash scheme.
> - added support for Atlassian’s PBKDF2 password hash
> - added support for all hashes used by the Roundup Issue Tracker
> - bsdi\_crypt, sha1\_crypt now check for OS crypt() support
> - `salt_size` keyword added to encrypt() method of all
> the hashes which support variable-length salts.
> - security fix: disabled unix\_fallback’s “wildcard password” support
> unless explicitly enabled by user.

### CryptContext [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#cryptcontext "Permalink to this headline")

> - host\_context now dynamically detects which formats
> OS crypt() supports, instead of guessing based on sys.platform.
> - added predefined context for Roundup Issue Tracker database.
> - added CryptContext.verify\_and\_update() convenience method,
> to make it easier to perform both operations at once.
> - _bugfix:_ fixed NameError in category+min\_verify\_time border case
> - apps & hosts modules now use new
> `LazyCryptContext` wrapper class -
> this should speed up initial import,
> and reduce memory by not loading unneeded hashes.

### Documentation [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#documentation "Permalink to this headline")

> - greatly expanded documentation on how to use CryptContexts.
> - roughly documented framework for writing & testing
> custom password handlers.
> - various minor improvements.

### Internals [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#internals "Permalink to this headline")

> - added generate\_password() convenience method
> - refactored framework for building hash handlers,
> using new mixin-based system.
> - deprecated old handler framework - will remove in 1.5
> - deprecated list\_to\_bytes & bytes\_to\_list - not used, will remove in 1.5

### Other [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#other "Permalink to this headline")

> - password hash api - as part of cleaning up optional attributes
> specification, renamed a number of them to reduce ambiguity:
>
>
> > - renamed _{xxx}\_salt\_chars_ attributes -> _xxx\_salt\_size_
> > - renamed _salt\_charset_ -\> _salt\_chars_
> > - old attributes still present, but deprecated - will remove in 1.5
>
> - password hash api - tightened specifications for salt & rounds parameters,
> added support for hashes w/ no max salt size.
>
> - improved password hash api conformance tests
>
> - PyPy compatibility

## **1.3.1** (2011-03-28) [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#id2 "Permalink to this headline")

> Minor bugfix release.
>
> - bugfix: replaced “sys.maxsize” reference that was failing under py25
> - bugfix: fixed default\_rounds>max\_rounds border case that could
> cause ValueError during CryptContext.encrypt()
> - minor documentation changes
> - added instructions for building html documentation from source

## **1.3** (2011-03-25) [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#id3 "Permalink to this headline")

> First public release.
>
> - documentation completed
> - 99% unittest coverage
> - some refactoring and lots of bugfixes
> - added support for a number of additional password schemes:
> bigcrypt, crypt16, sun md5 crypt, nthash, lmhash, oracle10 & 11,
> phpass, sha1, generic hex digests, ldap digests.

## **1.2** (2011-01-06) [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#id4 "Permalink to this headline")

> Note
>
> For this and all previous versions, Passlib did not exist independently,
> but as a subpackage of _BPS_, a private & unreleased toolkit library.
>
> - many bugfixes
> - global registry added
> - transitional release for applications using BPS library.
> - first truly functional release since splitting from BPS library (see below).

## **1.0** (2009-12-11) [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#id5 "Permalink to this headline")

> - CryptContext & CryptHandler framework
> - added support for: des-crypt, bcrypt (via py-bcrypt), postgres, mysql
> - added unit tests

## **0.5** (2008-05-10) [¶](https://passlib.readthedocs.io/en/stable/history/ancient.html\#id6 "Permalink to this headline")

> - initial production version
> - consolidated from code scattered across multiple applications
> - MD5-Crypt, SHA256-Crypt, SHA512-Crypt support

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
- [API Reference](https://passlib.readthedocs.io/en/stable/lib/index.html)
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html)
  - [Frequently Asked Questions](https://passlib.readthedocs.io/en/stable/faq.html)
  - [Modular Crypt Format](https://passlib.readthedocs.io/en/stable/modular_crypt_format.html)
  - [Release History](https://passlib.readthedocs.io/en/stable/history/index.html)
    - [1.7 Series](https://passlib.readthedocs.io/en/stable/history/1.7.html)
    - [1.6 Series](https://passlib.readthedocs.io/en/stable/history/1.6.html)
    - [1.5 Series](https://passlib.readthedocs.io/en/stable/history/1.5.html)
    - [1.4 & Earlier](https://passlib.readthedocs.io/en/stable/history/ancient.html#)
      - [**1.4** (2011-05-04)](https://passlib.readthedocs.io/en/stable/history/ancient.html#id1)
        - [Hashes](https://passlib.readthedocs.io/en/stable/history/ancient.html#hashes)
        - [CryptContext](https://passlib.readthedocs.io/en/stable/history/ancient.html#cryptcontext)
        - [Documentation](https://passlib.readthedocs.io/en/stable/history/ancient.html#documentation)
        - [Internals](https://passlib.readthedocs.io/en/stable/history/ancient.html#internals)
        - [Other](https://passlib.readthedocs.io/en/stable/history/ancient.html#other)
      - [**1.3.1** (2011-03-28)](https://passlib.readthedocs.io/en/stable/history/ancient.html#id2)
      - [**1.3** (2011-03-25)](https://passlib.readthedocs.io/en/stable/history/ancient.html#id3)
      - [**1.2** (2011-01-06)](https://passlib.readthedocs.io/en/stable/history/ancient.html#id4)
      - [**1.0** (2009-12-11)](https://passlib.readthedocs.io/en/stable/history/ancient.html#id5)
      - [**0.5** (2008-05-10)](https://passlib.readthedocs.io/en/stable/history/ancient.html#id6)
  - [Copyrights & Licenses](https://passlib.readthedocs.io/en/stable/copyright.html)

«
hide menumenusidebar
»


### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/copyright.html "Copyrights & Licenses")
- [previous](https://passlib.readthedocs.io/en/stable/history/1.5.html "Passlib 1.5")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Other Documentation](https://passlib.readthedocs.io/en/stable/other.html) »
- [Release History](https://passlib.readthedocs.io/en/stable/history/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/history/ancient.html)**[stable](https://passlib.readthedocs.io/en/stable/history/ancient.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/history/ancient.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)