import subprocess

def test_chatter():
    process = subprocess.check_output("kecal", shell=True)
    assert process == b"Hello world!\n"