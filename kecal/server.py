import argparse
import asyncio

import kecal


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


async def async_main():
    parser = argparse.ArgumentParser(
             prog='kecal-server',
             description='Chatting server.',
             epilog="Let get connected!")
    args = kecal.make_argparser(parser).parse_args()

    server = await asyncio.start_server(
        handle_echo, args.server_ip, args.server_port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

def main():
    asyncio.run(async_main())