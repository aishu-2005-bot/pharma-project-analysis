# mock_apis.py
from fastapi import APIRouter


router = APIRouter()


@router.get('/iqvia/market')
def iqvia_market(therapy: str = 'Respiratory', country: str = 'IN'):
 return {
"therapy": therapy,
"country": country,
"market_size_usd_m": 420,
"cagr_pct": 6.8,
"top_competitors": [
{"name": "Company A", "market_share_pct": 18},
{"name": "Company B", "market_share_pct": 12}
],
"segment_breakdown": [
{"sub": "Asthma", "size_m": 220},
{"sub": "COPD", "size_m": 200}
]
}


@router.get('/clinical/trials')
def clinical_trials(drug: str = 'MoleculeX'):
 return {
"drug": drug,
"trials": [
{"id": "CT-001", "title": "Phase 2 study on COPD", "phase": "Phase 2", "status": "Recruiting", "location": "India"},
{"id": "CT-002", "title": "Phase 1 inhalation safety", "phase": "Phase 1", "status": "Completed", "location": "US"}
]
}


@router.get('/patents/search')
def patent_search(query: str = 'MoleculeX'):
 return {
"query": query,
"patents": [
{"id": "US-12345", "title": "Composition patent", "country": "US", "expiry": "2032-05-01", "fpo_flag": False},
{"id": "IN-54321", "title": "Formulation patent", "country": "IN", "expiry": "2028-11-12", "fpo_flag": True}
]
}