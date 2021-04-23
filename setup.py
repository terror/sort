import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="sort",
    version="1.0.0",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description=("Sorting algorithms!"),
    long_description_content_type="text/markdown",
    url="https://github.com/terror/sort",
    license="BSD",
    keywords="sort",
    packages=find_packages(),
    long_description=read("README.md"),
    python_requires=">=3.7",
)
