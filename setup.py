from setuptools import setup

setup(
   name='untweeter',
   version='.2',
   description="Untweet and unfave tweets",
   author='Robert Guggenberger',
   author_email='robertsadresse@gmx.de',
   license="MIT",
   packages=['untweeter'],
   install_requires=["python-twitter", "confuse"],
   entry_points = {
        'console_scripts': ['untweet=untweeter.__main__:main'],
    }
)
