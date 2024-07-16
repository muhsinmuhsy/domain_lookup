from django.shortcuts import render, redirect
from django.contrib import messages
import whois
import datetime


# def index(request):
#     whois_domain = None  # Initialize the variable

#     if request.method == 'POST':
#         domain = request.POST.get('domain')

#         try:
#             whois_domain = whois.whois(domain)
#         except Exception as e:
#             whois_domain = f'Error fetching WHOIS data: {str(e)}'

#     return render(request, 'index.html', {'whois_domain': whois_domain})


def format_dates(date_data):
    if date_data is None:
        return None
    elif isinstance(date_data, list):
        return ', '.join([dt.strftime('%Y-%m-%d %H:%M:%S') for dt in date_data])
    else:
        return datetime.datetime.strptime(str(date_data), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    
def index(request):
    whois_domain = None

    if request.method == 'POST':
        domain = request.POST.get('domain')

        try:
            whois_data = whois.whois(domain)

            # if isinstance(whois_data.updated_date, list):
            #     updated_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in whois_data.updated_date]
            #     updated_date_str = ', '.join(updated_dates)
            # else:
            #     updated_date_str = datetime.datetime.strptime(str(whois_data.updated_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

            # if isinstance(whois_data.creation_date, list):
            #     creation_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in whois_data.creation_date]
            #     creation_date_str = ', '.join(creation_dates)
            # else:
            #     creation_date_str = datetime.datetime.strptime(str(whois_data.creation_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

            # if isinstance(whois_data.expiration_date, list):
            #     expiration_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in whois_data.expiration_date]
            #     expiration_date_str = ', '.join(expiration_dates)
            # else:
            #     expiration_date_str = datetime.datetime.strptime(str(whois_data.expiration_date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

            # '%B %d, %Y, %I %p'

            updated_date_str = format_dates(whois_data.updated_date)
            creation_date_str = format_dates(whois_data.creation_date)
            expiration_date_str = format_dates(whois_data.expiration_date)

            whois_domain = {
                "domain_name": whois_data.domain_name,
                "registrar": whois_data.registrar,
                "whois_server": whois_data.whois_server,
                "referral_url": whois_data.referral_url,
                "updated_date": updated_date_str,
                "creation_date": creation_date_str,
                "expiration_date": expiration_date_str,
                "name_servers": whois_data.name_servers,
                "status": whois_data.status,
                "emails": whois_data.emails,
                "dnssec": whois_data.dnssec,
                "name": whois_data.name,
                "org": whois_data.org,
                "address": whois_data.address,
                "city": whois_data.city,
                "state": whois_data.state,
                "registrant_postal_code": whois_data.registrant_postal_code,
                "country": whois_data.country,
            }
            
        except Exception as e:
            messages.error(request, f'Error fetching WHOIS data: {str(e)}')
            return redirect('index')

    context = {
        'whois_domain': whois_domain
    }

    return render(request, 'index.html', context)

# def index(request):
#     if request.method == 'POST':
#         domain = request.POST.get('domain')

#         try:
#             whois_data = whois.whois(domain)
            
#         except Exception as e:
#             messages.error(request, f'Error fetching WHOIS data: {str(e)}')
#             return redirect('index')

#     context = {
#         'whois_data': whois_data
#     }

#     return render(request, 'index.html', context)