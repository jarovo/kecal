import subprocess

def test_chatter():
    server_process = subprocess.Popen("kecal", shell=True)
    client_process = subprocess.Popen("kecal", shell=True)
    assert server_process == b"Listening on (127.0.0.1', 8888)\n"