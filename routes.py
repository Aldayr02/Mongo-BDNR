#!/usr/bin/env python3
from typing import List

from fastapi import APIRouter, Body, HTTPException, Request, Response, status
from fastapi.encoders import jsonable_encoder
from model import Flight, FlightSummary

router = APIRouter()


@router.post(
    "/",
    response_description="Post a new flight",
    status_code=status.HTTP_201_CREATED,
    response_model=Flight,  # Ensure that this response model reflects the Flight schema
)
def create_flight(request: Request, flight: Flight = Body(...)):
    flight = jsonable_encoder(flight)
    new_flight = request.app.database["flights"].insert_one(flight)
    created_flight = request.app.database["flights"].find_one(
        {"_id": new_flight.inserted_id}
    )
    return created_flight


@router.get(
    "/flight-summary-by-ticket",
    response_description="Get monthly flight summaries for each airline based on ticket type",
    response_model=List[FlightSummary],
    status_code=status.HTTP_200_OK,
)
def get_flight_summary_by_ticket(request: Request, ticket: str):
    pipeline = [
        {
            "$match": {
                "age": {"$gt": 18},
                "transit": "Car rental",
                "connection": False,
                "ticket": ticket,  # Use the ticket type provided by the user
            }
        },
        {
            "$group": {
                "_id": {"airline": "$airline", "month": "$month"},
                "count": {"$sum": 1},
            }
        },
        {"$sort": {"count": -1}},
        {
            "$group": {
                "_id": "$_id.airline",
                "mostFlightsMonth": {"$first": "$_id.month"},
                "flights": {"$first": "$count"},
            }
        },
        {
            "$project": {
                "_id": 0,
                "airline": "$_id",
                "mostFlightsMonth": 1,
                "flights": 1,
            }
        },
    ]
    result = list(request.app.database["flights"].aggregate(pipeline))
    return result
