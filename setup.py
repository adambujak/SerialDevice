from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Serial Device Manager'
LONG_DESCRIPTION = 'Serial device manager - transferring data between PC and embedded device easily'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="userial",
        version=VERSION,
        author="Adam Bujak",
        author_email="adamjbujak@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 1 - Mucking Around",
            "Intended Audience :: Embedded Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
