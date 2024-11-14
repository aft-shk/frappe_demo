# Copyright (c) 2024, aftab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WorkerAttendance(Document):
	
	def validate_worker_attendance(doc, method):
		pass
    
	
	# for attendance in doc.attendance_details:  # Assuming 'attendance_details' is the name of the child table field
    #     if attendance.worker_id in worker_ids:
    #         frappe.throw(f"Duplicate entry for Worker Id: {attendance.worker_id}")
    #     worker_ids.add(attendance.worker_id)

