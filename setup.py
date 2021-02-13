import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='simplestr',
    version='0.1',
    scripts=['simplestr'] ,
    author="Leo Ertuna",
    author_email="leo.ertuna@gmail.com",
    description="Simple annotations to automatically generate __str__ and __repr__ methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jpleorx/simplestr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)