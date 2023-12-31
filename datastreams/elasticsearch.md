
## Create the `logs-benchmark-policy` ILM Policy

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

## Create the `logs-benchmark` Index Template

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

## Create the datastream

```js
PUT _data_stream/logs-benchmark-dev
```

Done!