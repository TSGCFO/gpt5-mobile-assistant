<!-- Source: https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html -->

### Navigation

- [index](https://passlib.readthedocs.io/en/stable/genindex.html "General Index")
- [modules](https://passlib.readthedocs.io/en/stable/py-modindex.html "Python Module Index")
- [toc](https://passlib.readthedocs.io/en/stable/contents.html "Table Of Contents")
- [next](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html "TOTP Tutorial")
- [previous](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html "PasswordHash Tutorial")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

# [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html\#passlib.context.CryptContext "passlib.context.CryptContext") Tutorial [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#cryptcontext-tutorial "Permalink to this headline")

## Overview [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#overview "Permalink to this headline")

The [`passlib.context`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#module-passlib.context "passlib.context: CryptContext class, for managing multiple password hash schemes") module contains one main class: `passlib.context.CryptContext`.
This class is designed to take care of many of the more frequent
coding patterns which occur in applications that need to handle multiple
password hashes at once:

> - identifying the algorithm used by a hash, and then verify a password.
> - configure the default algorithm, load in support for new algorithms,
> deprecate old ones, set defaults for time-cost parameters, etc.
> - migrate hashes / re-hash passwords when an algorithm has been deprecated.
> - load said configuration from a sysadmin configurable file.

The following sections contain a walkthrough of this class, starting
with some simple examples, and working up to a complex “full-integration” example.

See also

The [`passlib.context`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#module-passlib.context "passlib.context: CryptContext class, for managing multiple password hash schemes") api reference,
which lists all the options and methods supported by this class.

## Walkthrough Outline [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#walkthrough-outline "Permalink to this headline")

- [Basic Usage](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#basic-usage)
- [Using Default Settings](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#using-default-settings)
- [Loading & Saving a CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#loading-saving-a-cryptcontext)
- [Deprecation & Hash Migration](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#deprecation-hash-migration)
- [Full Integration Example](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#full-integration-example)

Todo

This tutorial doesn’t yet cover the [User Categories](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories) system;
and a few other parts could use elaboration.

## Basic Usage [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#basic-usage "Permalink to this headline")

At its base, the `CryptContext` class is just a collection of
[`PasswordHash`](https://passlib.readthedocs.io/en/stable/lib/passlib.ifc.html#passlib.ifc.PasswordHash "passlib.ifc.PasswordHash") objects, imported by name
from the [`passlib.hash`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#module-passlib.hash "passlib.hash: all password hashes provided by Passlib") module. The following snippet creates
a new context object which supports three hash algorithms
( [sha256\_crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html),
[md5\_crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html), and
[des\_crypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.des_crypt.html)):

```
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])

```

This new object exposes a very similar set of methods to the `PasswordHash`
interface, and hashing and verifying passwords is equally as straightforward:

```
>>> # this loads first algorithm in the schemes list (sha256_crypt),
>>> # generates a new salt, and hashes the password:
>>> hash1 = myctx.hash("joshua")
>>> hash1
'$5$rounds=80000$HFEGd1wnFknpibRl$VZqjyYcTenv7CtOf986hxuE0pRaGXnuLXyfb7m9xL69'

>>> # when verifying a password, the algorithm is identified automatically:
>>> myctx.verify("gtnw", hash1)
False
>>> myctx.verify("joshua", hash1)
True

>>> # alternately, you can explicitly pick one of the configured algorithms,
>>> # through this is rarely needed in practice:
>>> hash2 = myctx.hash("dogsnamehere", scheme="md5_crypt")
>>> hash2
'$1$e2nig/AC$stejMS1ek6W0/UogYKFao/'

>>> myctx.verify("letmein", hash2)
False
>>> myctx.verify("dogsnamehere", hash2)
True

```

If not told otherwise, the context object will use the first algorithm listed
in `schemes` when creating new hashes. This default can be changed by
using the `default` keyword:

```
>>> myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"],
                         default="des_crypt")
>>> hash = myctx.hash("password")
>>> hash
'bIwNofDzt1LCY'

>>> myctx.identify(hash)
'des_crypt'

```

This concludes the basics of how to use a CryptContext object.
The rest of the sections detail the various features it offers,
which probably provide a better argument for _why_ you’d want to use it.

See also

- the [`CryptContext.hash()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.hash "passlib.context.CryptContext.hash"), [`verify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify "passlib.context.CryptContext.verify"), and [`identify()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.identify "passlib.context.CryptContext.identify") methods.
- the [schemes](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-schemes-option) and [default](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-default-option) constructor options.

## Using Default Settings [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#using-default-settings "Permalink to this headline")

While creating and verifying hashes is useful enough, it’s not much
more than could be done by importing the objects into a list.
The next feature of the `CryptContext` class is that it
can store various customized settings for the different algorithms,
instead of hardcoding them into each `hash()` call.
As an example, the `sha256_crypt`
algorithm supports a `rounds` parameter which defaults to 80000,
and the `ldap_salted_md5` algorithm uses
8-byte salts by default:

```
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(["sha256_crypt", "ldap_salted_md5"])

>>> # sha256_crypt using 80000 rounds...
>>> myctx.hash("password", scheme="sha256_crypt")
'$5$rounds=80000$GgU/gwNBs9SaObqs$ohY23/zm.8O0TpkGx5fxk0aeVdFpaeKo9GUkMJ0VrMC'
           ^^^^^

>>> # ldap_salted_md5 with an 8 byte salt...
>>> myctx.hash("password", scheme="ldap_salted_md5")
'{SMD5}cIYrPh5f/TeUKg9oghECB5fSeu8='
       ^^^^^^^^^^

```

Instead of having to pass `rounds=91234` or `salt_size=16` every time
`encrypt()` is called, CryptContext supports setting algorithm-specific
defaults which will be used every time a CryptContext method is invoked.
These is done by passing the CryptContext constructor a keyword with the format `scheme__setting`:

```
>>> # this reconfigures the existing context object so that
>>> # sha256_crypt now uses 91234 rounds,
>>> # and ldap_salted_md5 will use 16 byte salts:
>>> myctx.update(sha256_crypt__default_rounds=91234,
...              ldap_salted_md5__salt_size=16)

>>> # the effect of this can be seen the next time encrypt is called:
>>> myctx.hash("password", scheme="sha256_crypt")
'$5$rounds=91234$GgU/gwNBs9SaObqs$ohY23/zm.8O0TpkGx5fxk0aeVdFpaeKo9GUkMJ0VrMC'
           ^^^^^

>>> myctx.hash("password", scheme="ldap_salted_md5")
'{SMD5}NnQh2S2pjnFxwtMhjbVH59TaG6P0/l/r3RsDwPj/n/M='
       ^^^^^^^^^^^^^^^^^^^^^

```

See also

- the [`CryptContext.update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.update "passlib.context.CryptContext.update") method.
- the [default\_rounds](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-default-rounds-option) and
[per-scheme setting](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-other-option) constructor options.

## Loading & Saving a CryptContext [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#loading-saving-a-cryptcontext "Permalink to this headline")

The previous example built up a `CryptContext` instance
in two stages, first by calling the constructor, and then the `update()`
method to make some additional changes. The same configuration
could of course be done in one step:

```
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes=["sha256_crypt", "ldap_salted_md5"],
...                      sha256_crypt__default_rounds=91234,
...                      ldap_salted_md5__salt_size=16)

```

This is not much more useful, since these settings still have to be
hardcoded somewhere in the application. This is where the CryptContext’s
serialization abilities come into play. As a starting point,
every CryptContext object can dump its configuration as a dictionary
suitable for passing back into its constructor:

```
>>> myctx.to_dict()
{'schemes': ['sha256_crypt', 'ldap_salted_md5'],
'ldap_salted_md5__salt_size': 16,
'sha256_crypt__default_rounds': 91234}

```

However, this has been taken a step further, as CryptContext objects
can also dump their configuration into a [ConfigParser](http://docs.python.org/library/configparser.html)-compatible
string, allowing the configuration to be written to a file:

```
>>> cfg = print myctx.to_string()
>>> print cfg
[passlib]
schemes = sha256_crypt, ldap_salted_md5
ldap_salted_md5__salt_size = 16
sha256_crypt__default_rounds = 912345

```

This “INI” format consists of a section named `"[passlib]"`,
following by key/value pairs which correspond exactly to the CryptContext
constructor keywords (Keywords which accepts lists of names (such as `schemes`)
are automatically converted to/from a comma-separated string)
This format allows CryptContext configurations to be created
in a separate file (say as part of an application’s larger config file),
and loaded into the CryptContext at runtime. Such strings can be
loaded directly when creating the context object:

```
>>> # using the special from_string() constructor to
>>> # load the exported configuration created in the previous step:
>>> myctx2 = CryptContext.from_string(cfg)

>>> # or it can be loaded from a local file:
>>> myctx3 = CryptContext.from_path("/some/path/on/local/system")

```

This allows applications to completely extract their password hashing
policies from the code, and into a configuration file with other security settings.

Note

For CryptContext instances which already exist,
the [`load()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load "passlib.context.CryptContext.load") and [`load_path()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.load_path "passlib.context.CryptContext.load_path")
methods can be used to replace the existing state.

See also

- the [`to_dict()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_dict "passlib.context.CryptContext.to_dict") and [`to_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.to_string "passlib.context.CryptContext.to_string") methods.
- the [`CryptContext.from_string()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_string "passlib.context.CryptContext.from_string") and [`CryptContext.from_path()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.from_path "passlib.context.CryptContext.from_path") constructors.

## Deprecation & Hash Migration [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#deprecation-hash-migration "Permalink to this headline")

The final and possibly most useful feature of the [`CryptContext`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext "passlib.context.CryptContext") class
is that it can take care of deprecating and migrating existing hashes,
re-hashing them using the current default algorithm and settings.
All that is required is that a few settings be added to the configuration,
and that the application call one extra method whenever a user logs in.

### Deprecating Algorithms [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#deprecating-algorithms "Permalink to this headline")

The first setting that enables the hash migration features is the `deprecated`
setting. This should be a list algorithms which are no longer desirable to have
around, but are included in `schemes` to provide legacy support.
For example:

```
>>> # this sets a context that supports 3 algorithms, but considers
>>> # two of them (md5_crypt and des_crypt) to be deprecated...
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"],
                         deprecated=["md5_crypt", "des_crypt"])

```

All of the basic methods of this object will behave normally, but after
an application has verified the user entered the correct password, it can
check to see if the hash has been deprecated using the
[`needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.needs_update "passlib.context.CryptContext.needs_update") method:

```
>>> # assume the user's password was stored as a sha256_crypt hash,
>>> # needs_update will show that the hash is still allowed.
>>> hash = '$5$rounds=80000$zWZFpsA2egmQY8R9$xp89Vvg1HeDCJ/bTDDN6qkdsCwcMM61vHtM1RNxXur.'
>>> myctx.needs_update(hash)
False

>>> # but if the user's password was stored as md5_crypt hash,
>>> # need_update will indicate that it is deprecated,
>>> # and that the original password needs to be re-hashed...
>>> hash = '$1$fmWm78VW$uWjT69xZNMHWyEQjq852d1'
>>> myctx.needs_update(hash)
True

```

Note

Internally, this is not the only thing `needs_update()` does.
It also checks for other issues, such as rounds / salts which are
known to be weak under certain algorithms, improperly encoded hash
strings, and other configurable behaviors that are detailed later.

### Integrating Hash Migration [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#integrating-hash-migration "Permalink to this headline")

To summarize the process described in the previous section,
all the actions an application would usually need to
perform can be combined into the following bit of skeleton code:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br>hash = get_hash_from_user(user)<br>if pass_ctx.verify(password, hash):<br>    if pass_ctx.needs_update(hash):<br>        new_hash = pass_ctx.hash(password)<br>        replace_user_hash(user, new_hash)<br>    do_successful_things()<br>else:<br>    reject_user_login()<br>``` |

Since this is a very common pattern, the CryptContext object provides
a shortcut: the [`verify_and_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify_and_update "passlib.context.CryptContext.verify_and_update") method,
which allows replacing the above skeleton code with the following
that uses 2 fewer calls (and is much more efficient internally):

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br>hash = get_hash_from_user(user)<br>valid, new_hash = pass_ctx.verify_and_update(password, hash)<br>if valid:<br>    if new_hash:<br>        replace_user_hash(user, new_hash)<br>    do_successful_things()<br>else:<br>    reject_user_login()<br>``` |

### Settings Rounds Limitations [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#settings-rounds-limitations "Permalink to this headline")

In addition to deprecating entire algorithms, the deprecations system
also allows you to place limits on algorithms that support the
variable time-cost parameter `rounds`:

As an example, take a typical system containing a number of user passwords,
all stored using [`sha256_crypt`](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.sha256_crypt.html#passlib.hash.sha256_crypt "passlib.hash.sha256_crypt").
As computers get faster, the minimum number of rounds that should be used
gets larger, yet the existing passwords will remain in the system
hashed using their original value. To solve this, the CryptContext
object lets you place minimum bounds on what `rounds`
values are allowed, using the `scheme__min_rounds` set of keywords…
any hashes whose rounds are outside this limit are considered deprecated,
and in need of re-encoding using the current policy:

First, we set up a context which requires all `sha256_crypt` hashes
to have at least 131072 rounds:

```
>>> from passlib.context import CryptContext
>>> myctx = CryptContext(schemes="sha256_crypt",
...                      sha256_crypt__min_rounds=131072)

```

New hashes generated by this context will always honor the minimum
(just as if `default_rounds` was set to the same value):

```
>>> # plain call to encrypt:
>>> hash1 = myctx.hash("password")
'$5$rounds=131072$i6xuFK6j8r66ahGn$r.7H8HUk30qiH7fIWRJFJfhWG925nRZh90aYPMdewr3'
           ^^^^^^
>>> # hashes with enough rounds won't show up as deprecated...
>>> myctx.needs_update(hash1)
False

```

If an existing hash below the minimum is tested, it will show up as needing rehashing:

```
>>> # this has only 80000 rounds:
>>> hash3 = '$5$rounds=80000$qoCFY.akJr.flB7V$8cIZXLwSTzuCRLcJbgHlxqYKEK0cVCENy6nFIlROj05'
>>> myctx.needs_update(hash3)
True

>>> # and verify_and_update() will upgrade this hash automatically:
>>> myctx.verify_and_update("wrong", hash3)
(False, None)
>>> myctx.verify_and_update("password", hash3)
(True, '$5$rounds=131072$rnMqBaemVZ6QGu7v$vrAVQLEbsBoxhgem8ynvAbToCae8vpzl6ZuDS3/adlA')
                  ^^^^^^

```

See also

- the [deprecated](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-deprecated-option),
[min\_rounds](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-min-rounds-option),
and [max\_rounds](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-max-rounds-option) constructor options.
- the [`needs_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.needs_update "passlib.context.CryptContext.needs_update") and [`verify_and_update()`](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify_and_update "passlib.context.CryptContext.verify_and_update") methods.

## Undocumented Features [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#undocumented-features "Permalink to this headline")

Todo

Document usage of the [Disabled Hash Managment](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-disabled-hashes) options.

## Full Integration Example [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#full-integration-example "Permalink to this headline")

The following is an extended example showing how to fully interface
a CryptContext object into your application. The sample configuration
is somewhat more ornate that would usually be needed, just to highlight
some features, but should none-the-less be secure.

### Policy Configuration File [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#policy-configuration-file "Permalink to this headline")

The first thing to do is setup a configuration string for the CryptContext to use.
This can be a dictionary or string defined in a python config file,
or (in this example), part of a large INI-formatted config file.
All of the documented [Context Options](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#context-options) are allowed.

```
; the options file uses the INI file format,
; and passlib will only read the section named "passlib",
; so it can be included along with other application configuration.

[passlib]

; setup the context to support pbkdf2_sha256, and some other hashes:
schemes = pbkdf2_sha256, sha512_crypt, sha256_crypt, md5_crypt, des_crypt

; flag md5_crypt and des_crypt as deprecated
deprecated = md5_crypt, des_crypt

; set boundaries for the pbkdf2 rounds parameter
; (pbkdf2 hashes outside this range will be flagged as needs-updating)
pbkdf2_sha256__min_rounds = 10000
pbkdf2_sha256__max_rounds = 50000

; set the default rounds to use when hashing new passwords.
pbkdf2_sha1__default_rounds = 15000

; applications can choose to treat certain user accounts differently,
; by assigning different types of account to a 'user category',
; and setting special policy options for that category.
; this create a category named 'admin', which will have a larger default
; rounds value.
admin__pbkdf2_sha1__min_rounds = 18000
admin__pbkdf2_sha1__default_rounds = 20000

```

### Initializing the CryptContext [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#initializing-the-cryptcontext "Permalink to this headline")

Applications which choose to use a policy file will typically want
to create the CryptContext at the module level, and then load
the configuration once the application starts:

1. Within a common module in your application (e.g. `myapp.model.security`):





```
#
# create a crypt context that can be imported and used wherever is needed...
# the instance will be configured later.
#
from passlib.context import CryptContext
user_pwd_context = CryptContext()

```

2. Within some startup function within your application:





```
#
# when the app starts, import the context from step 1 and
# configure it... such as by loading a policy file (see above)
#

from myapp.model.security import user_pwd_context

def myapp_startup():

       #
       # ... other code ...
       #

       #
       # load configuration from some application-specified path
       # using load_path() ... or use the load() method, which can
       # load a dict or in-memory string containing the INI file.
       #
       ##user_pwd_context.load(policy_config_string)
       user_pwd_context.load_path(policy_config_path)

       #
       # if you want to reconfigure the context without restarting the application,
       # simply repeat the above step at another point.
       #

       #
       # ... other code ...
       #

```


### Encrypting New Passwords [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#encrypting-new-passwords "Permalink to this headline")

When it comes time to create a new user’s password, insert
the following code in the correct function:

```
from myapp.model.security import user_pwd_context

def handle_user_creation():

    #
    # ... other code ...
    #

    # vars:
    #   'secret' containing the putative password
    #   'category' containing a category assigned to the user account
    #

    hash = user_pwd_context.hash(secret, category=category)

    #... perform appropriate actions to store hash...

    #
    # ... other code ...
    #

```

Note

In the above code, the ‘category’ kwd can be omitted entirely, _OR_
set to a string matching a user category specified in the policy file.
In the latter case, any category-specific policy settings will be enforced.

For the purposes of this example (and the sample config file listed above),
it’s assumed this value will be `None` for most users, and `"admin"` for special users.
This namespace is entirely up to the application, it just has to match the
category names used in the config file.

See [User Categories](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#user-categories) for more details.

### Verifying & Migrating Existing Passwords [¶](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html\#verifying-migrating-existing-passwords "Permalink to this headline")

Finally, when it comes time to check a users’ password, insert
the following code at the correct place:

```
from myapp.model.security import user_pwd_context

def handle_user_login():

    #
    # ... other code ...
    #

    #
    # this example both checks the user's password AND upgrades deprecated hashes...
    #
    # vars:
    #   'hash' containing the specified user's hash.
    #   'secret' containing the putative password
    #   'category' containing a category assigned to the user account
    #
    # NOTE: if the user account is missing, or has no hash,
    #       you can pass ``hash=None`` to verify_and_update()
    #       mask this from the attacker by simulating the delay
    #       a real verification would have taken.
    #       hash=None will never verify.

    ok, new_hash = user_pwd_context.verify_and_update(secret, hash, category=category)
    if not ok:
        # ... password did not match. do mean things ...
        pass

    else:
        #... password matched ...

        if new_hash:
            # old hash was deprecated by policy.

            # ... replace hash w/ new_hash for user account ...
            pass

        # ... do successful login actions ...

```

[![Logo](https://passlib.readthedocs.io/en/stable/_static/masthead.png)](https://passlib.readthedocs.io/en/stable/index.html "index")

### Quick search

### [Table of Contents](https://passlib.readthedocs.io/en/stable/contents.html)

- [Introduction](https://passlib.readthedocs.io/en/stable/index.html)
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html)
  - [Installation](https://passlib.readthedocs.io/en/stable/install.html)
  - [Library Overview](https://passlib.readthedocs.io/en/stable/narr/overview.html)
  - [New Application Quickstart Guide](https://passlib.readthedocs.io/en/stable/narr/quickstart.html)
  - [`PasswordHash` Tutorial](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html)
  - [`CryptContext` Tutorial](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#)
    - [Overview](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#overview)
    - [Walkthrough Outline](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#walkthrough-outline)
    - [Basic Usage](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#basic-usage)
    - [Using Default Settings](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#using-default-settings)
    - [Loading & Saving a CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#loading-saving-a-cryptcontext)
    - [Deprecation & Hash Migration](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#deprecation-hash-migration)
      - [Deprecating Algorithms](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#deprecating-algorithms)
      - [Integrating Hash Migration](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#integrating-hash-migration)
      - [Settings Rounds Limitations](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#settings-rounds-limitations)
    - [Undocumented Features](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#undocumented-features)
    - [Full Integration Example](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#full-integration-example)
      - [Policy Configuration File](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#policy-configuration-file)
      - [Initializing the CryptContext](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#initializing-the-cryptcontext)
      - [Encrypting New Passwords](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#encrypting-new-passwords)
      - [Verifying & Migrating Existing Passwords](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#verifying-migrating-existing-passwords)
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
- [next](https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html "TOTP Tutorial")
- [previous](https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html "PasswordHash Tutorial")
- [Passlib 1.7 Documentation](https://passlib.readthedocs.io/en/stable/index.html) »
- [Walkthrough & Tutorials](https://passlib.readthedocs.io/en/stable/narr/index.html) »

Versions[latest](https://passlib.readthedocs.io/en/latest/narr/context-tutorial.html)**[stable](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html)**[1.7.3](https://passlib.readthedocs.io/en/1.7.3/narr/context-tutorial.html)Downloads[PDF](https://passlib.readthedocs.io/_/downloads/en/stable/pdf/)[HTML](https://passlib.readthedocs.io/_/downloads/en/stable/htmlzip/)On Read the Docs[Project Home](https://app.readthedocs.org/projects/passlib/?utm_source=passlib&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/passlib/builds/?utm_source=passlib&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=passlib&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=passlib&utm_content=flyout)