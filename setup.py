import setuptools

# thanks to ceddlyburge/python_world sample

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_world",
    version="0.0.1",
    author="Foo Bar",
    author_email="foo@bar.com",
    description="Keras model for CTC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LanceNorskog/CTCModel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
