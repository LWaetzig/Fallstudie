from django.shortcuts import render
from plotly.offline import plot
from .models import Share

from .src.get_stock_data import create_visualization

# Create your views here.
def home_view(request):
    return render(request=request, template_name="index.html")


def about_us_view(request):
    return render(request=request, template_name="aboutUs.html")


def risk_analysis_view(request):
    return render(request=request, template_name="risikoanalyse.html")


def fideo_view(request):

    share_list = Share.objects.all()
    pop_shares = dict()


    fig1 = create_visualization("fideo/data/hist/AAPL.csv")
    fig2 = create_visualization("fideo/data/hist/AMZN.csv")
    fig3 = create_visualization("fideo/data/hist/TSLA.csv")

    plot1 = plot(fig1, output_type="div")
    plot2 = plot(fig2, output_type="div")
    plot3 = plot(fig3, output_type="div")

    context = {
        "share_list" : share_list,

        "plots" : [plot1, plot2, plot3],
    }

    return render(request=request, template_name="fideo.html", context=context)


def impressum_view(request):
    return render(request=request, template_name="impressum.html")


def login_view(request):
    return render(request=request, template_name="login.html")


def factory(request):
    return render(request=request, template_name="factory.html")