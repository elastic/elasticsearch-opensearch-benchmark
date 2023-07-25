## Create the `logs-benchmark-policy` ISM Policy


```
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

```

## Create the `logs-benchmark-template` Index Template

```js
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
```


## Create the datastream

```js
PUT _data_stream/logs-benchmark-dev
```

Done!

