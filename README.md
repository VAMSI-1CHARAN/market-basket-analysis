# 🛒 Market Basket Analysis using Apriori Algorithm & Tableau

This project performs Market Basket Analysis on simulated retail transactions using the Apriori algorithm to discover hidden product purchase patterns. The results are visualized through an interactive Tableau Public dashboard.

---

## 🔍 Objective

- Discover associations between frequently bought products
- Generate strong rules using support, confidence, and lift
- Visualize top rules, matrix views, and rule strength comparisons

---

## 📁 Project Structure

market-basket-analysis/
│
├── data/
│ └── products.csv # Raw transactional data
│
├── src/
│ ├── preview.py # Initial CSV preview
│ ├── preprocess.py # One-hot encoding with TransactionEncoder
│ └── rules.py # Apriori algorithm and rule generation
│
├── output/
│ └── association_rules.xlsx # Final association rules file
│
├── dashboard/
│ └── tableau_dashboard_link.txt # Tableau Public link
│
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)


---

## ⚙️ How It Works

1. **Data Input**: Simulated transaction log with product names
2. **Preprocessing**: Tokenize product lists, one-hot encode using `mlxtend`
3. **Apriori Rule Mining**: Discover rules with minimum support & confidence
4. **Export**: Save rules to Excel for external BI visualization
5. **Tableau Dashboard**: Visualize strongest rules, lift vs confidence, top products, and matrix patterns

---

## 📊 Tableau Dashboard

🧠 View the full interactive dashboard with 6 analytical sheets:
- Top Rules by Confidence
- Top Rules by Lift
- Lift vs Confidence (Scatter)
- Rule Matrix (Lift Heatmap)
- Top Antecedents
- All Rules Table

🔗 https://public.tableau.com/views/MarketBasketInsightsAssociationRuleMining/MarketBasketDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt

**## Main Python Libraries:**
mlxtend
pandas
openpyxl

---

