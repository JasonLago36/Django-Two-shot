from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Receipt, Account, ExpenseCategory
from .forms import ReceiptForm, ExpenseCategoryForm, AccountForm

# Create your views here.


@login_required
def receipt_list(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_object": receipt,
    }

    return render(request, "receipts/home.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }

    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    receipt = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "receipt_object": receipt,
    }

    return render(request, "receipts/categories.html", context)


@login_required
def accounts_list(request):
    receipt = Account.objects.filter(owner=request.user)
    context = {
        "receipt_object": receipt,
    }

    return render(request, "receipts/accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.owner = request.user
            receipt.save()
            return redirect("categories")
    else:
        form = ExpenseCategoryForm()
    context = {
        "form": form,
    }

    return render(request, "receipts/ExpenseCategory.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.owner = request.user
            receipt.save()
            return redirect("accounts")
    else:
        form = AccountForm()
    context = {
        "form": form,
    }

    return render(request, "receipts/createaccounts.html", context)
