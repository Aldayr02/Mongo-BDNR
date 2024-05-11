#!/usr/bin/env python3
import uuid
from typing import Optional

from pydantic import BaseModel, Field


class Flight(BaseModel):
    airline: str = Field(...)
    from_: str = Field(..., alias="from")
    to: str = Field(...)
    day: int = Field(...)
    month: int = Field(...)
    year: int = Field(...)
    duration: int = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    reason: str = Field(...)
    stay: str = Field(...)
    transit: str = Field(...)
    connection: bool = Field(...)
    wait: int = Field(...)
    ticket: str = Field(...)
    checked_bags: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "663eacf55bab0ed855291a64",
                "airline": "Volaris",
                "from": "SJC",
                "to": "JFK",
                "day": 21,
                "month": 4,
                "year": 2015,
                "duration": 257,
                "age": 3,
                "gender": "male",
                "reason": "On vacation/Pleasure",
                "stay": "Hotel",
                "transit": "Public Transportation",
                "connection": False,
                "wait": 0,
                "ticket": "Economy",
                "checked_bags": 0,
            }
        }


class FlightSummary(BaseModel):
    airline: str
    mostFlightsMonth: int
    flights: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "airline": "Example Airline",
                "mostFlightsMonth": 7,  # Example month as July
                "flights": 150,  # Example number of flights
            }
        }
