"""."""

from setuptools import setup

setup(
    name='pyastrx',
    packages=['pyastrx'],
    version='0.0.1',
    description='',
    license='MIT',
    author='Bruno Messias',
    author_email='devmessias@gmail.com',
    url='',
    extras_require={
        'xpath': ['lxml>=3.3.5', ]
    },
    entry_points={
        'console_scripts': [
            'pyastrx = pyastrx.frontend.cli:pyastrx',

        ]
    },
    keywords='xpath xml ast asts syntax query',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ]
)
