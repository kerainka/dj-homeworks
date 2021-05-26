from django.shortcuts import render
import pandas as pd
import json


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    df = pd.read_csv("inflation_russia.csv", sep=";")
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    context = {'data': data}

    return render(request, template_name, context)



