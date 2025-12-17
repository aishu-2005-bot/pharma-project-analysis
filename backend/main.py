# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mock_apis import router as mock_router
import workers
import report_generator


app = FastAPI()
app.include_router(mock_router)


app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
 prompt: str
 therapy: str = 'Respiratory'
 country: str = 'IN'
 molecule: str = 'MoleculeX'


@app.post('/analyze')
async def analyze(payload: AnalyzeRequest):
# 1) Dispatch workers (mocked)
 market = workers.run_iqvia(therapy=payload.therapy, country=payload.country)
 trials = workers.run_clinical(drug=payload.molecule)
 patents = workers.run_patent(query=payload.molecule)


# 2) Simple synthesis (mocked) — in real system use LLM to synthesize
 exec_summary = f"Executive summary for {payload.molecule}:\n"
 exec_summary += f"Market {market['therapy']} in {market['country']} size: ${market['market_size_usd_m']}M (CAGR: {market['cagr_pct']}%).\n"
 exec_summary += f"Clinical trials found: {len(trials['trials'])}.\n"
 exec_summary += f"Patent hits: {len(patents['patents'])}.\n"
 exec_summary += "Recommendation: Consider inhalation formulation feasibility studies and a Phase 2a trial for COPD.\n"


 pdf_file = report_generator.generate_pdf(exec_summary, filename='report_output.pdf')


 return {
'summary': exec_summary,
'market': market,
'trials': trials,
'patents': patents,
'report': f'/reports/{pdf_file}'
}


@app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
 contents = await file.read()
# simply save file — in demo we don't index it
 with open(f'uploaded_{file.filename}', 'wb') as f:
  f.write(contents)
 return {'filename': file.filename, 'size': len(contents)}


# static route to serve generated report (for demo)
from fastapi.staticfiles import StaticFiles
import os
if not os.path.exists('reports'):
 os.makedirs('reports')
# move created file to reports on generate (here simplified)
app.mount('/reports', StaticFiles(directory='reports'), name='reports')