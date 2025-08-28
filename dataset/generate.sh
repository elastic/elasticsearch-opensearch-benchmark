#!/bin/bash

# Full path to elastic-integration-corpus-generator-tool binary tool
export GENERATOR=/Users/sachin/Source/big5-benchmarking/dataset/bin/elastic-integration-corpus-generator-tool-arm
# Where the dataset should be written
export DATASET=/Users/sachin/Source/big5-benchmarking/dataset
export CORPORA_ROOT=/Users/sachin/Source/big5-benchmarking/dataset/generated
export CORPORA=/Users/sachin/Source/big5-benchmarking/dataset/generated/corpora
export CONFIG=config-1.yml
export BUCKET=gs://big5-benchmarking/2025-08-06/

mkdir $CORPORA_ROOT

# 1GB = 1070741824 bytes

for i in {1..1024}
do
    echo "Generating file #$i"
    $GENERATOR generate-with-template template.tpl fields.yml -t 1070741824 -c "${CONFIG}" -y gotext

    for FILE in $CORPORA/*.tpl
    do

      echo "Gzipping ${FILE/-template.tpl/.ndjson}"
      mv "${FILE}" "${FILE/-template.tpl/.ndjson}"
      gzip "${FILE/-template.tpl/.ndjson}"

      echo "Copying to ${BUCKET}"
      gsutil cp "${FILE/-template.tpl/.ndjson}.gz" "${BUCKET}"

      echo "Removing ${FILE/-template.tpl/.ndjson}.gz"
      rm "${FILE/-template.tpl/.ndjson}.gz"
    done

done