# from tables import *
import tables as tb


class Config(tb.IsDescription):
    name = tb.StringCol(16)  # 16-character String
    n_epochs = tb.UInt64Col()  # Signed 64-bit integer
    n_batch = tb.UInt64Col()  # Signed 64-bit integer
    x_min = tb.Float64Col()  # double (double-precision)
    x_max = tb.Float64Col()  # double (double-precision)
    random_real = tb.BoolCol()


fname = "./discriminator.h5"
with tb.open_file(fname, "a") as h5_mod:
    node = h5_mod.get_node("/")

    try:
        h5_mod.remove_node("/training_config", recursive=True)
    except tb.NoSuchNodeError:
        print("file does not have training_config node")

    # try:
    #     node.__contains__(node.training_config)
    #     print('contains training_config')
    # except tb.NoSuchNodeError:
    #     print('there is no training_config, will create it')
    print("Create training_config node")
    group = h5_mod.create_group(
        "/", "training_config", "Training configurationinformation"
    )
    table = h5_mod.create_table(group, "config", Config, "config data")
    config = table.row
    config["name"] = f"Config: 1"
    config["n_epochs"] = 1000
    config["n_batch"] = 128
    config["x_min"] = -0.5
    config["x_max"] = 0.5
    config["random_real"] = True
    # Insert a new config record
    config.append()
    table.flush()
    h5_mod.close()
