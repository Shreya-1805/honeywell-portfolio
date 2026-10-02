# Honeywell Software Engineer Portfolio

| Project | Skills shown |
|---|---|
| salesforce/ (Apex trigger, handler, tests, LWC) | Salesforce development, bulk-safe patterns, 75%+ test coverage |
| python/iot_anomaly | Python, FastAPI, pandas, pytest, Salesforce REST integration |
| python/code_review | Code reviews and coding standards (automated) |
| python/agile | Agile / sprint metrics |

Deploy Salesforce: `sf project deploy start --source-dir salesforce/force-app` (needs sfdx-project.json).
Run Python: `cd python/iot_anomaly && pip install -r requirements.txt && pytest && uvicorn api:app`.
