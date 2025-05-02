from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# Define the lattice parameters
a = 4.2  # Lattice parameter a
b = 4.2  # Lattice parameter b
c = 4.2  # Lattice parameter c
alpha = 90  # Lattice angle alpha in degrees
beta = 90  # Lattice angle beta in degrees
gamma = 90  # Lattice angle gamma in degrees

# Create the lattice
lattice = Lattice.from_parameters(a, b, c, alpha, beta, gamma)

# Define the atomic positions
species = ["Cu", "Cu", "Cu", "O", "O", "O"]
positions = [[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5], [0.5, 0, 0], [0, 0.5, 0]]

# Create the structure
structure = Structure(lattice, species, positions)

# Get the spacegroup analyzer
analyzer = SpacegroupAnalyzer(structure)

# Get the conventional standard structure
conventional_structure = analyzer.get_conventional_standard_structure()

# Get the HKL indices
hkl_indices = analyzer.get_hkl_family_indices()

# Print the HKL indices
print("HKL indices:")
for hkl_family, indices in hkl_indices.items():
    print(f"{hkl_family}: {indices}")
