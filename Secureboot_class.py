import subprocess

class Secureboot:
    def sb_state(self):
        state = subprocess.run(
            "mokutil --sb-state",
            shell=True,
            capture_output=True,
            text=True
        )
        if state.returncode :
            return state.stdout
        else :
            print ("Mokutil command was not executed")
            return -1

sb_object=Secureboot()

def test_secureboot_state():
    value = sb_object.sb_state()

    assert value != -1 and "enabled" in value, "Secureboot is disabled"


