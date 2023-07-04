import setuptools


LONG_DESCRIPTION = """

"""

setuptools.setup(
    name="fast-checkers",
    version="1.1.2",
    author="Michał Skibiński",
    author_email="mskibinski109@gmail.com",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    files_to_include=["fast_checkers"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)