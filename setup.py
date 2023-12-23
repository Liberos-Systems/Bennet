from setuptools import setup
from config import version

setup(
    name="Bennet",
    version=version,
    description="Bennet is a tool similar to Yarn, but it is specifically designed for Linux projects written in C/C++/Python/JavaScript and can work with GTK and various build systems.",
    author="Kacper Paczos",
    author_email="kacper-paczos@linux.pl",
    url="https://github.com/kacperpaczos/Bennet",
    packages=["Bennet"],
    entry_points={"console_scripts": ["bennet = bennet.__main__:main"]},
    license="GNU GPLv3",
)
