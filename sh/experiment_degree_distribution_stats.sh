STATS_FOLDER=$1
PREFIX="$STATS_FOLDER/dist"

for j in "oc" "mh" "15" "fb" "wi" "db"
do
rm "${PREFIX}_stats_${j}"
rm "${PREFIX}_stats_r_${j}"
for i in $(seq 1 20)
do
  python ../python/run_degree_distribution_stats.py "${PREFIX}_${j}" "${i}" "," "${PREFIX}_stats_${j}"  0 1 2
  python ../python/run_degree_distribution_stats.py "${PREFIX}_r_${j}" "${i}" "," "${PREFIX}_stats_r_${j}"  0 1 2
done
done
