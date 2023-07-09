from setuptools import setup, find_packages

setup(
    name='gpx-concatenator',
    version='0.1.0',
    author='I am Brianna',
    author_email='iambrianna@proton.me',
    description='GPX Concatenator',
    long_description='A tool to concatenate GPX files.',
    long_description_content_type='text/markdown',
    url='https://github.com/i-am-brianna/gpx-concatenator',
    packages=find_packages(where='src'),
    install_requires=[
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'gpx-concatenator=gpx_concatenator.main:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
