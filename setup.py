"""
SSSA Python
===========
"""

from setuptools import setup

setup(
    name="sssa-python",
    version="0.0.2",
    url="https://github.com/SSSaaS/sssa-python",
    license="MIT",
    author="Alexander Scheel",
    author_email="alexander.m.scheel@gmail.com",
    description=("Helper Shamir's Secret Sharing module for Python"),
    packages=["SSSA"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
    ],
)
