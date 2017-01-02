PREFIX=$1
for i in "oc" "mh" "15" "fb" "wi" "db"
do
  sort -R "${PREFIX}/timeline_${i}" > "${PREFIX}/timeline_r_${i}" &
done
wait
