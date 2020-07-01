import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wltr-phonetics",
    version="1.0.2",
    author="Walter Avelino",
    author_email="walter.avelin@gmail.com",
    description="Wltr Phonetics é uma biblioteca de algoritmos fonéticos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walteravelino/wltr-phonetics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
