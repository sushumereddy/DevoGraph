import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devolearn",
    version="0.3.0",
    author="jihang lee, Bradly Alicea", 
    author_email="lspongebobjh@gmail.com, balicea@openworm.org", #Subject to change, we can also use Devolearn official Email address.
    description="Accelerate data driven research in developmental biology with deep learning models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevoLearn/devolearn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires= required,
    python_requires='==3.7',   
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose']   
)
