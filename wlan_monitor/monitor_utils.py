import subprocess
import argparse
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def start_monitoring(interface, channel=None):
    clean_cmd = [
        "airmon-ng",
        "check",
        "kill"
    ]
    start_cmd = ["airmon-ng",
        "start",
        interface,
        ]
    if channel:
        start_cmd.extend(str(channel))
    subprocess.call(clean_cmd)
    subprocess.call(start_cmd)


def stop_monitoring(interface):
    interface += 'mon'
    stop_cmd = ["airmon-ng",
        "stop",
        interface,
        ]
    subprocess.call(stop_cmd)


def switch_interface(interface, channel):
    stop_monitoring(interface)
    start_monitoring(interface, channel)


def change_interface_channel(interface, channel=None):
    stop_monitoring(interface)
    start_monitoring(interface, channel)


