import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

Repo_name = "Text-Summarization-using-NLP"
AUTHOR_USERNAME = "richikraj30"
SRC_REPO = "text_summarization"
AUTHOR_EMAIL = "richikraj30@gmail.com"

setuptools.setup(
    name=Repo_name,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization tool using Natural Language Processing (NLP) techniques.",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/richikraj30/" + Repo_name,
    project_urls={
        "Issue Tracker": f"https://github.com/{AUTHOR_USERNAME}/{Repo_name}/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)
