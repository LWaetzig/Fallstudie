from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

# Create your views here.
def home_view(request):
    return render(request=request, template_name="index.html")

def about_us_view(request):
    return render(request=request , template_name="aboutUs.html")

def fideo_view(request):
    return render(request=request , template_name="fideo.html")

def impressum_view(request):
    return render(request=request , template_name="impressum.html")

def login_view(request):
    return render(request=request , template_name="login.html")

def factory(request):

    fig = go.Figure()
    fig2 = go.Figure()
    fig3 = go.Figure()
    scatter = go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 2, 3], mode="lines", name="test")
    scatter2 = go.Scatter(x=[0,1,2,3] , y=[5,4,2,7] , mode="lines")
    scatter3 = go.Scatter(x=[0,1,2,3] , y=[7,1,2,10] , mode="lines")

    fig.add_trace(scatter)
    fig2.add_trace(scatter2)
    fig3.add_trace(scatter3)
    plot_div = plot(fig , output_type="div", include_plotlyjs=False, show_link=False)
    plot_div2 = plot(fig2 , output_type="div" , include_plotlyjs=False , show_link=False)
    plot_div3 = plot(fig3 , output_type="div" , include_plotlyjs=False , show_link=False)


    context = {"plot_div" : plot_div , "plot_div2" : plot_div2 , "plot_div3" : plot_div3}

    return render(request=request, template_name="factory.html", context=context)

