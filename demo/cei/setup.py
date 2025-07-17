from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculator=calculator.__main__:main',
        ],
    },
    python_requires='>=3.6',
)