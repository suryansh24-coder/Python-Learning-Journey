import pandas as pd
x = pd.read_csv('fitness_data.csv')
print(x.head(10)) 
print(x.tail(10))

import pandas as pd
x = pd.read_csv('fitness_data.csv')
print(x.info()) 