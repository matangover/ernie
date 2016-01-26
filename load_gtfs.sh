wget ftp://gtfs.mot.gov.il/israel-public-transportation.zip -O /tmp/gtfs.zip
unzip -o /tmp/gtfs.zip -d /tmp/gtfs
rm /tmp/gtfs/shapes.txt
mv /tmp/gtfs/stop_times.txt /tmp/gtfs/stop_times.txt.bkp
mv /tmp/gtfs/trips.txt /tmp/gtfs/trips.txt.bkp
python trim_stop_times.py /tmp/gtfs/stop_times.txt.bkp /tmp/gtfs/stop_times.txt
python trim_trips.py /tmp/gtfs/stop_times.txt /tmp/gtfs/trips.txt.bkp /tmp/gtfs/trips.txt
gtfs2db append /tmp/gtfs "$DATABASE_URL"
