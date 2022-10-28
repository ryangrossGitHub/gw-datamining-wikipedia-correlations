#!/bin/bash
aws s3 cp s3://ryangrossgwudatamining/Relation_Extraction_Worker.zip .
unzip Relation_Extraction_Worker.zip
cd Relation_Extraction_Worker
nohup sh run.sh &