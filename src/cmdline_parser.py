from dataclasses import dataclass
import argparse


@dataclass(frozen=True)
class LauncherConfig:
    config: str


def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', required=True)
    arguments = parser.parse_args(args)

    return LauncherConfig(arguments.config)
