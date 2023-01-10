from django.shortcuts import render
from plotly.offline import plot
import os

from .src.get_stock_data import create_visualization

# Create your views here.
def home_view(request):
    return render(request=request, template_name="index.html")


def about_us_view(request):
    return render(request=request, template_name="aboutUs.html")


def fideo_view(request):

    fig1 = create_visualization("fideo/data/AAPL.csv")
    fig2 = create_visualization("fideo/data/AMZN.csv")
    fig3 = create_visualization("fideo/data/TSLA.csv")

    plot1 = plot(fig1 , output_type="div")
    plot2 = plot(fig2 , output_type="div")
    plot3 = plot(fig3 , output_type="div")


    context = {
        "plot1" : plot1,
        "share_tag1" : "Apple Inc.",
        "plot2" : plot2,
        "share_tag2" : "Amazon 4Müll",
        "plot3" : plot3,
        "share_tag3" : "Tesla",
    }

    return render(request=request, template_name="fideo.html" , context=context)


def impressum_view(request):
    return render(request=request, template_name="impressum.html")


def login_view(request):
    return render(request=request, template_name="login.html")


def factory(request):

    fig = create_visualization(
        "/Users/lwaetzig/Documents/B_Studium/3_Semester_WSM_2/9_Fallstudie/Fallstudie/shares/AAPL.csv"
    )
    plot1 = plot(fig, output_type="div")

    context = {"plot1": plot1}

    return render(request=request, template_name="factory.html", context=context)