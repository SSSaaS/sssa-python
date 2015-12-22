# sssa-python
[![Build Status](https://travis-ci.org/SSSaaS/sssa-python.svg?branch=master)](https://travis-ci.org/SSSaaS/sssa-python)

An implementation of Shamir's Secret Sharing Algorithm in Python
Compatible with both Python 2.7 and 3.5; other versions untested.

    Copyright (C) 2015 Alexander Scheel, Joel May, Matthew Burket  
    See Contributors.md for a complete list of contributors.  
    Licensed under the MIT License.  

## Usage
Note: this library is for a pure implementation of SSS in Python;
if you are looking for the API Library for SSSaaS, look [here](https://github.com/SSSAAS/sssaas-python).

    sssa.create(minimum, shares, raw) - creates a set of shares

    sssa.combine(shares) - combines shares into secret

For more detailed documentation, check out docs/sssa.md

## Contributing
We welcome pull requests, issues, security advice on this library, or other contributions you feel are necessary. Feel free to open an issue to discuss any questions you have about this library.

The reference implementation for this cross-language project was written in Go, [here](https://github.com/SSSAAS/sssa-golang).
Please make sure all tests pass before submitting a pull request. In particular,
`python ./utils_tests.py && python ./sssa_tests.py` will run all internal tests
and the [go-libtest](https://github.com/SSSAAS/go-libtest) suite's tests should be run
against the changes before submission.

For security issues, send a GPG-encrypted email to <alexander.m.scheel@gmail.com> with public key [0xBDC5F518A973035E](https://pgp.mit.edu/pks/lookup?op=vindex&search=0xBDC5F518A973035E).
