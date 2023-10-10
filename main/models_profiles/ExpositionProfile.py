
from django.contrib import admin
class ExpositionAdmin(admin.ModelAdmin): 
    list_display = ['exponame','exposyear','vendor_FirstName','vendor_LastName']
    def vendor_FirstName(self, obj):
        if obj.organizerid:
            return obj.organizerid.get_user().firstname if obj.organizerid.get_user() else 'None'
        else: return 'None'
    def vendor_LastName(self, obj):
        if obj.organizerid:
            return obj.organizerid.get_user().lastname if obj.organizerid.get_user() else 'None'
        else: return 'None'
    
    vendor_FirstName.admin_order_field = "organizerid__companyid__userid__firstname"
    vendor_LastName.admin_order_field = "organizerid__companyid__userid__lastname"
    list_filter = ['exponame','exposyear',"organizerid__companyid__userid__firstname","organizerid__companyid__userid__lastname"]

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='ExpositionAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
