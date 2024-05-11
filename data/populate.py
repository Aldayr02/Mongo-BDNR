#!/usr/bin/env python3
import csv

import requests

BASE_URL = "http://localhost:8000"


def main():
    with open("flights.csv") as fd:
        flights_csv = csv.DictReader(fd)
        for flight in flights_csv:
            response = requests.post(BASE_URL + "/flight", json=flight)
            if not response.ok:
                print(f"Failed to post flight {flight} - {response.text}")


if __name__ == "__main__":
    main()
