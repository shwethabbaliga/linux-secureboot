
import pytest
import subprocess


def test_verify_secureboot_enabled():
    state=subprocess.run(
        ["mokutil","--sb-state"],
        capture_output=True,
        text=True)
    assert (state.returncode == 0 and "enabled" in state.stdout) "Secureboot is disabled"


