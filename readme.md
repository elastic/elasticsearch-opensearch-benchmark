
# Elasticsearch vs OpenSearch

## 1 - Provisioning the infrastructure

Use [this terraform script](./terraform/main.tf) to provision a Kubernetes cluster with:
- 1 Node pool for Elasticsearch with 6 `e2-standard-32` machines (128GB RAM and 32 CPUs)
- 1 Node pool for OpenSearch with 6 `e2-standard-32` machines (128GB RAM and 32 CPUs)
- 1 Node pool for Rally with 2 `t2a-standard-16` machines (64GB RAM and 16 CPUs)


## Creating Elasticsearch and Opensearch clusters

### Install ECK

```bash
kubectl create -f https://download.elastic.co/downloads/eck/2.6.1/crds.yaml
kubectl apply -f https://download.elastic.co/downloads/eck/2.6.1/operator.yaml
```

Deploy the Elasticsearch Kubernetes Manifest [here](./k8s/elasticsearch-cluster.yml)

```bash
kubectl apply -f k8s/elasticsearch-cluster.yml
```

Get the elastic username and password with:

```c
kubectl get secret es-cluster-es-elastic-user -o "jsonpath={.data.elastic}" | base64 -d; echo
```

Open up the Kibana port and access it under http://localhost:5601

```c
 kubectl port-forward service/es-cluster-kb-http 9243:5601
```



#### Configure and create the datastream

ILM Policy
```js
PUT _ilm/policy/logs-benchmark-policy
{
  "policy": {
      "phases": {
        "hot": {
          "min_age": "0ms",
          "actions": {
            "rollover": {
              "max_primary_shard_size": "25gb"
            }
          }
        },
        "warm": {
          "min_age": "0d",
          "actions": {
            "allocate": {
              "number_of_replicas": 1
            },
            "forcemerge": {
              "max_num_segments": 1
            },
            "readonly": {},
            "set_priority": {
              "priority": 50
            }
          }
        }
      }
    }
}

```

Index Template

```js

PUT _index_template/logs-benchmark
{
  "index_patterns": [
    "logs-benchmark-*"
  ],
  "priority": 500,
  "data_stream": {},
  "template": {
    "settings": {
      "index": {
        "lifecycle": {
          "name": "logs-benchmark-policy"
        },
        "codec": "best_compression",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "query": {
          "default_field": [
            "message"
          ]
        },
        "number_of_replicas": "1"
      }
    },
    "mappings": {
      "dynamic_templates": [
        {
          "match_ip": {
            "match": "ip",
            "match_mapping_type": "string",
            "mapping": {
              "type": "ip"
            }
          }
        },
        {
          "match_message": {
            "match": "message",
            "match_mapping_type": "string",
            "mapping": {
              "type": "match_only_text"
            }
          }
        },
        {
          "strings_as_keyword": {
            "match_mapping_type": "string",
            "mapping": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        }
      ],
      "date_detection": false,
      "properties": {
        "@timestamp": {
          "type": "date"
        },
        "agent": {
          "properties": {
            "ephemeral_id": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "id": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "name": {
              "type": "keyword",
              "time_series_dimension": true
            },
            "type": {
              "type": "keyword",
              "time_series_dimension": true
            },
            "version": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "aws": {
          "properties": {
            "cloudwatch": {
              "properties": {
                "ingestion_time": {
                  "type": "keyword",
                  "ignore_above": 1024
                },
                "log_group": {
                  "type": "keyword",
                  "time_series_dimension": true
                },
                "log_stream": {
                  "type": "keyword",
                  "time_series_dimension": true
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
              "type": "keyword",
              "time_series_dimension": true
            }
          }
        },
        "ecs": {
          "properties": {
            "version": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "event": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "id": {
              "type": "keyword",
              "time_series_dimension": true
            },
            "ingested": {
              "type": "date"
            }
          }
        },
        "host": {
          "type": "object"
        },
        "input": {
          "properties": {
            "type": {
              "type": "keyword",
              "time_series_dimension": true
            }
          }
        },
        "log": {
          "properties": {
            "file": {
              "properties": {
                "path": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "message": {
          "type": "match_only_text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "time_series_dimension": true
            }
          }
        },
        "metrics": {
          "properties": {
            "size": {
              "type": "long",
              "time_series_metric": "gauge"
            },
            "tmin": {
              "type": "long",
              "time_series_metric": "gauge"
            }
          }
        },
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "time_series_dimension": true
            }
          }
        },
        "tags": {
          "type": "keyword",
          "ignore_above": 1024
        }
      }
    }
  }
}
```

Create the datastream

```js
PUT _data_stream/logs-benchmark-dev
```

Done!

### Install OpenSearch Kubernetes Operator
```bash
helm repo add opensearch-operator https://opster.github.io/opensearch-k8s-operator/
helm install opensearch-operator opensearch-operator/opensearch-operator
```

Deploy the OpenSearch Kubernetes Manifest [here](./k8s/opensearch-cluster.yml)

```bash
kubectl apply -f k8s/opensearch-cluster.yml
```

Open up the Dashboards port and access it under http://localhost:5601

```c
  kubectl port-forward service/opensearch-dashboards-service 5601:5601
```

Default username in OpenSearch is `admin` with password `admin`

## Configure and create the datastream

```js
DELETE _data_stream/logs-benchmark-dev
DELETE _index_template/logs-benchmark-template

PUT _index_template/logs-benchmark-template
{
  "index_patterns": [
    "logs-benchmark-*"
  ],
  "template": {
    "settings": {
      "index.codec": "best_compression",
      "index.number_of_shards": "1",
      "index.translog.sync_interval": "30s",
      "index.translog.durability": "async",
      "index.number_of_replicas": "1"
    },
    "mappings": {
      "properties": {
        "agent": {
          "type": "object",
          "properties": {
            "name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "id": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "ephemeral_id": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "type": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "version": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "process": {
          "type": "object",
          "properties": {
            "name": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "log": {
          "type": "object",
          "properties": {
            "file": {
              "type": "object",
              "properties": {
                "path": {
                  "ignore_above": 1024,
                  "type": "keyword"
                }
              }
            }
          }
        },
        "message": {
          "type": "text"
        },
        "tags": {
          "ignore_above": 1024,
          "type": "keyword"
        },
        "cloud": {
          "type": "object",
          "properties": {
            "region": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "input": {
          "type": "object",
          "properties": {
            "type": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "@timestamp": {
          "type": "date"
        },
        "ecs": {
          "type": "object",
          "properties": {
            "version": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "meta": {
          "type": "object",
          "properties": {
            "file": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "host": {
          "type": "object"
        },
        "metrics": {
          "type": "object",
          "properties": {
            "size": {
              "type": "long"
            },
            "tmax": {
              "type": "long"
            },
            "tmin": {
              "type": "long"
            }
          }
        },
        "aws": {
          "type": "object",
          "properties": {
            "cloudwatch": {
              "type": "object",
              "properties": {
                "log_group": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "ingestion_time": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "log_stream": {
                  "ignore_above": 1024,
                  "type": "keyword"
                }
              }
            }
          }
        },
        "event": {
          "type": "object",
          "properties": {
            "ingested": {
              "type": "date"
            },
            "id": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "dataset": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        }
      }
    }
  },
  "composed_of": [],
  "priority": "200",
  "data_stream": {
    "timestamp_field": {
      "name": "@timestamp"
    }
  }
}


DELETE _plugins/_ism/policies/logs-benchmark-policy
PUT _plugins/_ism/policies/logs-benchmark-policy
{
  "policy": {
    "policy_id": "logs-benchmark-policy",
    "description": "logs benchmark policy",
    "default_state": "hot",
    "states": [
      {
        "name": "hot",
        "actions": [
          {
            "retry": {
              "count": 3,
              "backoff": "exponential",
              "delay": "1m"
            },
            "rollover": {
              "min_primary_shard_size": "25gb"
            }
          }
        ],
        "transitions": [
          {
            "state_name": "warm"
          }
        ]
      },
      {
        "name": "warm",
        "actions": [
          {
            "retry": {
              "count": 3,
              "backoff": "exponential",
              "delay": "1m"
            },
            "force_merge": {
              "max_num_segments": 1
            }
          }
        ],
        "transitions": [
          
        ]
      }
    ],
    "ism_template": [
      {
        "index_patterns": [
          "logs-benchmark-*"
        ],
        "priority": 200
      }
    ]
  }
}

PUT _data_stream/logs-benchmark-dev
```

## 2 - Generating the dataset

[This script](./dataset/generate.sh) relies on the [elastic integration corpus generator tool](https://github.com/elastic/) to generate 1TB of data split into 1024 files of 1GB each and then upload the files to a Google Cloud Storage bucket.

```bash
# Full path to elastic-integration-corpus-generator-tool binary tool
export GENERATOR=/full/path/to/elastic-integration-corpus-generator-tool-arm
# Where the dataset should be written
export CORPORA_ROOT=/full/path/to/dataset/generated
export CONFIG=config-1.yml
export BUCKET=gs://my-gcp-bucket/2023-01-01/
```

The binaries of the elastic integration corpus generator tool are also provided in the repository for ARM and Intel architectures, in the `dataset/bin` folder.


## 3 - Ingesting the dataset

Now that our data is in a Google Cloud Storage bucket, we will use the `google-cloud-storage` input plugin for Logstash, and we are also going to need the `logstash-output-opensearch` to send data to OpenSearch. Those two plugins dont come installed by default in Logstash, luckly this can be easily fixed with a custom Docker image, for which a [Dockerfile](./logstash-custom/Dockerfile) is provided.

Let's build our custom Logstash image using the Makefile in `logstash-custom/Makefile`, the image is multi-arch so it will work on both ARM and Intel machines, you just need to change the `$TAG` variable to match your docker username, the makefile will use docker buildx to build the image and push to the repository.

```makefile
TAG := ugosan/logstash-custom:8.8.2-dev

ARM_TAG := $(TAG)-manifest-arm64v8
AMD_TAG := $(TAG)-manifest-amd64

all: build push pull

build:
	@echo "\n::: Building $(ARM_TAG)"
	docker buildx build --push -f Dockerfile --platform linux/arm64/v8 --tag $(ARM_TAG) .
	@echo "\n::: Building $(AMD_TAG)"
	docker buildx build --push -f Dockerfile --platform linux/amd64 --tag $(AMD_TAG) .
	docker manifest create $(TAG) --amend $(ARM_TAG) --amend $(AMD_TAG)
	@echo "\n::: Building done!"

push:
	docker manifest push $(TAG) --purge

pull:
	docker pull $(TAG)
```

Just run `make` in `logstash-custom` and you will be good to go.

Now lets use Logstash to index the data from GCS to Elasticsearch and OpenSearch, for which two Kubernetes manifests are provided: `logstash-es.yml` and `logstash-os.yml`, but before you run them, make sure you included your `credentials.json` from GCP into `logstash-gcp-credentials.yml`.

Get a base64 encoded version of your `credentials.json` and add it to `logstash-gcp-credentials.yml` then apply it:

```
kubectl apply -f logstash-gcp-credentials.yml
```

The Logstash Pods must be allocated to a separate nodepool from Elasticsearch and OpenSearch ones, for which we will be using the `rally-nodes` nodepool we have configured in terraform. We also specify the `image` we have just made and the `GCP_FILE_MATCH_REGEX` to fetch the `*.ndjson.gz` dataset files. 

```yml
apiVersion: v1
kind: Pod
metadata:
  name: logstash-es
spec:
  nodeSelector:
    cloud.google.com/gke-nodepool: rally-nodes
  containers:
  - name: logstash
    image: ugosan/logstash-custom:8.8.2-dev
    imagePullPolicy: Always
    env: 
      - name: GCP_FILE_MATCH_REGEX
        value: "2023-01-03/.*\\.gz"
...
```


Run the Logstash instances and wait (probably a lot) until all the data is indexed:

```
kubectl apply -f logstash-es.yml logstash-os.yml
```

Note you can run multiple logstash instances with different `GCP_FILE_MATCH_REGEX` to speed up the process, don't worry about data being ingested twice because the document id's are unique and both Elasticsearch and OpenSearch will reject "upserts" to the data. The Google Cloud Storage plugin also writes a metadata field to every file it has already ingested (set it in `metadata_key`), also make sure to adjust the `pipeline.batch.size`. All those configurations can be done in the `ConfigMap` at the bottom of `logstash-es.yml` and `logstash-os.yml`

After a while you will have the dataset fully loaded, in our case we have ingested a little bit over 5.5 billion documents that would fall between 1st January 2023 and 7th January 2023, the Rally tracks are also considering the data to exist within this time range.

<kbd><img src="screenshots/2023-07-25-12-04-28.png" width="640"></kbd>

## 4 - Running the benchmarks with Rally

Rally is an open-source tool developed by Elastic for benchmarking and performance testing of Elasticsearch only. However, since OpenSearch is a fork of Elasticsearch and we are not using anything exclusive to Elasticsearch like Runtime Fields (schema-on-read) in our searches, we can safely assume both solutions will work for our set of queries, we just need to bypass the code where the system verification is made.

### Build our custom image

Just like for Logstash, we also have a custom Dockerfile and a Makefile to build the docker image. In the Dockerfile we are just reusing the elastic/rally:2.8.0 image and injecting a modified client library into it (one that does not check if the counterpart is Elasticsearch). We also copy a custom track we are calling "big5" that will run a series of queries against the logs-benchmark-* datastreams.

Change the `$TAG` to match your username and repository, then run `make` inside `rally-custom`

```makefile
TAG := ugosan/rally-custom:2.8.0-dev
ARM_TAG := $(TAG)-manifest-arm64v8
AMD_TAG := $(TAG)-manifest-amd64

all: build push pull

build:
	@echo "\n::: Building $(ARM_TAG)"
	docker buildx build --push -f Dockerfile --platform linux/arm64/v8 --tag $(ARM_TAG) .
	@echo "\n::: Building $(AMD_TAG)"
	docker buildx build --push -f Dockerfile --platform linux/amd64 --tag $(AMD_TAG) .
	docker manifest create $(TAG) --amend $(ARM_TAG) --amend $(AMD_TAG)
	@echo "\n::: Building done!"

push:
	docker manifest push $(TAG) --purge

pull:
	docker pull $(TAG)
```

The `rally-config.yml` contains the `rally.ini` configuration, in which you must change the [reporting] section so the results are shipped to an Elasticsearch cluster (different from the one we are using to actual run the benchmarks, obviously), elastic cloud has a 14 trial you can use.


Apply the configmap first:

```bash
kubectl apply -f k8s/rally-config.yml
````

Then the rally pods:

```bash
 kubectl apply -f rally-big5-es.yml rally-big5-os.yml
```
