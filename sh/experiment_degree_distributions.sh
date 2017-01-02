DATA_FOLDER=$1
OUT_FOLDER=$2
for i in "oc" "mh" "15" "fb" "wi" "db"
do
  python ../python/run_degree_distributions.py ${DATA_FOLDER}/timeline_$i ${OUT_FOLDER} dist_$i &
  python ../python/run_degree_distributions.py ${DATA_FOLDER}/timeline_r_$i ${OUT_FOLDER} dist_r_$i &
done
wait
