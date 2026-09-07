"""Manually defined OpenAPI paths merged into generated Swagger JSON.

Each entry maps to a Frappe API used in WerkIQ Go.postman_collection.json.
WerkIQ Go custom APIs (werkiq_go.api.*) are auto-discovered — not listed here.
"""

_JSON_BODY = {
    "required": True,
    "content": {
        "application/json": {
            "schema": {"type": "object"},
        },
    },
}

_OK_RESPONSE = {
    "200": {
        "description": "Successful response",
        "content": {
            "application/json": {"schema": {"type": "object"}},
        },
    },
}

CUSTOM_APIS = {
    # ==================================================================
    # Travel Expense Claim (Postman folder)
    # ==================================================================
    "/api/resource/Travel Expense Claim": {
        "post": {
            "summary": "Travel Expense Claim — Add",
            "description": "Create a new Travel Expense Claim document.",
            "tags": ["Travel Expense Claim"],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Travel Expense Claim/{name}": {
        "put": {
            "summary": "Travel Expense Claim — Edit",
            "description": "Update an existing Travel Expense Claim document.",
            "tags": ["Travel Expense Claim"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "KMAH-TR-2026-00006",
                },
            ],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Expense Approver CC": {
        "get": {
            "summary": "Travel Expense Claim — get_approver_cc",
            "description": "Get Expense Approver CC rows for an employee.",
            "tags": ["Travel Expense Claim"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '["parent","custom_leave_approver_cc"]',
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '[["parent","=","HR-EMP-00532"]]',
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Other Expense Claim (Postman folder)
    # ==================================================================
    "/api/resource/Other Expense Claim": {
        "post": {
            "summary": "Other Expense Claim — Add",
            "description": "Create a new Other Expense Claim document.",
            "tags": ["Other Expense Claim"],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Other Expense Claim/{name}": {
        "put": {
            "summary": "Other Expense Claim — Edit",
            "description": "Update an existing Other Expense Claim document.",
            "tags": ["Other Expense Claim"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "EGDE-OEC-2026-00010",
                },
            ],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Entertainment Expense Claim (Postman folder)
    # ==================================================================
    "/api/resource/Entertainment Expense Claim": {
        "post": {
            "summary": "Entertainment Expense Claim — Add",
            "description": "Create a new Entertainment Expense Claim document.",
            "tags": ["Entertainment Expense Claim"],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Entertainment Expense Claim/{name}": {
        "put": {
            "summary": "Entertainment Expense Claim — Edit",
            "description": "Update an existing Entertainment Expense Claim document.",
            "tags": ["Entertainment Expense Claim"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "EGDE-EN-2026-00017",
                },
            ],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Travel Request (Postman folder)
    # ==================================================================
    "/api/resource/Travel Request": {
        "post": {
            "summary": "Travel Request — Add",
            "description": "Create a new Travel Request document.",
            "tags": ["Travel Request"],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
        "get": {
            "summary": "Travel Request — List",
            "description": "List Travel Request documents.",
            "tags": ["Travel Request"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "limit_page_length",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer"},
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Travel Request/{name}": {
        "put": {
            "summary": "Travel Request — Edit",
            "description": "Update an existing Travel Request document.",
            "tags": ["Travel Request"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "KMAH-TRQ-2026-00007",
                },
            ],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
        "delete": {
            "summary": "Travel Request — Delete",
            "description": "Delete a Travel Request document.",
            "tags": ["Travel Request"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "EGDE-TRQ-2026-00006",
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Purpose of Travel": {
        "get": {
            "summary": "Travel Request — Purpose of Travel",
            "description": "List Purpose of Travel master records.",
            "tags": ["Travel Request"],
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Attendance (Postman folder — Frappe resource only)
    # ==================================================================
    "/api/resource/Attendance": {
        "get": {
            "summary": "Attendance — Attendance List",
            "description": "List Attendance records for an employee.",
            "tags": ["Attendance"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '["name","employee","employee_name","attendance_date","status","in_time","out_time","working_hours"]',
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '[["employee","=","HR-EMP-00277"]]',
                },
                {
                    "name": "order_by",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": "attendance_date desc",
                },
                {
                    "name": "limit_page_length",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer"},
                    "example": 100,
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Leave (werkiq_go.api.leave.get_leave_balance is auto-discovered;
    # create/list/edit use Frappe REST on Leave Application)
    # ==================================================================
    "/api/resource/Leave Application": {
        "get": {
            "summary": "Leave Application — List",
            "description": "List leave applications for the logged-in employee.",
            "tags": ["Leave"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '["name","employee","leave_type","from_date","to_date","total_leave_days","status","workflow_state"]',
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '[["employee","=","HR-EMP-00277"]]',
                },
                {
                    "name": "order_by",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": "from_date desc",
                },
                {
                    "name": "limit_page_length",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer"},
                    "example": 20,
                },
            ],
            "responses": _OK_RESPONSE,
        },
        "post": {
            "summary": "Leave Application — Add",
            "description": "Create a new Leave Application document.",
            "tags": ["Leave"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "doctype": {"type": "string", "example": "Leave Application"},
                                "employee": {"type": "string", "example": "HR-EMP-00277"},
                                "leave_type": {"type": "string", "example": "JUR - Jahresurlaub"},
                                "from_date": {"type": "string", "format": "date"},
                                "to_date": {"type": "string", "format": "date"},
                                "half_day": {"type": "integer", "example": 0},
                                "description": {"type": "string"},
                            },
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Leave Application/{name}": {
        "get": {
            "summary": "Leave Application — Get",
            "description": "Get a single Leave Application by name.",
            "tags": ["Leave"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "HR-LAP-2026-00001",
                },
            ],
            "responses": _OK_RESPONSE,
        },
        "put": {
            "summary": "Leave Application — Edit",
            "description": "Update an existing Leave Application document.",
            "tags": ["Leave"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "HR-LAP-2026-00001",
                },
            ],
            "requestBody": _JSON_BODY,
            "responses": _OK_RESPONSE,
        },
        "delete": {
            "summary": "Leave Application — Delete",
            "description": "Delete a draft Leave Application document.",
            "tags": ["Leave"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "HR-LAP-2026-00001",
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Leave Type": {
        "get": {
            "summary": "Leave Type — List",
            "description": "List available leave types for the leave application form.",
            "tags": ["Leave"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '["name","max_leaves_allowed","is_lwp"]',
                },
                {
                    "name": "limit_page_length",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer"},
                    "example": 0,
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Workflow (Postman: submit / approve / reject on all claim types)
    # ==================================================================
    "/api/method/frappe.model.workflow.apply_workflow": {
        "post": {
            "summary": "Apply Workflow Action",
            "description": (
                "Submit For Approval, Approve, or Reject a document. "
                "Used for Travel Expense Claim, Other Expense Claim, "
                "Entertainment Expense Claim, Travel Request, and Leave Application."
            ),
            "tags": ["Frappe Workflow"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": ["doc", "action"],
                            "properties": {
                                "doc": {
                                    "type": "object",
                                    "properties": {
                                        "doctype": {"type": "string"},
                                        "name": {"type": "string"},
                                        "workflow_state": {"type": "string"},
                                    },
                                },
                                "action": {
                                    "type": "string",
                                    "example": "Approve",
                                },
                            },
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Auth & master data (Postman root-level requests)
    # ==================================================================
    "/api/method/login": {
        "post": {
            "summary": "login 2 — Frappe Login",
            "description": "Frappe built-in session login (usr + pwd).",
            "tags": ["Auth"],
            "security": [],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": ["usr", "pwd"],
                            "properties": {
                                "usr": {"type": "string", "example": "user@example.com"},
                                "pwd": {"type": "string", "format": "password"},
                            },
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/logout": {
        "post": {
            "summary": "logout",
            "description": "Frappe built-in session logout.",
            "tags": ["Auth"],
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.auth.get_logged_user": {
        "get": {
            "summary": "get_user_id — Get Logged User",
            "description": "Returns the currently logged-in Frappe user email.",
            "tags": ["Auth"],
            "responses": {
                "200": {
                    "description": "Successful response",
                    "content": {
                        "application/json": {"schema": {"type": "string"}},
                    },
                },
            },
        },
    },
    "/api/resource/Employee": {
        "get": {
            "summary": "get_employee_list / get_employee_id",
            "description": (
                "List Employee records. Use fields for employee list or "
                "filters for lookup by user_id."
            ),
            "tags": ["Employee"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '["name","company","employee_name"]',
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": '[["user_id","=","user@example.com"]]',
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Department": {
        "get": {
            "summary": "department_list",
            "description": "List Department records.",
            "tags": ["Employee"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/User/{name}": {
        "put": {
            "summary": "language update",
            "description": "Update User document (e.g. language preference).",
            "tags": ["Employee"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "user@example.com",
                },
            ],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "language": {"type": "string", "example": "en"},
                            },
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Country": {
        "get": {
            "summary": "Country List",
            "description": "List all Country records.",
            "tags": ["Master Data"],
            "parameters": [
                {
                    "name": "limit_page_length",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer"},
                    "example": 0,
                },
            ],
            "responses": _OK_RESPONSE,
        },
    },
}
