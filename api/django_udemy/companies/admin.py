from django.contrib import admin

from api.django_udemy.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
