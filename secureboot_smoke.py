
import pytest
import subprocess


def test_verify_secureboot_enabled():
    print(subprocess.run("mokutil","--sb-state"))


