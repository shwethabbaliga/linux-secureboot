import subprocess

class Secureboot:
    def sb_state(self):
        state = subprocess.run(
            "mokutil --sb-state",
            shell=True,
            capture_output=True,
            text=True
        )
        return state.capture_output


