import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trello_client-basics-api-fifo2019", version="0.0.1", author="Pavel", author_email="pavel@mail.ru",
    description="trello_api", long_description=long_description,
    long_description_content_type="text/markdown",
    url="[https://github.com/fifo2019/TrelloApi]",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.6',)

