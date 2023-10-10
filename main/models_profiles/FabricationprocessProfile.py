from django.contrib import admin
from django.db.models import Count
class FabricationprocessAdmin(admin.ModelAdmin): 
    list_display = ['processname','vendor_FirstName','vendor_LastName']
    def vendor_FirstName(self, obj):
        if obj.factoryid.vendorid:
            return obj.factoryid.vendorid.get_user().firstname if obj.factoryid.vendorid.get_user() else 'None'
        else: return 'None'
    def vendor_LastName(self, obj):
        if obj.factoryid.vendorid:
            return obj.factoryid.vendorid.get_user().lastname if obj.factoryid.vendorid.get_user() else 'None'
        else: return 'None'
    
    vendor_FirstName.admin_order_field = "factoryid__vendorid__companyid__userid__firstname"
    vendor_LastName.admin_order_field = "factoryid__vendorid__companyid__userid__lastname"
    list_filter = ['processname',
                   'factoryid__vendorid__companyid__userid__firstname',
                   'factoryid__vendorid__companyid__userid__lastname']
    
    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
