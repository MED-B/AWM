from django.contrib import admin
from django.db.models import Count
class QuantitylivraisonAdmin(admin.ModelAdmin): 
    list_display = ['productName','quantity','livraison']
    def productName(self, obj):
        return obj.productid.productname if obj.productid else 'None'
    
    productName.admin_order_field = "productid__productname"
    list_filter = ['productid__productname','quantity','livraison']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)