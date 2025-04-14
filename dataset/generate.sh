#!/bin/bash

# Full path to elastic-integration-corpus-generator-tool binary tool
export GENERATOR=/full/path/to/elastic-integration-corpus-generator-tool-arm
# Where the dataset should be written
export CORPORA_ROOT=/full/path/to/dataset/generated
export CONFIG=config-1.yml
export BUCKET=gs://<bucket_id>

mkdir $CORPORA_ROOT

# 1GB = 1070741824 bytes

for i in {1..1024}
do
    echo "Generating file #$i"
    $GENERATOR generate-with-template template.tpl fields.yml -t 1070741824 -c "${CONFIG}" -y gotext
    pushd $CORPORA_ROOT/corpora

    for file in *.tpl
    do

      echo "Gzipping ${file/-template.tpl/.ndjson}"
      mv "${file}" "${file/-template.tpl/.ndjson}"
      gzip "${file/-template.tpl/.ndjson}"

      echo "Copying to ${BUCKET}"
      gcloud storage cp "${file/-template.tpl/.ndjson}.gz" "${BUCKET}"

      echo "Removing ${file/-template.tpl/.ndjson}.gz"
      rm "${file/-template.tpl/.ndjson}.gz"
    done

    popd
done