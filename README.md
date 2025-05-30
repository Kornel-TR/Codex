# Reablement Service Demo

This repository contains a small Python module `reablement_system.py` that
implements a simple in-memory system for managing clients, employees, visit
types, and visits. It also includes a placeholder route optimization function.

The `ReablementService` class offers helper methods to create and store data
entries and to retrieve an optimized list of visits for a given day. The route
optimization currently sorts visits by client address. Integrate with Google
Maps or another service if you need real optimization logic.

Example usage:

```python
from datetime import datetime
from reablement_system import ReablementService

service = ReablementService()
client_id = service.create_client("Alice", "221B Baker Street")
employee_id = service.create_employee("Bob")
visit_type_id = service.create_visit_type("Morning Support", 60)
visit_id = service.create_visit(client_id, employee_id, visit_type_id, datetime.now())

optimized = service.optimize_route(datetime.now().date())
for visit in optimized:
    print(service.clients[visit.client_id].name, visit.start_time)
```

This is only a demonstration module and does not persist data between runs.
