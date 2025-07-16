import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("products.csv")

# Step 2: Convert comma-separated Products into list
df['Products'] = df['Products'].apply(lambda x: [item.strip() for item in x.split(',')])

# Step 3: Create one-hot encoded transaction matrix
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(df['Products']).transform(df['Products'])
basket = pd.DataFrame(te_ary, columns=te.columns_)

print(basket.head())
