from setuptools import setup, find_packages

setup(
    name='mfglab',
    version='0.1.0',
    description='for manufacturing industry',
    author='jaeho',
    author_email='uehoza98@gmail.com',
    url='https://github.com/qqrr33/mfglab.git',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['mfglab', 'manufacturing'],
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



