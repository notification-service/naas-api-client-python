import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='naas-client',
        version='0.0.1',
        url='https://github.com/quicksprout/naas-api-client-python.git',
        license='MIT',
        author='Nate Klaiber',
        author_email='nate@deviceindependent.com',
        description='API Client to access the NAAS API',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=['naas.client',],
        install_requires=[
            "requests == 2.21.0",
            "uritemplate == 3.0.0"
        ]
)
