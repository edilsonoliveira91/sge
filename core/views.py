import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url='login')
def home(request):
    context = {
        'product_metrics': metrics.get_product_metrics(),
        'sales_metrics': metrics.get_sales_metrics(),
        'daily_sales_data': json.dumps(metrics.get_daily_sales_data()),
        'daily_sales_quantity_data': json.dumps(metrics.get_daily_sales_quantity_data()),
        'product_count_by_category': json.dumps(metrics.get_product_count_by_category()),
        'product_count_by_brand': json.dumps(metrics.get_graphic_product_brand_metric()),
    }
    return render(request, 'home.html', context)