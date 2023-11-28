import io
from flask import Blueprint, render_template, redirect, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from .spectroworks_api_interface import Connection, analyze_test, analyze_range, plotting, API_KEY

views = Blueprint("views", __name__)

@views.route("/home")
def home_redirect():
    return redirect("/")

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        global moving_average
        global remove_outliers

        moving_average = True if request.form.get('moving_average_check') != None else False
        remove_outliers = True if request.form.get('remove_outliers_check') != None else False

        global test_number
        try:
            test_number = int(request.form.get('test_number'))
        except:
            test_number = 9


    return render_template("home.html")

test_number = 9 # Default value

@views.route("/result")
def result():

    return render_template("home.html")

@views.route("/plot_old.png")
def render_old_plot():
    try:
        response = Response(plot_bytes, mimetype='image/png')
    except NameError:
        plot_png()
        return Response(plot_bytes, mimetype='image/png')
    else:
        return response

@views.route("/plot.png")
def render_plot():
    plot_png()
    return Response(plot_bytes, mimetype='image/png')

def plot_png():
    connection = Connection(API_KEY, f'https://api.spectroworks.com/prod/api/')

    project = connection.get_project('Vinyl chloride in water')
    project.get_items()

    data = analyze_test(project, test_number=test_number, moving_average=moving_average, remove_outliers=remove_outliers)

    axis, fig = plotting(data)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    global plot_bytes
    plot_bytes = output.getvalue()