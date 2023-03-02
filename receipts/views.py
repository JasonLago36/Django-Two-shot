from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Receipt
# Create your views here.


@login_required
def receipt_list(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_object": receipt,
    }

    return render(request, "receipts/home.html", context)
