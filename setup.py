"""Setup for the natlparks package."""

import setuptools


with open("README.rst") as f:
    README = f.read()

setuptools.setup(
    author="Ira Horecka",
    author_email="ira89@icloud.com",
    name="python-natlparks",
    license="MIT",
    description="Simple API wrapper for US National Park Services",
    version="v0.1.3",
    long_description=README,
    url="https://github.com/irahorecka/python-natlparks",
    packages=["natlparks"],
    python_requires=">=3.5",
    install_requires=["requests"],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
)
