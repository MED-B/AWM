from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['name','sector']

    def sector(self, obj):
        return obj.sectorid.name if obj.sectorid else 'None'
    
    sector.admin_order_field = "sectorid__name"
    list_filter = ['name','sectorid__name']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='CategoryAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
