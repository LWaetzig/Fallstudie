from django.shortcuts import render
from plotly.offline import plot

from .models import Share, User
from .create_visualizations import create_small_visualization, create_full_visualization


def home_view(request):
    return render(request , template_name="index.html")


def about_us_view(request):
    return render(request , template_name="aboutUs.html")


def impressum_view(request):
    return render(request , template_name="impressum.html")

def fideo_view(request):
    shares = Share.objects.all().order_by("share_name")
    share_plots = list()
    for i in shares:
        fig = create_full_visualization(str(i.share_historical) , i.risk_level)
        share_plots.append(plot(fig , output_type="div"))

    shares_order_by_marketcap = Share.objects.all().order_by("-share_market_cap").values()
    popular_shares = shares_order_by_marketcap[:3]
    popular_shares_plots = list()
    for i in popular_shares:
        fig = create_small_visualization(str(i["share_historical"]))
        popular_shares_plots.append(plot(fig , output_type="div"))

    context = {
        "shares" : shares,
        "share_plots" : share_plots,
        "popular_shares" : popular_shares,
        "popular_shares_plots" : popular_shares_plots,

        }
    return render(request , template_name="fideo.html" , context=context)

def risk_analysis_view(request):
    share_list = Share.objects.all().order_by("share_name")

    if request.method == "POST":
        print("get post from risk_analysis:" , request.POST["risk_level"])
        my_risk_level = request.POST["risk_level"]
        if len(User.objects.all()) == 0:
            User.objects.create(risk_level=my_risk_level)
        else:
            User.objects.update(risk_level=my_risk_level)

    user_risk_level = User.objects.all()[0].risk_level
    print(user_risk_level)

    context = {
        "share_list": share_list,
        "user_risk_level" : user_risk_level,
    }

    return render(request , template_name="risikoanalyse.html" , context = context)