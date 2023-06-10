import asyncio
import pytest


@pytest.mark.asyncio
async def test_chatter():
    #    server_process = await asyncio.create_subprocess_shell('kecal-server', stdout=asyncio.subprocess.PIPE)
    client_process = await asyncio.create_subprocess_shell("kecal-client")

    # Read one line of output.
    #   data = await asyncio.wait_for(server_process.stdout.readline(), timeout=3)
    # line = data.decode('ascii').rstrip()
    #    assert line == b"Listening on ('127.0.0.1', 8888)\n"

    #    data = await server_process.stdout.readline()
    #    line = data.decode('ascii').rstrip()
    #    assert line == b"Hello world!\n"

    # Wait for the subprocess exit.
    await client_process.wait()


#   await server_process.wait()
