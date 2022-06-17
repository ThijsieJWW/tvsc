from setuptools import setup, find_packages


description = "A compiler made in python"
long_description = description

try:
    fp = open("README.md", "r")
    long_description = fp.read()

except Exception as e:
    print("Warning: long description not loaded: " + str(e))

finally:
    fp.close()

setup(
    name="tvsc",
    version="0.0.001",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Thijs van Straaten",
    maintainer="Thijs van Straaten",
    url="https://github.com/ThijsieJWW/tvsc",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Compilers",
    ],
    packages=find_packages(),
    entry_points={"console_scripts": ["tvsc = tvsc.__main__:main"]},
)
