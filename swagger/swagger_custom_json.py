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
    # Travel Expense Claim (Postman folder — 6 requests only)
    # ==================================================================
    "/api/resource/Travel Expense Claim": {
        "post": {
            "summary": "Add",
            "description": "Create a new Travel Expense Claim document.",
            "tags": ["Travel Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Travel Expense Claim",
                            "company": "KMS Autohof-Betriebs 123",
                            "posting_date": "2026-08-01",
                            "edit_posting_date": 0,
                            "copy_recipient": [],
                            "hotel_booking_with_breakfast": "Yes",
                            "country": "Germany",
                            "employee_id": "HR-EMP-00277",
                            "employee_name": "Approver",
                            "company_code": "KMAH",
                            "approver": "chohan95332@gmail.com",
                            "departure_date_and_time": "2026-07-28 21:58:00",
                            "arrival_date_and_time": "2026-07-29 00:00:00",
                            "full_day": 28,
                            "half_day": 14,
                            "daily_allowance": 1,
                            "daily_allowance_details": [
                                {
                                    "doctype": "Travel Expense Daily Allowance Detail",
                                    "is_overnight_stay": 0,
                                    "category_code": "101802",
                                    "breakfast": 1,
                                    "lunch": 0,
                                    "dinner": 0,
                                    "tip_amount": 0,
                                    "total": 8.4,
                                    "travel_date": "2026-07-28",
                                    "overnight_stay": 14,
                                    "number_of_overnight_stay": 1,
                                },
                                {
                                    "doctype": "Travel Expense Daily Allowance Detail",
                                    "is_overnight_stay": 0,
                                    "category_code": "101802",
                                    "breakfast": 1,
                                    "lunch": 0,
                                    "dinner": 0,
                                    "tip_amount": 0,
                                    "total": 8.4,
                                    "travel_date": "2026-07-29",
                                    "overnight_stay": 14,
                                    "number_of_overnight_stay": 1,
                                },
                            ],
                            "invoice_claim": 1,
                            "use_ai": 1,
                            "replacement_receipt": 0,
                            "invoice_claim_details": [
                                {
                                    "doctype": "Travel Expense Invoice Claim Detail",
                                    "quantity": 1,
                                    "currency": "EUR",
                                    "vat_rate": 19,
                                    "price": 85.63,
                                    "vat_amount": 16.27,
                                    "net_amount": 85.63,
                                    "gross_amount": 101.9,
                                    "vendor_name": "cyberport",
                                    "invoice_no": "600265812752",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/MPPS6ASF_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "tax_included": "Yes",
                                    "description": "1Q07-033 Microsoft Surface Slim Pen 2",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Flight Ticket (Domestic)",
                                    "exchange_rate": 1,
                                    "category_code": "101803",
                                },
                                {
                                    "doctype": "Travel Expense Invoice Claim Detail",
                                    "quantity": 1,
                                    "currency": "EUR",
                                    "vat_rate": 19,
                                    "price": 119.24,
                                    "vat_amount": 22.66,
                                    "net_amount": 119.24,
                                    "gross_amount": 141.9,
                                    "vendor_name": "cyberport",
                                    "invoice_no": "600165812752",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/MPPS6ASF_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "tax_included": "Yes",
                                    "description": "1T27-02Y Microsoft Surface Pro",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Flight Ticket (Domestic)",
                                    "exchange_rate": 1,
                                    "category_code": "101803",
                                },
                            ],
                            "private_car": 1,
                            "private_car_expense_detail": [
                                {
                                    "doctype": "Travel Expense Private Car Detail",
                                    "category_code": "101801",
                                    "travel_date": "2026-08-01",
                                    "from_address": "Lahore",
                                    "to_address": "Karachi",
                                    "travelled_kilometers": 1200,
                                    "rate_per_km": 0.38,
                                    "claimed_amount": 456,
                                    "vat_rate": 0,
                                    "vat_amount": 0,
                                }
                            ],
                            "total_tip": 0,
                            "total_vat_amount": 38.93,
                            "grand_total": 733.4,
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Travel Expense Claim/{name}": {
        "put": {
            "summary": "Edit",
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
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Travel Expense Claim",
                            "company": "KMS Autohof-Betriebs",
                            "posting_date": "2026-08-01",
                            "edit_posting_date": 0,
                            "copy_recipient": [],
                            "hotel_booking_with_breakfast": "Yes",
                            "country": "Germany",
                            "employee_id": "HR-EMP-00277",
                            "employee_name": "Approver",
                            "company_code": "KMAH",
                            "approver": "chohan95332@gmail.com",
                            "departure_date_and_time": "2026-07-28 21:58:00",
                            "arrival_date_and_time": "2026-07-29 00:00:00",
                            "full_day": 28,
                            "half_day": 14,
                            "reason_business_purpose": "test 1",
                            "daily_allowance": 1,
                            "daily_allowance_details": [
                                {
                                    "doctype": "Travel Expense Daily Allowance Detail",
                                    "is_overnight_stay": 0,
                                    "category_code": "101802",
                                    "breakfast": 1,
                                    "lunch": 0,
                                    "dinner": 0,
                                    "tip_amount": 0,
                                    "total": 8.4,
                                    "travel_date": "2026-07-28",
                                    "overnight_stay": 14,
                                    "number_of_overnight_stay": 1,
                                },
                                {
                                    "doctype": "Travel Expense Daily Allowance Detail",
                                    "is_overnight_stay": 0,
                                    "category_code": "101802",
                                    "breakfast": 1,
                                    "lunch": 0,
                                    "dinner": 0,
                                    "tip_amount": 0,
                                    "total": 8.4,
                                    "travel_date": "2026-07-29",
                                    "overnight_stay": 14,
                                    "number_of_overnight_stay": 1,
                                },
                            ],
                            "invoice_claim": 1,
                            "use_ai": 1,
                            "replacement_receipt": 0,
                            "invoice_claim_details": [
                                {
                                    "doctype": "Travel Expense Invoice Claim Detail",
                                    "quantity": 1,
                                    "currency": "EUR",
                                    "vat_rate": 19,
                                    "price": 85.63,
                                    "vat_amount": 16.27,
                                    "net_amount": 85.63,
                                    "gross_amount": 101.9,
                                    "vendor_name": "cyberport",
                                    "invoice_no": "600265812752",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/MPPS6ASF_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "tax_included": "Yes",
                                    "description": "1Q07-033 Microsoft Surface Slim Pen 2",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Flight Ticket (Domestic)",
                                    "exchange_rate": 1,
                                    "category_code": "101803",
                                },
                                {
                                    "doctype": "Travel Expense Invoice Claim Detail",
                                    "quantity": 1,
                                    "currency": "EUR",
                                    "vat_rate": 19,
                                    "price": 119.24,
                                    "vat_amount": 22.66,
                                    "net_amount": 119.24,
                                    "gross_amount": 141.9,
                                    "vendor_name": "cyberport",
                                    "invoice_no": "600165812752",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/MPPS6ASF_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "tax_included": "Yes",
                                    "description": "1T27-02Y Microsoft Surface Pro",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Flight Ticket (Domestic)",
                                    "exchange_rate": 1,
                                    "category_code": "101803",
                                },
                            ],
                            "private_car": 1,
                            "private_car_expense_detail": [
                                {
                                    "doctype": "Travel Expense Private Car Detail",
                                    "category_code": "101801",
                                    "travel_date": "2026-08-01",
                                    "from_address": "Lahore",
                                    "to_address": "Karachi",
                                    "travelled_kilometers": 1200,
                                    "rate_per_km": 0.38,
                                    "claimed_amount": 456,
                                    "vat_rate": 0,
                                    "vat_amount": 0,
                                }
                            ],
                            "total_tip": 0,
                            "total_vat_amount": 38.93,
                            "grand_total": 733.4,
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Expense Approver CC": {
        "get": {
            "summary": "get_approver_cc",
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
    "/api/method/frappe.model.workflow.apply_workflow/submit-for-approval": {
        "post": {
            "summary": "submit for approval",
            "description": "Travel Expense Claim — submit for approval via apply_workflow.",
            "tags": ["Travel Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Travel Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Draft",
                            },
                            "action": "Submit For Approval",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/approve": {
        "post": {
            "summary": "approve",
            "description": "Travel Expense Claim — approve via apply_workflow.",
            "tags": ["Travel Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Travel Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Approve",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/reject": {
        "post": {
            "summary": "Reject",
            "description": "Travel Expense Claim — reject via apply_workflow.",
            "tags": ["Travel Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Travel Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Reject",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Other Expense Claim (Postman folder — 5 requests)
    # ==================================================================
    "/api/resource/Other Expense Claim": {
        "post": {
            "summary": "Add",
            "description": "Create a new Other Expense Claim document.",
            "tags": ["Other Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Other Expense Claim",
                            "company": "EG Deutschland GmbH",
                            "posting_date": "2026-08-01",
                            "edit_posting_date": 0,
                            "copy_recipient": [
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "adasd@gmail.com",
                                }
                            ],
                            "paid": 0,
                            "processed": 0,
                            "use_ai": 0,
                            "replacement_receipt": 1,
                            "other_expense_detail": [
                                {
                                    "doctype": "Other Expense Detail",
                                    "currency": "EUR",
                                    "category_code": "101862",
                                    "exchange_rate": 1,
                                    "price": 86.96,
                                    "vat_rate": 15,
                                    "vat_amount": 13.04,
                                    "net_amount": 86.96,
                                    "gross_amount": 100,
                                    "base_price": 100,
                                    "base_vat_amount": 13.04,
                                    "base_net_amount": 86.96,
                                    "base_gross_amount": 100,
                                    "base_tip_amount": 0,
                                    "tip_amount": 0,
                                    "vendor_name": "ATest",
                                    "invoice_date": "2026-08-01",
                                    "invoice_no": "OTH-100001",
                                    "tax_included": "Yes",
                                }
                            ],
                            "total_vat_amount": 13.04,
                            "total_tip": 0,
                            "grand_total": 100,
                            "employee_id": "HR-EMP-00276",
                            "employee_name": "Applicant",
                            "company_code": "EGDE",
                            "approver": "chohan952@gmail.com",
                            "reason_business_purpose": "Test 1",
                            "travel_request": "EGDE-TRQ-2026-00004",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Other Expense Claim/{name}": {
        "put": {
            "summary": "Edit",
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
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Other Expense Claim",
                            "company": "EG Deutschland GmbH",
                            "posting_date": "2026-08-01",
                            "edit_posting_date": 0,
                            "copy_recipient": [
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "adasd@gmail.com",
                                }
                            ],
                            "paid": 0,
                            "processed": 0,
                            "use_ai": 0,
                            "replacement_receipt": 1,
                            "other_expense_detail": [
                                {
                                    "doctype": "Other Expense Detail",
                                    "currency": "EUR",
                                    "category_code": "101862",
                                    "exchange_rate": 1,
                                    "price": 86.96,
                                    "vat_rate": 15,
                                    "vat_amount": 13.04,
                                    "net_amount": 86.96,
                                    "gross_amount": 100,
                                    "base_price": 100,
                                    "base_vat_amount": 13.04,
                                    "base_net_amount": 86.96,
                                    "base_gross_amount": 100,
                                    "base_tip_amount": 0,
                                    "tip_amount": 0,
                                    "vendor_name": "ATest",
                                    "invoice_date": "2026-08-01",
                                    "invoice_no": "OTH-100001",
                                    "tax_included": "Yes",
                                }
                            ],
                            "total_vat_amount": 13.04,
                            "total_tip": 0,
                            "grand_total": 100,
                            "employee_id": "HR-EMP-00276",
                            "employee_name": "Applicant",
                            "company_code": "EGDE",
                            "approver": "chohan952@gmail.com",
                            "reason_business_purpose": "Test 1112",
                            "travel_request": "EGDE-TRQ-2026-00004",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/other-expense-claim/submit-for-approval": {
        "post": {
            "summary": "submit for approval",
            "description": "Other Expense Claim — submit for approval via apply_workflow.",
            "tags": ["Other Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Other Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Draft",
                            },
                            "action": "Submit For Approval",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/other-expense-claim/approve": {
        "post": {
            "summary": "approve",
            "description": "Other Expense Claim — approve via apply_workflow.",
            "tags": ["Other Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Other Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Approve",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/other-expense-claim/reject": {
        "post": {
            "summary": "Reject",
            "description": "Other Expense Claim — reject via apply_workflow.",
            "tags": ["Other Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Other Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Reject",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Entertainment Expense Claim (Postman folder — 5 requests)
    # ==================================================================
    "/api/resource/Entertainment Expense Claim": {
        "post": {
            "summary": "Add",
            "description": "Create a new Entertainment Expense Claim document.",
            "tags": ["Entertainment Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Entertainment Expense Claim",
                            "company": "EG Deutschland GmbH",
                            "posting_date": "2026-07-10",
                            "edit_posting_date": 0,
                            "copy_recipient": [
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "adasd@gmail.com",
                                }
                            ],
                            "paid": 0,
                            "processed": 0,
                            "participants": [],
                            "hospitality_expense": 1,
                            "hospitality_expense_attachment_use_ai": 1,
                            "hospitality_replacement_receipt": 0,
                            "hospitality_expense_detail": [
                                {
                                    "doctype": "Hospitality Expense Detail",
                                    "currency": "EUR",
                                    "exchange_rate": 1,
                                    "base_price": 101.9,
                                    "base_vat_amount": 16.27,
                                    "base_net_amount": 85.63,
                                    "base_gross_amount": 101.9,
                                    "base_tip_amount": 0,
                                    "price": 85.63,
                                    "vat_amount": 16.27,
                                    "net_amount": 85.63,
                                    "gross_amount": 101.9,
                                    "tip_amount": 0,
                                    "expense_sub_category": "Entertainment expenses for business partners",
                                    "description": "Microsoft Surface Slim Pen 2",
                                    "category_code": "101852",
                                    "vendor_name": "Cyberport SE",
                                    "payment_method": "Card",
                                    "invoice_date": "2026-03-05",
                                    "invoice_no": "HOSP-100001",
                                    "quantity": 1,
                                    "vat_rate": 19,
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/07/10/File/288D3IVO_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                },
                                {
                                    "doctype": "Hospitality Expense Detail",
                                    "currency": "EUR",
                                    "exchange_rate": 1,
                                    "base_price": 141.9,
                                    "base_vat_amount": 22.66,
                                    "base_net_amount": 119.24,
                                    "base_gross_amount": 141.9,
                                    "base_tip_amount": 0,
                                    "price": 119.24,
                                    "vat_amount": 22.66,
                                    "net_amount": 119.24,
                                    "gross_amount": 141.9,
                                    "tip_amount": 0,
                                    "expense_sub_category": "Entertainment expenses for business partners",
                                    "description": "Microsoft Surface Pro",
                                    "category_code": "101852",
                                    "vendor_name": "Cyberport SE",
                                    "payment_method": "Card",
                                    "invoice_date": "2026-03-05",
                                    "invoice_no": "HOSP-100002",
                                    "quantity": 1,
                                    "vat_rate": 19,
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/07/10/File/288D3IVO_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                },
                            ],
                            "party_expense": 1,
                            "party_expense_attachment_use_ai": 1,
                            "party_replacement_receipt": 0,
                            "party_expense_detail": [
                                {
                                    "doctype": "Party Expense Detail",
                                    "currency": "EUR",
                                    "quantity": 1,
                                    "base_price": 101.9,
                                    "base_vat_amount": 16.27,
                                    "base_net_amount": 85.63,
                                    "base_gross_amount": 101.9,
                                    "base_tip_amount": 0,
                                    "price": 85.63,
                                    "vat_amount": 16.27,
                                    "net_amount": 85.63,
                                    "gross_amount": 101.9,
                                    "tip_amount": 0,
                                    "vendor_name": "Cyberport",
                                    "invoice_no": "PARTY-100001",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/337WNVWL_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "vat_rate": 19,
                                    "tax_included": "Yes",
                                    "description": "Microsoft Surface Slim Pen 2",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Company Event",
                                    "exchange_rate": 1,
                                    "category_code": "101860",
                                },
                                {
                                    "doctype": "Party Expense Detail",
                                    "currency": "EUR",
                                    "quantity": 1,
                                    "base_price": 141.9,
                                    "base_vat_amount": 22.66,
                                    "base_net_amount": 119.24,
                                    "base_gross_amount": 141.9,
                                    "base_tip_amount": 0,
                                    "price": 119.24,
                                    "vat_amount": 22.66,
                                    "net_amount": 119.24,
                                    "gross_amount": 141.9,
                                    "tip_amount": 0,
                                    "vendor_name": "Cyberport",
                                    "invoice_no": "PARTY-100002",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/337WNVWL_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "vat_rate": 19,
                                    "tax_included": "Yes",
                                    "description": "Microsoft Surface Pro",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Company Event",
                                    "exchange_rate": 1,
                                    "category_code": "101860",
                                },
                            ],
                            "gift_expense": 1,
                            "gift_expense_attachment_use_ai": 1,
                            "gift_replacement_receipt": 0,
                            "gift_expense_detail": [
                                {
                                    "doctype": "Gift Expense Claim Detail",
                                    "occasion": "Birthday",
                                    "currency": "EUR",
                                    "gift_category": "Below 35 EUR",
                                    "vat_rate": 19,
                                    "base_tip_amount": 0,
                                    "price": 15.04,
                                    "vat_amount": 2.86,
                                    "net_amount": 15.04,
                                    "gross_amount": 17.9,
                                    "vendor_name": "Premier Inn Köln City Süd",
                                    "invoice_no": "GIFT-100001",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/CGD1RVI5_scan-invoice.jpeg&file_name=scan-invoice.jpeg",
                                    "invoice_date": "2025-12-11",
                                    "payment_method": "Card",
                                    "quantity": 1,
                                    "base_price": 17.9,
                                    "base_vat_amount": 2.86,
                                    "base_gross_amount": 17.9,
                                    "base_net_amount": 15.04,
                                    "tax_included": "Yes",
                                    "description": "Frühstück Speisen",
                                    "expense_category": "Travel",
                                    "expense_sub_category": "Birthday Gift to Business Partner",
                                    "exchange_rate": 1,
                                    "tip_amount": 0,
                                    "category_code": "101856",
                                },
                                {
                                    "doctype": "Gift Expense Claim Detail",
                                    "occasion": "Birthday",
                                    "currency": "EUR",
                                    "gift_category": "Above 53 EUR",
                                    "vat_rate": 7,
                                    "base_tip_amount": 0,
                                    "price": 89.42,
                                    "vat_amount": 6.26,
                                    "net_amount": 89.42,
                                    "gross_amount": 95.68,
                                    "vendor_name": "Premier Inn Köln City Süd",
                                    "invoice_no": "GIFT-100002",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/CGD1RVI5_scan-invoice.jpeg&file_name=scan-invoice.jpeg",
                                    "invoice_date": "2025-12-11",
                                    "payment_method": "Card",
                                    "quantity": 1,
                                    "base_price": 95.68,
                                    "base_vat_amount": 6.26,
                                    "base_gross_amount": 95.68,
                                    "base_net_amount": 89.42,
                                    "tax_included": "Yes",
                                    "description": "Übernachtung",
                                    "expense_category": "Travel",
                                    "expense_sub_category": "Birthday Gift to Business Partner",
                                    "exchange_rate": 1,
                                    "tip_amount": 0,
                                    "category_code": "101856",
                                },
                            ],
                            "total_vat_amount": 86.98,
                            "total_tip_amount": 0,
                            "grand_total": 601.18,
                            "employee_id": "HR-EMP-00276",
                            "employee_name": "Applicant",
                            "company_code": "EGDE",
                            "approver": "chohan952@gmail.com",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Entertainment Expense Claim/{name}": {
        "put": {
            "summary": "Edit",
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
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Entertainment Expense Claim",
                            "name": "EGDE-EN-2026-00017",
                            "company": "EG Deutschland GmbH",
                            "posting_date": "2026-07-10",
                            "edit_posting_date": 0,
                            "copy_recipient": [
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "adasd@gmail.com",
                                }
                            ],
                            "participants": [
                                {
                                    "type": "Employee",
                                    "participant_name": "Tasawar",
                                    "company": "Timestx",
                                },
                                {
                                    "type": "Business Partner",
                                    "participant_name": "Junaid",
                                    "company": "TimesTx",
                                },
                            ],
                            "paid": 0,
                            "processed": 0,
                            "hospitality_expense": 1,
                            "hospitality_expense_attachment_use_ai": 1,
                            "hospitality_replacement_receipt": 0,
                            "hospitality_expense_detail": [
                                {
                                    "currency": "EUR",
                                    "exchange_rate": 1,
                                    "base_price": 101.9,
                                    "base_vat_amount": 16.27,
                                    "base_net_amount": 85.63,
                                    "base_gross_amount": 101.9,
                                    "base_tip_amount": 0,
                                    "price": 85.63,
                                    "vat_amount": 16.27,
                                    "net_amount": 85.63,
                                    "gross_amount": 101.9,
                                    "tip_amount": 0,
                                    "expense_sub_category": "Entertainment expenses for business partners",
                                    "description": "Microsoft Surface Slim Pen 21",
                                    "category_code": "101852",
                                    "vendor_name": "Cyberport SE",
                                    "payment_method": "Card",
                                    "invoice_date": "2026-03-05",
                                    "invoice_no": "HOSP-100001",
                                    "quantity": 1,
                                    "vat_rate": 19,
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/07/10/File/288D3IVO_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                },
                                {
                                    "currency": "EUR",
                                    "exchange_rate": 1,
                                    "base_price": 141.9,
                                    "base_vat_amount": 22.66,
                                    "base_net_amount": 119.24,
                                    "base_gross_amount": 141.9,
                                    "base_tip_amount": 0,
                                    "price": 119.24,
                                    "vat_amount": 22.66,
                                    "net_amount": 119.24,
                                    "gross_amount": 141.9,
                                    "tip_amount": 0,
                                    "expense_sub_category": "Entertainment expenses for business partners",
                                    "description": "Microsoft Surface Pro",
                                    "category_code": "101852",
                                    "vendor_name": "Cyberport SE",
                                    "payment_method": "Card",
                                    "invoice_date": "2026-03-05",
                                    "invoice_no": "HOSP-100002",
                                    "quantity": 1,
                                    "vat_rate": 19,
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/07/10/File/288D3IVO_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                },
                            ],
                            "party_expense": 1,
                            "party_expense_attachment_use_ai": 1,
                            "party_replacement_receipt": 0,
                            "party_expense_detail": [
                                {
                                    "currency": "EUR",
                                    "quantity": 1,
                                    "base_price": 101.9,
                                    "base_vat_amount": 16.27,
                                    "base_net_amount": 85.63,
                                    "base_gross_amount": 101.9,
                                    "base_tip_amount": 0,
                                    "price": 85.63,
                                    "vat_amount": 16.27,
                                    "net_amount": 85.63,
                                    "gross_amount": 101.9,
                                    "tip_amount": 0,
                                    "vendor_name": "Cyberport",
                                    "invoice_no": "PARTY-100001",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/337WNVWL_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "vat_rate": 19,
                                    "tax_included": "Yes",
                                    "description": "Microsoft Surface Slim Pen 2",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Company Event",
                                    "exchange_rate": 1,
                                    "category_code": "101860",
                                },
                                {
                                    "currency": "EUR",
                                    "quantity": 1,
                                    "base_price": 141.9,
                                    "base_vat_amount": 22.66,
                                    "base_net_amount": 119.24,
                                    "base_gross_amount": 141.9,
                                    "base_tip_amount": 0,
                                    "price": 119.24,
                                    "vat_amount": 22.66,
                                    "net_amount": 119.24,
                                    "gross_amount": 141.9,
                                    "tip_amount": 0,
                                    "vendor_name": "Cyberport",
                                    "invoice_no": "PARTY-100002",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/337WNVWL_No_vat_amount.jpg&file_name=No_vat_amount.jpg",
                                    "invoice_date": "2026-03-05",
                                    "payment_method": "Card",
                                    "vat_rate": 19,
                                    "tax_included": "Yes",
                                    "description": "Microsoft Surface Pro",
                                    "expense_category": "Office",
                                    "expense_sub_category": "Company Event",
                                    "exchange_rate": 1,
                                    "category_code": "101860",
                                },
                            ],
                            "gift_expense": 1,
                            "gift_expense_attachment_use_ai": 1,
                            "gift_replacement_receipt": 0,
                            "gift_expense_detail": [
                                {
                                    "occasion": "Birthday",
                                    "currency": "EUR",
                                    "gift_category": "Below 35 EUR",
                                    "vat_rate": 19,
                                    "base_tip_amount": 0,
                                    "price": 15.04,
                                    "vat_amount": 2.86,
                                    "net_amount": 15.04,
                                    "gross_amount": 17.9,
                                    "vendor_name": "Premier Inn Köln City Süd",
                                    "invoice_no": "GIFT-100001",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/CGD1RVI5_scan-invoice.jpeg&file_name=scan-invoice.jpeg",
                                    "invoice_date": "2025-12-11",
                                    "payment_method": "Card",
                                    "quantity": 1,
                                    "base_price": 17.9,
                                    "base_vat_amount": 2.86,
                                    "base_gross_amount": 17.9,
                                    "base_net_amount": 15.04,
                                    "tax_included": "Yes",
                                    "description": "Frühstück Speisen",
                                    "expense_category": "Travel",
                                    "expense_sub_category": "Birthday Gift to Business Partner",
                                    "exchange_rate": 1,
                                    "tip_amount": 0,
                                    "category_code": "101856",
                                },
                                {
                                    "occasion": "Birthday",
                                    "currency": "EUR",
                                    "gift_category": "Above 53 EUR",
                                    "vat_rate": 7,
                                    "base_tip_amount": 0,
                                    "price": 89.42,
                                    "vat_amount": 6.26,
                                    "net_amount": 89.42,
                                    "gross_amount": 95.68,
                                    "vendor_name": "Premier Inn Köln City Süd",
                                    "invoice_no": "GIFT-100002",
                                    "expense_attachment": "/api/method/frappe_s3_attachment.controller.generate_file?key=EG/2026/08/03/File/CGD1RVI5_scan-invoice.jpeg&file_name=scan-invoice.jpeg",
                                    "invoice_date": "2025-12-11",
                                    "payment_method": "Card",
                                    "quantity": 1,
                                    "base_price": 95.68,
                                    "base_vat_amount": 6.26,
                                    "base_gross_amount": 95.68,
                                    "base_net_amount": 89.42,
                                    "tax_included": "Yes",
                                    "description": "Übernachtung",
                                    "expense_category": "Travel",
                                    "expense_sub_category": "Birthday Gift to Business Partner",
                                    "exchange_rate": 1,
                                    "tip_amount": 0,
                                    "category_code": "101856",
                                },
                            ],
                            "total_vat_amount": 86.98,
                            "total_tip_amount": 0,
                            "grand_total": 601.18,
                            "employee_id": "HR-EMP-00276",
                            "employee_name": "Applicant",
                            "company_code": "EGDE",
                            "approver": "chohan952@gmail.com",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/entertainment-expense-claim/submit-for-approval": {
        "post": {
            "summary": "submit for approval",
            "description": "Entertainment Expense Claim — submit for approval via apply_workflow.",
            "tags": ["Entertainment Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Other Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Draft",
                            },
                            "action": "Submit For Approval",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/entertainment-expense-claim/approve": {
        "post": {
            "summary": "approve",
            "description": "Entertainment Expense Claim — approve via apply_workflow.",
            "tags": ["Entertainment Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Other Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Approve",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/entertainment-expense-claim/reject": {
        "post": {
            "summary": "Reject",
            "description": "Entertainment Expense Claim — reject via apply_workflow.",
            "tags": ["Entertainment Expense Claim"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Other Expense Claim",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Reject",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Travel Request (Postman folder — 7 requests)
    # ==================================================================
    "/api/resource/Travel Request": {
        "post": {
            "summary": "Add",
            "description": "Create a new Travel Request document.",
            "tags": ["Travel Request"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Travel Request",
                            "custom_expense_approver_cc": [
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "christian.lange@eg.group",
                                },
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "clemens.steiner@eg.group",
                                },
                            ],
                            "travel_type": "Domestic",
                            "travel_funding": "",
                            "custom_country": "Germany",
                            "itinerary": [
                                {
                                    "doctype": "Travel Itinerary",
                                    "mode_of_travel": "Flight",
                                    "meal_preference": "",
                                    "travel_from": "Lahore",
                                    "travel_to": "Karachi",
                                    "departure_date": "2026-08-15 19:35:00",
                                    "arrival_date": "2026-08-17 10:35:00",
                                }
                            ],
                            "employee": "HR-EMP-00277",
                            "purpose_of_travel": "Work",
                            "custom_estimated_cost": 100,
                            "description": "test 1",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Travel Request/{name}": {
        "put": {
            "summary": "Edit",
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
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doctype": "Travel Request",
                            "custom_expense_approver_cc": [
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "christian.lange@eg.group",
                                },
                                {
                                    "doctype": "Expense Approver CC",
                                    "approver": "clemens.steiner@eg.group",
                                },
                            ],
                            "travel_type": "Domestic",
                            "travel_funding": "",
                            "custom_country": "Germany",
                            "itinerary": [
                                {
                                    "doctype": "Travel Itinerary",
                                    "mode_of_travel": "Flight",
                                    "meal_preference": "",
                                    "travel_from": "Lahore",
                                    "travel_to": "Karachi",
                                    "departure_date": "2026-08-15 19:35:00",
                                    "arrival_date": "2026-08-17 10:35:00",
                                }
                            ],
                            "employee": "HR-EMP-00277",
                            "purpose_of_travel": "Work",
                            "custom_estimated_cost": 100,
                            "description": "test 11",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
        "delete": {
            "summary": "Delete",
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
    "/api/method/frappe.model.workflow.apply_workflow/travel-request/submit-for-approval": {
        "post": {
            "summary": "Submit for approval",
            "description": "Travel Request — submit for approval via apply_workflow.",
            "tags": ["Travel Request"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Travel Request",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Draft",
                            },
                            "action": "Submit For Approval",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/travel-request/approve": {
        "post": {
            "summary": "Approve",
            "description": "Travel Request — approve via apply_workflow.",
            "tags": ["Travel Request"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Travel Request",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Approve",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/travel-request/reject": {
        "post": {
            "summary": "Reject",
            "description": "Travel Request — reject via apply_workflow.",
            "tags": ["Travel Request"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Travel Request",
                                "name": "EGDE-OEC-2026-00011",
                                "workflow_state": "Submit For Approval",
                            },
                            "action": "Reject",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Purpose of Travel": {
        "get": {
            "summary": "Purpose of Travel",
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
    # create/list/edit + workflow use Frappe REST on Leave Application)
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
                            "required": [
                                "doctype",
                                "employee",
                                "leave_type",
                                "from_date",
                                "to_date",
                                "leave_approver",
                            ],
                            "properties": {
                                "doctype": {"type": "string", "example": "Leave Application"},
                                "employee": {
                                    "type": "string",
                                    "description": "Employee ID.",
                                    "example": "HR-EMP-00001",
                                },
                                "leave_type": {"type": "string", "example": "EZT - Elternzeit"},
                                "from_date": {"type": "string", "format": "date"},
                                "to_date": {"type": "string", "format": "date"},
                                "leave_approver": {
                                    "type": "string",
                                    "description": "Leave approver User email.",
                                    "example": "chohan95332@gmail.com",
                                },
                                "custom_replacement": {
                                    "type": "string",
                                    "description": "Optional replacement Employee ID.",
                                    "example": "HR-EMP-00277",
                                },
                                "custom_leave_approver_cc": {
                                    "type": "array",
                                    "description": (
                                        "Optional CC approvers (Table MultiSelect). "
                                        "Each item: {\"approver\": \"user@example.com\"}."
                                    ),
                                    "items": {
                                        "type": "object",
                                        "required": ["approver"],
                                        "properties": {
                                            "approver": {
                                                "type": "string",
                                                "description": "CC approver User email.",
                                                "example": "christian.lange@eg.group",
                                            },
                                        },
                                    },
                                },
                                "half_day": {"type": "integer", "example": 0},
                                "description": {"type": "string"},
                            },
                        },
                        "example": {
                            "doctype": "Leave Application",
                            "employee": "HR-EMP-00001",
                            "leave_type": "EZT - Elternzeit",
                            "from_date": "2026-09-10",
                            "to_date": "2026-09-10",
                            "leave_approver": "chohan95332@gmail.com",
                            "custom_replacement": "HR-EMP-00277",
                            "custom_leave_approver_cc": [
                                {"approver": "christian.lange@eg.group"},
                                {"approver": "clemens.steiner@eg.group"},
                            ],
                            "half_day": 0,
                            "description": "test leave",
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
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": [
                                "doctype",
                                "employee",
                                "leave_type",
                                "from_date",
                                "to_date",
                                "leave_approver",
                            ],
                            "properties": {
                                "doctype": {"type": "string", "example": "Leave Application"},
                                "name": {
                                    "type": "string",
                                    "description": "Leave Application document name.",
                                    "example": "HR-LAP-2026-00001",
                                },
                                "employee": {
                                    "type": "string",
                                    "description": "Employee ID.",
                                    "example": "HR-EMP-00001",
                                },
                                "leave_type": {"type": "string", "example": "EZT - Elternzeit"},
                                "from_date": {"type": "string", "format": "date"},
                                "to_date": {"type": "string", "format": "date"},
                                "leave_approver": {
                                    "type": "string",
                                    "description": "Leave approver User email.",
                                    "example": "chohan95332@gmail.com",
                                },
                                "custom_replacement": {
                                    "type": "string",
                                    "description": "Optional replacement Employee ID.",
                                    "example": "HR-EMP-00277",
                                },
                                "custom_leave_approver_cc": {
                                    "type": "array",
                                    "description": (
                                        "Optional CC approvers (Table MultiSelect). "
                                        "Each item: {\"approver\": \"user@example.com\"}."
                                    ),
                                    "items": {
                                        "type": "object",
                                        "required": ["approver"],
                                        "properties": {
                                            "approver": {
                                                "type": "string",
                                                "description": "CC approver User email.",
                                                "example": "christian.lange@eg.group",
                                            },
                                        },
                                    },
                                },
                                "half_day": {"type": "integer", "example": 0},
                                "description": {"type": "string"},
                            },
                        },
                        "example": {
                            "doctype": "Leave Application",
                            "name": "HR-LAP-2026-00001",
                            "employee": "HR-EMP-00001",
                            "leave_type": "EZT - Elternzeit",
                            "from_date": "2026-09-10",
                            "to_date": "2026-09-10",
                            "leave_approver": "chohan95332@gmail.com",
                            "custom_replacement": "HR-EMP-00277",
                            "custom_leave_approver_cc": [
                                {"approver": "christian.lange@eg.group"},
                                {"approver": "clemens.steiner@eg.group"},
                            ],
                            "half_day": 0,
                            "description": "updated leave",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/leave-application/submit-for-approval": {
        "post": {
            "summary": "submit for approval",
            "description": "Leave Application — submit for approval via apply_workflow.",
            "tags": ["Leave"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Leave Application",
                                "name": "HR-LAP-2026-00001",
                                "workflow_state": "Draft",
                            },
                            "action": "Submit For Approval",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/leave-application/approve": {
        "post": {
            "summary": "approve",
            "description": "Leave Application — approve via apply_workflow.",
            "tags": ["Leave"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Leave Application",
                                "name": "HR-LAP-2026-00001",
                                "workflow_state": "Submitted",
                            },
                            "action": "Approve",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/leave-application/reject": {
        "post": {
            "summary": "Reject",
            "description": "Leave Application — reject via apply_workflow.",
            "tags": ["Leave"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Leave Application",
                                "name": "HR-LAP-2026-00001",
                                "workflow_state": "Submitted",
                            },
                            "action": "Reject",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Timesheet (Frappe REST on Employee Timesheet + workflow)
    # ==================================================================
    "/api/resource/Employee Timesheet": {
        "get": {
            "summary": "Employee Timesheet — List",
            "description": "List Employee Timesheet documents for an employee.",
            "tags": ["Timesheet"],
            "parameters": [
                {
                    "name": "fields",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": (
                        '["name","employee","employee_name","month","year",'
                        '"expected_hours","timesheet_approver","workflow_state","modified"]'
                    ),
                },
                {
                    "name": "filters",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": (
                        '[["employee","=","HR-EMP-00277"],'
                        '["month","=","September"],["year","=","2026"]]'
                    ),
                },
                {
                    "name": "order_by",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "string"},
                    "example": "modified desc",
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
            "summary": "Employee Timesheet — Add",
            "description": (
                "Create a new Employee Timesheet for a month. "
                "One timesheet per employee/month/year. "
                "Child rows go in table_miqy (Employee Timesheet Entry)."
            ),
            "tags": ["Timesheet"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": [
                                "doctype",
                                "employee",
                                "month",
                                "year",
                                "timesheet_approver",
                            ],
                            "properties": {
                                "doctype": {"type": "string", "example": "Employee Timesheet"},
                                "employee": {
                                    "type": "string",
                                    "description": "Employee ID.",
                                    "example": "HR-EMP-00277",
                                },
                                "month": {
                                    "type": "string",
                                    "description": "Month name (January–December).",
                                    "example": "September",
                                },
                                "year": {
                                    "type": "string",
                                    "description": "Calendar year.",
                                    "example": "2026",
                                },
                                "timesheet_approver": {
                                    "type": "string",
                                    "description": "Timesheet approver User email.",
                                    "example": "chohan95332@gmail.com",
                                },
                                "timesheet_approver_cc": {
                                    "type": "array",
                                    "description": (
                                        "Optional CC approvers (Table MultiSelect). "
                                        "Each item: {\"approver\": \"user@example.com\"}."
                                    ),
                                    "items": {
                                        "type": "object",
                                        "required": ["approver"],
                                        "properties": {
                                            "approver": {
                                                "type": "string",
                                                "example": "christian.lange@eg.group",
                                            },
                                        },
                                    },
                                },
                                "table_miqy": {
                                    "type": "array",
                                    "description": "Daily timesheet rows (Employee Timesheet Entry).",
                                    "items": {
                                        "type": "object",
                                        "required": ["doctype", "date"],
                                        "properties": {
                                            "doctype": {
                                                "type": "string",
                                                "example": "Employee Timesheet Entry",
                                            },
                                            "date": {"type": "string", "format": "date"},
                                            "start": {
                                                "type": "string",
                                                "description": "Check-in time (HH:MM:SS).",
                                                "example": "08:00:00",
                                            },
                                            "end": {
                                                "type": "string",
                                                "description": "Check-out time (HH:MM:SS).",
                                                "example": "17:00:00",
                                            },
                                            "pause_hour": {
                                                "type": "string",
                                                "description": "Break duration (HH:MM:SS).",
                                                "example": "00:45:00",
                                            },
                                            "entry_type": {
                                                "type": "string",
                                                "description": (
                                                    "WKE - Weekend / GFT - Public Holidays for "
                                                    "holiday rows; leave codes for manual leave."
                                                ),
                                                "example": "Default",
                                            },
                                            "comments": {
                                                "type": "string",
                                                "description": (
                                                    "Leave rows synced from Leave Application "
                                                    "use prefix \"Leave: <type>\"."
                                                ),
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        "example": {
                            "doctype": "Employee Timesheet",
                            "employee": "HR-EMP-00277",
                            "month": "September",
                            "year": "2026",
                            "timesheet_approver": "chohan95332@gmail.com",
                            "timesheet_approver_cc": [
                                {"approver": "christian.lange@eg.group"},
                                {"approver": "clemens.steiner@eg.group"},
                            ],
                            "table_miqy": [
                                {
                                    "doctype": "Employee Timesheet Entry",
                                    "date": "2026-09-01",
                                    "start": "08:00:00",
                                    "end": "17:00:00",
                                    "pause_hour": "00:45:00",
                                    "entry_type": "Default",
                                },
                                {
                                    "doctype": "Employee Timesheet Entry",
                                    "date": "2026-09-06",
                                    "entry_type": "WKE - Weekend",
                                },
                                {
                                    "doctype": "Employee Timesheet Entry",
                                    "date": "2026-09-08",
                                    "comments": "Leave: EZT - Elternzeit",
                                },
                            ],
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/resource/Employee Timesheet/{name}": {
        "get": {
            "summary": "Employee Timesheet — Get",
            "description": "Get a single Employee Timesheet with table_miqy rows.",
            "tags": ["Timesheet"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "HR-ET-2026-00001",
                },
            ],
            "responses": _OK_RESPONSE,
        },
        "put": {
            "summary": "Employee Timesheet — Edit",
            "description": (
                "Update an existing Employee Timesheet. "
                "Send table_miqy rows with start/end/pause_hour changes. "
                "Editing a submitted timesheet resets workflow_state to Draft."
            ),
            "tags": ["Timesheet"],
            "parameters": [
                {
                    "name": "name",
                    "in": "path",
                    "required": True,
                    "schema": {"type": "string"},
                    "example": "HR-ET-2026-00001",
                },
            ],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": [
                                "doctype",
                                "name",
                                "employee",
                                "month",
                                "year",
                                "timesheet_approver",
                            ],
                            "properties": {
                                "doctype": {"type": "string", "example": "Employee Timesheet"},
                                "name": {
                                    "type": "string",
                                    "example": "HR-ET-2026-00001",
                                },
                                "employee": {"type": "string", "example": "HR-EMP-00277"},
                                "month": {"type": "string", "example": "September"},
                                "year": {"type": "string", "example": "2026"},
                                "timesheet_approver": {
                                    "type": "string",
                                    "example": "chohan95332@gmail.com",
                                },
                                "timesheet_approver_cc": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "required": ["approver"],
                                        "properties": {
                                            "approver": {"type": "string"},
                                        },
                                    },
                                },
                                "reason": {
                                    "type": "string",
                                    "description": "Rejection reason (set by approver on reject).",
                                },
                                "table_miqy": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "doctype": {
                                                "type": "string",
                                                "example": "Employee Timesheet Entry",
                                            },
                                            "name": {
                                                "type": "string",
                                                "description": "Child row name (for updates).",
                                            },
                                            "date": {"type": "string", "format": "date"},
                                            "start": {"type": "string"},
                                            "end": {"type": "string"},
                                            "pause_hour": {"type": "string"},
                                            "entry_type": {"type": "string"},
                                            "comments": {"type": "string"},
                                        },
                                    },
                                },
                            },
                        },
                        "example": {
                            "doctype": "Employee Timesheet",
                            "name": "HR-ET-2026-00001",
                            "employee": "HR-EMP-00277",
                            "month": "September",
                            "year": "2026",
                            "timesheet_approver": "chohan95332@gmail.com",
                            "timesheet_approver_cc": [
                                {"approver": "christian.lange@eg.group"},
                            ],
                            "table_miqy": [
                                {
                                    "doctype": "Employee Timesheet Entry",
                                    "name": "abc123def",
                                    "date": "2026-09-01",
                                    "start": "08:30:00",
                                    "end": "17:30:00",
                                    "pause_hour": "00:45:00",
                                    "entry_type": "Default",
                                },
                                {
                                    "doctype": "Employee Timesheet Entry",
                                    "name": "xyz789ghi",
                                    "date": "2026-09-02",
                                    "start": "09:00:00",
                                    "end": "18:00:00",
                                    "pause_hour": "01:00:00",
                                    "entry_type": "Default",
                                },
                            ],
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/employee-timesheet/submit-for-approval": {
        "post": {
            "summary": "submit for approval",
            "description": "Employee Timesheet — submit for approval via apply_workflow.",
            "tags": ["Timesheet"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Employee Timesheet",
                                "name": "HR-ET-2026-00001",
                                "workflow_state": "Draft",
                            },
                            "action": "Submit For Approval",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/employee-timesheet/approve": {
        "post": {
            "summary": "approve",
            "description": "Employee Timesheet — approve via apply_workflow.",
            "tags": ["Timesheet"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Employee Timesheet",
                                "name": "HR-ET-2026-00001",
                                "workflow_state": "Submitted",
                            },
                            "action": "Approve",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    "/api/method/frappe.model.workflow.apply_workflow/employee-timesheet/reject": {
        "post": {
            "summary": "Reject",
            "description": (
                "Employee Timesheet — reject via apply_workflow. "
                "Set reason on the document before rejecting."
            ),
            "tags": ["Timesheet"],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"type": "object"},
                        "example": {
                            "doc": {
                                "doctype": "Employee Timesheet",
                                "name": "HR-ET-2026-00001",
                                "workflow_state": "Submitted",
                                "reason": "Missing entries for 3 days",
                            },
                            "action": "Reject",
                        },
                    },
                },
            },
            "responses": _OK_RESPONSE,
        },
    },
    # ==================================================================
    # Requests (werkiq_go.api.requests.get_requests — query params override
    # auto-discovery because the endpoint reads frappe.form_dict, not args)
    # ==================================================================
    "/api/method/werkiq_go.api.requests.get_requests": {
        "get": {
            "summary": "Get Requests",
            "description": (
                "Paginated request lists per DocType for the logged-in employee "
                "(Travel Request, Travel Expense Claim, Entertainment Expense Claim, "
                "Other Expense Claim). Draft rows appear only when owner is the session user."
            ),
            "tags": ["Requests"],
            "parameters": [
                {
                    "name": "from_date",
                    "in": "query",
                    "required": True,
                    "schema": {"type": "string", "format": "date"},
                    "description": (
                        "Start date (YYYY-MM-DD). Travel Request filters on creation; "
                        "expense claims filter on posting_date."
                    ),
                    "example": "2026-01-01",
                },
                {
                    "name": "to_date",
                    "in": "query",
                    "required": True,
                    "schema": {"type": "string", "format": "date"},
                    "description": "End date (YYYY-MM-DD).",
                    "example": "2026-09-08",
                },
                {
                    "name": "page",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer", "minimum": 1, "default": 1},
                    "example": 1,
                },
                {
                    "name": "limit",
                    "in": "query",
                    "required": False,
                    "schema": {"type": "integer", "minimum": 1, "default": 10},
                    "example": 10,
                },
                {
                    "name": "workflow_state",
                    "in": "query",
                    "required": False,
                    "schema": {
                        "type": "string",
                        "enum": ["Draft", "Submitted", "Approved", "Rejected"],
                    },
                    "description": "Optional filter by workflow state.",
                },
                {
                    "name": "status",
                    "in": "query",
                    "required": False,
                    "schema": {
                        "type": "string",
                        "enum": ["Draft", "Submitted", "Approved", "Rejected"],
                    },
                    "description": "Alias for workflow_state.",
                },
            ],
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
