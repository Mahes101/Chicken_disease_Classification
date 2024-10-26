import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken_disease_Classification",
AUTHOR_USER_NAME = "Mahes101",
SRC_REPO = "cnnClassifier", 
AUTHOR_EMAIL = "maheswariuma2592@gmail.com"    

setuptools.setup(
    name="cnnClassifier",
    version="0.0.1",
    author="Mahes101",
    author_email="maheswariuma2592.com",
    description="A small python package for CNN app",
    long_description=long_description,  
    long_description_content_type="text/markdown",
    url="https://github.com/Mahes101/Chicken_disease_Classification",
    project_urls={
        "Bug Tracker": "https://github.com/Mahes101/Chicken_disease_Classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages()
)