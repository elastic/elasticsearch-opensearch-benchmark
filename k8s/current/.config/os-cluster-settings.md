# Cluster settings

```
GET _cluster/settings?include_defaults
```

```json
{
  "persistent": {},
  "transient": {
    "cluster": {
      "routing": {
        "allocation": {
          "enable": "all"
        }
      }
    }
  },
  "defaults": {
    "task_resource_tracking": {
      "enabled": "true"
    },
    "cluster": {
      "max_voting_config_exclusions": "10",
      "metadata": {
        "perf_analyzer": {
          "collectors": {
            "mode": "0"
          },
          "state": "0",
          "config": {
            "overrides": ""
          },
          "pa_node_stats_setting": "1"
        }
      },
      "no_master_block": "metadata_write",
      "persistent_tasks": {
        "allocation": {
          "enable": "all",
          "recheck_interval": "30s"
        }
      },
      "initial_cluster_manager_nodes": [
        "os-cluster-bootstrap-0"
      ],
      "remote": {
        "node": {
          "attr": ""
        },
        "initial_connect_timeout": "30s",
        "connect": "true",
        "connections_per_cluster": "3"
      },
      "no_cluster_manager_block": "metadata_write",
      "ingest": {
        "max_number_processors": "2147483647",
        "system_pipeline_enabled": "true"
      },
      "routing": {
        "rebalance": {
          "enable": "all"
        },
        "allocation": {
          "node_initial_primaries_recoveries": "4",
          "same_shard": {
            "host": "false"
          },
          "shard_movement_strategy": "no_preference",
          "type": "balanced",
          "rebalance": {
            "primary": {
              "enable": "false",
              "buffer": "0.1"
            }
          },
          "awareness": {
            "balance": "false",
            "attributes": []
          },
          "balance": {
            "index": "0.55",
            "threshold": "1.0",
            "shard": "0.45",
            "prefer_primary": "false"
          },
          "remote_primary": {
            "ignore_throttle": "true"
          },
          "node_concurrent_incoming_recoveries": "2",
          "move": {
            "primary_first": "false"
          },
          "total_shards_per_node": "-1",
          "cluster_concurrent_recoveries": "-1",
          "primary_constraint": {
            "threshold": "10"
          },
          "shard_state": {
            "reroute": {
              "priority": "NORMAL"
            }
          },
          "disk": {
            "threshold_enabled": "true",
            "watermark": {
              "flood_stage": "95%",
              "high": "90%",
              "low": "85%",
              "enable_for_single_data_node": "false"
            },
            "include_relocations": "true",
            "warm_threshold_enabled": "true",
            "reroute_interval": "60s"
          },
          "node_initial_replicas_recoveries": "4",
          "load_awareness": {
            "allow_unassigned_primaries": "true",
            "flat_skew": "2",
            "skew_factor": "50.0",
            "provisioned_capacity": "-1"
          },
          "node_concurrent_outgoing_recoveries": "2",
          "allow_rebalance": "indices_all_active",
          "balanced_shards_allocator": {
            "schedule_reroute": {
              "priority": "NORMAL"
            },
            "allocator_timeout": "-1"
          },
          "cluster_concurrent_rebalance": "2",
          "node_concurrent_recoveries": "2",
          "shards_batch_gateway_allocator": {
            "replica_allocator_timeout": "20s",
            "schedule_reroute": {
              "priority": "NORMAL"
            },
            "primary_allocator_timeout": "20s"
          },
          "total_primary_shards_per_node": "-1",
          "total_shards_limit": "-1"
        },
        "ignore_weighted_routing": "false",
        "search_replica": {
          "strict": "true"
        },
        "use_adaptive_replica_selection": "true",
        "weighted": {
          "strict": "true",
          "fail_open": "true",
          "default_weight": "1.0"
        }
      },
      "default": {
        "index": {
          "max_merge_at_once": "30",
          "refresh_interval": "1s"
        }
      },
      "search": {
        "request": {
          "slowlog": {
            "level": "TRACE",
            "threshold": {
              "warn": "-1",
              "trace": "-1",
              "debug": "-1",
              "info": "-1"
            }
          }
        },
        "ignore_awareness_attributes": "true"
      },
      "allocator": {
        "existing_shards_allocator": {
          "batch_enabled": "true"
        },
        "gateway": {
          "batch_size": "2000"
        }
      },
      "remote_state": {
        "download": {
          "serve_read_api": {
            "enabled": "true"
          }
        }
      },
      "default_number_of_replicas": "1",
      "join": {
        "timeout": "60000ms"
      },
      "info": {
        "update": {
          "interval": "30s",
          "timeout": "15s"
        }
      },
      "auto_shrink_voting_configuration": "true",
      "election": {
        "duration": "500ms",
        "initial_timeout": "100ms",
        "max_timeout": "10s",
        "back_off_time": "100ms",
        "strategy": "default"
      },
      "remote_store": {
        "compatibility_mode": "STRICT",
        "translog": {
          "buffer_interval": "650ms",
          "max_readers": "1000",
          "path": {
            "prefix": ""
          },
          "transfer_timeout": "30s"
        },
        "publication": {
          "enabled": "false"
        },
        "segment": {
          "transfer_timeout": "30m"
        },
        "routing_table": {
          "path_hash_algo": "FNV_1A_BASE64",
          "path": {
            "prefix": ""
          },
          "path_type": "HASHED_PREFIX"
        },
        "index": {
          "path": {
            "hash_algorithm": "FNV_1A_COMPOSITE_1",
            "type": "HASHED_PREFIX"
          },
          "segment_metadata": {
            "retention": {
              "max_count": "10"
            }
          },
          "restrict": {
            "async-durability": "false"
          },
          "translog": {
            "translog_metadata": "true"
          }
        },
        "state": {
          "cleanup_interval": "5m",
          "path": {
            "prefix": ""
          },
          "checksum_validation": {
            "mode": "NONE"
          },
          "metadata_manifest": {
            "upload_timeout": "20000ms"
          },
          "global_metadata": {
            "upload_timeout": "20000ms"
          },
          "read_timeout": "20000ms",
          "enabled": "false",
          "index_metadata": {
            "upload_timeout": "20000ms"
          }
        },
        "pinned_timestamps": {
          "lookback_interval": "1m",
          "enabled": "false",
          "scheduler_interval": "3m"
        },
        "index_metadata": {
          "path_hash_algo": "FNV_1A_BASE64",
          "path_type": "HASHED_PREFIX"
        },
        "segments": {
          "path": {
            "prefix": ""
          }
        }
      },
      "blocks": {
        "create_index": "false",
        "read_only_allow_delete": "false",
        "read_only": "false",
        "create_index.auto_release": "true"
      },
      "ignore_dot_indexes": "false",
      "index": {
        "restrict": {
          "replication": {
            "type": "false"
          }
        },
        "refresh": {
          "fixed_interval_scheduling": {
            "enabled": "false"
          },
          "shard_level": {
            "enabled": "false"
          }
        }
      },
      "follower_lag": {
        "timeout": "90000ms"
      },
      "indices": {
        "replication": {
          "strategy": "DOCUMENT"
        },
        "tombstones": {
          "size": "500"
        },
        "close": {
          "enable": "true"
        }
      },
      "application_templates": {
        "enabled": "false"
      },
      "nodes": {
        "reconnect_interval": "10s"
      },
      "task": {
        "consumers": {
          "top_n": {
            "size": "10",
            "frequency": "60s"
          }
        }
      },
      "service": {
        "slow_cluster_manager_task_logging_threshold": "10s",
        "slow_task_logging_threshold": "30s"
      },
      "publish": {
        "timeout": "30000ms",
        "info_timeout": "10000ms"
      },
      "migration": {
        "direction": "NONE"
      },
      "name": "os-cluster",
      "auto_force_merge": {
        "enabled": "false"
      },
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
      "filecache": {
        "remote_data_ratio": "0.0"
      },
      "initial_master_nodes": [
        "os-cluster-bootstrap-0"
      ],
      "minimum": {
        "index": {
          "refresh_interval": "0ms"
        }
      },
      "snapshot": {
        "info": {
          "max_concurrent_fetches": "5"
        },
        "shard": {
          "path": {
            "prefix": ""
          }
        }
      }
    },
    "opendistro": {
      "scheduled_jobs": {
        "request_timeout": "10s",
        "sweeper": {
          "backoff_millis": "50ms",
          "period": "5m",
          "page_size": "100"
        },
        "enabled": "true",
        "retry_count": "3"
      },
      "asynchronous_search": {
        "max_wait_for_completion_timeout": "1m",
        "expired": {
          "persisted_response": {
            "cleanup_interval": "30m"
          }
        },
        "max_search_running_time": "12h",
        "persist_search_failures": "false",
        "active": {
          "context": {
            "reaper_interval": "5m"
          }
        },
        "node_concurrent_running_searches": "20",
        "max_keep_alive": "5d"
      },
      "destination": {
        "host": {
          "deny_list": []
        }
      },
      "index_state_management": {
        "coordinator": {
          "backoff_millis": "50ms",
          "sweep_period": "10m",
          "backoff_count": "2"
        },
        "restricted_index_pattern": """\.opendistro_security|\.kibana.*|\.opendistro-ism-config""",
        "allow_list": [
          "alias",
          "allocation",
          "close",
          "delete",
          "force_merge",
          "index_priority",
          "notification",
          "open",
          "read_only",
          "read_write",
          "replica_count",
          "rollup",
          "rollover",
          "shrink",
          "snapshot",
          "transform",
          "stop_replication",
          "convert_index_to_remote"
        ],
        "history": {
          "max_age": "24h",
          "number_of_shards": "1",
          "rollover_retention_period": "30d",
          "rollover_check_period": "8h",
          "max_docs": "2500000",
          "number_of_replicas": "1",
          "enabled": "true"
        },
        "job_interval": "5",
        "enabled": "true",
        "snapshot": {
          "deny_list": []
        }
      },
      "anomaly_detection": {
        "ad_result_history_rollover_period": "12h",
        "max_anomaly_features": "5",
        "breaker": {
          "enabled": "true"
        },
        "request_timeout": "60s",
        "backoff_initial_delay": "1000ms",
        "batch_task_piece_size": "1000",
        "max_cache_miss_handling_per_second": "100",
        "enabled": "true",
        "max_batch_task_per_node": "10",
        "cooldown_minutes": "5m",
        "model_max_size_percent": "0.1",
        "max_primary_shards": "10",
        "ad_result_history_max_docs": "250000000",
        "ad_result_history_retention_period": "30d",
        "backoff_minutes": "15m",
        "detection_window_delay": "0m",
        "index_pressure_soft_limit": "0.8",
        "max_entities_for_preview": "30",
        "max_multi_entity_anomaly_detectors": "10",
        "max_entities_per_query": "1000",
        "max_retry_for_unresponsive_node": "5",
        "detection_interval": "10m",
        "batch_task_piece_interval_seconds": "5",
        "max_old_ad_task_docs_per_detector": "1",
        "max_retry_for_backoff": "3",
        "max_anomaly_detectors": "1000",
        "filter_by_backend_roles": "false"
      },
      "alerting": {
        "alert_backoff_millis": "50ms",
        "index_timeout": "60s",
        "move_alerts_backoff_count": "3",
        "alert_history_max_age": "30d",
        "request_timeout": "10s",
        "bulk_timeout": "120s",
        "destination": {
          "allow_list": [
            "chime",
            "slack",
            "custom_webhook",
            "email",
            "test_action"
          ]
        },
        "monitor": {
          "max_monitors": "1000"
        },
        "action_throttle_max_value": "24h",
        "alert_history_rollover_period": "12h",
        "alert_history_max_docs": "1000",
        "alert_backoff_count": "2",
        "move_alerts_backoff_millis": "250ms",
        "alert_history_retention_period": "60d",
        "alert_history_enabled": "true",
        "input_timeout": "30s",
        "filter_by_backend_roles": "false"
      },
      "jobscheduler": {
        "jitter_limit": "0.6",
        "request_timeout": "10s",
        "sweeper": {
          "backoff_millis": "50ms",
          "period": "5m",
          "page_size": "100"
        },
        "threadpool": {
          "queue_size": "200",
          "size": "15"
        },
        "retry_count": "3"
      },
      "rollup": {
        "search": {
          "backoff_millis": "1000ms",
          "backoff_count": "5",
          "enabled": "true"
        },
        "dashboards": {
          "enabled": "true"
        },
        "enabled": "true",
        "ingest": {
          "backoff_millis": "1000ms",
          "backoff_count": "5"
        }
      }
    },
    "plugins": {
      "destination": {
        "host": {
          "deny_list": []
        }
      },
      "calcite": {
        "fallback": {
          "allowed": "true"
        },
        "enabled": "false",
        "pushdown": {
          "rowcount": {
            "estimation": {
              "factor": "0.9"
            }
          },
          "enabled": "true"
        }
      },
      "index_state_management": {
        "coordinator": {
          "backoff_millis": "50ms",
          "sweep_period": "10m",
          "sweep_skip_period": "5m",
          "backoff_count": "2"
        },
        "jitter": "0.6",
        "restricted_index_pattern": """\.opendistro_security|\.kibana.*|\.opendistro-ism-config""",
        "action_validation": {
          "enabled": "false"
        },
        "allow_list": [
          "alias",
          "allocation",
          "close",
          "delete",
          "force_merge",
          "index_priority",
          "notification",
          "open",
          "read_only",
          "read_write",
          "replica_count",
          "rollup",
          "rollover",
          "shrink",
          "snapshot",
          "transform",
          "stop_replication",
          "convert_index_to_remote"
        ],
        "history": {
          "max_age": "24h",
          "number_of_shards": "1",
          "rollover_retention_period": "30d",
          "rollover_check_period": "8h",
          "max_docs": "2500000",
          "number_of_replicas": "1",
          "enabled": "true"
        },
        "job_interval": "5",
        "enabled": "true",
        "snapshot": {
          "deny_list": []
        }
      },
      "alerting": {
        "alert_backoff_millis": "50ms",
        "index_timeout": "60s",
        "move_alerts_backoff_count": "3",
        "alert_history_max_age": "30d",
        "request_timeout": "10s",
        "remote_metadata_endpoint": "",
        "destination": {
          "allow_list": [
            "chime",
            "slack",
            "custom_webhook",
            "email",
            "test_action"
          ]
        },
        "comments_history_rollover_period": "12h",
        "max_comment_character_length": "2000",
        "max_actionable_alert_count": "50",
        "remote_metadata_region": "",
        "action_throttle_max_value": "24h",
        "alert_history_rollover_period": "12h",
        "alert_history_max_docs": "1000",
        "alert_backoff_count": "2",
        "alert_history_retention_period": "60d",
        "cross_cluster_monitoring_enabled": "true",
        "input_timeout": "30s",
        "remote_metadata_service_name": "",
        "remote_metadata_type": "",
        "alert_findings_indexing_batch_size": "1000",
        "alert_finding_max_docs": "1000",
        "bulk_timeout": "120s",
        "alert_finding_rollover_period": "12h",
        "finding_history_max_age": "30d",
        "monitor": {
          "max_monitors": "1000",
          "doc_level_monitor_shard_fetch_size": "10000",
          "percolate_query_docs_size_memory_percentage_limit": "10",
          "doc_level_monitor_fanout_max_duration": "3m",
          "doc_level_monitor_fan_out_nodes": "1000",
          "percolate_query_max_num_docs_in_memory": "50000",
          "doc_level_monitor_execution_max_duration": "4m",
          "doc_level_monitor_query_field_names_enabled": "true"
        },
        "max_comments_per_notification": "3",
        "comments_history_retention_period": "60d",
        "alert_finding_enabled": "true",
        "comments_enabled": "true",
        "comments_history_max_docs": "1000",
        "max_comments_per_alert": "500",
        "comments_history_max_age": "30d",
        "finding_history_retention_period": "60d",
        "move_alerts_backoff_millis": "250ms",
        "alert_history_enabled": "true",
        "filter_by_backend_roles": "false"
      },
      "rollup": {
        "search": {
          "backoff_millis": "1000ms",
          "search_source_indices": "false",
          "search_all_jobs": "false",
          "backoff_count": "5",
          "enabled": "true"
        },
        "dashboards": {
          "enabled": "true"
        },
        "enabled": "true",
        "ingest": {
          "backoff_millis": "1000ms",
          "backoff_count": "5"
        }
      },
      "search_relevance": {
        "query_set": {
          "maximum": "1000"
        },
        "workbench_enabled": "false",
        "stats_enabled": "true"
      },
      "sql": {
        "cursor": {
          "keep_alive": "1m"
        },
        "slowlog": "2",
        "enabled": "true"
      },
      "ml_commons": {
        "monitoring_request_count": "100",
        "allow_custom_deployment_plan": "false",
        "sync_up_job_interval_in_seconds": "10",
        "max_batch_ingestion_tasks": "10",
        "remote_metadata_endpoint": "",
        "ml_task_timeout_in_seconds": "600",
        "remote_metadata_region": "",
        "task_dispatcher": {
          "eligible_node_role": {
            "local_model": [
              "data",
              "ml"
            ],
            "remote_model": [
              "data",
              "ml"
            ]
          }
        },
        "trusted_url_regex": "^(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]",
        "disk_free_space_threshold": "5368709120b",
        "metrics_collection_enabled": "false",
        "model_auto_deploy": {
          "enable": "true"
        },
        "rag_pipeline_feature_enabled": "true",
        "task_dispatch_policy": "round_robin",
        "offline_batch_inference_enabled": "true",
        "offline_batch_ingestion_enabled": "true",
        "remote_job": {
          "status_field": [
            "status",
            "Status",
            "TransformJobStatus"
          ],
          "status_regex": {
            "cancelled": "(stopped|cancelled)",
            "completed": "(complete|completed|partiallyCompleted)",
            "expired": "(expired|timeout)",
            "failed": "(failed)",
            "cancelling": "(stopping|cancelling)"
          }
        },
        "max_ml_task_per_node": "10",
        "exclude_nodes": {
          "_name": ""
        },
        "local_model": {
          "enabled": "true"
        },
        "max_batch_inference_tasks": "10",
        "model_access_control_enabled": "false",
        "native_memory_threshold": "90",
        "metrics_static_collection_enabled": "false",
        "model_auto_redeploy": {
          "lifetime_retry_times": "3",
          "enable": "true"
        },
        "model_auto_redeploy_success_ratio": "0.8",
        "controller_enabled": "true",
        "batch_ingestion_bulk_size": "500",
        "jvm_heap_memory_threshold": "85",
        "remote_metadata_service_name": "",
        "agent_framework_enabled": "true",
        "remote_metadata_type": "",
        "memory_feature_enabled": "true",
        "only_run_on_ml_node": "true",
        "max_register_model_tasks_per_node": "10",
        "allow_registering_model_via_local_file": "false",
        "safe_delete_model": "false",
        "multi_tenancy_enabled": "false",
        "connector": {
          "private_ip_enabled": "false"
        },
        "max_model_on_node": "10",
        "mcp_connector_enabled": "false",
        "trusted_connector_endpoints_regex": [
          """^https://runtime\.sagemaker\..*[a-z0-9-]\.amazonaws\.com/.*$""",
          """^https://api\.sagemaker\..*[a-z0-9-]\.amazonaws\.com/.*$""",
          """^https://api\.openai\.com/.*$""",
          """^https://api\.cohere\.ai/.*$""",
          """^https://api\.deepseek\.com/.*$""",
          """^https://bedrock-runtime\..*[a-z0-9-]\.amazonaws\.com/.*$""",
          """^https://bedrock-agent-runtime\..*[a-z0-9-]\.amazonaws\.com/.*$""",
          """^https://bedrock\..*[a-z0-9-]\.amazonaws\.com/.*$""",
          """^https://textract\..*[a-z0-9-]\.amazonaws\.com$""",
          """^https://comprehend\..*[a-z0-9-]\.amazonaws\.com$""",
          """^https://rekognition(-fips)?\..*[a-z0-9-]\.amazonaws\.com$"""
        ],
        "remote_inference": {
          "enabled": "true"
        },
        "connector_access_control_enabled": "false",
        "mcp_server_enabled": "false",
        "enable_inhouse_python_model": "false",
        "max_deploy_model_tasks_per_node": "10",
        "allow_registering_model_via_url": "false"
      },
      "transform": {
        "circuit_breaker": {
          "jvm": {
            "threshold": "85"
          },
          "enabled": "true"
        },
        "internal": {
          "index": {
            "backoff_millis": "1000ms",
            "backoff_count": "5"
          },
          "search": {
            "backoff_millis": "1000ms",
            "backoff_count": "5"
          }
        }
      },
      "geospatial": {
        "ip2geo": {
          "processor": {
            "cache_size": "1000"
          },
          "datasource": {
            "update_interval_in_days": "3",
            "endpoint": "https://geoip.maps.opensearch.org/v1/geolite2-city/manifest.json",
            "batch_size": "10000",
            "endpoint.denylist": [
              "127.0.0.0/8",
              "169.254.0.0/16",
              "10.0.0.0/8",
              "172.16.0.0/12",
              "192.168.0.0/16",
              "0.0.0.0/8",
              "100.64.0.0/10",
              "192.0.0.0/24",
              "192.0.2.0/24",
              "198.18.0.0/15",
              "192.88.99.0/24",
              "198.51.100.0/24",
              "203.0.113.0/24",
              "224.0.0.0/4",
              "240.0.0.0/4",
              "255.255.255.255/32",
              "::1/128",
              "fe80::/10",
              "fc00::/7",
              "::/128",
              "2001:db8::/32",
              "ff00::/8"
            ]
          },
          "timeout": "30s"
        }
      },
      "timeseries": {
        "max_cached_deleted_tasks": "1000",
        "max_retry_for_unresponsive_node": "5",
        "breaker": {
          "enabled": "true"
        },
        "cooldown_minutes": "5m",
        "backoff_minutes": "15m"
      },
      "index_management": {
        "filter_by_backend_roles": "false"
      },
      "neural_search": {
        "reranker_max_document_fields": "50",
        "stats_enabled": "false"
      },
      "jobscheduler": {
        "jitter_limit": "0.6",
        "request_timeout": "10s",
        "sweeper": {
          "backoff_millis": "50ms",
          "period": "5m",
          "page_size": "100"
        },
        "retry_count": "3"
      },
      "replication": {
        "leader": {
          "thread_pool": {
            "queue_size": "1000",
            "size": "0"
          }
        },
        "autofollow": {
          "concurrent_replication_jobs_trigger_size": "3",
          "fetch_poll_interval": "30s",
          "retry_poll_interval": "1h"
        },
        "follower": {
          "poll_interval": "50ms",
          "concurrent_readers_per_shard": "2",
          "concurrent_writers_per_shard": "2",
          "index": {
            "ops_batch_size": "50000",
            "recovery": {
              "chunk_size": "10mb",
              "max_concurrent_file_chunks": "5"
            }
          },
          "block": {
            "start": "false"
          },
          "retention_lease_max_failure_duration": "1h",
          "metadata_sync_interval": "60s"
        }
      },
      "flow_framework": {
        "remote_metadata_service_name": "",
        "task_request_retry_duration": "5s",
        "remote_metadata_type": "",
        "request_timeout": "10s",
        "remote_metadata_endpoint": "",
        "workflow_thread_pool_size": "4",
        "remote_metadata_region": "",
        "enabled": "true",
        "max_workflow_steps": "50",
        "multi_tenancy_enabled": "false",
        "max_workflows": "1000",
        "max_active_deprovisions_per_tenant": "1",
        "deprovision_thread_pool_size": "4",
        "provision_thread_pool_size": "8",
        "max_active_provisions_per_tenant": "2",
        "filter_by_backend_roles": "false"
      },
      "security_config": {
        "ssl_dual_mode_enabled": "false"
      },
      "query": {
        "executionengine": {
          "spark": {
            "result": {
              "index": {
                "ttl": "60d"
              }
            },
            "session_inactivity_timeout_millis": "180000",
            "streamingjobs": {
              "housekeeper": {
                "interval": "15m"
              }
            },
            "auto_index_management": {
              "enabled": "true"
            },
            "session": {
              "limit": "10",
              "index": {
                "ttl": "30d"
              }
            },
            "config": "",
            "refresh_job": {
              "limit": "5"
            }
          },
          "async_query": {
            "enabled": "true",
            "external_scheduler": {
              "enabled": "true",
              "interval": ""
            }
          }
        },
        "memory_limit": "85%",
        "metrics": {
          "rolling_interval": "60",
          "rolling_window": "3600"
        },
        "datasources": {
          "limit": "20",
          "uri": {
            "hosts": {
              "denylist": []
            }
          },
          "enabled": "true"
        },
        "field_type_tolerance": "true",
        "size_limit": "10000"
      },
      "scheduled_jobs": {
        "request_timeout": "10s",
        "sweeper": {
          "backoff_millis": "50ms",
          "period": "5m",
          "page_size": "100"
        },
        "enabled": "true",
        "retry_count": "3"
      },
      "asynchronous_search": {
        "max_wait_for_completion_timeout": "1m",
        "expired": {
          "persisted_response": {
            "cleanup_interval": "30m"
          }
        },
        "max_search_running_time": "12h",
        "persist_search_failures": "false",
        "active": {
          "context": {
            "reaper_interval": "5m"
          }
        },
        "node_concurrent_running_searches": "20",
        "max_keep_alive": "5d"
      },
      "forecast": {
        "checkpoint_write_queue_concurrency": "2",
        "request_timeout": "10s",
        "checkpoint_read_queue_max_heap_percent": "0.001",
        "cold_start_queue_max_heap_percent": "0.001",
        "backoff_initial_delay": "1000ms",
        "checkpoint_ttl": "7d",
        "forecast_result_history_rollover_period": "12h",
        "enabled": "true",
        "checkpoint_read_queue_batch_size": "25",
        "category_field_limit": "2",
        "checkpoint_write_queue_batch_size": "25",
        "default_window_delay": "0m",
        "expected_cold_entity_execution_time_in_millisecs": "3000",
        "max_entities_per_interval": "1000000",
        "model_max_size_percent": "0.1",
        "result_write_queue_batch_size": "5000",
        "expected_checkpoint_maintain_time_in_millisecs": "1000",
        "max_primary_shards": "10",
        "result_write_queue_concurrency": "2",
        "max_hc_forecasters": "10",
        "result_write_queue_max_heap_percent": "0.01",
        "cold_entity_queue_max_heap_percent": "0.001",
        "max_forecasters": "1000",
        "max_old_task_docs_per_forecaster": "1",
        "page_size": "1000",
        "cold_start_queue_concurrency": "1",
        "default_interval": "10m",
        "backoff_minutes": "15m",
        "delete_forecast_result_when_delete_forecaster": "false",
        "checkpoint_read_queue_concurrency": "1",
        "checkpoint_write_queue_max_heap_percent": "0.01",
        "index_pressure_soft_limit": "0.6",
        "forecast_result_history_max_docs_per_shard": "1350000000",
        "index_pressure_hard_limit": "0.9",
        "checkpoint_saving_freq": "12h",
        "forecast_result_history_retention_period": "30d",
        "max_model_size_per_node": "100",
        "checkpoint_maintain_queue_max_heap_percent": "0.001",
        "dedicated_cache_size": "10",
        "max_retry_for_backoff": "3",
        "filter_by_backend_roles": "false"
      },
      "security_analytics": {
        "index_timeout": "60s",
        "threat_intel_timeout": "30s",
        "alert_history_max_age": "30d",
        "request_timeout": "10s",
        "auto_correlations_enabled": "false",
        "ioc_finding_enabled": "true",
        "enable_workflow_usage": "true",
        "threatintel": {
          "tifjob": {
            "update_interval": "1440m",
            "batch_size": "10000"
          }
        },
        "correlation_history_retention_period": "60d",
        "correlation_time_window": "5m",
        "action_throttle_max_value": "24h",
        "alert_history_rollover_period": "12h",
        "alert_history_max_docs": "1000",
        "correlation_history_max_docs": "1000",
        "ioc_finding_history_max_docs": "1000",
        "alert_history_retention_period": "60d",
        "correlation_history_max_age": "30d",
        "correlation_history_rollover_period": "12h",
        "ioc_finding_history_max_age": "30d",
        "alert_finding_max_docs": "1000",
        "alert_finding_rollover_period": "12h",
        "finding_history_max_age": "30d",
        "enable_detectors_with_dedicated_query_indices": "true",
        "mappings": {
          "default_schema": "ecs"
        },
        "alert_finding_enabled": "true",
        "finding_history_retention_period": "60d",
        "ioc_finding_history_rollover_period": "12h",
        "alert_history_enabled": "true",
        "ioc": {
          "index_retention_period": "30d",
          "scan_max_terms_count": "65536",
          "max_indices_per_alias": "2"
        },
        "ioc_finding_history_retention_period": "60d",
        "filter_by_backend_roles": "false"
      },
      "snapshot_management": {
        "filter_by_backend_roles": "false"
      },
      "ppl": {
        "pattern": {
          "mode": "LABEL",
          "buffer": {
            "limit": "100000"
          },
          "method": "SIMPLE_PATTERN",
          "max": {
            "sample": {
              "count": "10"
            }
          }
        },
        "enabled": "true"
      },
      "anomaly_detection": {
        "entity_cold_start_queue_max_heap_percent": "0.001",
        "max_anomaly_features": "5",
        "breaker": {
          "enabled": "true"
        },
        "request_timeout": "60s",
        "checkpoint_read_queue_max_heap_percent": "0.001",
        "max_batch_task_per_node": "10",
        "checkpoint_read_queue_batch_size": "25",
        "max_top_entities_for_historical_analysis": "1000",
        "jvm_heap_usage_threshold": "95",
        "cooldown_minutes": "5m",
        "expected_cold_entity_execution_time_in_millisecs": "3000",
        "model_max_size_percent": "0.1",
        "max_running_entities_per_detector_for_historical_analysis": "10",
        "door_keeper_in_cache": {
          "enabled": "false"
        },
        "page_size": "1000",
        "checkpoint_read_queue_concurrency": "1",
        "index_pressure_soft_limit": "0.6",
        "max_multi_entity_anomaly_detectors": "10",
        "max_entities_per_query": "1000000",
        "checkpoint_saving_freq": "12h",
        "delete_anomaly_result_when_delete_detector": "false",
        "max_concurrent_preview": "2",
        "max_cached_deleted_tasks": "1000",
        "max_retry_for_unresponsive_node": "5",
        "entity_cold_start_queue_concurrency": "1",
        "ad_result_history_max_docs_per_shard": "1350000000",
        "batch_task_piece_interval_seconds": "5",
        "checkpoint_maintain_queue_max_heap_percent": "0.001",
        "dedicated_cache_size": "10",
        "filter_by_backend_roles": "false",
        "ad_result_history_rollover_period": "12h",
        "checkpoint_write_queue_concurrency": "2",
        "hcad_cold_start_interpolation": {
          "enabled": "false"
        },
        "backoff_initial_delay": "1000ms",
        "batch_task_piece_size": "1000",
        "checkpoint_ttl": "7d",
        "enabled": "true",
        "category_field_limit": "2",
        "checkpoint_write_queue_batch_size": "25",
        "result_write_queue_batch_size": "5000",
        "expected_checkpoint_maintain_time_in_millisecs": "1000",
        "max_primary_shards": "10",
        "result_write_queue_concurrency": "2",
        "result_write_queue_max_heap_percent": "0.01",
        "cold_entity_queue_max_heap_percent": "0.001",
        "ad_result_history_retention_period": "30d",
        "backoff_minutes": "15m",
        "detection_window_delay": "0m",
        "checkpoint_write_queue_max_heap_percent": "0.01",
        "max_entities_for_preview": "5",
        "index_pressure_hard_limit": "0.9",
        "max_model_size_per_node": "100",
        "detection_interval": "10m",
        "max_old_ad_task_docs_per_detector": "1",
        "max_retry_for_backoff": "3",
        "max_anomaly_detectors": "1000"
      }
    },
    "logger": {
      "level": "INFO"
    },
    "processors": "15",
    "ingest": {
      "useragent": {
        "processors": {
          "allowed": []
        }
      },
      "geoip": {
        "cache_size": "1000",
        "processors": {
          "allowed": []
        }
      },
      "common": {
        "processors": {
          "allowed": []
        }
      },
      "user_agent": {
        "cache_size": "1000"
      },
      "grok": {
        "watchdog": {
          "max_execution_time": "1s",
          "interval": "1s"
        }
      }
    },
    "pidfile": "",
    "path": {
      "data": [],
      "logs": "/usr/share/opensearch/logs",
      "shared_data": "",
      "home": "/usr/share/opensearch",
      "repo": []
    },
    "repositories": {
      "fs": {
        "compress": "false",
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
        "shard_count": {
          "limit": "9223372036854775807"
        }
      },
      "destructive_requires_name": "false"
    },
    "rule-threadpool": {
      "queue_size": "100",
      "size": "1"
    },
    "opensearch_dashboards": {
      "system_indices": [
        ".opensearch_dashboards",
        ".opensearch_dashboards_*",
        ".reporting-*",
        ".apm-agent-configuration",
        ".apm-custom-link"
      ]
    },
    "admission_control": {
      "cluster": {
        "admin": {
          "cpu_usage": {
            "limit": "95"
          }
        }
      },
      "search": {
        "cpu_usage": {
          "limit": "95"
        },
        "io_usage": {
          "limit": "95"
        }
      },
      "transport": {
        "cpu_usage": {
          "mode_override": "disabled"
        },
        "mode": "disabled",
        "io_usage": {
          "mode_override": "disabled"
        }
      },
      "indexing": {
        "cpu_usage": {
          "limit": "95"
        },
        "io_usage": {
          "limit": "95"
        }
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
    "point_in_time": {
      "init": {
        "keep_alive": "30s"
      },
      "max_keep_alive": "24h"
    },
    "reindex": {
      "remote": {
        "allowlist": [],
        "retry": {
          "initial_backoff": "500ms",
          "max_count": "15"
        }
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
      "remote_refresh_retry": {
        "core": "1",
        "max": "8",
        "keep_alive": "5m"
      },
      "force_merge": {
        "queue_size": "-1",
        "size": "1"
      },
      "fetch_shard_started": {
        "core": "1",
        "max": "30",
        "keep_alive": "5m"
      },
      "listener": {
        "queue_size": "-1",
        "size": "8"
      },
      "snapshot_deletion": {
        "core": "1",
        "max": "64",
        "keep_alive": "5m"
      },
      "remote_recovery": {
        "core": "1",
        "max": "30",
        "keep_alive": "5m"
      },
      "index_searcher": {
        "queue_size": "1000",
        "size": "30"
      },
      "remote_purge": {
        "core": "1",
        "max": "8",
        "keep_alive": "5m"
      },
      "skills": {
        "queue_size": "100",
        "size": "14"
      },
      "ml_commons": {
        "opensearch_ml_ingest": {
          "queue_size": "30",
          "size": "60"
        },
        "opensearch_ml_register": {
          "queue_size": "10",
          "size": "14"
        },
        "opensearch_ml_predict": {
          "queue_size": "10000",
          "size": "30"
        },
        "opensearch_ml_sdkclient": {
          "queue_size": "10000",
          "size": "60"
        },
        "opensearch_ml_deploy": {
          "queue_size": "10",
          "size": "14"
        },
        "opensearch_ml_execute": {
          "queue_size": "10000",
          "size": "60"
        },
        "opensearch_ml_predict_remote": {
          "queue_size": "10000",
          "size": "60"
        },
        "opensearch_ml_train": {
          "queue_size": "10",
          "size": "14"
        },
        "opensearch_ml_general": {
          "queue_size": "100",
          "size": "14"
        }
      },
      "search": {
        "queue_size": "1000",
        "size": "23"
      },
      "opensearch_asynchronous_search_generic": {
        "core": "1",
        "max": "30",
        "keep_alive": "30m"
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
        "size": "15"
      },
      "remote_state_read": {
        "queue_size": "120000",
        "size": "32"
      },
      "system_read": {
        "queue_size": "2000",
        "size": "5"
      },
      "estimated_time_interval": "200ms",
      "write": {
        "queue_size": "10000",
        "size": "15"
      },
      "flow_framework": {
        "opensearch_provision_workflow": {
          "core": "1",
          "max": "14",
          "keep_alive": "5m"
        },
        "opensearch_deprovision_workflow": {
          "core": "1",
          "max": "14",
          "keep_alive": "1m"
        },
        "opensearch_workflow": {
          "core": "1",
          "max": "14",
          "keep_alive": "1m"
        }
      },
      "query_insights_executor": {
        "core": "1",
        "max": "5",
        "keep_alive": "5m"
      },
      "refresh": {
        "core": "1",
        "max": "8",
        "keep_alive": "5m"
      },
      "remote_state_checksum": {
        "queue_size": "1000",
        "size": "11"
      },
      "translog_sync": {
        "queue_size": "10000",
        "size": "60"
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
      "translog_transfer": {
        "core": "1",
        "max": "8",
        "keep_alive": "5m"
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
        "max": "5",
        "keep_alive": "5m"
      },
      "search_throttled": {
        "queue_size": "100",
        "size": "1"
      }
    },
    "index": {
      "codec": "default",
      "recovery": {
        "type": ""
      },
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
        "type": "",
        "fs": {
          "fs_lock": "native"
        },
        "preload": []
      },
      "composite_store": {
        "type": "default"
      }
    },
    "replication_leader": {
      "queue_size": "1000",
      "size": "23"
    },
    "task_cancellation": {
      "duration_millis": "10000",
      "enabled": "true"
    },
    "script": {
      "allowed_contexts": [],
      "max_compilations_rate": "use-context",
      "cache": {
        "max_size": "100",
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
        "limit": "10%"
      }
    },
    "node": {
      "data": "true",
      "resource": {
        "tracker": {
          "global_cpu_usage": {
            "window_duration": "30s"
          },
          "global_io_usage": {
            "window_duration": "120s"
          },
          "global_jvmmp": {
            "window_duration": "30s"
          }
        }
      },
      "roles": [
        "data",
        "cluster_manager"
      ],
      "max_local_storage_nodes": "1",
      "processors": "15",
      "store": {
        "allow_mmap": "true"
      },
      "ingest": "true",
      "master": "true",
      "pidfile": "",
      "search": {
        "cache": {
          "size": "0"
        }
      },
      "remote_cluster_client": "true",
      "enable_lucene_segment_infos_trace": "false",
      "local_storage": "true",
      "name": "os-cluster-data-1",
      "auto_force_merge": {
        "jvm": {
          "threshold": "75.0"
        },
        "scheduler": {
          "interval": "30m"
        },
        "disk": {
          "threshold": "90.0"
        },
        "merge_delay": "10s",
        "translog": {
          "age": "30m"
        },
        "segment": {
          "count": "1"
        },
        "cpu": {
          "threshold": "80.0"
        },
        "threads": {
          "concurrency_multiplier": "2"
        }
      },
      "id": {
        "seed": "0"
      },
      "attr": {
        "shard_indexing_pressure_enabled": "true"
      },
      "portsfile": "false"
    },
    "null": {
      "queue_size": "1000",
      "size": "15"
    },
    "_plugin_geospatial_ip2geo_datasource_update": {
      "queue_size": "1000",
      "size": "1"
    },
    "http": {
      "cors": {
        "max-age": "1728000",
        "allow-origin": "",
        "allow-headers": "X-Requested-With,Content-Type,Content-Length",
        "allow-credentials": "false",
        "allow-methods": "OPTIONS,HEAD,GET,POST,PUT,DELETE",
        "enabled": "false"
      },
      "connect_timeout": "0ms",
      "max_chunk_size": "8192b",
      "compression_level": "3",
      "max_initial_line_length": "4096b",
      "type": "org.opensearch.security.http.SecurityHttpServerTransport",
      "pipelining": {
        "max_events": "10000"
      },
      "type.default": "netty4",
      "content_type": {
        "required": "true"
      },
      "host": [],
      "publish_port": "-1",
      "read_timeout": "0ms",
      "max_content_length": "100mb",
      "netty": {
        "receive_predictor_size": "65536b",
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
      "port": "9200",
      "max_header_size": "16384b",
      "tcp_no_delay": "true",
      "compression": "false",
      "publish_host": []
    },
    "wlm": {
      "workload_group": {
        "mode": "monitor_only",
        "node": {
          "memory_rejection_threshold": "0.8",
          "memory_cancellation_threshold": "0.9",
          "cpu_rejection_threshold": "0.8",
          "cpu_cancellation_threshold": "0.9"
        },
        "duress_streak": "3",
        "enforcement_interval": "1000"
      }
    },
    "snapshot": {
      "repository_data": {
        "cache": {
          "threshold": "150323855b"
        }
      },
      "max_shards_allowed_in_status_api": "200000",
      "max_concurrent_operations": "1000"
    },
    "aux": {
      "transport": {
        "types": []
      }
    },
    "bootstrap": {
      "memory_lock": "false",
      "system_call_filter": "true",
      "ctrlhandler": "true"
    },
    "network": {
      "host": [],
      "tcp": {
        "reuse_address": "true",
        "keep_count": "-1",
        "connect_timeout": "30s",
        "keep_interval": "-1",
        "no_delay": "true",
        "keep_alive": "true",
        "receive_buffer_size": "-1b",
        "keep_idle": "-1",
        "send_buffer_size": "-1b"
      },
      "bind_host": [
        "0.0.0.0"
      ],
      "server": "true",
      "breaker": {
        "inflight_requests": {
          "limit": "100%",
          "overhead": "2.0"
        }
      },
      "publish_host": [
        "os-cluster-data-1"
      ]
    },
    "search": {
      "default_search_timeout": "-1",
      "max_aggregation_rewrite_filters": "3000",
      "max_open_pit_context": "300",
      "insights": {
        "top_queries": {
          "excluded_indices": [],
          "cpu": {
            "top_n_size": "10",
            "window_size": "5m",
            "enabled": "true"
          },
          "exporter": {
            "type": "local_index",
            "template_priority": "1847",
            "delete_after_days": "7"
          },
          "memory": {
            "top_n_size": "10",
            "window_size": "5m",
            "enabled": "true"
          },
          "grouping": {
            "group_by": "none",
            "max_groups_excluding_topn": "100",
            "attributes": {
              "field_type": "true",
              "field_name": "true"
            }
          },
          "latency": {
            "top_n_size": "10",
            "window_size": "5m",
            "enabled": "true"
          }
        }
      },
      "keyword_index_or_doc_values_enabled": "false",
      "max_open_scroll_context": "500",
      "query": {
        "fieldtype": {
          "cache": {
            "size": "0.1%"
          }
        },
        "metrics": {
          "enabled": "false"
        }
      },
      "concurrent": {
        "max_slice_count": "4"
      },
      "max_buckets": "65535",
      "aggregation_rewrite_filters": {
        "segment_threshold": {
          "docs_per_bucket": "1000"
        }
      },
      "keep_alive_interval": "1m",
      "max_keep_alive": "24h",
      "derived_field": {
        "enabled": "true"
      },
      "concurrent_segment_search": {
        "mode": "auto",
        "enabled": "false"
      },
      "pipeline": {
        "common": {
          "request": {
            "processors": {
              "allowed": []
            }
          },
          "response": {
            "processors": {
              "allowed": []
            }
          },
          "search": {
            "phase": {
              "results": {
                "processors": {
                  "allowed": []
                }
              }
            }
          }
        }
      },
      "highlight": {
        "term_vector_multi_value": "true"
      },
      "cancel_after_time_interval": "-1",
      "default_allow_partial_results": "true",
      "dynamic_pruning": {
        "cardinality_aggregation": {
          "max_allowed_cardinality": "100"
        }
      },
      "request_stats_enabled": "true",
      "low_level_cancellation": "true",
      "phase_took_enabled": "false",
      "allow_expensive_queries": "true",
      "default_keep_alive": "5m"
    },
    "security": {
      "manager": {
        "filter_bad_defaults": "true"
      }
    },
    "segrep": {
      "replication": {
        "time": {
          "limit": "0m"
        }
      },
      "pressure": {
        "checkpoint": {
          "limit": "30"
        },
        "time": {
          "limit": "5m"
        },
        "replica": {
          "stale": {
            "limit": "0.5"
          }
        },
        "enabled": "false"
      }
    },
    "cat": {
      "shards": {
        "response": {
          "limit": {
            "number_of_shards": "-1"
          }
        }
      },
      "indices": {
        "response": {
          "limit": {
            "number_of_indices": "-1"
          }
        }
      },
      "segments": {
        "response": {
          "limit": {
            "number_of_indices": "-1"
          }
        }
      }
    },
    "client": {
      "type": "node"
    },
    "opendistro_security_config": {
      "ssl_dual_mode_enabled": "false"
    },
    "rest": {
      "action": {
        "multi": {
          "allow_explicit_index": "true"
        }
      }
    },
    "remote_store": {
      "moving_average_window_size": "20",
      "segment": {
        "pressure": {
          "bytes_lag": {
            "variance_factor": "10.0"
          },
          "consecutive_failures": {
            "limit": "5"
          },
          "time_lag": {
            "variance_factor": "10.0"
          },
          "enabled": "true"
        }
      }
    },
    "replication_follower": {
      "core": "1",
      "max": "10",
      "keep_alive": "1m"
    },
    "knn": {
      "remote_index_build": {
        "client": {
          "timeout": "60m"
        },
        "poll": {
          "interval": "5s"
        },
        "repository": "",
        "size": {
          "max": "0b"
        },
        "enabled": "false",
        "service": {
          "endpoint": ""
        }
      },
      "algo_param": {
        "index_thread_qty": "1"
      },
      "cache": {
        "item": {
          "expiry": {
            "enabled": "false",
            "minutes": "3h"
          }
        }
      },
      "memory": {
        "circuit_breaker": {
          "limit": "50%",
          "enabled": "true"
        }
      },
      "feature": {
        "cache": {
          "force_evict": {
            "enabled": "false"
          }
        }
      },
      "queue_size": "1",
      "size": "1",
      "faiss": {
        "avx512_spr": {
          "disabled": "false"
        },
        "avx2": {
          "disabled": "false"
        },
        "avx512": {
          "disabled": "false"
        }
      },
      "circuit_breaker": {
        "unset": {
          "percentage": "75.0"
        },
        "triggered": "false"
      },
      "model": {
        "index": {
          "number_of_shards": "1",
          "number_of_replicas": "1"
        },
        "cache": {
          "size": {
            "limit": "10%"
          }
        }
      },
      "vector_streaming_memory": {
        "limit": "1%"
      },
      "quantization": {
        "cache": {
          "size": {
            "limit": "5%"
          },
          "expiry": {
            "minutes": "60m"
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
          "healthy_timeout_threshold": "60s",
          "refresh_interval": "60s",
          "enabled": "true",
          "slow_path_logging_threshold": "5s"
        },
        "refresh_interval": "1s"
      }
    },
    "ltr": {
      "breaker": {
        "enabled": "true"
      },
      "caches": {
        "expire_after_write": "1h",
        "expire_after_read": "1h",
        "max_mem": "10mb"
      },
      "plugin": {
        "enabled": "true"
      }
    },
    "transport": {
      "tcp": {
        "reuse_address": "true",
        "keep_count": "-1",
        "connect_timeout": "30s",
        "keep_interval": "-1",
        "compress": "false",
        "port": "9300-9400",
        "no_delay": "true",
        "keep_alive": "true",
        "receive_buffer_size": "-1b",
        "keep_idle": "-1",
        "send_buffer_size": "-1b"
      },
      "bind_host": [],
      "connect_timeout": "30s",
      "compress": "false",
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
          "internal:coordination/fault_detection/*",
          "cluster:monitor/nodes/liveness"
        ]
      },
      "type": "org.opensearch.security.ssl.http.netty.SecuritySSLNettyTransport",
      "ssl": {
        "dual_mode": {
          "enabled": "false"
        },
        "resolve_hostname": "true",
        "enforce_hostname_verification": "true"
      },
      "slow_operation_logging_threshold": "5s",
      "type.default": "netty4",
      "port": "9300-9400",
      "host": [],
      "publish_port": "-1",
      "tcp_no_delay": "true",
      "publish_host": [],
      "netty": {
        "receive_predictor_size": "65536b",
        "receive_predictor_max": "65536b",
        "worker_count": "15",
        "receive_predictor_min": "65536b",
        "boss_count": "1"
      }
    },
    "task_resource_consumers": {
      "enabled": "false"
    },
    "cluster_manager": {
      "throttling": {
        "retry": {
          "max": {
            "delay": "30s"
          },
          "base": {
            "delay": "5s"
          }
        }
      }
    },
    "indices": {
      "replication": {
        "retry_timeout": "60s",
        "max_bytes_per_sec": "-1b",
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
      "query": {
        "bool": {
          "max_clause_count": "1024"
        },
        "query_string": {
          "analyze_wildcard": "false",
          "allowLeadingWildcard": "true"
        }
      },
      "id_field_data": {
        "enabled": "true"
      },
      "recovery": {
        "internal_action_retry_timeout": "1m",
        "recovery_activity_timeout": "1800000ms",
        "retry_delay_network": "5s",
        "chunk_size": "524272b",
        "internal_action_timeout": "15m",
        "retry_delay_state_sync": "500ms",
        "max_concurrent_remote_store_streams": "7",
        "internal_action_long_timeout": "1800000ms",
        "max_concurrent_operations": "1",
        "internal_remote_upload_timeout": "1h",
        "max_bytes_per_sec": "41943040b",
        "max_concurrent_file_chunks": "2"
      },
      "requests": {
        "cache": {
          "maximum_cacheable_size": "0",
          "size": "1%",
          "cleanup": {
            "interval": "1m",
            "staleness_threshold": "0%"
          },
          "opensearch_onheap": {
            "size": "1%",
            "expire": "9223372036854775807nanos"
          },
          "expire": "0ms",
          "store": {
            "name": ""
          },
          "tiered_spillover": {
            "policies": {
              "took_time": {
                "threshold": "0ms"
              }
            },
            "disk": {
              "store": {
                "name": "",
                "policies": {
                  "took_time": {
                    "threshold": "10ms"
                  }
                },
                "size": "1073741824",
                "enabled": "true"
              }
            },
            "onheap": {
              "store": {
                "name": "",
                "size": "1%"
              }
            },
            "segments": "32"
          }
        }
      },
      "store": {
        "delete": {
          "shard": {
            "timeout": "30s"
          }
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
      "composite_index": {
        "translog": {
          "max_flush_threshold_size": "512mb"
        },
        "star_tree": {
          "enabled": "true"
        }
      },
      "fielddata": {
        "cache": {
          "size": "-1b"
        }
      },
      "publish_check_point": {
        "retry_timeout": "5m"
      },
      "time_series_index": {
        "default_index_merge_policy": "default"
      }
    },
    "plugin": {
      "mandatory": []
    },
    "opensearch": {
      "reports": {
        "general": {
          "operationTimeoutMs": "60000",
          "defaultItemsQueryCount": "100"
        }
      },
      "experimental": {
        "feature": {
          "extensions": {
            "enabled": "false"
          },
          "application_templates": {
            "enabled": "false"
          },
          "remote_store": {
            "migration": {
              "enabled": "false"
            }
          },
          "arrow": {
            "streams": {
              "enabled": "false"
            }
          },
          "telemetry": {
            "enabled": "false"
          },
          "merged_segment_warmer": {
            "enabled": "false"
          },
          "writable_warm_index": {
            "enabled": "false"
          }
        },
        "optimization": {
          "termversion": {
            "precommit": {
              "enabled": "false"
            }
          },
          "datetime_formatter_caching": {
            "enabled": "false"
          }
        }
      },
      "forecast": {
        "forecast-threadpool": {
          "core": "1",
          "max": "11",
          "keep_alive": "10m"
        }
      },
      "ad": {
        "ad-threadpool": {
          "core": "1",
          "max": "7",
          "keep_alive": "10m"
        },
        "ad-batch-task-threadpool": {
          "core": "1",
          "max": "1",
          "keep_alive": "10m"
        }
      },
      "observability": {
        "general": {
          "operationTimeoutMs": "60000",
          "defaultItemsQueryCount": "1000"
        },
        "access": {
          "filterBy": "NoFilter",
          "ignoreRoles": [
            "own_index",
            "opensearch_dashboards_user",
            "notebooks_full_access",
            "notebooks_read_access"
          ],
          "adminAccess": "AllObservabilityObjects"
        },
        "polling": {
          "maxLockRetries": "4",
          "jobLockDurationSeconds": "300",
          "maxPollingDurationSeconds": "900",
          "minPollingDurationSeconds": "300"
        }
      },
      "notifications": {
        "core": {
          "allowed_config_types": [
            "slack",
            "chime",
            "microsoft_teams",
            "webhook",
            "email",
            "sns",
            "ses_account",
            "smtp_account",
            "email_group"
          ],
          "tooltip_support": "true",
          "http": {
            "socket_timeout": "50000",
            "host_deny_list": [],
            "max_connections": "60",
            "connection_timeout": "5000",
            "max_connection_per_route": "20"
          },
          "max_http_response_size": "104857600",
          "email": {
            "minimum_header_length": "160",
            "size_limit": "10000000"
          }
        },
        "general": {
          "default_items_query_count": "100",
          "operation_timeout_ms": "60000",
          "filter_by_backend_roles": "false"
        }
      }
    },
    "discovery": {
      "seed_hosts": [
        "os-cluster-discovery"
      ],
      "unconfigured_bootstrap_timeout": "3s",
      "request_peers_timeout": "3000ms",
      "zen": {
        "hosts_provider": [],
        "ping": {
          "unicast": {
            "concurrent_connects": "10",
            "hosts": [],
            "hosts.resolve_timeout": "5s"
          }
        }
      },
      "initial_state_timeout": "30s",
      "cluster_formation_warning_timeout": "10000ms",
      "seed_providers": [],
      "find_peers_interval_during_decommission": "120s",
      "type": "zen",
      "seed_resolver": {
        "max_concurrent_resolvers": "10",
        "timeout": "5s"
      },
      "find_peers_interval": "1000ms",
      "probe": {
        "connect_timeout": "3000ms",
        "handshake_timeout": "1000ms"
      }
    },
    "search_backpressure": {
      "mode": "monitor_only",
      "cancellation_burst": "10.0",
      "cancellation_ratio": "0.1",
      "cancellation_rate": "0.003",
      "search_task": {
        "elapsed_time_millis_threshold": "45000",
        "heap_variance": "2.0",
        "heap_percent_threshold": "0.02",
        "cancellation_burst": "5.0",
        "cpu_time_millis_threshold": "30000",
        "cancellation_ratio": "0.1",
        "cancellation_rate": "0.003",
        "total_heap_percent_threshold": "0.05",
        "heap_moving_average_window_size": "100"
      },
      "node_duress": {
        "cpu_threshold": "0.9",
        "heap_threshold": "0.7",
        "num_successive_breaches": "3"
      },
      "search_shard_task": {
        "elapsed_time_millis_threshold": "30000",
        "heap_variance": "2.0",
        "heap_percent_threshold": "0.005",
        "cancellation_burst": "10.0",
        "cpu_time_millis_threshold": "15000",
        "cancellation_ratio": "0.1",
        "cancellation_rate": "0.003",
        "total_heap_percent_threshold": "0.05",
        "heap_moving_average_window_size": "100"
      }
    },
    "_plugin_neural_search_hybrid_query_executor": {
      "queue_size": "1000",
      "size": "30"
    },
    "shard_indexing_pressure": {
      "primary_parameter": {
        "node": {
          "soft_limit": "0.7"
        },
        "shard": {
          "min_limit": "0.001"
        }
      },
      "enforced": "false",
      "secondary_parameter": {
        "successful_request": {
          "max_outstanding_requests": "100",
          "elapsed_timeout": "300000ms"
        },
        "throughput": {
          "request_size_window": "2000",
          "degradation_factor": "5.0"
        }
      },
      "cache_store": {
        "max_size": "200"
      },
      "enabled": "false",
      "operating_factor": {
        "optimal": "0.85",
        "lower": "0.75",
        "upper": "0.95"
      }
    },
    "ubi": {
      "dataprepper": {
        "url": ""
      }
    },
    "gateway": {
      "recover_after_data_nodes": "-1",
      "expected_data_nodes": "-1",
      "write_dangling_indices_info": "true",
      "auto_import_dangling_indices": "false",
      "slow_write_logging_threshold": "10s",
      "recover_after_time": "0ms"
    }
  }
}
```
