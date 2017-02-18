#!/bin/bash
# This script votes for id 77 at the given url using curl.
for i in {0..1024}
do
    curl "http://54.221.6.249/level0.php" -X POST -d "id=77&holdthedoor=submit" > /dev/null 2>&1
done
