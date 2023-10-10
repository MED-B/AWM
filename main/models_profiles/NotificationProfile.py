from django.contrib import admin
from django.db.models import Count
class NotificationAdmin(admin.ModelAdmin): 
    list_display = ['firstName','lastName','type']

    def firstName(self, obj):
        if obj.userid:
            return obj.userid.firstname if obj.userid else 'None'
        else: return 'None'

    def lastName(self, obj):
        if obj.userid:
            return obj.userid.lastname if obj.userid else 'None'
        else: return 'None'
    ordering=['type']
    firstName.admin_order_field = "userid__firstname"
    lastName.admin_order_field = "userid__lastname"
    list_filter = ['userid__firstname','userid__lastname','type']
    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
