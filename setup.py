import setuptools

# setting long description to README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LambdataChrisSeiler",
    version="0.0.1",
    author="Christopher Seiler",
    author_email="exitiummc@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisseiler96/LambdataChrisSeiler.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
