import setuptools

with open("./testapp/__init__.py") as f:
    (
        productname,
        version,
        description,
        url,
        docs,
        author,
        email,
        license_,
        bug_tracker,
    ) = [l.split('"')[1] for l in f.readlines()[:9]]

with open("./README.md") as f:
    long_description = f.read()

setuptools.setup(
    name=productname,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email=email,
    license=license_,
    classifiers=[  # Find more classifiers at: https://pypi.org/classifiers/
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Documentation": docs,
        "Source": url,
        "Bug Tracker": bug_tracker,
    },
    python_requires=">=3.6.0",
    packages=setuptools.find_packages(exclude=["tests*"]),
)
