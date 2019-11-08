from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyqt5_simple",
    version="0.0.1",
    author="John Thornton",
    author_email="<doe.john@example.com>",
    description="A PyQt5 Simple Example with an import",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/pyq5_simple",
    download_url="https://github.com/jethornton/pyq5_simple/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'pyqt5-simple=pyqt5_simple.src:main',
        ],
    },
)
