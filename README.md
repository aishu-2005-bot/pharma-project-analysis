# Agentic AI Pharma Demo


## Backend (Python)
1. cd backend
2. python -m venv venv
3. source venv/bin/activate (on Windows: venv\Scripts\activate)
4. pip install -r requirements.txt
5. uvicorn main:app --reload --port 8000


## Frontend (React)
1. cd frontend
2. npm install
3. npm start

## test cases
Evaluate market opportunity, clinical development potential, and patent risks for this molecule.
MoleculeX
Respiratory

Provide an executive-level assessment covering market attractiveness, clinical maturity, and intellectual property risks.
RespiraNova-101
Respiratory


Analyze clinical trial landscape, competitive intensity, and intellectual property risks for this oncology candidate.
ONCO-A7
Oncology
US


Assess market size, unmet medical need, and commercialization feasibility for this cardiovascular drug.
CardioRelief-22
Cardiology
EU

Evaluate development feasibility, clinical trial readiness, and regulatory considerations for this infectious disease therapy.
AntiVir-X
Infectious Diseases
IN

Open http://localhost:3000 for frontend and ensure backend is running at http://localhost:8000


Notes: This is a mocked demo. The LLM synthesis is simplified. Replace synthesis with real LLM calls and integrate real subscription APIs for production.