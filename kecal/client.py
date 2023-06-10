import argparse
import asyncio

import kecal


async def tcp_echo_client(message) -> None:
    args = kecal.make_argparser().parse_args()

    reader, writer = await asyncio.open_connection(args.server_ip, args.server_port)

    print(f"Send: {message!r}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Received: {data.decode()!r}")

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


def main() -> None:
    asyncio.run(tcp_echo_client("Hello World!"))
