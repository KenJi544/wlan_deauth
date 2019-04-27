import subprocess
import csv
import logging


class CSVFileCreateException(Exception):
    pass


def create_csv(interface, bssid, channel=None):
    """
    Creates a CSV file of all STATION from the same BSSID
    and returns it's name
    """
    csv_file_name = 'targets_list'
    create_file_cmd = [
        'airodump-ng',
        '-d',
        bssid,
        '-w',
        csv_file_name,
        '--output-format',
        'csv',
        interface,
    ]
    if channel:
        create_file_cmd.append('-c '+channel)
    subprocess.call(create_file_cmd)


def gather_station_list(csv_file_name):
    """
    Generates a list of all stations from CSV file
    """
    if not csv_file_name:
        raise CSVFileCreateException("No CSV file was created")
        return -1

    station_list = ['']

    with open(csv_file_name, 'r') as f:
        reader = csv.reader(f)
        row_number = 0
        for row in reader:
            if row_number > 4 and row:
                station_name = row[0]
                station_list.append(station_name)
            row_number += 1
        del station_list[0]
    return station_list


def clean_tracks(csv_file_name):
    clean_cmd = ['rm', csv_file_name]
    subprocess(clean_cmd)


if __name__ == "__main__":
    pass
