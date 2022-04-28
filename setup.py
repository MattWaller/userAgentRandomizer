from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="userAgentRandomizer",
    version="0.1.7",
    author="Matt Waller",
    author_email="mattghwaller@gmail.com",
    description="Automatically Generate User agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MattWaller/userAgentRandomizer",
    project_urls={
        "Bug Tracker": "https://github.com/MattWaller/userAgentRandomizer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['userAgentRandomizer'],                      # root folder of your package
    package_dir={'/': ''},      # directory which contains the python code
    package_data={'/': ['assets/*.txt']},  # directory which contains your csvs
    python_requires=">=3.6",
    include_package_data=True,
)