import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blinkist_config",
    version="0.0.1",
    author="Peter Shoukry",
    author_email="peter@blinkist.com",
    description="Adapter based configuration handler (supports ENV and AWS SSM).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blinkist/blinkist-config-python",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
