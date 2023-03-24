
import argparse

def make_argparser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument('server_ip', type=str)
    parser.add_argument('server_port', type=int)
    return parser