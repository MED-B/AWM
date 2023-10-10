from django.contrib import admin
from django.db.models import Count
class ExportationcapacityAdmin(admin.ModelAdmin): 
    list_display = ['vendor_FirstName','vendor_LastName','exportationstartyear']
    def vendor_FirstName(self, obj):
        if obj.vendorid:
            return obj.vendorid.get_user().firstname if obj.vendorid.get_user() else 'None'
        else: return 'None'
    def vendor_LastName(self, obj):
        if obj.vendorid:
            return obj.vendorid.get_user().lastname if obj.vendorid.get_user() else 'None'
        else: return 'None'
    
    vendor_FirstName.admin_order_field = "vendorid__companyid__userid__firstname"
    vendor_LastName.admin_order_field = "vendorid__companyid__userid__lastname"
    list_filter = ["vendorid__companyid__userid__firstname", "vendorid__companyid__userid__lastname",'exportationstartyear']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
