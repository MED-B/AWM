from django.contrib import admin
from django.db.models import Count
class VendorAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName','company','verified']
    
    def firstName(self, obj):
        return obj.get_user().firstname if obj.get_user() else 'None'
    
    def lastName(self, obj):
        return obj.get_user().lastname if obj.get_user() else 'None'
    
    def company(self,obj):
        return obj.companyid.company_name if obj.companyid.company_name is not None else 'None'
    
    firstName.admin_order_field = "companyid__userid__firstname"
    lastName.admin_order_field = "companyid__userid__lastname"
    company.admin_order_field = "companyid__company_name"
    list_filter = ['companyid__userid__firstname','companyid__userid__lastname','companyid__company_name','verified']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='VendorAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
