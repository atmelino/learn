import tables as tb


class Config(tb.IsDescription):
    name = tb.StringCol(16)  # 16-character String
    n_epochs = tb.UInt64Col()  # Signed 64-bit integer
    n_batch = tb.UInt64Col()  # Signed 64-bit integer
    x_min = tb.Float64Col()  # double (double-precision)
    x_max = tb.Float64Col()  # double (double-precision)
    random_real = tb.BoolCol()



fname = "./models/discriminator.h5"
with tb.open_file(fname, "r") as h5file:
    node = h5file.get_node("/")

    table = h5file.root.training_config.config

    print(table)
    print(table.row)
    print("x_min=",table.col('x_min')[0])

    h5file.close()



