# import tables

from tables import *



class Particle(IsDescription):
    name      = StringCol(16)   # 16-character String
    idnumber  = Int64Col()      # Signed 64-bit integer
    ADCcount  = UInt16Col()     # Unsigned short integer
    TDCcount  = UInt8Col()      # unsigned byte
    grid_i    = Int32Col()      # 32-bit integer
    grid_j    = Int32Col()      # 32-bit integer
    pressure  = Float32Col()    # float  (single-precision)
    energy    = Float64Col()    # double (double-precision)

h5file = open_file("tutorial1.h5", mode="w", title="Test file")

group = h5file.create_group("/", 'detector', 'Detector information')

table = h5file.create_table(group, 'readout', Particle, "Readout example")

particle = table.row

for i in range(10):
    particle['name']  = f'Particle: {i:6d}'
    particle['TDCcount'] = i % 256
    particle['ADCcount'] = (i * 256) % (1 << 16)
    particle['grid_i'] = i
    particle['grid_j'] = 10 - i
    particle['pressure'] = float(i*i)
    particle['energy'] = float(particle['pressure'] ** 4)
    particle['idnumber'] = i * (2 ** 34)
    # Insert a new particle record
    particle.append()

table.flush()

print(h5file)

h5file

h5file.close()






