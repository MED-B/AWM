from django.contrib import admin
from django.db.models import Count
class SubcategoryAdmin(admin.ModelAdmin): 
    list_display = ['name','category']

    def category(self, obj):
        return obj.categoryid.name if obj.categoryid else 'None'
    
    category.admin_order_field = "categoryid__name"
    list_filter = ['name','categoryid__name']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='SubCategoryAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
