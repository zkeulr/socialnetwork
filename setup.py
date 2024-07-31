from setuptools import setup, find_packages

setup(
    name='social_network',
    version='0.1.0',
    description='A Python app to visualize social clusters',
    author='Zeke Ulrich',
    url='https://github.com/ezekielulrich/socialnetwork',  
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3',
)
