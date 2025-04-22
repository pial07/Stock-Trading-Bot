from django.apps import apps
from .utils import batch_insert_stock_data
import helpers.client as helper_clients 

def sync_company_stock_quotes(company_id,function="TIME_SERIES_INTRADAY", interval="1min", month="2024-02", verbose=False):
    Company = apps.get_model('market', 'Company')
    try:
        company_obj = Company.objects.get(id=company_id)
    except:
        company_obj= None
    if company_obj is None:
        raise Exception(f"Company with id {company_id} not found")
    company_ticker = company_obj.ticker
    if company_ticker is None:
        raise Exception(f"Company with id {company_id} has no ticker")
    client=helper_clients.AlphaVantageAPIClient(
                             ticker=company_ticker,
                             function=function,
                             interval=interval,
                             month=month
                                    )
    dataset=client.get_stock_data()
    if verbose:
        print(f"Dataset length {len(dataset)}")
    batch_insert_stock_data(company_obj=company_obj, dataset=dataset,verbose=verbose)

def sync_stock_data():
    Company = apps.get_model('market', 'Company')
    companies = Company.objects.filter(active=True).values_list('id',flat=True)
    for company_id in companies:
        sync_company_stock_quotes(company_id)