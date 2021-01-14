

class Molecule:
    def __init__(self, name, charge, symbols):
        self.name = name
        self.charge = charge
        self.symbols = symbols
        #self._num_atoms = len(symbols) #not good practive to still include this

    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        self._symbols = symbols
        self._num_atoms = len(symbols)

    def my_algorithm(self, parameter_list):
        self._first_stage(parameter_list)
        self._second_stage(parameter_list)
        self._third_stage(parameter_list)
        #fisrt stage
        #second
        #thrid

    def _first_stage(self, parameter_list):
        # performs firsty stage
        print(f'first {parameter_list}')

    def _second_stage(self, parameter_list):
        # performs firsty stage
        pass

    def _third_stage(self, parameter_list):
        # performs firsty stage
        pass


    def __str__(self):
        return f'name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}'


water_molecule = Molecule('water', 0.0, ['O', 'H', 'H'])
he_molecule = Molecule('He', 0.0, ['He'])
print(water_molecule)
print(water_molecule.__repr__())
print(water_molecule.name)
print(water_molecule.symbols)
print(water_molecule._num_atoms)
water_molecule.symbols = ['O', 'O', 'H', 'H']
print(water_molecule.symbols)
print(water_molecule._num_atoms)
print(he_molecule)
print(water_molecule.my_algorithm([1,2,3]))