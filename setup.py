from setuptools import setup, find_packages

with open("README.md", "r") as f:
    readme = f.read()

setup(
    version="1.0.3",
    name="makepymodule",
    author="Arvind Iyer",
    author_email="arvindi.me@gmail.com",
    description="CLI program to generate python module directory structure",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/arvind-iyer/makepymodule",
    package_dir={"": "src"},
    package_data={"": ["data/*"]},
    packages=find_packages(where="src"),
    install_requires=[""],
    entry_points={
        'console_scripts': [
            'makepymodule = makepymodule.cli:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX"
    ]
)
