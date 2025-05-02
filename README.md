# hkl_generator

**hkl_generator** is a Python-based tool for generating and analyzing crystallographic reflection conditions (hkl indices) using space group symmetry rules. The tool leverages data from the Bilbao Crystallographic Server to determine allowed reflections based on the space group's systematic absences.

## Features

- Generate allowed hkl reflections for a given crystallographic space group
- Supports both CSV and JSON formats for reflection condition data
- Includes pre-loaded condition tables for commonly used space groups

## Included Data Files

The repository provides example reflection condition files for several space groups:

- `bilbao_refl_cond_table_I411.csv`
- `bilbao_refl_cond_table_Ia-3d.json`
- `bilbao_refl_cond_table_P21_c.csv`
- `bilbao_refl_cond_table_Pm-3m.json`
- `bilbao_refl_cond_table_expanded_Pa-3.csv`

These files contain systematic absence rules for filtering valid hkl triplets.

## Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/MarcoVando/hkl_generator.git
cd hkl_generator
pip install -r requirements.txt
```

## Usage

You can run the script directly:
```
python main.py
```
The script will prompt for input parameters or allow you to choose a reflection condition file and generate the list of valid hkl reflections accordingly.

Alternatively, you can import functions from the module and use it programmatically:

from hkl_generator import generate_hkl

# Example usage
```
hkl_list = generate_hkl(space_group="Pm-3m", max_index=10)  
print(hkl_list)
```

# License

This project is licensed under the BSD 3-Clause License. See the LICENSE file for more information.

# Acknowledgments

Reflection condition data provided by the [Bilbao Crystallographic Server.]([https://chatgpt.com/c/6814e111-10b4-8001-9338-b8a9651c0b5a#:~:text=by%20the%20Bilbao-,Crystallographic,-Server](https://www.cryst.ehu.es))
