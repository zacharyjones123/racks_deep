import pandas as pd
from data.SAndBFilters.Products.FilterVariants import FilterVariant
import os

def get_filters_from_asap():
    print(os.curdir)
    df = pd.read_csv('./sheets/SAndBFilters/sAndBFilters_prices.csv', delimiter=',')
    df.fillna("asdf")
    print(df.keys())
    # Need to use this to make a class
    filters = []
    for i, r in df.iterrows():
        filters.append(FilterVariant(r['sku'], r['upc'], r['title'], r['vehicle_type'], r['vehicle_type'], r['map_price'], r['images']))
       #print((r['sku'], r['upc'], r['title'], r['filter_type'], r['vehicle_type'], r['map_price'], r['images']))
    return filters
get_filters_from_asap()