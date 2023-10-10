from django.contrib import admin
from django.db.models import Count
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productName','sector' ,'company','category','verified']

    def productName(self, obj):
        return obj.productname if obj.productname else 'None'
    
    def sector(self, obj):
        return obj.sectorid.name if obj.sectorid else 'None'
    
    def company(self, obj):
        if obj.ownerid:
            return obj.ownerid.companyid.company_name if obj.ownerid.companyid else 'None'
        else: return 'None'

    def category(self, obj):
        return obj.categoryid.name if obj.categoryid.name else 'None'
    
    productName.admin_order_field = "productname"
    sector.admin_order_field = "sectorid__name"
    company.admin_order_field = "ownerid__companyid__company_name"
    category.admin_order_field = "categoryid__name"
    list_filter = ['productname','sectorid__name' ,'ownerid__companyid__company_name',
                   'categoryid__name','verified']
    
    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='ProductAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
    