# Copyright (c) 2024, Omkar Darves and contributors
# For license information, please see license.txt

import frappe

no_cache = 1


def get_context(context):
	"""Provide Swagger Settings to the /swagger page without caching CSRF/session state."""
	context.no_cache = 1
	context.session_auth_enabled = False
	try:
		settings = frappe.get_single("Swagger Settings")
		context.session_auth_enabled = bool(settings.get("sessionauth"))
	except Exception:
		frappe.log_error("Unable to load Swagger Settings for /swagger")
