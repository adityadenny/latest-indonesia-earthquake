import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="detectearthquakeindonesia",
    version="0.1.1",
    author="Denny Aditya H",
    author_email="adityadenny6@gmail.com",
    description="This package will scrape from [BMKG](https://www.bmkg.go.id/) to get latest earthquake happened in "
                "Indonesia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adityadenny/latest-indonesia-earthquake",
    project_urls={
        "Website": "http://harinteam.com/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
