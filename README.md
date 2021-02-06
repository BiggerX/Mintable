# Mintable

To download a module: `python3 -m pip install <module_name>`

## Executing this notebook

Create a conda environment with the `requirements.txt` file:
`conda create --name mintable --file requirements.txt`

Activate the conda environment:
`conda activate mintable`

#### Additional Options

If necessary, create a conda environment with the `environment.yml` file:
`conda env create -n mintable -f environment.yml`

## Steps to create this notebook

Creating this conda environment:
`conda create --name mintable`

Activate the conda environment:
`conda activate mintable`

Installing two dependencies:
`conda install -n mintable -c conda-forge inquirer`
`conda install -n mintable -c conda-forge python-dotenv`
`conda install -n mintable -c conda-forge selenium`
`conda install -c conda-forge python-chromedriver-binary`
`conda install -c anaconda numpy`
`conda install -c conda-forge matplotlib`

Saving notebook dependencies to this environment:
`conda list -e > requirements.txt`
`conda env export > environment.yml`

## Miscellaneous

Deleting the conda environment:
`conda env remove -n mintable`

List Conda environments:
`conda env list`

Duplicate conda environments:
`conda create --name <clone_name> --clone <env_name>`
