from setuptools import setup, find_packages
from mfglab import __version__, __author__

setup(
    name='mfglab',
    version=__version__,
    description='for manufacturing industry',
    author=__author__,
    author_email='uehoza98@gmail.com',
    url='https://github.com/qqrr33/mfglab',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['mfglab', 'pypi'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)

