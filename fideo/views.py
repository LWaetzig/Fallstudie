from django.shortcuts import render
from plotly.offline import plot

from .models import Share
from .src.get_stock_data import (create_full_visualization,
                                 create_small_visualization)


# Create your views here.
def home_view(request):
    return render(request=request, template_name="index.html")


def about_us_view(request):
    return render(request=request, template_name="aboutUs.html")


def risk_analysis_view(request):
    share_list = Share.objects.all().order_by("share_name")

    context = {
        "share_list" : share_list,
    }
    
    return render(request=request, template_name="risikoanalyse.html" , context=context)


def fideo_view(request):

    share_list = Share.objects.all().order_by("share_name")
    all_share_plots = list()
    for i in share_list:
        fig = create_full_visualization(str(i.share_historical))
        all_share_plots.append(plot(fig, output_type="div"))

    # define most popular shares depending on their market capitalisation
    sh_list_market_cap = Share.objects.all().order_by("-share_market_cap").values()
    pop_shares = sh_list_market_cap[:3]
    pop_share_plots = list()
    for i in pop_shares:
        fig = create_small_visualization(str(i["share_historical"]))
        pop_share_plots.append(plot(fig, output_type="div"))

    context = {
        "share_list": share_list,
        "all_share_plots": all_share_plots,
        "pop_shares": pop_shares,
        "pop_share_plots": pop_share_plots,
        "pop_share_counter": range(4),
    }

    return render(request=request, template_name="fideo.html", context=context)


def impressum_view(request):
    return render(request=request, template_name="impressum.html")


def login_view(request):
    return render(request=request, template_name="login.html")


def factory(request):
    return render(request=request, template_name="factory.html")
