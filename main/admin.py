from django.contrib import admin
from django.db.models import Count
from main import models
from main.models import Buyer, Category, Certificate, Chat, Company, Contactstatus, Exportationcapacity, Exposition, Fabricationprocess, Factory, Keyword, Message, Notification, Product, Productkeyword, Quantityfabrication, Quantitylivraison, Quantityprice, Review, Sector, Sectorsincompany, Subcategory, Vendor
from main.models_profiles.BuyerProfile import BuyerAdmin
from main.models_profiles.CategoryProfile import CategoryAdmin
from main.models_profiles.CertificateProfile import CertificateAdmin
from main.models_profiles.ChatProfile import ChatAdmin
from main.models_profiles.CompanyProfile import CompanyAdmin
from main.models_profiles.ContactstatusProfile import ContactstatusAdmin
from main.models_profiles.ExportationcapacityProfile import ExportationcapacityAdmin
from main.models_profiles.ExpositionProfile import ExpositionAdmin
from main.models_profiles.FabricationprocessProfile import FabricationprocessAdmin
from main.models_profiles.FactoryProfile import FactoryAdmin
from main.models_profiles.KeywordProfile import KeywordAdmin
from main.models_profiles.MessageProfile import MessageAdmin
from main.models_profiles.NotificationProfile import NotificationAdmin
from main.models_profiles.ProductProfile import ProductAdmin
from main.models_profiles.Productkeyword import ProductkeywordAdmin
from main.models_profiles.QuantityfabricationProfile import QuantityfabricationAdmin
from main.models_profiles.QuantitylivraisonProfile import QuantitylivraisonAdmin
from main.models_profiles.QuantitypriceProfile import QuantitypriceAdmin
from main.models_profiles.ReviewProfile import ReviewAdmin
from main.models_profiles.SectorProfile import SectorAdmin
from main.models_profiles.SectorsincompanyProfile import SectorsincompanyAdmin
from main.models_profiles.SubcategoryProfile import SubcategoryAdmin
from main.models_profiles.UserProfile import UserAdmin
from main.models_profiles.VendorProfile import VendorAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.auth import models as pre_models

class CustomUserAdmin(BaseUserAdmin):
    def has_module_permission(self, request, obj=None):
        return not request.user.groups.filter(name='RestrictedAdminGroup').exists()

class CustomGroupAdmin(BaseGroupAdmin):
    def has_module_permission(self, request, obj=None):
        return not request.user.groups.filter(name='RestrictedAdminGroup').exists()

# Unregister the default User and Group admin classes
admin.site.unregister(pre_models.User)
admin.site.unregister(pre_models.Group)

# Register the User and Group models with the custom admin classes
admin.site.register(pre_models.User, CustomUserAdmin)
admin.site.register(pre_models.Group, CustomGroupAdmin)

# Register your models here
admin.site.register(models.User,UserAdmin)
admin.site.register(Exposition,ExpositionAdmin)
admin.site.register(Exportationcapacity,ExportationcapacityAdmin)
admin.site.register(Contactstatus,ContactstatusAdmin)
admin.site.register(Chat,ChatAdmin)
admin.site.register(Sectorsincompany,SectorsincompanyAdmin)

admin.site.register(Buyer,BuyerAdmin)
admin.site.register(Vendor,VendorAdmin) 
admin.site.register(Product,ProductAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Factory,FactoryAdmin)
admin.site.register(Certificate,CertificateAdmin)


admin.site.register(Fabricationprocess,FabricationprocessAdmin)
admin.site.register(Quantityprice,QuantitypriceAdmin)
admin.site.register(Quantityfabrication,QuantityfabricationAdmin)
admin.site.register(Quantitylivraison,QuantitylivraisonAdmin)
admin.site.register(Productkeyword,ProductkeywordAdmin)
admin.site.register(Keyword,KeywordAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Sector,SectorAdmin)