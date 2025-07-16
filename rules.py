import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the preprocessed basket (from preprocess step)
df = pd.read_csv("products.csv")
df['Products'] = df['Products'].apply(lambda x: [item.strip() for item in x.split(',')])

from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(df['Products']).transform(df['Products'])
basket = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.02, use_colnames=True)

# Generate rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Sort and display top rules
rules = rules.sort_values(by='confidence', ascending=False)
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())

# Optional: Save to Excel
rules.to_excel("association_rules.xlsx", index=False)
