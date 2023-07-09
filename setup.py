from setuptools import setup, find_packages

setup(
    name='gpx-concatenator',
    version='1.0',
    description='Tool for concatenating GPX files',
    author='iambrianna',
    author_email='iambrianna@proton.me',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gpx-concatenator = scripts.main:main',
        ],
    },
)
