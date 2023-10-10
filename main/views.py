from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count,Avg
from main.models import Certificate, Company, Exposition, Factory, Product, Review, Sector, Sectorsincompany, User

# Create your views here.
def users_info(request):
    total_users = User.objects.all().count()
    role_0_count = User.objects.filter(role=0, verifiedemail=1).count()
    role_1_count = User.objects.filter(role=1, verifiedemail=1).count()
    role_2_count = User.objects.filter(role=2, verifiedemail=1).count()

    response_data = {
        'total_users': total_users,
        'buyers': role_0_count,
        'vendors': role_1_count,
        'both': role_2_count,
    }

    return JsonResponse(response_data)


def company_info(request):
    # Number of all companies
    total_companies = Company.objects.all().count()

    # Number of certified companies
    certified_companies = Certificate.objects.values('companyid').distinct().count()

    # Number of uncertified companies
    uncertified_companies = total_companies - certified_companies

    # Distribution of companies through unique values of 'company_type'
    company_type_distribution = (
        Company.objects.values('company_type')
        .annotate(count=Count('company_type'))
        .order_by('-count')
    )

    response_data = {
        'total_companies': total_companies,
        'certified_companies': certified_companies,
        'uncertified_companies': uncertified_companies,
        'company_type_distribution': list(company_type_distribution),
    }

    return JsonResponse(response_data)

def general_infos(request):
    # Get counts for Certificate, Factory, and Exposition models
    certificate_count = Certificate.objects.count()
    factory_count = Factory.objects.count()
    exposition_count = Exposition.objects.count()

    # Create a dictionary with the counts
    response_data = {
        'certificate_count': certificate_count,
        'factory_count': factory_count,
        'exposition_count': exposition_count,
    }

    # Return the data as JSON response
    return JsonResponse(response_data)


def sector_distribution(request):
    # Get products count per sector
    product_distribution = (
        Product.objects.values('sectorid__name')
        .annotate(product_count=Count('id'))
    )

    # Get average review per sector
    review_distribution = (
        Review.objects.values('productid__sectorid__name')
        .annotate(avg_shipping_rating=Avg('shipping_rating'),
                  avg_productquality_rating=Avg('productquality_rating'),
                  avg_salesservices_rating=Avg('salesservices_rating'))
    )

    # Get companies count per sector
    company_distribution = (
        Sectorsincompany.objects.values('sectorid__name')
        .annotate(company_count=Count('companyid'))
    )

    response_data = {
        'product_distribution': list(product_distribution),
        'review_distribution': list(review_distribution),
        'company_distribution': list(company_distribution),
    }

    return JsonResponse(response_data)
