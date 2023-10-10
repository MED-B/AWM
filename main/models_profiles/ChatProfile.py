from django.contrib import admin
from django.db.models import Count
class ChatAdmin(admin.ModelAdmin): 
    list_display = ['user1_firstName','user1_lastName','user2_firstName','user2_lastName','blocked']
    def user1_firstName(self, obj):
        if obj.user1id:
            return obj.user1id.firstname if obj.user1id else 'None'
        else: return 'None'

    def user1_lastName(self, obj):
        if obj.user1id:
            return obj.user1id.lastname if obj.user1id else 'None'
        else: return 'None'
    def user2_firstName(self, obj):
        if obj.user2id:
            return obj.user2id.firstname if obj.user2id else 'None'
        else: return 'None'

    def user2_lastName(self, obj):
        if obj.user2id:
            return obj.user2id.lastname if obj.user2id else 'None'
        else: return 'None'
    user1_firstName.admin_order_field = "user1id__firstname"
    user1_lastName.admin_order_field = "user1id__lastname"
    user2_firstName.admin_order_field = "user2id__firstname"
    user2_lastName.admin_order_field = "user2id__lastname"
    list_filter = ["user1id__firstname", "user1id__lastname","user2id__firstname","user2id__lastname","blocked"] 
    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='ChatAdminGroup').exists() or request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
