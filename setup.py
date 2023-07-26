from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gpx-concatenator',
    version='1.0.7',
    description='Tool for concatenating GPX files',
    author='iambrianna',
    author_email='iambrianna@proton.me',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gpx-concatenator = scripts.main:main',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
