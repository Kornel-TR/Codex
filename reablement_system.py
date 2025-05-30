from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class Client:
    id: int
    name: str
    address: str

@dataclass
class Employee:
    id: int
    name: str

@dataclass
class VisitType:
    id: int
    name: str
    duration_minutes: int

@dataclass
class Visit:
    id: int
    client_id: int
    employee_id: int
    visit_type_id: int
    start_time: datetime

class ReablementService:
    """Simple in-memory reablement service."""

    def __init__(self) -> None:
        self.clients: Dict[int, Client] = {}
        self.employees: Dict[int, Employee] = {}
        self.visit_types: Dict[int, VisitType] = {}
        self.visits: Dict[int, Visit] = {}
        self._next_client_id = 1
        self._next_employee_id = 1
        self._next_visit_type_id = 1
        self._next_visit_id = 1

    # Creation helpers
    def create_client(self, name: str, address: str) -> int:
        cid = self._next_client_id
        self.clients[cid] = Client(id=cid, name=name, address=address)
        self._next_client_id += 1
        return cid

    def create_employee(self, name: str) -> int:
        eid = self._next_employee_id
        self.employees[eid] = Employee(id=eid, name=name)
        self._next_employee_id += 1
        return eid

    def create_visit_type(self, name: str, duration_minutes: int) -> int:
        vid = self._next_visit_type_id
        self.visit_types[vid] = VisitType(id=vid, name=name, duration_minutes=duration_minutes)
        self._next_visit_type_id += 1
        return vid

    def create_visit(
        self,
        client_id: int,
        employee_id: int,
        visit_type_id: int,
        start_time: datetime,
    ) -> int:
        vid = self._next_visit_id
        self.visits[vid] = Visit(
            id=vid,
            client_id=client_id,
            employee_id=employee_id,
            visit_type_id=visit_type_id,
            start_time=start_time,
        )
        self._next_visit_id += 1
        return vid

    def optimize_route(self, date: datetime.date) -> List[Visit]:
        """Return visits for the day in optimized order.

        This placeholder sorts by client address. Integrate with Google Maps
        or another service for real optimization.
        """
        visits_for_date = [v for v in self.visits.values() if v.start_time.date() == date]
        visits_for_date.sort(key=lambda v: self.clients[v.client_id].address)
        return visits_for_date
