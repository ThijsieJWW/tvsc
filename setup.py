from setuptools import setup


description = "Thijs van Straaten Compiler: Now only testing."
long_description = description

version = "0.0.0"

try:
    fp = open("README.md", "r")
    long_description = fp.read()

except Exception as e:
    print("Warning: long description not loaded: " + str(e))

finally:
    fp.close()
try:
    from tvsc.settings import version as _ver

    version = _ver
except Exception as e:
    print("Warning: version not loaded: " + str(e))

setup(
    name="tvsc",
    version="0.0.14",
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
    packages=["tvsc"],
    entry_points={"console_scripts": ["tvsc = tvsc.term:main"]},
)
