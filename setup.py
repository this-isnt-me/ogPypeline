import pathlib
from setuptools import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ogPypeline",
    version='0.0.1',
    description='Unit conversion for oil and gas calculations',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/this-isnt-me/ogPypeline",
    author="Tim Clarke",
    author_email="<info@hitchadvisor.info>",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=["ogPypeline"],
    include_package_data=True,
    install_requires=[],
    keywords=['python', 'engineering', 'oil', 'gas',
              'energy', 'unit', 'conversion']
)
