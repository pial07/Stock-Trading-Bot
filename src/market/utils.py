from django.apps import apps

def batch_insert_stock_data(batch_size=10, dataset=None, company_obj=None):
    StockQuotes = apps.get_model('market', 'StockQuotes')
    batch_size=10
    if company_obj is None:
        return 
    for i in range(0,len(dataset),batch_size):
        batch_chunk=dataset[i:i+batch_size]
        chunked_quotes=[]
        for data in batch_chunk:
            chunked_quotes.append(StockQuotes(company=company_obj, **data))
        StockQuotes.objects.bulk_create(chunked_quotes, ignore_conflicts=True)