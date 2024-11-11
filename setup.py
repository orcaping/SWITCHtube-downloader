from setuptools import setup, find_packages

setup(
    name="switchtube-downloader",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "webdriver-manager",
        "cookies",
        "downloader",
        "authentication",
        "python-dotenv",
        "argparse",
        "requests",
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/orcaping/SWITCHtube-downloader",
    author="Yanick Egli",
    author_email="nick.eglirohr@gmail.com",
)
