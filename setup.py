import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def read(fname):
    # readme
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Traveler",
    version="0.0.1",
    author="MrTrustworthy",
    author_email="tinywritingmakesmailhardtoread@gmail.com",
    description=("Traveler"),
    long_description=read('README.md'),
    license="MIT",
    url="https://github.com/MrTrustworthy/traveler",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    test_suite="tests",
    install_requires=[
        "requests>=2.11",
        "Flask>=0.11",
        "gunicorn>=19",
        "Sphinx>=1.4"
    ]
)
