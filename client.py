#!/usr/bin/env python3
import argparse
import logging
import os

import requests

# Set logger
log = logging.getLogger()
log.setLevel("INFO")
handler = logging.FileHandler("books.log")
handler.setFormatter(
    logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
)
log.addHandler(handler)

# Read env vars related to API connection
FLIGHTS_API_URL = os.getenv("BOOKS_API_URL", "http://localhost:8000")


def print_flight_summary(flight_summaries):
    for flight_summary in flight_summaries:
        # print(flight_summary)
        print(f"Airline: {flight_summary['airline']}")
        print(f"Month with Most Flights: {flight_summary['mostFlightsMonth']}")
        print(f"Number of Flights: {flight_summary['flights']}")
        print("-------------------------------")


def list_flight_summaries(ticket_type):
    suffix = "/flight/flight-summary-by-ticket"
    endpoint = FLIGHTS_API_URL + suffix
    params = {"ticket": ticket_type}
    response = requests.get(endpoint, params=params)

    if response.ok:
        json_resp = response.json()
        print_flight_summary(json_resp)
    else:
        print(f"Error: {response}")


def main():
    log.info(
        "Welcome to the flight management system. App requests to: [FLIGHTS_API_URL]"
    )

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--ticket",
        help="Search by ticket type (Economy, Business, First Class)",
        choices=["Economy", "Business", "First Class"],
        required=True,
    )

    args = parser.parse_args()

    if args.ticket:
        list_flight_summaries(args.ticket)
    else:
        log.error("No valid ticket type provided.")


if __name__ == "__main__":
    main()
