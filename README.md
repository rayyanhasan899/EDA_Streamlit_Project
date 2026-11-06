# CSV Exploration Lab

A small academic Streamlit lab for exploring a CSV dataset. It previews rows, reports dimensions and data types, counts missing values, and displays numeric summaries and a selected column's distribution.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

On Ubuntu use `.venv/bin/python` instead. Upload a CSV through the sidebar, then select a column. Numeric columns use a histogram; other columns use category counts. No online deployment or trained machine-learning model is provided.

## Scope and limitations

This is a lab exercise, not a substantial data platform. Large files, high-cardinality categories, encoding differences, and mixed-type columns need additional handling for broader use. Data is loaded into the local application process; avoid sensitive datasets on shared machines.

`Titanic-Dataset.csv` is an existing sample whose exact source/license is not documented in this repository. Confirm attribution and redistribution terms before repackaging it. You can use your own CSV instead.

Dependencies are listed in `requirements.txt`; the original repository does not pin a Python or package version. See [validation notes](docs/VALIDATION.md) for the environment actually checked.

Academic lab work by Syed Muhammad Rayyan Hassan.
