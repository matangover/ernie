wget ftp://gtfs.mot.gov.il/israel-public-transportation.zip -O /tmp/gtfs.zip
gtfs2db append /tmp/gtfs.zip "$DATABASE_URL"
