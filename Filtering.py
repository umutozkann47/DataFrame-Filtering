import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns= ["A","B","C","D","E"])

# To show column names
result = df.columns 

# To display the first five rows
result = df.head(5) 

# To display the last five rows
result = df.tail(5) 

# To display the first two rows of column A
result = df["A"].head(2) 

# To display the first five rows of columns A and B
result = df[["A","B"]].head()

# To display rows from the 5th row onwards for columns A and B
result = df[5::][["A","B"]].head()

####### FILTERING #######

# To check which cells satisfy the condition > 50
result = df > 50 

# To create a new DataFrame with cells > 50
result = df[df > 50] 

# To display rows where A > 50 and B < 80
result = df[(df["A"] > 50) & (df["B"] < 80)]

# To display rows where A >= 50 and A is even
result = df.query("A >= 50 & A % 2 == 0")
print(result)
