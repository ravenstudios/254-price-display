from django.shortcuts import render
from . import views
import pandas as pd
import os
from pyexcel_ods import get_data
import pyexcel as pe
import json
# from pyexcel.ext import ods



def index(request):
    # module_dir = os.path.dirname(__file__)
    # file_path = os.path.join(module_dir, 'static/Phone_Repair_Prices.ods')
    # data_file = open(file_path , 'r')
    # prices = pd.read_excel("display_app/Phone_Repair_Prices.ods", engine='odf')
    prices = get_data("display_app/Phone_Repair_Prices.ods")
    # prices = pe.get_book(file_name="display_app/Phone_Repair_Prices.ods

    # prices_data = json.dumps(prices["Sheet1"])
    prices_data = prices["Sheet1"]
    prices_header = prices_data[0]
    print(prices_header)
    context = {
        "prices": prices_data,
        "prices_header": prices_header
        }
    return render(request, 'display_app/index.html', context)
