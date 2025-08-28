# Index stats

```
GET logs-benchmark-dev?include_defaults
```

```json
{
  ".ds-logs-benchmark-dev-000001": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000001",
        "creation_date": "1755181979499",
        "number_of_replicas": "1",
        "uuid": "LP5wRza6TMOdXhq5TKHsjQ",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000002": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000002",
        "creation_date": "1755208226530",
        "number_of_replicas": "1",
        "uuid": "kj47HFzdRLuzR4XX_BG1fw",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000003": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000003",
        "creation_date": "1755234376798",
        "number_of_replicas": "1",
        "uuid": "ImHhOhl7QdaESbigMWq9Fg",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000004": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000004",
        "creation_date": "1755260519045",
        "number_of_replicas": "1",
        "uuid": "I2ecRTtwQdWc5CiL9KdhsA",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000005": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000005",
        "creation_date": "1755286712793",
        "number_of_replicas": "1",
        "uuid": "PP1CPNk5RXOPFLYwBk5Mxw",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000006": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000006",
        "creation_date": "1755313144893",
        "number_of_replicas": "1",
        "uuid": "kj7jT2IdTWG-QYTbNvNXTQ",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000007": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000007",
        "creation_date": "1755339656126",
        "number_of_replicas": "1",
        "uuid": "zLSMDN_BTS672hAwfRyh2A",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000008": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000008",
        "creation_date": "1755366184160",
        "number_of_replicas": "1",
        "uuid": "kEl5TQUpR1-6QLYP9N6vcw",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000009": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "blocks": {
          "write": "true"
        },
        "provided_name": ".ds-logs-benchmark-dev-000009",
        "creation_date": "1755392688387",
        "number_of_replicas": "1",
        "uuid": "4fBLQWP3S2O8Ax3tvHQGGg",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  },
  ".ds-logs-benchmark-dev-000010": {
    "aliases": {},
    "mappings": {
      "_data_stream_timestamp": {
        "enabled": true
      },
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
              "ignore_above": 1024
            },
            "type": {
              "type": "keyword",
              "ignore_above": 1024
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
                  "ignore_above": 1024
                },
                "log_stream": {
                  "type": "keyword",
                  "ignore_above": 1024
                }
              }
            }
          }
        },
        "cloud": {
          "properties": {
            "region": {
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
              "ignore_above": 1024
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
              "ignore_above": 1024
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
          "type": "text"
        },
        "meta": {
          "properties": {
            "file": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        },
        "metrics": {
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
        "process": {
          "properties": {
            "name": {
              "type": "keyword",
              "ignore_above": 1024
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
        "replication": {
          "type": "DOCUMENT"
        },
        "codec": "best_compression",
        "hidden": "true",
        "number_of_shards": "1",
        "translog": {
          "sync_interval": "30s",
          "durability": "async"
        },
        "provided_name": ".ds-logs-benchmark-dev-000010",
        "creation_date": "1755419250255",
        "number_of_replicas": "1",
        "uuid": "CbWAste9SZuPpBrBw3KGtw",
        "version": {
          "created": "137227827"
        }
      }
    },
    "defaults": {
      "index": {
        "composite_index.star_tree": {
          "field": {
            "default": {
              "date_intervals": ["minute", "half-hour"],
              "metrics": ["VALUE_COUNT", "SUM"]
            },
            "max_dimensions": "10",
            "max_base_metrics": "100",
            "max_date_intervals": "3"
          },
          "max_fields": "1",
          "default": {
            "max_leaf_docs": "10000"
          }
        },
        "opendistro": {
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
          }
        },
        "flush_after_merge": "512mb",
        "knn.remote_index_build": {
          "size": {
            "min": "52428800b"
          },
          "enabled": "true"
        },
        "knn.algo_param": {
          "ef_search": "100"
        },
        "auto_expand_search_replicas": "false",
        "plugins": {
          "replication": {
            "translog": {
              "retention_size": "536870912b",
              "retention_lease": {
                "pruning": {
                  "enabled": "false"
                }
              }
            },
            "follower": {
              "leader_index": ""
            }
          },
          "rollup_index": "false",
          "index_state_management": {
            "rollover_skip": "false",
            "auto_manage": "true",
            "policy_id": "",
            "rollover_alias": ""
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
        "ingestion_source": {
          "internal_queue_size": "100",
          "num_processor_threads": "1",
          "pointer": {
            "init": {
              "reset": "LATEST",
              "reset.value": ""
            }
          },
          "poll": {
            "max_batch_size": "1000",
            "timeout": "1000"
          },
          "type": "none",
          "error_strategy": "DROP"
        },
        "routing_partition_size": "1",
        "unreferenced_file_cleanup": {
          "enabled": "true"
        },
        "force_memory_term_dictionary": "false",
        "use_compound_file": "true",
        "max_docvalue_fields_search": "100",
        "merge": {
          "policy.max_merged_segment": "5368709120b",
          "scheduler": {
            "max_thread_count": "4",
            "auto_throttle": "true",
            "max_merge_count": "9"
          },
          "policy.max_merge_at_once": "30",
          "policy.expunge_deletes_allowed": "10.0",
          "policy.reclaim_deletes_weight": "2.0",
          "policy.floor_segment": "16777216b",
          "log_byte_size_policy": {
            "max_merge_segment": "5368709120b",
            "max_merge_segment_forced_merge": "9223372036854775807b",
            "merge_factor": "10",
            "min_merge": "16777216b",
            "no_cfs_ratio": "0.1",
            "max_merged_docs": "2147483647"
          },
          "policy.segments_per_tier": "10.0",
          "policy.deletes_pct_allowed": "20.0",
          "policy": "default"
        },
        "context": {
          "created_version": "0",
          "current_version": "0"
        },
        "number_of_search_replicas": "0",
        "max_refresh_listeners": "1000",
        "knn.memory_optimized_search": "false",
        "max_regex_length": "1000",
        "load_fixed_bitset_filters_eagerly": "true",
        "number_of_routing_shards": "1",
        "write": {
          "wait_for_active_shards": "1"
        },
        "append_only": {
          "enabled": "false"
        },
        "verified_before_close": "false",
        "mapping": {
          "coerce": "false",
          "nested_fields": {
            "limit": "50"
          },
          "depth": {
            "limit": "20"
          },
          "field_name_length": {
            "limit": "50000"
          },
          "total_fields": {
            "limit": "1000"
          },
          "nested_objects": {
            "limit": "10000"
          },
          "ignore_malformed": "false"
        },
        "soft_deletes": {
          "enabled": "true",
          "retention": {
            "operations": "0"
          },
          "retention_lease": {
            "period": "12h"
          }
        },
        "ltrstore_version": "2",
        "max_script_fields": "32",
        "query": {
          "max_nested_depth": "20",
          "parse": {
            "allow_unmapped_fields": "true"
          },
          "default_field": ["*"],
          "derived_field": {
            "enabled": "true"
          }
        },
        "format": "0",
        "history": {
          "uuid": "_na_"
        },
        "sort": {
          "missing": [],
          "mode": [],
          "field": [],
          "order": []
        },
        "priority": "1",
        "composite_index": "false",
        "codec": {
          "compression_level": "3",
          "qatmode": "auto"
        },
        "optimize_doc_id_lookup": {
          "fuzzy_set": {
            "enabled": "false",
            "false_positive_probability": "0.2047"
          }
        },
        "check_pending_flush": {
          "enabled": "true"
        },
        "correlation": "false",
        "max_rescore_window": "10000",
        "max_adjacency_matrix_filters": "100",
        "analyze": {
          "max_token_count": "10000"
        },
        "knn.disk": {
          "vector": {
            "shard_level_rescoring_disabled": "false"
          }
        },
        "gc_deletes": "60s",
        "searchable_snapshot": {
          "index": {
            "id": ""
          },
          "shard_path_type": "FIXED",
          "repository": "",
          "snapshot_id": {
            "name": "",
            "uuid": ""
          }
        },
        "auto_force_merge": {
          "enabled": "true"
        },
        "optimize_auto_generated_id": "true",
        "max_ngram_diff": "1",
        "knn.advanced": {
          "approximate_threshold": "0",
          "filtered_exact_search_threshold": "-1"
        },
        "translog": {
          "generation_threshold_size": "64mb",
          "flush_threshold_size": "512mb",
          "retention": {
            "size": "-1",
            "age": "-1"
          }
        },
        "auto_expand_replicas": "false",
        "mapper": {
          "dynamic": "true"
        },
        "recovery": {
          "type": ""
        },
        "requests": {
          "cache": {
            "enable": "true"
          }
        },
        "data_path": "",
        "merge_on_flush": {
          "enabled": "true",
          "max_full_flush_merge_wait_time": "10s",
          "policy": "default"
        },
        "highlight": {
          "max_analyzed_offset": "1000000"
        },
        "routing": {
          "rebalance": {
            "enable": "all"
          },
          "allocation": {
            "enable": "all",
            "total_primary_shards_per_node": "-1",
            "total_shards_per_node": "-1"
          }
        },
        "search": {
          "concurrent_segment_search": {
            "mode": "none",
            "enabled": "false"
          },
          "idle": {
            "after": "30s"
          },
          "concurrent": {
            "max_slice_count": "4"
          },
          "slowlog": {
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
          "default_pipeline": "_none",
          "star_tree_index": {
            "enabled": "true"
          },
          "throttled": "false"
        },
        "fielddata": {
          "cache": "node"
        },
        "default_pipeline": "_none",
        "max_slices_per_scroll": "1024",
        "shard": {
          "check_on_startup": "false"
        },
        "max_slices_per_pit": "1024",
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
        "remote_store": {
          "translog": {
            "buffer_interval": "650ms",
            "repository": "",
            "keep_extra_gen": "100"
          },
          "enabled": "false",
          "segment": {
            "repository": ""
          }
        },
        "compound_format": "0.1",
        "blocks": {
          "metadata": "false",
          "search_only": "false",
          "read": "false",
          "read_only_allow_delete": "false",
          "read_only": "false",
          "write": "false"
        },
        "max_result_window": "10000",
        "knn": "false",
        "store": {
          "hybrid": {
            "nio": {
              "extensions": [
                "segments_N",
                "write.lock",
                "si",
                "cfe",
                "fnm",
                "fdx",
                "fdt",
                "pos",
                "pay",
                "nvm",
                "dvm",
                "tvx",
                "tvd",
                "liv",
                "dii",
                "vem"
              ]
            }
          },
          "stats_refresh_interval": "10s",
          "type": "",
          "fs": {
            "fs_lock": "native"
          },
          "preload": []
        },
        "composite_store": {
          "type": "default"
        },
        "queries": {
          "cache": {
            "enabled": "true"
          }
        },
        "warmer": {
          "enabled": "true"
        },
        "max_shingle_diff": "3",
        "knn.derived_source": {
          "enabled": "false"
        },
        "query_string": {
          "lenient": "false"
        }
      }
    },
    "data_stream": "logs-benchmark-dev"
  }
}
```
