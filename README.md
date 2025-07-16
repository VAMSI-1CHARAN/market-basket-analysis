# 🛒 Market Basket Analysis – Association Rule Mining (Apriori)

This project uncovers product association rules from retail transactions using the Apriori algorithm and visualizes insights via Tableau Public dashboard.

---

## 📁 Project Structure

- `data/` – Raw retail dataset (`products.csv`)
- `src/` – Python scripts for:
  - Previewing data
  - Preprocessing into transaction format
  - Extracting association rules
- `output/` – Generated rule file (`association_rules.xlsx`)
- `dashboard/` – Link to Tableau dashboard
- `notebooks/` – (Optional) Jupyter notebook version
- `README.md` – Project overview
- `requirements.txt` – Dependencies

---

## 🔍 Techniques Used

- **Apriori Algorithm** (`mlxtend`)
- **Association Rules** (Support, Confidence, Lift)
- **One-Hot Encoding**
- **Tableau Dashboard** for:
  - Top Rules by Confidence
  - Lift vs Confidence
  - Rule Matrix
  - Top Antecedents

---

## 📊 Live Tableau Dashboard

🔗 https://public.tableau.com/views/MarketBasketInsightsAssociationRuleMining/MarketBasketDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

## 🚀 How to Run

```bash
pip install -r requirements.txt

python src/preview.py
python src/preprocess.py
python src/rules.py
