from django.shortcuts import render
from plotly.offline import plot
import os

from .src.get_stock_data import create_visualization

# Create your views here.
def home_view(request):
    return render(request=request, template_name="index.html")


def about_us_view(request):
    return render(request=request, template_name="aboutUs.html")


def risk_analysis_view(request):
    return render(request=request, template_name="risikoanalyse.html")


def fideo_view(request):

    fig1 = create_visualization("fideo/data/AAPL.csv")
    fig2 = create_visualization("fideo/data/AMZN.csv")
    fig3 = create_visualization("fideo/data/TSLA.csv")

    plot1 = plot(fig1, output_type="div")
    plot2 = plot(fig2, output_type="div")
    plot3 = plot(fig3, output_type="div")

    context = {
        "plots" : [plot1, plot2, plot3],
        "tags" : ["Apple Inc." , "Amazon 4Müll" , "Tesla"],
        "name_list": [
            "ADDDF",
            "ALIZF",
            "GOOGL",
            "AMZN",
            "AAPL",
            "BFFAF",
            "BAYZF",
            "BNTX",
            "BAMXF",
            "KO",
            "CRZBF",
            "MBGAF",
        ],
        "template_grid": range(4),
    }

    return render(request=request, template_name="fideo.html", context=context)


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
