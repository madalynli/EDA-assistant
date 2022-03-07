import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='EDA-assistant',
    version='0.0.2',
    author='Madalyn Li',
    author_email='mli2324@uw.edu',
    description='This package allows users to create an exploratory data analysis pdf report from any data set',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/madalynli/EDA-assistant',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
