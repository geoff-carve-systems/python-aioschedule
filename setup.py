import codecs
from setuptools import setup


SCHEDULE_VERSION = "1.1.1"
SCHEDULE_DOWNLOAD_URL = (
    "https://github.com/geoff-carve-systems/python-aioschedule/tarball/"
    + SCHEDULE_VERSION
)


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, "r", "utf8") as f:
        return f.read()


setup(
    name="aioschedule",
    packages=["aioschedule"],
    package_data={"aioschedule": ["py.typed"]},
    version=SCHEDULE_VERSION,
    description="Job scheduling for humans.",
    long_description=read_file("README.rst"),
    license="MIT",
    author="Daniel Bader, Cochise Ruhulessin, Geoff Robinson",
    author_email="geoff.robinson@carvesystems.com",
    url="https://github.com/geoff-carve-systems/python-aioschedule",
    download_url=SCHEDULE_DOWNLOAD_URL,
    keywords=[
        "aioschedule",
        "periodic",
        "jobs",
        "scheduling",
        "clockwork",
        "cron",
        "scheduler",
        "job scheduling",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
)
