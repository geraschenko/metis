# Metis

Project Metis implements simulation tools for clinical trial enrollment. Metis is being developed for the public good with the initial goal of expediting clinical validation of vaccine candidates for COVID-19, with a focus on targeted site selection to support enhanced recruitment for vaccine research. 

[Metis](https://github.com/verilylifesciences/metis/blob/Metis%20-%20Baseline.pdf) allows the user to input model forecasts for regional disease prevalence, as well as historical disease incidence data. One potential source of US-only model forecasts is the [CDC ensemble](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/forecasts-cases.html). A potential source of historical data is [Google Cloud’s open repository](https://github.com/GoogleCloudPlatform/covid-19-open-data).




# How to use Metis

This repository includes [Jupyter notebooks](https://jupyter.org/), a Python package, and [Dockerfiles](https://www.docker.com/) for the Metis simulation tools.

By default the notebooks run with a small amount of demo data, so you can run them anywhere that you can run Jupyter notebooks.

For use of the notebooks to run simulations on your own, larger scale data, you will need to run them on a machine with more CPUs and memory, such as those available via [Terra](https://app.terra.bio/). Please see the computational requirements listed at the top of each notebook.

Different trial designs will have different additional requirements for the simulations. You can reach the Project Metis team at metis@projectbaseline.com to discuss how those changes can be added to this tool.

# How to contribute to Metis

First please see the [contribution guidelines](docs/contributing.md). Then refer to the [development instructions](docs/development_and_deployment.md) for further detail.






