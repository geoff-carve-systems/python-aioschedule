import codecs
from setuptools import setup


SCHEDULE_VERSION = "1.1.0"
SCHEDULE_DOWNLOAD_URL = "https://github.com/dbader/schedule/tarball/" + SCHEDULE_VERSION

def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, "r", "utf8") as f:
        return f.read()


setup(
    name='aioschedule',
    packages=['aioschedule'],
    package_data={"aioschedule": ["py.typed"]},
    version=SCHEDULE_VERSION,
    description='Job scheduling for humans.',
    long_description=read_file('README.rst'),
    license='MIT',
    author='Daniel Bader, Cochise Ruhulessin',
    author_email='development@ibrb.io',
    url='https://github.com/ibrb/python-aioschedule',
    download_url=SCHEDULE_DOWNLOAD_URL,
    keywords=[
        'aioschedule', 'periodic', 'jobs', 'scheduling', 'clockwork',
        'cron', 'scheduler', 'job scheduling'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)
