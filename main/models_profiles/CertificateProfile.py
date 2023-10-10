
from django.contrib import admin
from django.db.models import Count
class CertificateAdmin(admin.ModelAdmin): 
    list_display = ['company','certificatename','certificateemissiondate','certificateexpirationdate']
    def company(self, obj):
        return obj.companyid.company_name if obj.companyid else 'None'
    company.admin_order_field = "companyid__company_name"
    list_filter = ['companyid__company_name','certificatename','certificateemissiondate','certificateexpirationdate']

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='CertificateAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
