# Global Olympic Sports Performance Analysis – Flask Web App

Embeds the Tableau Public dashboards and story in a Flask website.

## Run
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Pages
| Route | Content |
|---|---|
| / | Home: hero, KPIs, key insights |
| /about | Problem statement, dataset, tools |
| /dashboard | Global Sports Performance Analytics Dashboard |
| /efficiency | Olympic Performance & Regional Efficiency Dashboard |
| /story | 8-scene Tableau story |

Tableau view URLs are set in the `VIEWS` dictionary in `app.py`.
