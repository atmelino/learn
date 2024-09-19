# Convert diabetes dataset to Panda dataframe
# pd_diabetes = diabetes_df = pd.DataFrame(data=diabetes_X_load)
# df = pd.DataFrame(diabetes_X_load, columns=["age       sex       bmi        bp        s1        s2        s3 "])
mycolumns=["age","sex","bmi","bp","s1","s2","s3","s3","s3","s3"]
# df = pd.DataFrame(diabetes_X_load)
df = pd.DataFrame(diabetes_X_load, columns= mycolumns)
# display(df)
