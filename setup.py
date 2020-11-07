import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

DEPENDENCIES = open('requirements.txt', 'r').read().split('\n')

setuptools.setup(
    name='pypublicwww',
    version='1.0.0',
    description='Python library and command-line utility for search in publicwww ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Einar Lanfranco',
    author_email='einar.lanfranco@gmail.com',
    url='https://github.com/einar-lanfranco/publicwww',
    packages=['pypublicwww'],
    scripts=['pypublicwww/publicwww'],
    install_requires=DEPENDENCIES,
    keywords=['security', 'network'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6'
)