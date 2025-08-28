# Cluster settings

```
GET _cluster/settings?include_defaults
```

```json
{
  "persistent": {},
  "transient": {},
  "defaults": {
    "cluster": {
      "max_voting_config_exclusions": "10",
      "no_master_block": "write",
      "persistent_tasks": {
        "allocation": {
          "enable": "all",
          "recheck_interval": "30s"
        }
      },
      "auto_sharding": {
        "min_write_threads": "2",
        "max_write_threads": "32"
      },
      "remote": {
        "initial_connect_timeout": "30s",
        "node": {
          "attr": ""
        },
        "connections_per_cluster": "3"
      },
      "lifecycle": {
        "default": {
          "rollover": "max_age=auto,max_primary_shard_size=50gb,min_docs=1,max_primary_shard_docs=200000000"
        }
      },
      "routing": {
        "use_adaptive_replica_selection": "true",
        "rebalance": {
          "enable": "all"
        },
        "allocation": {
          "enforce_default_tier_preference": "true",
          "node_concurrent_incoming_recoveries": "2",
          "node_initial_primaries_recoveries": "4",
          "desired_balance": {
            "balanace_round_summaries_interval": "10s",
            "enable_balancer_round_summaries": "false",
            "max_balance_computation_time_during_index_creation": "1s",
            "progress_log_interval": "1m",
            "undesired_allocations": {
              "log_interval": "1h",
              "threshold": "0.1"
            }
          },
          "estimated_heap": {
            "threshold_enabled": "false"
          },
          "same_shard": {
            "host": "false"
          },
          "total_shards_per_node": "-1",
          "type": "desired_balance",
          "write_load_decider": {
            "high_utilization_threshold": "90%",
            "queue_latency_threshold": "30s",
            "high_utilization_duration": "10m",
            "shard_write_load_polling_interval": "60s",
            "enabled": "DISABLED",
            "reroute_interval": "60s"
          },
          "disk": {
            "threshold_enabled": "true",
            "reroute_interval": "60s",
            "watermark": {
              "flood_stage.frozen.max_headroom": "20GB",
              "flood_stage": "95%",
              "high": "90%",
              "low": "85%",
              "flood_stage.frozen": "95%",
              "flood_stage.max_headroom": "100GB",
              "low.max_headroom": "200GB",
              "high.max_headroom": "150GB"
            }
          },
          "awareness": {
            "attributes": [
              "k8s_node_name"
            ]
          },
          "balance": {
            "disk_usage": "2.0E-11",
            "index": "0.55",
            "threshold": "1.0",
            "shard": "0.45",
            "write_load": "10.0"
          },
          "stats": {
            "cache": {
              "ttl": "1m"
            }
          },
          "enable": "all",
          "node_concurrent_outgoing_recoveries": "2",
          "allow_rebalance": "always",
          "cluster_concurrent_rebalance": "2",
          "node_concurrent_recoveries": "2"
        }
      },
      "max_shards_per_node.frozen": "3000",
      "deprecation_indexing": {
        "flush_interval": "5s",
        "enabled": "true",
        "x_opaque_id_used": {
          "enabled": "true"
        }
      },
      "info": {
        "update": {
          "interval": "30s",
          "timeout": "15s"
        }
      },
      "auto_shrink_voting_configuration": "true",
      "discovery_configuration_check": {
        "interval": "30000ms"
      },
      "election": {
        "duration": "500ms",
        "initial_timeout": "100ms",
        "max_timeout": "10s",
        "back_off_time": "100ms",
        "strategy": "supports_voting_only"
      },
      "blocks": {
        "read_only_allow_delete": "false",
        "read_only": "false"
      },
      "follower_lag": {
        "timeout": "90000ms"
      },
      "indices": {
        "validate_ignored_dot_patterns": [
          """\.ml-state-\d+""",
          """\.slo-observability\.sli-v\d+.*""",
          """\.slo-observability\.summary-v\d+.*""",
          """\.entities\.v\d+\.latest\..*""",
          """\.monitoring-es-8-.*""",
          """\.monitoring-logstash-8-.*""",
          """\.monitoring-kibana-8-.*""",
          """\.monitoring-beats-8-.*""",
          """\.monitoring-ent-search-8-.*"""
        ],
        "tombstones": {
          "size": "500"
        },
        "validate_dot_prefixes": "true",
        "close": {
          "enable": "true"
        }
      },
      "join_validation": {
        "cache_timeout": "60s"
      },
      "nodes": {
        "reconnect_interval": "10s"
      },
      "logsdb": {
        "enabled": "true"
      },
      "service": {
        "slow_master_task_logging_threshold": "10s",
        "slow_task_logging_threshold": "30s",
        "master_service_starvation_logging_threshold": "5m",
        "slow_task_thread_dump_timeout": "30s"
      },
      "publish": {
        "timeout": "30000ms",
        "info_timeout": "10000ms"
      },
      "name": "es-cluster",
      "fault_detection": {
        "leader_check": {
          "interval": "1000ms",
          "timeout": "10000ms",
          "retry_count": "3"
        },
        "follower_check": {
          "interval": "1000ms",
          "timeout": "10000ms",
          "retry_count": "3"
        }
      },
      "max_shards_per_node": "1000",
      "initial_master_nodes": [
        "es-cluster-es-default-0",
        "es-cluster-es-default-1",
        "es-cluster-es-default-2",
        "es-cluster-es-default-3",
        "es-cluster-es-default-4",
        "es-cluster-es-default-5"
      ],
      "snapshot": {
        "info": {
          "max_concurrent_fetches": "5"
        }
      }
    },
    "stack": {
      "templates": {
        "enabled": "true"
      }
    },
    "time_series": {
      "poll_interval": "5m"
    },
    "logger": {
      "level": "INFO"
    },
    "esql_worker": {
      "queue_size": "1000",
      "size": "23"
    },
    "repository": {
      "azure": {
        "http_client": {
          "connection_max_idle_time": "60s",
          "event_loop_executor_thread_count": "1",
          "connection_timeout": "30s",
          "max_open_connections": "50"
        }
      }
    },
    "health_node": {
      "transport_action_timeout": "5s"
    },
    "ingest": {
      "user_agent": {
        "cache_size": "1000"
      },
      "geoip": {
        "cache_size": "1000",
        "downloader": {
          "endpoint": "https://geoip.elastic.co/v1/database",
          "poll": {
            "interval": "3d"
          },
          "eager": {
            "download": "false"
          },
          "enabled": "true"
        }
      },
      "grok": {
        "watchdog": {
          "max_execution_time": "1s",
          "interval": "1s"
        }
      }
    },
    "path": {
      "data": [
        "/usr/share/elasticsearch/data"
      ],
      "logs": "/usr/share/elasticsearch/logs",
      "shared_data": "",
      "home": "/usr/share/elasticsearch",
      "repo": []
    },
    "ccr": {
      "wait_for_metadata_timeout": "60s",
      "indices": {
        "recovery": {
          "recovery_activity_timeout": "60s",
          "chunk_size": "1mb",
          "internal_action_timeout": "60s",
          "max_bytes_per_sec": "40mb",
          "max_concurrent_file_chunks": "5"
        }
      },
      "auto_follow": {
        "wait_for_metadata_timeout": "60s"
      }
    },
    "remote_cluster": {
      "tcp": {
        "reuse_address": "true",
        "keep_count": "-1",
        "keep_interval": "-1",
        "no_delay": "true",
        "keep_alive": "true",
        "keep_idle": "-1",
        "send_buffer_size": "-1b"
      },
      "bind_host": [],
      "port": "9443",
      "host": [],
      "max_request_header_size": "64kb",
      "publish_port": "-1",
      "publish_host": []
    },
    "repositories": {
      "fs": {
        "chunk_size": "9223372036854775807b",
        "location": ""
      },
      "url": {
        "supported_protocols": [
          "http",
          "https",
          "ftp",
          "file",
          "jar"
        ],
        "allowed_urls": [],
        "url": "http:"
      }
    },
    "action": {
      "auto_create_index": "true",
      "search": {
        "pre_filter_shard_size": {
          "default": "128"
        },
        "shard_count": {
          "limit": "9223372036854775807"
        }
      },
      "destructive_requires_name": "true"
    },
    "enrich": {
      "max_force_merge_attempts": "3",
      "cache": {
        "size": null
      },
      "cache_size": null,
      "cleanup_period": "15m",
      "fetch_size": "10000",
      "coordinator_proxy": {
        "max_concurrent_requests": "8",
        "max_lookups_per_request": "128",
        "queue_capacity": "1024"
      },
      "max_concurrent_policy_executions": "50"
    },
    "repository_s3": {
      "compare_and_exchange": {
        "time_to_live": "15s",
        "anti_contention_delay": "1s"
      }
    },
    "cache": {
      "recycler": {
        "page": {
          "limit": {
            "heap": "10%"
          },
          "type": "CONCURRENT",
          "weight": {
            "longs": "1.0",
            "ints": "1.0",
            "bytes": "1.0",
            "objects": "0.1"
          }
        }
      }
    },
    "reindex": {
      "remote": {
        "whitelist": []
      }
    },
    "resource": {
      "reload": {
        "enabled": "true",
        "interval": {
          "low": "60s",
          "high": "5s",
          "medium": "30s"
        }
      }
    },
    "thread_pool": {
      "force_merge": {
        "queue_size": "-1",
        "size": "1"
      },
      "search_coordination": {
        "queue_size": "1000",
        "size": "8"
      },
      "snapshot_meta": {
        "core": "1",
        "max": "45",
        "keep_alive": "30s"
      },
      "fetch_shard_started": {
        "core": "1",
        "max": "30",
        "keep_alive": "5m"
      },
      "estimated_time_interval.warn_threshold": "5s",
      "scheduler": {
        "warn_threshold": "5s"
      },
      "cluster_coordination": {
        "queue_size": "-1",
        "size": "1"
      },
      "search": {
        "queue_size": "23000",
        "size": "23"
      },
      "write_coordination": {
        "queue_size": "10000",
        "size": "15"
      },
      "fetch_shard_store": {
        "core": "1",
        "max": "30",
        "keep_alive": "5m"
      },
      "flush": {
        "core": "1",
        "max": "5",
        "keep_alive": "5m"
      },
      "get": {
        "queue_size": "1000",
        "size": "23"
      },
      "merge": {
        "core": "1",
        "max": "15",
        "keep_alive": "5m"
      },
      "system_read": {
        "queue_size": "2000",
        "size": "5"
      },
      "system_critical_read": {
        "queue_size": "2000",
        "size": "5"
      },
      "estimated_time_interval": "200ms",
      "write": {
        "queue_size": "10000",
        "size": "15",
        "ewma_alpha": "0.02"
      },
      "search_worker": {
        "queue_size": "0",
        "size": "0"
      },
      "system_critical_write": {
        "queue_size": "1500",
        "size": "5"
      },
      "refresh": {
        "core": "1",
        "max": "8",
        "keep_alive": "5m"
      },
      "repository_azure": {
        "core": "0",
        "max": "5",
        "keep_alive": "30s"
      },
      "system_write": {
        "queue_size": "1000",
        "size": "5"
      },
      "generic": {
        "core": "4",
        "max": "128",
        "keep_alive": "30s"
      },
      "warmer": {
        "core": "1",
        "max": "5",
        "keep_alive": "5m"
      },
      "auto_complete": {
        "queue_size": "100",
        "size": "3"
      },
      "azure_event_loop": {
        "core": "0",
        "max": "1",
        "keep_alive": "30s"
      },
      "profiling": {
        "core": "0",
        "max": "1",
        "keep_alive": "30m"
      },
      "management": {
        "core": "1",
        "max": "5",
        "keep_alive": "5m"
      },
      "analyze": {
        "queue_size": "16",
        "size": "1"
      },
      "snapshot": {
        "core": "1",
        "max": "10",
        "keep_alive": "5m"
      },
      "search_throttled": {
        "queue_size": "0",
        "size": "0"
      }
    },
    "index": {
      "codec": "default",
      "recovery": {
        "type": ""
      },
      "store": {
        "type": "",
        "fs": {
          "fs_lock": "native"
        },
        "preload": [],
        "snapshot": {
          "uncached_chunk_size": "-1b",
          "cache": {
            "excluded_file_types": []
          }
        }
      }
    },
    "runtime_fields": {
      "grok": {
        "watchdog": {
          "max_execution_time": "1s",
          "interval": "1s"
        }
      }
    },
    "cluster_state": {
      "document_page_size": "1mb"
    },
    "deprecation": {
      "skip_deprecated_settings": []
    },
    "script": {
      "allowed_contexts": [],
      "max_compilations_rate": "150/5m",
      "cache": {
        "max_size": "3000",
        "expire": "0ms"
      },
      "painless": {
        "regex": {
          "enabled": "limited",
          "limit-factor": "6"
        }
      },
      "max_size_in_bytes": "65535",
      "allowed_types": [],
      "disable_max_compilations_rate": "false"
    },
    "indexing_pressure": {
      "memory": {
        "coordinating": {
          "limit": "10%"
        },
        "split_bulk": {
          "watermark": {
            "high": "7.5%",
            "high.bulk_size": "1mb",
            "low": "5.0%",
            "low.bulk_size": "4mb"
          }
        },
        "replica": {
          "limit": "4509715660b"
        },
        "limit": "10%",
        "max_operation_size": "10%",
        "split_bulk_threshold": "8.5%",
        "primary": {
          "limit": "10%"
        }
      }
    },
    "node": {
      "bandwidth": {
        "recovery": {
          "disk": {
            "write": "-1",
            "read": "-1"
          },
          "factor": {
            "write": "0.4",
            "read": "0.4"
          },
          "operator": {
            "factor.read": "0.4",
            "factor.write": "0.4",
            "factor": "0.4",
            "factor.max_overcommit": "100.0"
          },
          "network": "-1"
        }
      },
      "roles": [
        "data",
        "data_cold",
        "data_content",
        "data_frozen",
        "data_hot",
        "data_warm",
        "ingest",
        "master",
        "ml",
        "remote_cluster_client",
        "transform"
      ],
      "external_id": "es-cluster-es-default-5",
      "maximum_reindexing_grace_period": "10s",
      "maximum_shutdown_grace_period": "0ms",
      "processors": "15.0",
      "store": {
        "allow_mmap": "true"
      },
      "enable_lucene_segment_infos_trace": "false",
      "_internal": {
        "default_refresh_interval": "1s"
      },
      "name": "es-cluster-es-default-5",
      "id": {
        "seed": "0"
      },
      "attr": {
        "k8s_node_name": "gke-es-benchmarks-bi-elasticsearch-no-9b454d14-q72s",
        "transform": {
          "config_version": "10.0.0"
        },
        "xpack": {
          "installed": "true"
        },
        "ml": {
          "max_jvm_size": "30064771072",
          "allocated_processors": "15",
          "machine_memory": "60129542144",
          "config_version": "12.0.0",
          "allocated_processors_double": "15.0"
        }
      },
      "portsfile": "false"
    },
    "slm": {
      "health": {
        "failed_snapshot_warn_threshold": "5"
      },
      "minimum_interval": "15m",
      "retention_schedule": "0 30 1 * * ?",
      "retention_duration": "1h",
      "history_index_enabled": "true"
    },
    "http": {
      "cors": {
        "max-age": "1728000",
        "allow-origin": "",
        "allow-headers": "X-Requested-With,Content-Type,Content-Length,Authorization,Accept,User-Agent,X-Elastic-Client-Meta",
        "allow-credentials": "false",
        "allow-methods": "OPTIONS,HEAD,GET,POST,PUT,DELETE",
        "enabled": "false"
      },
      "max_chunk_size": "8kb",
      "compression_level": "3",
      "max_initial_line_length": "4kb",
      "shutdown_grace_period": "0ms",
      "type": "security4",
      "pipelining": {
        "max_events": "10000"
      },
      "shutdown_poll_period": "5m",
      "type.default": "netty4",
      "host": [],
      "publish_port": "-1",
      "read_timeout": "0ms",
      "max_content_length": "100mb",
      "netty": {
        "receive_predictor_size": "64kb",
        "max_composite_buffer_components": "69905",
        "worker_count": "0"
      },
      "tcp": {
        "reuse_address": "true",
        "keep_count": "-1",
        "keep_interval": "-1",
        "no_delay": "true",
        "keep_alive": "true",
        "receive_buffer_size": "-1b",
        "keep_idle": "-1",
        "send_buffer_size": "-1b"
      },
      "bind_host": [],
      "client_stats": {
        "enabled": "true",
        "closed_channels": {
          "max_age": "5m",
          "max_count": "10000"
        }
      },
      "reset_cookies": "false",
      "max_warning_header_count": "-1",
      "tracer": {
        "include": [],
        "exclude": []
      },
      "max_warning_header_size": "-1b",
      "detailed_errors": {
        "enabled": "true"
      },
      "port": "9200-9300",
      "max_header_size": "16kb",
      "compression": "false",
      "publish_host": [
        "es-cluster-es-default-5.es-cluster-es-default.default.svc"
      ]
    },
    "telemetry": {
      "tracing": {
        "sanitize_field_names": [
          "password",
          "passwd",
          "pwd",
          "secret",
          "*key",
          "*token*",
          "*session*",
          "*credit*",
          "*card*",
          "*auth*",
          "*principal*",
          "set-cookie"
        ],
        "enabled": "false",
        "names": {
          "include": [],
          "exclude": []
        }
      },
      "metrics": {
        "enabled": "false"
      }
    },
    "snapshot": {
      "refresh_repo_uuid_on_restore": "true",
      "max_concurrent_operations": "1000"
    },
    "migrate": {
      "max_concurrent_indices_reindexed_per_data_stream": "1",
      "data_stream_reindex_max_request_per_second": "1000.0"
    },
    "readiness": {
      "port": "8080"
    },
    "bootstrap": {
      "memory_lock": "false",
      "ctrlhandler": "true"
    },
    "mustache": {
      "max_output_size_bytes": "1mb"
    },
    "network": {
      "tcp": {
        "reuse_address": "true",
        "keep_count": "-1",
        "keep_interval": "-1",
        "no_delay": "true",
        "keep_alive": "true",
        "receive_buffer_size": "-1b",
        "keep_idle": "-1",
        "send_buffer_size": "-1b"
      },
      "bind_host": [
        "0"
      ],
      "server": "true",
      "breaker": {
        "inflight_requests": {
          "limit": "100%",
          "overhead": "2.0"
        }
      },
      "host": [
        "0"
      ],
      "thread": {
        "watchdog": {
          "quiet_time": "10m",
          "interval": "5s"
        }
      },
      "publish_host": [
        "10.36.1.4"
      ]
    },
    "searchable_snapshots": {
      "blob_cache": {
        "periodic_cleanup": {
          "interval": "1h",
          "batch_size": "100",
          "pit_keep_alive": "10m",
          "retention_period": "1h"
        }
      }
    },
    "search": {
      "default_search_timeout": "-1",
      "online_prewarming_threshold_poolsize_factor": "10",
      "query_phase_parallel_collection_enabled": "true",
      "max_open_scroll_context": "500",
      "max_buckets": "65536",
      "max_async_search_response_size": "10mb",
      "worker_threads_enabled": "true",
      "batched_query_phase": "true",
      "keep_alive_interval": "1m",
      "max_keep_alive": "24h",
      "memory_accounting_buffer_size": "1mb",
      "highlight": {
        "term_vector_multi_value": "true"
      },
      "ccs": {
        "collect_telemetry": "true"
      },
      "default_allow_partial_results": "true",
      "low_level_cancellation": "true",
      "allow_expensive_queries": "true",
      "check_ccs_compatibility": "false",
      "default_keep_alive": "5m",
      "aggs": {
        "only_allowed_metric_scripts": "false",
        "allowed_inline_metric_scripts": [],
        "rewrite_to_filter_by_filter": "true",
        "tdigest_execution_hint": "DEFAULT",
        "allowed_stored_metric_scripts": []
      }
    },
    "security": {
      "manager": {
        "filter_bad_defaults": "true"
      }
    },
    "xpack": {
      "watcher": {
        "execution": {
          "scroll": {
            "size": "0",
            "timeout": ""
          },
          "default_throttle_period": "5s"
        },
        "internal": {
          "ops": {
            "bulk": {
              "default_timeout": ""
            },
            "index": {
              "default_timeout": ""
            },
            "search": {
              "default_timeout": ""
            }
          }
        },
        "max": {
          "history": {
            "record": {
              "size": "10mb"
            }
          }
        },
        "thread_pool": {
          "queue_size": "1000",
          "size": "50"
        },
        "index": {
          "rest": {
            "direct_access": ""
          }
        },
        "use_ilm_index_management": "true",
        "trigger": {
          "schedule": {
            "ticker": {
              "tick_interval": "500ms"
            }
          }
        },
        "enabled": "true",
        "input": {
          "search": {
            "default_timeout": ""
          }
        },
        "encrypt_sensitive_data": "false",
        "transform": {
          "search": {
            "default_timeout": ""
          }
        },
        "stop": {
          "timeout": "30s"
        },
        "watch": {
          "scroll": {
            "size": "0"
          }
        },
        "bulk": {
          "concurrent_requests": "0",
          "flush_interval": "1s",
          "size": "1mb",
          "actions": "1"
        },
        "actions": {
          "bulk": {
            "default_timeout": ""
          },
          "index": {
            "default_timeout": ""
          }
        }
      },
      "eql": {
        "default_allow_partial_sequence_results": "false",
        "enabled": "true",
        "default_allow_partial_results": "true"
      },
      "mapping": {
        "synthetic_source_fallback_to_stored_source": "false"
      },
      "otel_data": {
        "registry": {
          "enabled": "true"
        }
      },
      "inference": {
        "utility_thread_pool": {
          "core": "0",
          "max": "10",
          "keep_alive": "10m"
        },
        "truncator": {
          "reduction_percentage": "0.5"
        },
        "elastic": {
          "authorization_request_interval": "10m",
          "http": {
            "connection_ttl": "60s",
            "ssl": {
              "enabled": "true"
            }
          },
          "periodic_authorization_enabled": "true",
          "url": "",
          "max_authorization_request_jitter": "5m"
        },
        "http": {
          "max_total_connections": "50",
          "request_executor": {
            "task_poll_frequency": "50ms",
            "rate_limit_group_cleanup_interval": "1d",
            "rate_limit_group_stale_duration": "10d",
            "queue_capacity": "2000"
          },
          "max_route_connections": "20",
          "connect_timeout": "5s",
          "max_response_size": "50mb",
          "connection_eviction_interval": "1m",
          "connection_eviction_max_idle_time": "1m",
          "retry": {
            "debug_frequency_amount": "5m",
            "initial_delay": "1s",
            "debug_frequency_mode": "OFF",
            "max_delay_bound": "5s",
            "timeout": "30s"
          }
        },
        "logging": {
          "reset_interval": "1d",
          "interval": "1h",
          "wait_duration": "1h"
        },
        "skip_validate_and_start": "false",
        "eis": {
          "gateway": {
            "url": ""
          }
        }
      },
      "ent_search": {
        "enabled": "true"
      },
      "monitoring": {
        "migration": {
          "decommission_alerts": "false"
        },
        "collection": {
          "cluster": {
            "stats": {
              "timeout": "10s"
            }
          },
          "node": {
            "stats": {
              "timeout": "10s"
            }
          },
          "indices": [],
          "ccr": {
            "stats": {
              "timeout": "10s"
            }
          },
          "enrich": {
            "stats": {
              "timeout": "10s"
            }
          },
          "index": {
            "stats": {
              "timeout": "10s"
            },
            "recovery": {
              "active_only": "false",
              "timeout": "10s"
            }
          },
          "interval": "10s",
          "enabled": "false",
          "ml": {
            "job": {
              "stats": {
                "timeout": "10s"
              }
            }
          }
        },
        "history": {
          "duration": "168h"
        },
        "elasticsearch": {
          "collection": {
            "enabled": "true"
          }
        },
        "templates": {
          "enabled": "true"
        }
      },
      "graph": {
        "enabled": "true"
      },
      "searchable": {
        "snapshot": {
          "cache": {
            "range_size": "32mb",
            "sync": {
              "max_files": "10000",
              "interval": "60s",
              "shutdown_timeout": "10s"
            },
            "recovery_range_size": "128kb"
          },
          "shared_cache": {
            "recovery_range_size": "128kb",
            "region_size": "16mb",
            "concurrent_evictions": "5",
            "size": "0",
            "min_time_delta": "60s",
            "decay": {
              "interval": "60s"
            },
            "count_reads": "true",
            "size.max_headroom": "-1",
            "mmap": "false",
            "range_size": "16mb",
            "max_freq": "100"
          }
        }
      },
      "rollup": {
        "task_thread_pool": {
          "queue_size": "-1",
          "size": "1"
        }
      },
      "searchable_snapshots": {
        "cache_fetch_async_thread_pool": {
          "core": "0",
          "max": "45",
          "keep_alive": "30s"
        },
        "cache_prewarming_thread_pool": {
          "core": "0",
          "max": "16",
          "keep_alive": "30s"
        }
      },
      "downsample": {
        "thread_pool": {
          "queue_size": "256",
          "size": "1"
        }
      },
      "license": {
        "upload": {
          "types": [
            "trial",
            "enterprise"
          ]
        },
        "self_generated": {
          "type": "basic"
        }
      },
      "notification": {
        "pagerduty": {
          "default_account": ""
        },
        "webhook": {
          "additional_token_enabled": "false"
        },
        "email": {
          "recipient_allowlist": [
            "*"
          ],
          "html": {
            "sanitization": {
              "allow": [
                "body",
                "head",
                "_tables",
                "_links",
                "_blocks",
                "_formatting",
                "img:embedded"
              ],
              "disallow": [],
              "enabled": "true"
            }
          },
          "account": {
            "domain_allowlist": [
              "*"
            ]
          },
          "default_account": ""
        },
        "reporting": {
          "retries": "40",
          "warning": {
            "enabled": "true"
          },
          "interval": "15s"
        },
        "jira": {
          "default_account": ""
        },
        "slack": {
          "default_account": ""
        }
      },
      "security": {
        "operator_privileges": {
          "enabled": "false"
        },
        "dls_fls": {
          "enabled": "true"
        },
        "dls": {
          "bitset": {
            "cache": {
              "size": "10%",
              "ttl": "2h"
            }
          }
        },
        "transport": {
          "filter": {
            "allow": [],
            "deny": [],
            "enabled": "true"
          },
          "ssl": {
            "enabled": "true"
          }
        },
        "remote_cluster_server": {
          "ssl": {
            "enabled": "true"
          }
        },
        "ssl": {
          "diagnose": {
            "trust": "true"
          }
        },
        "enabled": "true",
        "crypto": {
          "thread_pool": {
            "queue_size": "1000",
            "size": "8"
          }
        },
        "enrollment": {
          "enabled": "false"
        },
        "filter": {
          "always_allow_bound_address": "true"
        },
        "encryption": {
          "algorithm": "AES/CTR/NoPadding"
        },
        "remote_cluster_client": {
          "ssl": {
            "enabled": "true"
          }
        },
        "remote_cluster": {
          "filter": {
            "allow": [],
            "deny": []
          }
        },
        "audit": {
          "enabled": "false",
          "logfile": {
            "emit_cluster_name": "false",
            "emit_node_id": "true",
            "emit_node_name": "false",
            "emit_node_host_address": "false",
            "emit_cluster_uuid": "true",
            "emit_node_host_name": "false",
            "events": {
              "emit_request_body": "false",
              "include": [
                "ACCESS_DENIED",
                "ACCESS_GRANTED",
                "ANONYMOUS_ACCESS_DENIED",
                "AUTHENTICATION_FAILED",
                "CONNECTION_DENIED",
                "TAMPERED_REQUEST",
                "RUN_AS_DENIED",
                "RUN_AS_GRANTED",
                "SECURITY_CONFIG_CHANGE"
              ],
              "exclude": []
            }
          }
        },
        "authc": {
          "realms": {
            "native": {
              "native1": {
                "order": "-99"
              }
            },
            "file": {
              "file1": {
                "order": "-100"
              }
            }
          },
          "password_hashing": {
            "algorithm": "BCRYPT"
          },
          "success_cache": {
            "size": "10000",
            "enabled": "true",
            "expire_after_access": "1h"
          },
          "api_key": {
            "doc_cache": {
              "ttl": "5m"
            },
            "cache": {
              "hash_algo": "SSHA256",
              "max_keys": "25000",
              "ttl": "24h"
            },
            "delete": {
              "interval": "24h",
              "retention_period": "7d",
              "timeout": "-1"
            },
            "enabled": "true",
            "hashing": {
              "algorithm": "SSHA256"
            }
          },
          "anonymous": {
            "authz_exception": "true",
            "roles": [],
            "username": "_anonymous"
          },
          "run_as": {
            "enabled": "true"
          },
          "reserved_realm": {
            "enabled": "false"
          },
          "service_token": {
            "cache": {
              "hash_algo": "ssha256",
              "max_tokens": "100000",
              "ttl": "20m"
            }
          },
          "token": {
            "delete": {
              "interval": "30m",
              "timeout": "-1"
            },
            "enabled": "true",
            "thread_pool": {
              "queue_size": "1000",
              "size": "1"
            },
            "timeout": "20m"
          }
        },
        "autoconfiguration": {
          "enabled": "true"
        },
        "fips_mode": {
          "enabled": "false",
          "required_providers": []
        },
        "encryption_key": {
          "length": "128",
          "algorithm": "AES"
        },
        "http": {
          "filter": {
            "allow": [],
            "deny": [],
            "enabled": "true"
          },
          "ssl": {
            "enabled": "true"
          }
        },
        "automata": {
          "max_determinized_states": "100000",
          "cache": {
            "size": "10000",
            "ttl": "48h",
            "enabled": "true"
          }
        },
        "user": null,
        "authz": {
          "timer": {
            "indices": {
              "enabled": "false",
              "threshold": {
                "warn": "200ms",
                "debug": "20ms",
                "info": "100ms"
              }
            }
          },
          "store": {
            "privileges": {
              "cache": {
                "ttl": "24h",
                "max_size": "10000"
              }
            },
            "roles": {
              "has_privileges": {
                "cache": {
                  "max_size": "1000"
                }
              },
              "cache": {
                "max_size": "10000"
              },
              "negative_lookup_cache": {
                "max_size": "10000"
              },
              "field_permissions": {
                "cache": {
                  "max_size_in_bytes": "104857600"
                }
              }
            }
          }
        }
      },
      "transform": {
        "num_transform_failure_retries": "10",
        "transform_scheduler_frequency": "1s"
      },
      "ccr": {
        "enabled": "true",
        "ccr_thread_pool": {
          "queue_size": "100",
          "size": "32"
        }
      },
      "idp": {
        "privileges": {
          "application": "",
          "cache": {
            "size": "100",
            "ttl": "90m"
          }
        },
        "metadata": {
          "signing": {
            "keystore": {
              "alias": ""
            }
          }
        },
        "slo_endpoint": {
          "post": "https:",
          "redirect": "https:"
        },
        "defaults": {
          "nameid_format": "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
          "authn_expiry": "5m"
        },
        "allowed_nameid_formats": [
          "urn:oasis:names:tc:SAML:2.0:nameid-format:transient"
        ],
        "contact": {
          "given_name": "",
          "email": "",
          "surname": ""
        },
        "organization": {
          "display_name": "",
          "name": "",
          "url": "http:"
        },
        "sso_endpoint": {
          "post": "https:",
          "redirect": "https:"
        },
        "entity_id": "",
        "signing": {
          "keystore": {
            "alias": ""
          }
        },
        "sp": {
          "cache": {
            "size": "1000",
            "ttl": "60m"
          },
          "wildcard": {
            "path": "wildcard_services.json"
          }
        },
        "enabled": "false"
      },
      "profiling": {
        "check_outdated_indices": "true",
        "enabled": "true",
        "query": {
          "stacktrace": {
            "max_slices": "16"
          },
          "details": {
            "max_slices": "16"
          },
          "realtime": "true"
        },
        "templates": {
          "enabled": "false"
        }
      },
      "http": {
        "tcp": {
          "keep_alive": "true"
        },
        "default_connection_timeout": "10s",
        "proxy": {
          "host": "",
          "scheme": "",
          "port": "0"
        },
        "connection_pool_ttl": "-1",
        "max_response_size": "10mb",
        "whitelist": [
          "*"
        ],
        "default_read_timeout": "10s"
      },
      "autoscaling": {
        "memory": {
          "monitor": {
            "timeout": "15s"
          }
        }
      },
      "apm_data": {
        "registry": {
          "enabled": "true"
        },
        "enabled": "true"
      },
      "applications": {
        "behavioral_analytics": {
          "ingest": {
            "bulk_processor": {
              "max_events_per_bulk": "500",
              "flush_delay": "10s",
              "max_bytes_in_flight": "5%",
              "max_number_of_retries": "1"
            }
          }
        },
        "rules": {
          "max_rules_per_ruleset": "100"
        }
      },
      "ml": {
        "dummy_entity_processors": "0",
        "utility_thread_pool": {
          "core": "1",
          "max": "2048",
          "keep_alive": "10m"
        },
        "enable_config_migration": "true",
        "delayed_data_check_freq": "15m",
        "min_disk_space_off_heap": "5gb",
        "model_repository": "https://ml-models.elastic.co",
        "use_auto_machine_memory_percent": "false",
        "inference_model": {
          "cache_size": "40%",
          "time_to_live": "5m"
        },
        "node_concurrent_job_allocations": "2",
        "enabled": "true",
        "max_ml_node_size": "0b",
        "dummy_entity_memory": "0b",
        "datafeed_thread_pool": {
          "core": "1",
          "max": "512",
          "keep_alive": "1m"
        },
        "native_inference_comms_thread_pool": {
          "core": "3",
          "max": "345",
          "keep_alive": "1m"
        },
        "process_connect_timeout": "10s",
        "job_comms_thread_pool": {
          "core": "4",
          "max": "2048",
          "keep_alive": "1m"
        },
        "max_anomaly_records": "500",
        "max_open_jobs": "512",
        "allocated_processors_scale": "1",
        "nightly_maintenance_requests_per_second": "-1.0",
        "max_model_memory_limit": "0b",
        "max_lazy_ml_nodes": "0",
        "model_download_thread_pool": {
          "queue_size": "-1",
          "size": "5"
        },
        "max_machine_memory_percent": "30",
        "persist_results_max_retries": "20",
        "trained_models": {
          "adaptive_allocations": {
            "scale_to_zero_time": "24h",
            "scale_up_cooldown_time": "5m"
          }
        },
        "autodetect_process": "true",
        "max_inference_processors": "50"
      }
    },
    "rest": {
      "action": {
        "multi": {
          "allow_explicit_index": "true"
        }
      },
      "incremental_bulk": "true"
    },
    "async_search": {
      "index_cleanup_interval": "1h"
    },
    "esql": {
      "default_data_partitioning": "AUTO",
      "querylog": {
        "include": {
          "user": "false"
        },
        "threshold": {
          "warn": "-1",
          "trace": "-1",
          "debug": "-1",
          "info": "-1"
        }
      },
      "values_loading_jumbo_size": "29360128b",
      "query": {
        "string_like_on_index": "true",
        "result_truncation_default_size": "1000",
        "allow_partial_results": "true",
        "result_truncation_max_size": "10000"
      }
    },
    "health": {
      "periodic_logger": {
        "output_mode": [
          "logs",
          "metrics"
        ],
        "poll_interval": "60s",
        "enabled": "false"
      },
      "node": {
        "enabled": "true"
      },
      "master_history": {
        "has_master_lookup_timeframe": "30s",
        "identity_changes_threshold": "4",
        "no_master_transitions_threshold": "4"
      },
      "ilm": {
        "max_time_on_action": "1d",
        "max_time_on_step": "1d",
        "max_retries_per_step": "100"
      },
      "shards_availability": {
        "replica_unassigned_buffer_time": "5s"
      },
      "reporting": {
        "local": {
          "monitor": {
            "interval": "30s"
          }
        }
      }
    },
    "monitor": {
      "jvm": {
        "gc": {
          "enabled": "true",
          "overhead": {
            "warn": "50",
            "debug": "10",
            "info": "25"
          },
          "refresh_interval": "1s"
        },
        "refresh_interval": "1s"
      },
      "process": {
        "refresh_interval": "1s"
      },
      "os": {
        "refresh_interval": "1s"
      },
      "fs": {
        "health": {
          "enabled": "true",
          "refresh_interval": "120s",
          "slow_path_logging_threshold": "5s"
        },
        "refresh_interval": "1s"
      }
    },
    "transport": {
      "tcp": {
        "reuse_address": "true",
        "keep_count": "-1",
        "keep_interval": "-1",
        "no_delay": "true",
        "keep_alive": "true",
        "receive_buffer_size": "-1b",
        "keep_idle": "-1",
        "send_buffer_size": "-1b"
      },
      "bind_host": [],
      "connect_timeout": "30s",
      "compress": "INDEXING_DATA",
      "ping_schedule": "-1",
      "connections_per_node": {
        "recovery": "2",
        "state": "1",
        "bulk": "3",
        "reg": "6",
        "ping": "1"
      },
      "tracer": {
        "include": [],
        "exclude": [
          "internal:coordination/fault_detection/*"
        ]
      },
      "type": "security4",
      "enable_stack_protection": "false",
      "slow_operation_logging_threshold": "5s",
      "type.default": "netty4",
      "rst_on_close": "false",
      "port": "9300-9399",
      "compression_scheme": "LZ4",
      "host": [],
      "publish_port": "-1",
      "publish_host": [],
      "netty": {
        "receive_predictor_size": "64kb",
        "receive_predictor_max": "64kb",
        "worker_count": "15",
        "receive_predictor_min": "64kb",
        "boss_count": "1"
      }
    },
    "remote_cluster_server": {
      "enabled": "false"
    },
    "snapshots": {
      "shutdown": {
        "progress": {
          "interval": "5s"
        }
      }
    },
    "indices": {
      "replication": {
        "retry_timeout": "60s",
        "initial_retry_backoff_bound": "50ms"
      },
      "cache": {
        "cleanup_interval": "1m"
      },
      "mapping": {
        "dynamic_timeout": "30s",
        "max_in_flight_updates": "10"
      },
      "memory": {
        "interval": "5s",
        "max_index_buffer_size": "-1",
        "shard_inactive_time": "5m",
        "index_buffer_size": "10%",
        "min_index_buffer_size": "48mb"
      },
      "breaker": {
        "request": {
          "limit": "60%",
          "type": "memory",
          "overhead": "1.0"
        },
        "total": {
          "limit": "95%",
          "use_real_memory": "true"
        },
        "fielddata": {
          "limit": "40%",
          "type": "memory",
          "overhead": "1.03"
        },
        "type": "hierarchy"
      },
      "inference": {
        "batch_size": "1mb"
      },
      "write_ack_delay_interval": "0ms",
      "query": {
        "bool": {
          "max_nested_depth": "30",
          "max_clause_count": "4096"
        },
        "query_string": {
          "analyze_wildcard": "false",
          "allowLeadingWildcard": "true"
        }
      },
      "id_field_data": {
        "enabled": "false"
      },
      "recovery": {
        "internal_action_retry_timeout": "1m",
        "retry_delay_network": "5s",
        "chunk_size": "512kb",
        "internal_action_timeout": "15m",
        "retry_delay_state_sync": "500ms",
        "max_concurrent_snapshot_file_downloads": "5",
        "internal_action_long_timeout": "1800000ms",
        "max_concurrent_operations": "1",
        "max_bytes_per_sec": "40mb",
        "recovery_activity_timeout": "1800000ms",
        "max_concurrent_snapshot_file_downloads_per_node": "25",
        "use_snapshots": "true",
        "max_concurrent_file_chunks": "2"
      },
      "requests": {
        "cache": {
          "size": "1%",
          "expire": "0ms"
        }
      },
      "store": {
        "max_concurrent_closing_shards": "10",
        "delete": {
          "shard": {
            "timeout": "30s"
          }
        },
        "shard_lock_retry": {
          "interval": "1s",
          "timeout": "1m"
        }
      },
      "analysis": {
        "hunspell": {
          "dictionary": {
            "ignore_case": "false",
            "lazy": "false"
          }
        }
      },
      "queries": {
        "cache": {
          "count": "10000",
          "size": "10%",
          "all_segments": "false"
        }
      },
      "pause": {
        "on": {
          "throttle": "false"
        }
      },
      "lifecycle": {
        "poll_interval": "10m",
        "rollover": {
          "only_if_has_documents": "true"
        },
        "step": {
          "master_timeout": "30s"
        },
        "history_index_enabled": "true"
      },
      "write_ack_delay_randomness_bound": "70ms",
      "fielddata": {
        "cache": {
          "size": "-1b",
          "expire": "1h"
        }
      },
      "stats": {
        "recent_read_load": {
          "half_life": "5m"
        },
        "recent_write_load": {
          "half_life": "5m"
        }
      },
      "merge": {
        "scheduler": {
          "use_thread_pool": "true"
        },
        "disk": {
          "check_interval": "5s",
          "watermark": {
            "high": "95%",
            "high.max_headroom": "100gb"
          }
        },
        "policy": {
          "max_merged_segment": "5gb",
          "max_time_based_merged_segment": "100gb"
        }
      }
    },
    "master_history": {
      "max_age": "30m"
    },
    "plugin": {
      "mandatory": []
    },
    "ingest_node": {
      "transport_action_timeout": "20s"
    },
    "logsdb": {
      "prior_logs_usage": "false"
    },
    "discovery": {
      "seed_hosts": [],
      "unconfigured_bootstrap_timeout": "3s",
      "request_peers_timeout": "3000ms",
      "initial_state_timeout": "30s",
      "cluster_formation_warning_timeout": "10000ms",
      "seed_providers": [
        "file"
      ],
      "type": "multi-node",
      "seed_resolver": {
        "max_concurrent_resolvers": "10",
        "timeout": "5s"
      },
      "find_peers_interval": "1000ms",
      "probe": {
        "connect_timeout": "30s",
        "handshake_timeout": "30s"
      }
    },
    "write_load_forecaster": {
      "max_index_age": "7d"
    },
    "data_streams": {
      "lifecycle": {
        "poll_interval": "5m",
        "retention": {
          "failures_default": "30d",
          "max": "-1",
          "default": "-1"
        },
        "signalling": {
          "error_retry_interval": "10"
        },
        "target": {
          "merge": {
            "policy": {
              "floor_segment": "100mb",
              "merge_factor": "16"
            }
          }
        }
      },
      "failure_store": {
        "enabled": []
      },
      "auto_sharding": {
        "decrease_shards": {
          "cooldown": "3d",
          "load_metric": "PEAK"
        },
        "excludes": [],
        "increase_shards": {
          "cooldown": "270s",
          "load_metric": "PEAK"
        }
      }
    },
    "gateway": {
      "recover_after_data_nodes": "-1",
      "expected_data_nodes": "-1",
      "write_dangling_indices_info": "true",
      "slow_write_logging_threshold": "10s",
      "recover_after_time": "0ms"
    }
  }
}
```
