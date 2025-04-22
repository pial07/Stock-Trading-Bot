from django.apps import apps

def batch_insert_stock_data(batch_size=10, dataset=None, company_obj=None, verbose=False):
    StockQuotes = apps.get_model('market', 'StockQuotes')
    batch_size=10
    if company_obj is None:
        raise Exception(f"Company object {company_obj} is invalid") 
    for i in range(0,len(dataset),batch_size):
        if verbose:
            print("Doing Chunk",i)
        batch_chunk=dataset[i:i+batch_size]
        chunked_quotes=[]
        for data in batch_chunk:
            chunked_quotes.append(StockQuotes(company=company_obj, **data))
        StockQuotes.objects.bulk_create(chunked_quotes, ignore_conflicts=True)
        if verbose:
            if verbose:
              print("Ending Chunk",i)