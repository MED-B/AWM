
from django.contrib import admin

class BuyerAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName']

    def firstName(self, obj):
        return obj.first_name if obj.first_name else 'None'
    
    def lastName(self, obj):
        return obj.last_name if obj.last_name else 'None'
    
    firstName.admin_order_field = "first_name"
    lastName.admin_order_field = "last_name"
    list_filter = ['first_name','last_name']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='BuyerAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)