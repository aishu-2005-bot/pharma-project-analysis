from mock_apis import iqvia_market, clinical_trials, patent_search

def run_iqvia(therapy='Respiratory', country='IN'):
    return iqvia_market(therapy=therapy, country=country)

def run_clinical(drug='MoleculeX'):
    return clinical_trials(drug=drug)

def run_patent(query='MoleculeX'):
    return patent_search(query=query)
