from setuptools import setup, find_packages

setup(
    name='hbty',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),

    author='akira furukawa',
    author_email='minguu42@gmail.com',

    url='https://github.com/Minguu42/hbty',

    description='This is a birthday card generator',
    long_description=open('README.md').read(),
    logn_description_content_type='text/markdown',
    keywords='birthday',

    python_requires='~3.7',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    install_requires=[
        'Click~=7.1.1',
        'Pillow~=7.1.1',
        'requests~=2.23.0',
    ],
    entry_points={
        'console_scripts': [
            'hbty=hbty.core:cli'
        ]
    }
)
