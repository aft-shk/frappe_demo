# Copyright (c) 2024, aftab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import *

class Site_Attendance(Document):
    def validate(self):
        # check the status of site
        site_status = frappe.db.get_value('Site_Master', self.sitename, 'active')
        if not site_status:
            frappe.throw(f"The selected site {self.sitename} is not active.")

        # Fetch the Site Start Date from Site Master
        site_start_date = frappe.db.get_value('Site_Master', self.sitename, 'sitedate')

        # Check if Attendance Date is greater than or equal to Site Start Date
        if get_datetime(self.atten_date) < get_datetime(site_start_date):
            frappe.throw(f"Attendance Date cannot be earlier than Site Start Date ({site_start_date}) for the selected site.")
        
        # Checking  for duplicate records
        duplicate_record = frappe.db.exists('Site_Attendance', {
            'sitename': self.sitename,
            #'attendance_date': self.attendance_date
        })
        
        if duplicate_record:
            frappe.throw(f"Attendance record already exists for {self.sitename}. Duplicates are not allowed.")
