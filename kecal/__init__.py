import argparse


def make_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kecal-client", description="Chatting client.", epilog="Have a nice chat!"
    )
    parser.add_argument("server_ip", type=str)
    parser.add_argument("server_port", type=int)
    return parser
