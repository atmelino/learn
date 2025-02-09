import termcolor
import pandas
# assume `df['foo']` is a `pandas.DataFrame` column with
#     boolean values...
#
df = pandas.DataFrame({'foo': [False]}) # this is a fake df with
                                        # no real data.  Ensure 
                                        # you have a real
                                        # DataFrame stored in 
                                        # df...

# NOTE: there's probably a more idiomatic pandas incantation 
# for what I'm doing here, but this is intended to 
# demonstrate the concept of colorizing `colorized_df['foo']`
colorized_df = None
colored_str_value = ""
colorized_row = []
for original_value in df['foo'].values:
    # casting `original_value` bools as strings to color them red...
    colored_str_value = termcolor.colored(str(original_value), 'red')
    colorized_row.append(colored_str_value)
colorized_df = pandas.DataFrame({'foo': colorized_row})
# Do something here with colorized_df...
print(colorized_df)




