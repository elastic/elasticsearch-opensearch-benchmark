
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


## 3 - Ingesting the dataset


## 4 - Running the benchmark with Rally


Apply the configmap first:

```bash
kubectl apply -f k8s/rally-config.yml
````

Then the rally pods:

```bash
 kubectl apply -f rally-big5-es.yml rally-big5-os.yml
```
