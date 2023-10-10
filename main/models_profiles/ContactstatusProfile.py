from django.contrib import admin
from django.db.models import Count
class ContactstatusAdmin(admin.ModelAdmin): 
    list_display = ['sender_firstName','sender_lastName','reciever_firstName','reciever_lastName','status']
    def sender_firstName(self, obj):
        if obj.senderid:
            return obj.senderid.firstname if obj.senderid else 'None'
        else: return 'None'

    def sender_lastName(self, obj):
        if obj.senderid:
            return obj.senderid.lastname if obj.senderid else 'None'
        else: return 'None'
    def reciever_firstName(self, obj):
        if obj.receiverid:
            return obj.receiverid.firstname if obj.receiverid else 'None'
        else: return 'None'

    def reciever_lastName(self, obj):
        if obj.receiverid:
            return obj.receiverid.lastname if obj.receiverid else 'None'
        else: return 'None'
    sender_firstName.admin_order_field = "senderid__firstname"
    sender_lastName.admin_order_field = "senderid__lastname"
    reciever_firstName.admin_order_field = "receiverid__firstname"
    reciever_lastName.admin_order_field = "receiverid__lastname"
    list_filter = ["senderid__firstname", "senderid__lastname","receiverid__firstname","receiverid__lastname",'status'] 

    def response_based_on_group(self,request):
         # Limit change permission based on the user's group
            if request.user.groups.filter(name='AllAdminGroup').exists():
                return True  # User is in the CompanyAdminGroup, grant permission
            else:
                return False  # User is not in the CompanyAdminGroup, deny permission
            

    def has_module_permission(self, request, obj=None):
            # Limit change permission based on the user's group
        return self.response_based_on_group(request)
