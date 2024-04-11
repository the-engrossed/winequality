import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "winequality"
AUTHOR_USER_NAME = "the-engrossed"
SRC_REPO="winepred"
AUTHOR_EMAIL = "tanmaireddy5598@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for ml app",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src") 

)