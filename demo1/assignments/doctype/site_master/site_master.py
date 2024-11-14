# Copyright (c) 2024, aftab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class Site_Master(Document):
    
	def create_site_record(doc):
		required_doc = frappe.new_doc("Site Activation Details")
		required_doc.site_name = doc.sitename
		required_doc.startdate = nowdate()
		required_doc.insert()

	def after_insert(self):
		self.create_site_record()

	# def update_site_record(site):
	# 	# finding the existing record 
		
	# 	record = frappe.get_doc("Site Activation Details",{"site_name": site.sitename})
	# 	if record:
	# 		record.deactivation_date = nowdate()
	# 		record.save()

	# def after_save(self):
	# 	self.update_site_record(self)


    
