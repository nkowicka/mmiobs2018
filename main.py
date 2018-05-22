import numpy as np


class Cast:
    map = None
    min_ca_coords = None

    def __init__(self):
        self.map = np.zeros((100, 100, 100))

    def create_cast(self, data):
        return

    def get_min_ca_coords(self, data):
        for ca in data:
            if self.min_ca_coords is None:
                self.min_ca_coords = ca[1]
            else:
                for coord in range(3):
                    if self.min_ca_coords[coord] > ca[1][coord]:
                        self.min_ca_coords[coord] = ca[1][coord]

    def get_shift(self, data):
        pass  # TODO
        # for ca in data:
        #     print(ca[1], ca[1] - self.min_ca)

    def __str__(self):
        return str(self.map)

class Simulation:

    def __init__(self, n_rep, f):
        self.n_rep = n_rep
        self.n_steps = 0
        self.file = f

    # Caster chce dostac liste wszystkich wegli alfa
    # i to on ma wyznaczyc minimum i dzielic na biny

    def read_pdb_file(self):
        with open(self.file, 'r+') as f:
            data, cas = [], []
            for line in f.readlines():
                if line.startswith('ATOM'):
                    row = line.split()
                    amino_acid = (row[3], np.array(row[6:9]).astype(np.float).round(1))
                    if row[2] == 'CA':
                        cas.append(amino_acid)
                    else:
                        data.append(amino_acid)
            return data, cas


s = Simulation(100, '1fn3.pdb')
c = Cast()

print(s.read_pdb_file()[1])
