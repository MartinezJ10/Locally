from django.shortcuts import render
from django.contrib import messages
import requests

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Honduras"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    data_req = response['response']
    source = data_req[0] 

    context = {
        'all': format(source['cases']['total'], ",d"),
        'recovered':  format(source['cases']['recovered'], ",d"),
        'deaths': format(source['deaths']['total'], ",d"),
        'newDeaths': format(source['deaths']['new']),
        'new': format(source['cases']['new']),
        'active': format(source['cases']['active'], ",d"),
    }
    return render(request,'locally/home.html',context)

def globalView(request):

    if request.method == 'POST':
        search = request.POST['search']
        querystring = {"country":search}
        print(querystring)

        url = "https://covid-193.p.rapidapi.com/statistics"

        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        if response['results'] > 0:
            data_req = response['response']
            source = data_req[0]

            context = {
                'all': format(source['cases']['total'], ",d"),
                'recovered':  format(source['cases']['recovered'], ",d"),
                'deaths': format(source['deaths']['total'], ",d"),
                'newDeaths': source['deaths']['new'],
                'new': source['cases']['new'],
                'active': format(source['cases']['active'], ",d"),
                'search':search,
            }
            return render(request, 'locally/global.html', context)
        else:
            messages.info(request, "País no encontrado")
    return render(request, 'locally/global.html')