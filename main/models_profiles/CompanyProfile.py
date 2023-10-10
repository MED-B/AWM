from django.contrib import admin
from django.db.models import Count
class CompanyAdmin(admin.ModelAdmin): 
    list_display = ['companyName','companyType', 'factories', 'expositions','firstName','lastName']

    def companyName(self, obj):
        return obj.company_name if obj.company_name else 'None'
    
    def companyType(self, obj):
        return obj.company_type if obj.company_type else 'None'

    def firstName(self, obj):
        if obj.userid:
            return obj.userid.firstname if obj.userid else 'None'
        else: return 'None'

    def lastName(self, obj):
        if obj.userid:
            return obj.userid.lastname if obj.userid else 'None'
        else: return 'None'
    
    def factories(self, obj):
        return obj.factory_count

    def expositions(self, obj):
        return obj.exposition_count
    
    def get_queryset(self, request):
        # Annotate the queryset with counts of related factories and expositions
        queryset = super().get_queryset(request).annotate(
            factory_count=Count('vendor__factory', distinct=True),
            exposition_count=Count('vendor__exposition', distinct=True)
        )
        return queryset
    
    factories.admin_order_field = 'factory_count'
    expositions.admin_order_field = 'exposition_count'
    companyName.admin_order_field = "company_name"
    companyType.admin_order_field = "company_type"
    firstName.admin_order_field = "userid__firstname"
    lastName.admin_order_field = "userid__lastname"
    list_filter = ['company_name','company_type','userid__firstname',
                   'userid__lastname']
    
    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='CompanyAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)