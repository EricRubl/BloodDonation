class RequestStatus(object):
    to_string = {
        0: "open",
        1: "escalated",
        2: "in_progress",
        3: "closed"
    }

    to_code = {
        "open": 0,
        "escalated": 1,
        "in_progress": 2,
        "closed": 3
    }
