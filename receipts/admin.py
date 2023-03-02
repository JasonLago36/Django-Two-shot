from django.contrib import admin
from .models import ExpenseCategory, Account, Receipt

# Register your models here.


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (

    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (

    )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (

    )
