# E-commerce Product Review System (FastAPI)

**What this contains**
- FastAPI backend (serves JSON API and simple Jinja2 HTML pages)
- pytest unit/integration tests
- Selenium UI test (Chrome) for submitting a review
- Postman collection (JSON) for API validation
- GitHub Actions workflow to run pytest
- Requirements file

**Run locally (quick)**
1. Create virtualenv: `python -m venv .venv && source .venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Start app: `uvicorn app.main:app --reload --port 8000`
4. Open http://localhost:8000

**Run tests**
- Unit tests: `pytest tests/test_api.py -q`
- Selenium UI test (requires Chrome + chromedriver available in PATH): `pytest tests/test_ui_selenium.py -q`
- Run all with report: `PYTHONPATH=$(pwd) pytest -q --html=reports/report.html`

**Notes**
- Selenium test expects ChromeDriver compatible with your Chrome version in PATH.
- Postman collection file: `postman_collection.json` (import into Postman).
