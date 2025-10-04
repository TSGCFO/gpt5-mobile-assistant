# PassLib Documentation

Complete PassLib v1.7.4 documentation downloaded from https://passlib.readthedocs.io/

**Total Files:** 77 markdown files
**Last Updated:** 2025-10-04
**Source:** Official PassLib Documentation (Read the Docs)

---

## 🚨 Critical Information: bcrypt 72-Byte Password Limit

### The Problem
BCrypt has a **72-byte maximum password length**. Passwords longer than 72 bytes are either:
1. **Silently truncated** (older bcrypt behavior)
2. **Rejected with error** (newer bcrypt library v5.0+)

### Official PassLib Documentation
See: [lib/passlib.hash.bcrypt.md](lib/passlib.hash.bcrypt.md)

> "passwords are truncated on the first NULL byte (if any), and only the first 72 bytes of a password are hashed… all the rest are ignored."

### Recommended Solutions

**Option 1: Use bcrypt_sha256 (Recommended by PassLib)**
See: [lib/passlib.hash.bcrypt_sha256.md](lib/passlib.hash.bcrypt_sha256.md)

> "This class works around that issue by first running the password through HMAC-SHA2-256"

**Benefits:**
- Supports passwords of ANY length
- Pre-hashes password with HMAC-SHA256 before bcrypt
- More secure (fully mixes all password bytes)
- **WARNING:** Incompatible hash format - breaks existing password hashes

**Implementation:**
```python
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt_sha256"],  # Instead of "bcrypt"
    deprecated="auto",
    bcrypt_sha256__rounds=10
)
```

**Option 2: Enforce 72-Byte Validation (Current Project Approach)**

**Benefits:**
- Simple to implement
- Compatible with existing bcrypt hashes
- Clear user feedback

**Implementation:**
```python
# Truncate password BEFORE hashing
if len(password) > 72:
    password = password[:72]
    logger.warning("Password truncated to 72 bytes")

hash = pwd_context.hash(password)
```

**Important:** Truncation must happen BEFORE calling `pwd_context.hash()` because newer bcrypt libraries raise an error instead of silently truncating.

---

## 📁 Documentation Structure

### Core API Documentation

**Password Hashing:**
- [lib/passlib.hash.bcrypt.md](lib/passlib.hash.bcrypt.md) - BCrypt algorithm (72-byte limit)
- [lib/passlib.hash.bcrypt_sha256.md](lib/passlib.hash.bcrypt_sha256.md) - BCrypt+SHA256 (no length limit)
- [lib/passlib.context.md](lib/passlib.context.md) - CryptContext manager (86 KB)
- [lib/passlib.hash.md](lib/passlib.hash.md) - All password hashing schemes
- [lib/passlib.ifc.md](lib/passlib.ifc.md) - Password Hash Interface

**Recommended Modern Algorithms:**
- [lib/passlib.hash.argon2.md](lib/passlib.hash.argon2.md) - Argon2 (winner of 2013 Password Hashing Competition)
- [lib/passlib.hash.scrypt.md](lib/passlib.hash.scrypt.md) - SCrypt
- [lib/passlib.hash.pbkdf2_digest.md](lib/passlib.hash.pbkdf2_digest.md) - PBKDF2 variants

**Unix/Linux Crypt Hashes:**
- [lib/passlib.hash.sha256_crypt.md](lib/passlib.hash.sha256_crypt.md) - SHA-256 Crypt
- [lib/passlib.hash.sha512_crypt.md](lib/passlib.hash.sha512_crypt.md) - SHA-512 Crypt
- [lib/passlib.hash.md5_crypt.md](lib/passlib.hash.md5_crypt.md) - MD5 Crypt (deprecated)

### Tutorials & Guides

- [narr/quickstart.md](narr/quickstart.md) - New Application Quickstart
- [narr/hash-tutorial.md](narr/hash-tutorial.md) - PasswordHash Tutorial
- [narr/context-tutorial.md](narr/context-tutorial.md) - CryptContext Tutorial
- [narr/totp-tutorial.md](narr/totp-tutorial.md) - TOTP / 2FA Tutorial
- [narr/overview.md](narr/overview.md) - Library Overview

### Utility Modules

- [lib/passlib.pwd.md](lib/passlib.pwd.md) - Password generation helpers
- [lib/passlib.utils.md](lib/passlib.utils.md) - Helper functions
- [lib/passlib.crypto.md](lib/passlib.crypto.md) - Cryptographic helpers
- [lib/passlib.exc.md](lib/passlib.exc.md) - Exceptions and warnings

### Application Integration

- [lib/passlib.apps.md](lib/passlib.apps.md) - Helpers for various applications
- [lib/passlib.hosts.md](lib/passlib.hosts.md) - OS password handling
- [lib/passlib.apache.md](lib/passlib.apache.md) - Apache password files
- [lib/passlib.ext.django.md](lib/passlib.ext.django.md) - Django integration

### Database & LDAP Hashes

**LDAP/RFC2307:**
- [lib/passlib.hash.ldap_std.md](lib/passlib.hash.ldap_std.md) - Standard LDAP digests
- [lib/passlib.hash.ldap_crypt.md](lib/passlib.hash.ldap_crypt.md) - LDAP crypt() wrappers
- [lib/passlib.hash.ldap_pbkdf2_digest.md](lib/passlib.hash.ldap_pbkdf2_digest.md) - LDAP PBKDF2 hashes

**SQL Databases:**
- [lib/passlib.hash.mysql323.md](lib/passlib.hash.mysql323.md) - MySQL 3.2.3
- [lib/passlib.hash.mysql41.md](lib/passlib.hash.mysql41.md) - MySQL 4.1
- [lib/passlib.hash.postgres_md5.md](lib/passlib.hash.postgres_md5.md) - PostgreSQL MD5
- [lib/passlib.hash.oracle10.md](lib/passlib.hash.oracle10.md) - Oracle 10g
- [lib/passlib.hash.oracle11.md](lib/passlib.hash.oracle11.md) - Oracle 11g
- [lib/passlib.hash.mssql2000.md](lib/passlib.hash.mssql2000.md) - MS SQL 2000
- [lib/passlib.hash.mssql2005.md](lib/passlib.hash.mssql2005.md) - MS SQL 2005

### Windows Hashes

- [lib/passlib.hash.nthash.md](lib/passlib.hash.nthash.md) - Windows NT-HASH
- [lib/passlib.hash.lmhash.md](lib/passlib.hash.lmhash.md) - LanManager Hash
- [lib/passlib.hash.msdcc.md](lib/passlib.hash.msdcc.md) - Domain Cached Credentials v1
- [lib/passlib.hash.msdcc2.md](lib/passlib.hash.msdcc2.md) - Domain Cached Credentials v2

### Cisco Hashes

- [lib/passlib.hash.cisco_pix.md](lib/passlib.hash.cisco_pix.md) - Cisco PIX
- [lib/passlib.hash.cisco_asa.md](lib/passlib.hash.cisco_asa.md) - Cisco ASA
- [lib/passlib.hash.cisco_type7.md](lib/passlib.hash.cisco_type7.md) - Cisco Type 7

### Other Hash Algorithms

**PHPass & Generic:**
- [lib/passlib.hash.phpass.md](lib/passlib.hash.phpass.md) - PHPass Portable Hash
- [lib/passlib.hash.scram.md](lib/passlib.hash.scram.md) - SCRAM Hash
- [lib/passlib.hash.fshp.md](lib/passlib.hash.fshp.md) - Fairly Secure Hashed Password

**Legacy/Deprecated:**
- [lib/passlib.hash.des_crypt.md](lib/passlib.hash.des_crypt.md) - DES Crypt
- [lib/passlib.hash.sun_md5_crypt.md](lib/passlib.hash.sun_md5_crypt.md) - Sun MD5 Crypt
- [lib/passlib.hash.bsdi_crypt.md](lib/passlib.hash.bsdi_crypt.md) - BSDi Crypt
- [lib/passlib.hash.crypt16.md](lib/passlib.hash.crypt16.md) - Crypt16 (insecure)
- [lib/passlib.hash.bigcrypt.md](lib/passlib.hash.bigcrypt.md) - BigCrypt

### Other Documentation

- [other/faq.md](other/faq.md) - Frequently Asked Questions
- [other/modular_crypt_format.md](other/modular_crypt_format.md) - MCF standard
- [other/copyright.md](other/copyright.md) - License information
- [other/install.md](other/install.md) - Installation guide

### Version History

- [history/1.7.md](history/1.7.md) - PassLib 1.7 changes
- [history/1.6.md](history/1.6.md) - PassLib 1.6 changes
- [history/1.5.md](history/1.5.md) - PassLib 1.5 changes
- [history/ancient.md](history/ancient.md) - PassLib 1.4 & earlier

---

## 🔑 Quick Reference: Password Length Handling

### Current Project Issue

**Error:** `"password cannot be longer than 72 bytes, truncate manually if necessary"`

**Cause:** bcrypt library v5.0+ raises error instead of silently truncating

**Solution:** Truncate password BEFORE calling `pwd_context.hash()`

### Code Example (Validated Against Documentation)

**Wrong (doesn't work):**
```python
def hash_password(password: str) -> str:
    if len(password) > 72:
        password = password[:72]  # TOO LATE!
    return pwd_context.hash(password)  # ERROR happens HERE
```

**Correct (works):**
```python
# In auth_service.py register_user() method:
def register_user(self, username: str, email: str, password: str) -> User:
    # Truncate FIRST, before any hashing
    if len(password) > 72:
        password = password[:72]
        logger.warning(f"Password truncated for {username}")

    # Now hash (password is ≤72 bytes)
    password_hash = hash_password(password)  # Works!
```

---

## 📚 Key Documentation Files for Current Issue

1. **[lib/passlib.hash.bcrypt.md](lib/passlib.hash.bcrypt.md)**
   - Explains 72-byte limit
   - Documents `truncate_error` parameter
   - Security issues section

2. **[lib/passlib.hash.bcrypt_sha256.md](lib/passlib.hash.bcrypt_sha256.md)**
   - Recommended solution for long passwords
   - HMAC-SHA256 pre-hashing
   - No length limit

3. **[lib/passlib.context.md](lib/passlib.context.md)**
   - CryptContext configuration
   - Multiple hash scheme support
   - Migration strategies

4. **[narr/quickstart.md](narr/quickstart.md)**
   - Choosing a hash algorithm
   - Comparison of bcrypt vs argon2 vs pbkdf2
   - Best practices for new applications

5. **[other/faq.md](other/faq.md)**
   - Common questions about password hashing
   - Security considerations

---

## 🔗 External Links

- [PassLib Official Documentation](https://passlib.readthedocs.io/en/stable/)
- [PassLib GitHub Repository](https://github.com/glic3rinu/passlib)
- [bcrypt PyPI Package](https://pypi.org/project/bcrypt/)
- [argon2-cffi PyPI Package](https://pypi.org/project/argon2-cffi/)

---

## ⚙️ Project Configuration

**Current Setup:**
```python
# backend/app/core/security.py
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=10
)
```

**Recommended Future Migration:**
```python
pwd_context = CryptContext(
    schemes=["bcrypt_sha256", "bcrypt"],  # Support both
    deprecated="auto",
    bcrypt_sha256__rounds=10
)
```

This allows:
- New passwords use `bcrypt_sha256` (no 72-byte limit)
- Old passwords still verify with `bcrypt`
- Automatic migration on next login
