import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "FALL",
    version = "1.2",
    author = "Devansh Raghav",
    author_email = "indiananonymous75@gmail.com",
    description = ("A automated penetration testing tool"),
    license = "MIT",
    keywords = ["FALL", "Bug Bounty", "pentesting", "security"],
    url = "https://github.com/DevanshRaghav75/FALL",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],

    entry_points={
        'console_scripts': [
            'FALL = FALL.__main__:main'
        ]
    },
)