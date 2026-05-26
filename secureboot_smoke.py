
import pytest
import subprocess
import os

def test_secureboot_state():
    state=subprocess.run(
        ["mokutil","--sb-state"],
        capture_output=True,
        text=True)
    assert (state.returncode == 0 and "enabled" in state.stdout),"Secureboot is disabled"

def test_secboot_dmesgcheck():
    dmesg=subprocess.Popen(
        "dmesg",
        stdout=subprocess.PIPE,
        text=True
    )

    secboot=subprocess.Popen(
        ["grep", "secureboot"],
        stdin=dmesg.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    
    output, error = secboot.communicate()

    print (output, error)

    assert (error == 0 and "enabled" in output), "secureboot enabled string not available in dmesg"

def test_efi_exposure_sysfs():
    assert os.path.isdir("/sys/firmware/efi/efivars")
    