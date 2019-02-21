from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def get_requirements(filename='requirements.txt'):
    deps = []
    with open(filename, 'r') as f:
        for pkg in f.readlines():
            if pkg.strip():
                deps.append(pkg)
    return deps


setup(
    name='ys-downloader',
    version='0.0.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='appleholic',
    keywords='ys_downloader',
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['download-ys=ys_downloader.run:main'],
    }
)
