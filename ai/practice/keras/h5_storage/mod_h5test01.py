# import tables

# from tables import *
import tables as tb

class Config(tb.IsDescription):
    name      = tb.StringCol(16)   # 16-character String
    n_epochs  = tb.UInt64Col()      # Signed 64-bit integer
    n_batch  = tb.UInt64Col()      # Signed 64-bit integer
    idnumber  = tb.Int64Col()      # Signed 64-bit integer
    ADCcount  = tb.UInt16Col()     # Unsigned short integer
    TDCcount  = tb.UInt8Col()      # unsigned byte
    grid_i    = tb.Int32Col()      # 32-bit integer
    pressure  = tb.Float32Col()    # float  (single-precision)
    energy    = tb.Float64Col()    # double (double-precision)


fname='./discriminator.h5'
with tb.open_file(fname, 'a') as h5_mod:
    node = h5_mod.get_node('/')

    # h5_mod.remove_node('/training_config',recursive=True)
    # exit()


    try:
        node.__contains__(node.training_config)
        h5_mod.remove_node('/training_config',recursive=True)
        print('contains training_config')
    except tb.NoSuchNodeError:
        print('there is no training_config, will create it')
        # handle.create_table('/', 'grades', grades)
        group = h5_mod.create_group("/", 'training_config', 'Training configurationinformation')
        table = h5_mod.create_table(group, 'config', Config, "config data")

        config = table.row

        config['name']  = f'Config: 1'
        config['n_epochs'] = 1000
        config['n_batch'] = 128
        # Insert a new config record
        config.append()

        table.flush()


    # node._v_attrs['test_meta'] = 'My test attibute {}'.format(3.1415)

    h5_mod.close()



