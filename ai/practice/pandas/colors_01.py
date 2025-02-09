# Importing the necessary libraries -->
import pandas as pd
import numpy as np
 
# Seeding random data from numpy
np.random.seed(24)
 
# Making the DataFrame
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), 
                                 columns=list('BCDE'))], axis=1)
 
# DataFrame without any styling
print("Original DataFrame:\n")
print(df)
print("\nModified Stlying DataFrame:")
df.style.set_properties(**{'background-color': 'black',
                           'color': 'green'})



