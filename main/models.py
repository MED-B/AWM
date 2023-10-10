# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activitytype(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    fabricant = models.IntegerField()
    fournisseur = models.IntegerField()
    bureauachat = models.IntegerField(db_column='bureauAchat')  # Field name made lowercase.
    commercial = models.IntegerField()
    gouvernementale = models.IntegerField()
    autre = models.IntegerField()
    companyid = models.OneToOneField('Company', models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.

    
    class Meta:
        managed = False
        db_table = 'ActivityType'
    



class Address(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    street = models.CharField(max_length=191)
    city = models.CharField(max_length=191)
    state = models.CharField(max_length=191)
    country_name = models.CharField(max_length=191)
    country_code = models.CharField(max_length=191)
    postalcode = models.CharField(db_column='postalCode', max_length=191)  # Field name made lowercase.
    companyid = models.OneToOneField('Company', models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.

    def __str__(self):
        if self.street and self.city and self.state:
            return self.street +","+ self.city +","+ self.state
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Address'


class Businesscard(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    senderid = models.ForeignKey('User', models.DO_NOTHING, db_column='senderId')  # Field name made lowercase.
    recieverid = models.ForeignKey('User', models.DO_NOTHING, db_column='recieverId', related_name='businesscard_recieverid_set')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BusinessCard'


class Buyer(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    annual_purchase_amount = models.IntegerField()
    companyid = models.OneToOneField('Company', models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name +" "+ self.last_name
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Buyer'


class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    name = models.CharField(unique=True, max_length=191)
    description = models.CharField(max_length=191)
    sectorid = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sectorId')  # Field name made lowercase.
    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Category'


class Certificate(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    certificateholder = models.CharField(db_column='certificateHolder', max_length=191)  # Field name made lowercase.
    certificatenum = models.CharField(db_column='certificateNum', max_length=191)  # Field name made lowercase.
    certificatename = models.CharField(db_column='certificateName', max_length=191)  # Field name made lowercase.
    certificateemissiondate = models.DateTimeField(db_column='certificateEmissionDate')  # Field name made lowercase.
    certificateexpirationdate = models.DateTimeField(db_column='certificateExpirationDate')  # Field name made lowercase.
    certificateimages = models.CharField(db_column='certificateImages', max_length=191)  # Field name made lowercase.
    licenseholder = models.CharField(db_column='licenseHolder', max_length=191, blank=True, null=True)  # Field name made lowercase.
    licensenum = models.CharField(db_column='licenseNum', max_length=191, blank=True, null=True)  # Field name made lowercase.
    licensename = models.CharField(db_column='licenseName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    licenseemissiondate = models.DateTimeField(db_column='licenseEmissionDate', blank=True, null=True)  # Field name made lowercase.
    licenseexpirationdate = models.DateTimeField(db_column='licenseExpirationDate', blank=True, null=True)  # Field name made lowercase.
    licenseimages = models.CharField(db_column='licenseImages', max_length=191, blank=True, null=True)  # Field name made lowercase.
    companyid = models.OneToOneField('Company', models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    def __str__(self):
        if self.certificatename:
            return self.certificatename
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Certificate'


class Chat(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    user1id = models.ForeignKey('User', models.DO_NOTHING, db_column='user1Id')  # Field name made lowercase.
    user2id = models.ForeignKey('User', models.DO_NOTHING, db_column='user2Id', related_name='chat_user2id_set')  # Field name made lowercase.
    blockedby = models.CharField(db_column='blockedBy', max_length=191)  # Field name made lowercase.
    blocked = models.IntegerField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    lastmessage = models.CharField(db_column='lastMessage', max_length=191)  # Field name made lowercase.
    lastvieweduser1 = models.DateTimeField(db_column='lastViewedUser1')  # Field name made lowercase.
    lastvieweduser2 = models.DateTimeField(db_column='lastViewedUser2')  # Field name made lowercase.
    lastskipuser1 = models.DateTimeField(db_column='lastSkipUser1')  # Field name made lowercase.
    lastskipuser2 = models.DateTimeField(db_column='lastSkipUser2')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Chat'


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    company_type = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    marchevise = models.CharField(db_column='marcheVise', max_length=191)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    password = models.CharField(max_length=191, blank=True, null=True)
    phone = models.CharField(max_length=191, blank=True, null=True)
    fax = models.CharField(max_length=191)
    creationyear = models.IntegerField(db_column='creationYear')  # Field name made lowercase.
    website = models.CharField(max_length=191)
    logo = models.CharField(max_length=191)
    companyimages = models.CharField(db_column='companyImages', max_length=191)  # Field name made lowercase.
    companyvideos = models.CharField(db_column='companyVideos', max_length=191)  # Field name made lowercase.
    employersnumber = models.CharField(db_column='employersNumber', max_length=191)  # Field name made lowercase.
    registerdate = models.DateTimeField(db_column='registerDate')  # Field name made lowercase.
    def __str__(self):
        if self.company_name:
            return self.company_name 
        else:
            return "Not named"    
    def get_certificate_count(self):
        return Certificate.objects.filter(companyid=self).count()
    
    class Meta:
        managed = False
        db_table = 'Company'


class Contactstatus(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    senderid = models.ForeignKey('User', models.DO_NOTHING, db_column='senderId')  # Field name made lowercase.
    receiverid = models.ForeignKey('User', models.DO_NOTHING, db_column='receiverId', related_name='contactstatus_receiverid_set')  # Field name made lowercase.
    status = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'ContactStatus'


class Exportationcapacity(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    vendorid = models.OneToOneField('Vendor', models.DO_NOTHING, db_column='vendorId')  # Field name made lowercase.
    exportationstartyear = models.IntegerField(db_column='exportationStartYear')  # Field name made lowercase.
    principalmarketsanddistribution = models.JSONField(db_column='principalMarketsAndDistribution')  # Field name made lowercase.
    shippingconditions = models.JSONField(db_column='shippingConditions')  # Field name made lowercase.
    accepteddevise = models.JSONField(db_column='acceptedDevise')  # Field name made lowercase.
    paymenttypes = models.JSONField(db_column='paymentTypes')  # Field name made lowercase.
    language = models.JSONField(db_column='Language')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExportationCapacity'


class Exposition(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    exponame = models.CharField(db_column='expoName', max_length=191)  # Field name made lowercase.
    description = models.CharField(max_length=191)
    organizerid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='organizerId')  # Field name made lowercase.
    pays = models.JSONField()
    exposyear = models.IntegerField(db_column='exposYear')  # Field name made lowercase.
    expoimages = models.CharField(db_column='expoImages', max_length=191)  # Field name made lowercase.
    index = models.IntegerField()
    def __str__(self):
        if self.exponame:
            return self.exponame 
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Exposition'


class Fabricationprocess(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    processname = models.CharField(db_column='processName', max_length=191)  # Field name made lowercase.
    processdescription = models.CharField(db_column='processDescription', max_length=191)  # Field name made lowercase.
    processimages = models.CharField(db_column='processImages', max_length=191)  # Field name made lowercase.
    factoryid = models.ForeignKey('Factory', models.DO_NOTHING, db_column='factoryId', blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField()
    def __str__(self):
        if self.processname :
            return self.processname 
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'FabricationProcess'


class Factory(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    factoryaddress = models.CharField(db_column='factoryAddress', max_length=191)  # Field name made lowercase.
    factorysize = models.CharField(db_column='factorySize', max_length=191)  # Field name made lowercase.
    productionlinesnumb = models.FloatField(db_column='productionLinesNumb', blank=True, null=True)  # Field name made lowercase.
    annualproductionvalue = models.FloatField(db_column='annualProductionValue', blank=True, null=True)  # Field name made lowercase.
    factoryimages = models.CharField(db_column='factoryImages', max_length=191, blank=True, null=True)  # Field name made lowercase.
    factoryvideos = models.CharField(db_column='factoryVideos', max_length=191, blank=True, null=True)  # Field name made lowercase.
    vendorid = models.OneToOneField('Vendor', models.DO_NOTHING, db_column='vendorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factory'


class Keyword(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    name = models.CharField(unique=True, max_length=191)
    def __str__(self):
        if self.name :
            return self.name 
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Keyword'


class Message(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    chatid = models.ForeignKey(Chat, models.DO_NOTHING, db_column='chatId')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    type = models.CharField(max_length=191)
    content = models.CharField(max_length=191)
    fileurl = models.CharField(db_column='fileUrl', max_length=191, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Message'


class Notification(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    type = models.CharField(max_length=191)
    content = models.CharField(max_length=191)
    notificationurl = models.CharField(db_column='notificationUrl', max_length=191, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=191, blank=True, null=True)  # Field name made lowercase.
    read = models.IntegerField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notification'


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    productname = models.CharField(db_column='productName', max_length=191)  # Field name made lowercase.
    marchevise = models.CharField(db_column='marcheVise', max_length=191)  # Field name made lowercase.
    marque = models.CharField(max_length=191)
    fabricationdate = models.DateTimeField(db_column='fabricationDate')  # Field name made lowercase.
    madein = models.CharField(db_column='madeIn', max_length=191)  # Field name made lowercase.
    modelnumber = models.CharField(db_column='modelNumber', max_length=191)  # Field name made lowercase.
    groupe = models.CharField(max_length=191)
    certifications = models.JSONField()
    currency = models.CharField(max_length=191)
    paymentmethod = models.JSONField(db_column='paymentMethod')  # Field name made lowercase.
    details = models.CharField(max_length=191)
    product_thumbnail_reference = models.CharField(max_length=191)
    productsphotos = models.CharField(db_column='productsPhotos', max_length=1000)  # Field name made lowercase.
    productsvideos = models.CharField(db_column='productsVideos', max_length=1000)  # Field name made lowercase.
    fixationprice = models.CharField(db_column='fixationPrice', max_length=191)  # Field name made lowercase.
    modelogistique = models.JSONField(db_column='modeLogistique')  # Field name made lowercase.
    port = models.CharField(max_length=191)
    descriptionemballage = models.CharField(db_column='descriptionEmballage', max_length=191)  # Field name made lowercase.
    imagesemballage = models.CharField(db_column='imagesEmballage', max_length=191)  # Field name made lowercase.
    termsandconditions = models.IntegerField(db_column='termsAndConditions')  # Field name made lowercase.
    productinformations = models.CharField(db_column='productInformations', max_length=191)  # Field name made lowercase.
    minquantity = models.CharField(db_column='minQuantity', max_length=191)  # Field name made lowercase.
    ownerid = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='ownerId')  # Field name made lowercase.
    verified = models.IntegerField()
    sectorid = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sectorId')  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    subcategory = models.ForeignKey('Subcategory', models.DO_NOTHING)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    rupturestock = models.IntegerField(db_column='ruptureStock')  # Field name made lowercase.
    def __str__(self):
        if self.productname :
            return self.productname 
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Product'


class Productkeyword(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productId')  # Field name made lowercase.
    keywordid = models.ForeignKey(Keyword, models.DO_NOTHING, db_column='keywordId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductKeyword'


class Quantityfabrication(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    quantity = models.CharField(max_length=191)
    unity = models.CharField(max_length=191)
    par = models.CharField(max_length=191)
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='productId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityFabrication'


class Quantitylivraison(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    quantity = models.CharField(max_length=191)
    livraison = models.CharField(max_length=191)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityLivraison'


class Quantityprice(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    quantity = models.CharField(max_length=191)
    price = models.FloatField()
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productId')  # Field name made lowercase.
    solde = models.IntegerField()
    soldeprice = models.FloatField(db_column='soldePrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityPrice'


class Review(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    comment = models.CharField(max_length=191)
    buyerid = models.ForeignKey(Buyer, models.DO_NOTHING, db_column='buyerid')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productId')  # Field name made lowercase.
    shipping_rating = models.FloatField()
    productquality_rating = models.FloatField(db_column='productQuality_rating')  # Field name made lowercase.
    salesservices_rating = models.FloatField(db_column='salesServices_rating')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'


class Sector(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    name = models.CharField(unique=True, max_length=191)
    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Sector'


class Sectorsincompany(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    sectorid = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sectorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectorsInCompany'


class Subcategory(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    name = models.CharField(unique=True, max_length=191)
    description = models.CharField(max_length=191)
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    def __str__(self):
        if self.name :
            return self.name 
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Subcategory'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    firstname = models.CharField(db_column='firstName', max_length=191)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=191)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=191)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=191)
    password = models.CharField(max_length=191)
    phone = models.CharField(max_length=191)
    countryname = models.CharField(db_column='countryName', max_length=191)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=191)  # Field name made lowercase.
    role = models.IntegerField()
    verifiedemail = models.IntegerField(db_column='verifiedEmail')  # Field name made lowercase.
    completedcompanyprofile = models.IntegerField(db_column='completedCompanyProfile')  # Field name made lowercase.
    completedfactory = models.IntegerField(db_column='completedFactory')  # Field name made lowercase.
    completedexportation = models.IntegerField(db_column='completedExportation')  # Field name made lowercase.
    completedcertification = models.IntegerField(db_column='completedCertification')  # Field name made lowercase.
    subscription = models.CharField(max_length=191)
    authprovider = models.CharField(db_column='authProvider', max_length=191)  # Field name made lowercase.
    blocked = models.IntegerField()
    def __str__(self):
        if self.firstname and self.lastname:
            return f"{self.firstname} {self.lastname}"
        else:
            return "Not named" 
    class Meta:
        managed = False
        db_table = 'User'


class Vendor(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    verified = models.IntegerField()
    companyid = models.OneToOneField(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
    
    
    def get_number_of_factories(self):
        return Factory.objects.filter(vendorid=self).count()
    
    def get_number_of_expositions(self):
        return Exposition.objects.filter(organizerid=self).count()
    
    def get_user(self):
        try:
            return self.companyid.userid
        except Exception:
            return None
    def __str__(self):
        if self.companyid.userid:
            return self.companyid.userid.__str__()
        else:
            return "Not named"    
    class Meta:
        managed = False
        db_table = 'Vendor'


class Usercontacts(models.Model):
    a = models.ForeignKey(User, models.DO_NOTHING, db_column='A')  # Field name made lowercase.
    b = models.ForeignKey(User, models.DO_NOTHING, db_column='B', related_name='usercontacts_b_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_UserContacts'
        unique_together = (('a', 'b'),)


class PrismaMigrations(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = '_prisma_migrations'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
