<p align="center"> <img src="https://raw.githubusercontent.com/WsdmSubmission28/networkgrowth/master/content/viz_oc.png" width="350"/> </p>


# Raising Graphs From Randomness to Reveal Information Networks

This repo is the collection of the codes used in the experiments of [Raising Graphs From Randomness to Reveal Information Networks](https://info.ilab.sztaki.hu/~rpalovics/edge-sampling-kdd-2016.pdf).

## Datasets

Datasets can be found [here](https://dms.sztaki.hu/en/letoltes/networkgrowth).
* All files have three columns: 1 unix timestamp, 2 user id, 3 user id.
* If the value in the 3rd column is "-1", then instead of an edge a root adopter was observed.
* Each undirected edge occurs once in the file, when it appeared first in the time series.
* Files are indexed by the same codes used in the paper.

## Requirements

The following modules are required to run the codes written in Python:
* Numpy
* Scipy
* Matplotlib
* Pandas
* Seaborn
* Networkx

## Running our measurements

These scripts generate all the statistics that we investigate in Section 4. Jupyter Notebooks introduced below will use the outputs of these measurements.
* To run all measurements, run the `sh/experiment_all.sh`
   * For `$DATA_FOLDER` please set the folder where you downloaded the network files
   * For `$STATS_FOLDER` please set an output folder where each measurement will be generated
* A short explanation of the executed scripts:
   * `experiment_random_shuffle.sh` creates randomly shuffled time series that we compare to the original network timelines
   * `experiment_degree_distribution_stats.sh` computes the degree distribution at different sizes for each network
   * `experiment_network_events.sh` computes the fraction of R,I,H events as the networks grow
   * `experiment_exponent_stats.sh` computes the degree distribution parameter estimates as the networks grow

##Measurements covered by Jupyter Notebooks

The following notebooks cover our measurements explained in Section 4 of our paper. Please modify the input folder that should be the output of the previously detailed scripts in each Jupyter notebook.

* [Average degree](https://github.com/rpalovics/networkgrowth/blob/master/notebooks/es_avgdeg.ipynb)
* [Evolving power-law degree distributions](https://github.com/rpalovics/networkgrowth/blob/master/notebooks/es_dist.ipynb)
* [Average degree and the exponent of the power-law degree distribution](https://github.com/rpalovics/networkgrowth/blob/master/notebooks/es_degdist.ipynb)
* [Microscopic view](https://github.com/rpalovics/networkgrowth/blob/master/notebooks/es_micro.ipynb)
* [No Fit to Uniform Edge Sampling](https://github.com/rpalovics/networkgrowth/blob/master/notebooks/es_random.ipynb)

##Exponential Model

* The C++ code can be found [here](https://github.com/rpalovics/networkgrowth/tree/master/cpp).
* An example script for running the model is [here](https://github.com/rpalovics/networkgrowth/blob/master/sh/experiment_exponential_model_example.sh).
