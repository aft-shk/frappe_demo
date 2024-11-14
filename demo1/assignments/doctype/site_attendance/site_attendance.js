frappe.ui.form.on('Site_Attendance', {
    refresh: function(frm) {
        frm.set_query('site', function() {
            return {
                filters: {
                    'active': 1  
                }
            };
        });
    },
});
