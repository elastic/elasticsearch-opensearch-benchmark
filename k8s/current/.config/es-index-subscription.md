# Index stats

```
GET logs-benchmark-dev?include_defaults
```

```json
{
  ".ds-logs-benchmark-dev-2025.09.10-000001": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "verified_read_only": "true",
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.10-000001",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757499909530",
        "priority": "50",
        "number_of_replicas": "1",
        "uuid": "6J3QFIc5TLq_pVj2uHtJpA",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy",
          "indexing_complete": "true"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_warm,data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "parse_origination_date": "false",
          "prefer_ilm": "true",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "rollover_alias": "",
          "origination_date": "-1"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-2025.09.10-000002": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "verified_read_only": "true",
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.10-000002",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757528943774",
        "priority": "50",
        "number_of_replicas": "1",
        "uuid": "_WkR0Vr1S1WXNVDexotQ0A",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy",
          "indexing_complete": "true"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_warm,data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "parse_origination_date": "false",
          "prefer_ilm": "true",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "rollover_alias": "",
          "origination_date": "-1"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-2025.09.11-000003": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "verified_read_only": "true",
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.11-000003",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757557743708",
        "priority": "50",
        "number_of_replicas": "1",
        "uuid": "q8u3CMhyTNaUkv8-d0MLfA",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy",
          "indexing_complete": "true"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_warm,data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "parse_origination_date": "false",
          "prefer_ilm": "true",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "rollover_alias": "",
          "origination_date": "-1"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-2025.09.11-000004": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "verified_read_only": "true",
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.11-000004",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757586543604",
        "priority": "50",
        "number_of_replicas": "1",
        "uuid": "RYXc4_LbR7ytmKoSeQie_A",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy",
          "indexing_complete": "true"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_warm,data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "parse_origination_date": "false",
          "prefer_ilm": "true",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "rollover_alias": "",
          "origination_date": "-1"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-2025.09.11-000005": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "verified_read_only": "true",
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.11-000005",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757615943568",
        "priority": "50",
        "number_of_replicas": "1",
        "uuid": "e5nx78ioToqCKyf-zOoJsQ",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy",
          "indexing_complete": "true"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_warm,data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "parse_origination_date": "false",
          "prefer_ilm": "true",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "rollover_alias": "",
          "origination_date": "-1"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-2025.09.12-000006": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "verified_read_only": "true",
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.12-000006",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757645343643",
        "priority": "50",
        "number_of_replicas": "1",
        "uuid": "fPbRYudjRbWzqgAEh_dDLw",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy",
          "indexing_complete": "true"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_warm,data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "parse_origination_date": "false",
          "prefer_ilm": "true",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "rollover_alias": "",
          "origination_date": "-1"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-2025.09.12-000007": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
          "type": "date",
          "ignore_malformed": false
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
        "data_stream": {
          "properties": {
            "dataset": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "namespace": {
              "type": "keyword",
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
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
    },
    "settings": {
      "index": {
        "hidden": "true",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "provided_name": ".ds-logs-benchmark-dev-2025.09.12-000007",
        "query": {
          "default_field": ["message"]
        },
        "creation_date": "1757674143650",
        "number_of_replicas": "1",
        "uuid": "NAZMUgtYQf-tBWwHriJnkQ",
        "version": {
          "created": "9033000"
        },
        "lifecycle": {
          "name": "logs-benchmark-policy"
        },
        "mode": "logsdb",
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_hot"
            }
          }
        },
        "number_of_shards": "1",
        "logsdb": {
          "add_host_name_field": "true",
          "sort_on_host_name": "true"
        }
      }
    },
    "defaults": {
      "index": {
        "flush_after_merge": "512mb",
        "time_series": {
          "end_time": "9999-12-31T23:59:59.999Z",
          "start_time": "-9999-01-01T00:00:00Z",
          "es87tsdb_codec": {
            "enabled": "true"
          }
        },
        "final_pipeline": "_none",
        "max_inner_result_window": "100",
        "unassigned": {
          "node_left": {
            "delayed_timeout": "1m"
          }
        },
        "max_terms_count": "65536",
        "rollup": {
          "source": {
            "name": "",
            "uuid": ""
          }
        },
        "lifecycle": {
          "prefer_ilm": "true",
          "rollover_alias": "",
          "origination_date": "-1",
          "parse_origination_date": "false",
          "skip": "false",
          "step": {
            "wait_time_threshold": "12h"
          },
          "indexing_complete": "false"
        },
        "routing_partition_size": "1",
        "force_memory_term_dictionary": "false",
        "max_docvalue_fields_search": "100",
        "merge": {
          "scheduler": {
            "max_thread_count": "1",
            "auto_throttle": "true",
            "max_merge_count": "6"
          },
          "policy": {
            "merge_factor": "32",
            "floor_segment": "2mb",
            "max_merge_at_once_explicit": "30",
            "max_merge_at_once": "10",
            "max_merged_segment": "0b",
            "expunge_deletes_allowed": "10.0",
            "segments_per_tier": "10.0",
            "type": "UNSET",
            "deletes_pct_allowed": "20.0"
          }
        },
        "max_refresh_listeners": "1000",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "seq_no": {
          "index_options": "DOC_VALUES_ONLY"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "semantic_text": {
            "use_legacy_format": "false"
          },
          "field_name_length": {
            "limit": "9223372036854775807"
          },
          "total_fields": {
            "limit": "1000",
            "ignore_dynamic_beyond_limit": "true"
          },
          "ignore_above": "8191",
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "true",
          "source": {
            "mode": "SYNTHETIC"
          },
          "synthetic_source": {
            "skip_ignored_source_read": "false",
            "skip_ignored_source_write": "false"
          },
          "nested_fields": {
            "limit": "50"
          },
          "synthetic_source_keep": "arrays",
          "depth": {
            "limit": "20"
          },
          "dimension_fields": {
            "limit": "32768"
          }
        },
        "source_only": "false",
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "max_script_fields": "32",
        "query": {
          "parse": {
            "allow_unmapped_fields": "true"
          }
        },
        "format": "0",
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "routing_path": [],
        "version": {
          "compatibility": "9033000"
        },
        "dense_vector": {
          "hnsw_filter_heuristic": "ACORN"
        },
        "codec": "best_compression",
        "max_rescore_window": "10000",
        "bloom_filter_for_id_field": {
          "enabled": "true"
        },
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "gc_deletes": "60s",
        "top_metrics_max_size": "10",
        "failure_store": {
          "version": "0"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "translog": {
          "flush_threshold_age": "1m",
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "10gb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "fast_refresh": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": "",
          "use_synthetic_source": "true"
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "highlight": {
          "max_analyzed_offset": "1000000",
          "weight_matches_mode": {
            "enabled": "true"
          }
        },
        "look_back_time": "2h",
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "disk": {
              "watermark": {
                "ignore": "false"
              }
            },
            "enable": "all",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "level": "TRACE",
            "threshold": {
              "fetch": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              },
              "query": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            }
          },
          "idle": {
            "after": "30s"
          }
        },
        "fielddata": {
          "cache": "node"
        },
        "look_ahead_time": "30m",
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "xpack": {
          "watcher": {
            "template": {
              "version": ""
            }
          },
          "version": "",
          "ccr": {
            "following_index": "false"
          }
        },
        "percolator": {
          "map_unmapped_fields_as_text": "false"
        },
        "verified_read_only": "false",
        "allocation": {
          "max_retries": "5",
          "existing_shards_allocator": "gateway_allocator"
        },
        "refresh_interval": "1s",
        "indexing": {
          "slowlog": {
            "include": {
              "user": "false"
            },
            "reformat": "true",
            "threshold": {
              "index": {
                "warn": "-1",
                "trace": "-1",
                "debug": "-1",
                "info": "-1"
              }
            },
            "source": "1000",
            "level": "TRACE"
          }
        },
        "compound_format": "1gb",
        "blocks": {
          "metadata": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false",
          "write": "false"
        },
        "esql": {
          "stored_fields_sequential_proportion": "0.2"
        },
        "max_result_window": "10000",
        "store": {
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": [],
          "snapshot": {
            "snapshot_name": "",
            "index_uuid": "",
            "cache": {
              "prewarm": {
                "enabled": "true"
              },
              "enabled": "true",
              "excluded_file_types": []
            },
            "repository_uuid": "",
            "uncached_chunk_size": "-1b",
            "delete_searchable_snapshot": "false",
            "index_name": "",
            "partial": "false",
            "blob_cache": {
              "metadata_files": {
                "max_length": "64kb"
              }
            },
            "repository_name": "",
            "snapshot_uuid": ""
          }
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "shard_limit": {
          "group": "normal"
        },
        "warmer": {
          "enabled": "true"
        },
        "downsample": {
          "interval": "",
          "source": {
            "name": "",
            "uuid": ""
          },
          "origin": {
            "name": "",
            "uuid": ""
          },
          "status": "unknown"
        },
        "logsdb": {
          "route_on_sort_fields": "false"
        },
        "override_write_load_forecast": "0.0",
        "max_shingle_diff": "3",
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  }
}
```
