from state_machine.wlan_machine import Wlan
from wlan_monitor.monitor_utils import start_monitoring, stop_monitoring

import logging
import argparse


logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description='pass interface to start/stop monitoring'
)
parser.add_argument(
    '-i',
    '--interface',
    required=True,
    type=str,
    help='interface name'
)
parser.add_argument(
    '-c',
    '--channel',
    type=str,
    help='channel number'
)
parser.add_argument(
    '--on',
    action='store_true',
    default=False,
    help='restart interface flag',
)
parser.add_argument(
    '--off',
    action='store_true',
    default=False,
    help='restart interface flag',
)
parser.add_argument(
    '-r',
    '--restart',
    action='store_true',
    default=False,
    help='restart interface flag',
)


interface = None
channel = None


def restart(interface, channel):
    """
    Restarts wlan monitoring
    """
    stop_monitoring(interface)
    start_monitoring(interface, channel)


if __name__=="__main__":
    arg = parser.parse_args()
    if not arg.interface:
        logger.error("Give a mon interface")
    interface = arg.interface
    channel = arg.channel
    if arg.off:
        stop_monitoring(interface)
    elif arg.on:
        start_monitoring(interface, channel)
    else:
        restart(interface, channel)
