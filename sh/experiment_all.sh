DATA_FOLDER="/home/rpalovics/networkgrowth/data"
STATS_FOLDER="home/rpalovics/networkgrowth/data/stats"
bash experiment_random_shuffle.sh $DATA_FOLDER
bash experiment_degree_distribution_evolution.sh $DATA_FOLDER $STATS_FOLDER
bash experiment_exponent_stats.sh $STATS_FOLDER
bash experiment_network_events.sh $DATA_FOLDER $STATS_FOLDER
