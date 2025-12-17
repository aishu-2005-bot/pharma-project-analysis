import React, { useState } from 'react'
import axios from 'axios'

function App() {
  const [prompt, setPrompt] = useState('')
  const [molecule, setMolecule] = useState('')
  const [therapy, setTherapy] = useState('')
  const [country, setCountry] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const submit = async () => {
	setLoading(true)
	try {
	  const res = await axios.post('http://localhost:8000/analyze', {
		prompt,
		molecule,
		therapy,
		country,
	  })
	  setResult(res.data)
	} catch (err) {
	  alert('Error: ' + err)
	} finally {
	  setLoading(false)
	}
  }

  const uploadFile = async (e) => {
	const file = e.target.files[0]
	if (!file) return
	const fd = new FormData()
	fd.append('file', file)
	try {
	  const r = await axios.post('http://localhost:8000/upload', fd, {
		headers: { 'Content-Type': 'multipart/form-data' },
	  })
	  alert('Uploaded: ' + r.data.filename)
	} catch (err) {
	  alert('Upload error: ' + err)
	}
  }

  return (
	<div className='container'>
	  <h1>Agentic AI - Pharma Innovation Finder (Demo)</h1>
	  <div className='card'>
		<label>Prompt</label>
		<textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={3}></textarea>
		<div className='row'>
		  <div>
			<label>Molecule</label>
			<input value={molecule} onChange={(e) => setMolecule(e.target.value)} />
		  </div>
		  <div>
			<label>Therapy</label>
			<input value={therapy} onChange={(e) => setTherapy(e.target.value)} />
		  </div>
		  <div>
			<label>Country</label>
			<input value={country} onChange={(e) => setCountry(e.target.value)} />
		  </div>
		</div>
		<div className='row'>
		  <input type='file' onChange={uploadFile} />
		  <button onClick={submit} disabled={loading}>{loading ? 'Running...' : 'Run Analysis'}</button>
		</div>
	  </div>

	  {result && (
		<div className='card'>
		  <h2>Executive Summary</h2>
		  <pre>{result.summary}</pre>

		  <h3>Market</h3>
		  <p><b>Market Size:</b> ${result.market.market_size_usd_m}M</p>
<p><b>CAGR:</b> {result.market.cagr_pct}%</p>


		  <h3>Clinical Trials</h3>
		  <pre>{JSON.stringify(result.trials, null, 2)}</pre>

		  <h3>Patents</h3>
		  <pre>{JSON.stringify(result.patents, null, 2)}</pre>

		  {result.report && (
			<a href={result.report} target='_blank' rel='noreferrer'>Download PDF Report</a>
		  )}
		</div>
	  )}
	</div>
  )
}

export default App