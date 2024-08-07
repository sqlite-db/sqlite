from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        subprocess.run(["say", "You have a new package installed"], check=True)
        install.run(self)


setup(
    name="sqlitedb",
    version="2.1",
    packages=find_packages(),
    cmdclass={
        "install": PostInstallCommand,
    },
)
