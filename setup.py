from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='inventory_scripts',  # Required
    version='0.0.1',  # Required
    description='inventory scripts shared code for bolo musee',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='git@github.com:museebolo/inventory_scripts.git',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='Musee bolo',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='someone@museebolo.ch',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'License :: CC0 1.0 Universal',
        'Programming Language :: Python :: 3',
    ],


    package_dir={'': 'src'},  # Optional

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.6, <4',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/museebolo/inventory_scripts/issues'
    },
)
