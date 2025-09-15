# Index stats

```
GET logs-benchmark-dev/_stats?human
```

```json
{
  "_shards": {
    "total": 14,
    "successful": 14,
    "failed": 0
  },
  "_all": {
    "primaries": {
      "docs": {
        "count": 1186701783,
        "deleted": 0,
        "total_size": "161gb",
        "total_size_in_bytes": 172901501190
      },
      "shard_stats": {
        "total_count": 7
      },
      "store": {
        "size": "161gb",
        "size_in_bytes": 172901507265,
        "total_data_set_size": "161gb",
        "total_data_set_size_in_bytes": 172901507265,
        "reserved": "0b",
        "reserved_in_bytes": 0
      },
      "indexing": {
        "index_total": 796199948,
        "index_time": "21.9h",
        "index_time_in_millis": 79051538,
        "index_current": 0,
        "index_failed": 0,
        "index_failed_due_to_version_conflict": 0,
        "delete_total": 0,
        "delete_time": "0s",
        "delete_time_in_millis": 0,
        "delete_current": 0,
        "noop_update_total": 0,
        "is_throttled": false,
        "throttle_time": "2.7m",
        "throttle_time_in_millis": 166875,
        "write_load": 0.13190870436172267,
        "recent_write_load": 4.964382658591041e-7,
        "peak_write_load": 1.1209712976327348
      },
      "get": {
        "total": 0,
        "getTime": "0s",
        "time_in_millis": 0,
        "exists_total": 0,
        "exists_time": "0s",
        "exists_time_in_millis": 0,
        "missing_total": 0,
        "missing_time": "0s",
        "missing_time_in_millis": 0,
        "current": 0
      },
      "search": {
        "open_contexts": 0,
        "query_total": 139,
        "query_time": "20.4s",
        "query_time_in_millis": 20454,
        "query_current": 0,
        "query_failure": 0,
        "fetch_total": 31,
        "fetch_time": "403ms",
        "fetch_time_in_millis": 403,
        "fetch_current": 0,
        "fetch_failure": 0,
        "scroll_total": 0,
        "scroll_time": "0s",
        "scroll_time_in_millis": 0,
        "scroll_current": 0,
        "suggest_total": 0,
        "suggest_time": "0s",
        "suggest_time_in_millis": 0,
        "suggest_current": 0,
        "recent_search_load": 2.1930330714393435e-68
      },
      "merges": {
        "current": 0,
        "current_docs": 0,
        "current_size": "0b",
        "current_size_in_bytes": 0,
        "total": 328,
        "total_time": "20h",
        "total_time_in_millis": 72056695,
        "total_docs": 2822182836,
        "total_size": "360.4gb",
        "total_size_in_bytes": 387018470151,
        "total_stopped_time": "0s",
        "total_stopped_time_in_millis": 0,
        "total_throttled_time": "2.8h",
        "total_throttled_time_in_millis": 10260739,
        "total_auto_throttle": "35mb",
        "total_auto_throttle_in_bytes": 36700160
      },
      "refresh": {
        "total": 2560,
        "total_time": "30m",
        "total_time_in_millis": 1803112,
        "external_total": 545,
        "external_total_time": "1.9m",
        "external_total_time_in_millis": 114128,
        "listeners": 0
      },
      "flush": {
        "total": 1988,
        "periodic": 1982,
        "total_time": "4.5h",
        "total_time_in_millis": 16237296,
        "total_time_excluding_waiting": "4.5h",
        "total_time_excluding_waiting_on_lock_in_millis": 16243131
      },
      "warmer": {
        "current": 0,
        "total": 535,
        "total_time": "20ms",
        "total_time_in_millis": 20
      },
      "query_cache": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "total_count": 1795,
        "hit_count": 0,
        "miss_count": 1795,
        "cache_size": 0,
        "cache_count": 0,
        "evictions": 0
      },
      "fielddata": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "evictions": 0,
        "global_ordinals": {
          "build_time": "279ms",
          "build_time_in_millis": 279
        }
      },
      "completion": {
        "size": "0b",
        "size_in_bytes": 0
      },
      "segments": {
        "count": 39,
        "memory": "0b",
        "memory_in_bytes": 0,
        "terms_memory": "0b",
        "terms_memory_in_bytes": 0,
        "stored_fields_memory": "0b",
        "stored_fields_memory_in_bytes": 0,
        "term_vectors_memory": "0b",
        "term_vectors_memory_in_bytes": 0,
        "norms_memory": "0b",
        "norms_memory_in_bytes": 0,
        "points_memory": "0b",
        "points_memory_in_bytes": 0,
        "doc_values_memory": "0b",
        "doc_values_memory_in_bytes": 0,
        "index_writer_memory": "0b",
        "index_writer_memory_in_bytes": 0,
        "version_map_memory": "0b",
        "version_map_memory_in_bytes": 0,
        "fixed_bit_set": "0b",
        "fixed_bit_set_memory_in_bytes": 0,
        "max_unsafe_auto_id_timestamp": -1,
        "file_sizes": {}
      },
      "translog": {
        "operations": 0,
        "size": "385b",
        "size_in_bytes": 385,
        "uncommitted_operations": 0,
        "uncommitted_size": "385b",
        "uncommitted_size_in_bytes": 385,
        "earliest_last_modified_age": 3907380
      },
      "request_cache": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "evictions": 0,
        "hit_count": 0,
        "miss_count": 1
      },
      "recovery": {
        "current_as_source": 0,
        "current_as_target": 0,
        "throttle_time": "12.8m",
        "throttle_time_in_millis": 773597
      },
      "bulk": {
        "total_operations": 199500,
        "total_time": "22.3h",
        "total_time_in_millis": 80501070,
        "total_size_in_bytes": 723353485479,
        "avg_time": "351ms",
        "avg_time_in_millis": 351,
        "avg_size_in_bytes": 3627935
      },
      "dense_vector": {
        "value_count": 0,
        "off_heap": {
          "total_size": "0b",
          "total_size_bytes": 0,
          "total_veb_size": "0b",
          "total_veb_size_bytes": 0,
          "total_vec_size": "0b",
          "total_vec_size_bytes": 0,
          "total_veq_size": "0b",
          "total_veq_size_bytes": 0,
          "total_vex_size": "0b",
          "total_vex_size_bytes": 0
        }
      },
      "sparse_vector": {
        "value_count": 0
      }
    },
    "total": {
      "docs": {
        "count": 2373403566,
        "deleted": 0,
        "total_size": "322gb",
        "total_size_in_bytes": 345759854037
      },
      "shard_stats": {
        "total_count": 14
      },
      "store": {
        "size": "322gb",
        "size_in_bytes": 345759864687,
        "total_data_set_size": "322gb",
        "total_data_set_size_in_bytes": 345759864687,
        "reserved": "0b",
        "reserved_in_bytes": 0
      },
      "indexing": {
        "index_total": 1982897731,
        "index_time": "1.8d",
        "index_time_in_millis": 158038855,
        "index_current": 0,
        "index_failed": 0,
        "index_failed_due_to_version_conflict": 0,
        "delete_total": 0,
        "delete_time": "0s",
        "delete_time_in_millis": 0,
        "delete_current": 0,
        "noop_update_total": 0,
        "is_throttled": false,
        "throttle_time": "3.9m",
        "throttle_time_in_millis": 237242,
        "write_load": 0.12557439647683036,
        "recent_write_load": 3.9433519291149364e-7,
        "peak_write_load": 0.8171252392193985
      },
      "get": {
        "total": 0,
        "getTime": "0s",
        "time_in_millis": 0,
        "exists_total": 0,
        "exists_time": "0s",
        "exists_time_in_millis": 0,
        "missing_total": 0,
        "missing_time": "0s",
        "missing_time_in_millis": 0,
        "current": 0
      },
      "search": {
        "open_contexts": 0,
        "query_total": 402,
        "query_time": "47.8s",
        "query_time_in_millis": 47854,
        "query_current": 0,
        "query_failure": 0,
        "fetch_total": 142,
        "fetch_time": "1.3s",
        "fetch_time_in_millis": 1307,
        "fetch_current": 0,
        "fetch_failure": 0,
        "scroll_total": 0,
        "scroll_time": "0s",
        "scroll_time_in_millis": 0,
        "scroll_current": 0,
        "suggest_total": 0,
        "suggest_time": "0s",
        "suggest_time_in_millis": 0,
        "suggest_current": 0,
        "recent_search_load": 4.93889356195667e-68
      },
      "merges": {
        "current": 0,
        "current_docs": 0,
        "current_size": "0b",
        "current_size_in_bytes": 0,
        "total": 756,
        "total_time": "1.8d",
        "total_time_in_millis": 158141160,
        "total_docs": 6204509602,
        "total_size": "790.2gb",
        "total_size_in_bytes": 848534615381,
        "total_stopped_time": "0s",
        "total_stopped_time_in_millis": 0,
        "total_throttled_time": "7.5h",
        "total_throttled_time_in_millis": 27052078,
        "total_auto_throttle": "70mb",
        "total_auto_throttle_in_bytes": 73400320
      },
      "refresh": {
        "total": 6132,
        "total_time": "1.2h",
        "total_time_in_millis": 4491291,
        "external_total": 1148,
        "external_total_time": "4m",
        "external_total_time_in_millis": 243963,
        "listeners": 0
      },
      "flush": {
        "total": 4944,
        "periodic": 4927,
        "total_time": "11.2h",
        "total_time_in_millis": 40595178,
        "total_time_excluding_waiting": "11.2h",
        "total_time_excluding_waiting_on_lock_in_millis": 40608090
      },
      "warmer": {
        "current": 0,
        "total": 1127,
        "total_time": "53ms",
        "total_time_in_millis": 53
      },
      "query_cache": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "total_count": 2859,
        "hit_count": 0,
        "miss_count": 2859,
        "cache_size": 0,
        "cache_count": 0,
        "evictions": 0
      },
      "fielddata": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "evictions": 0,
        "global_ordinals": {
          "build_time": "431ms",
          "build_time_in_millis": 431
        }
      },
      "completion": {
        "size": "0b",
        "size_in_bytes": 0
      },
      "segments": {
        "count": 63,
        "memory": "0b",
        "memory_in_bytes": 0,
        "terms_memory": "0b",
        "terms_memory_in_bytes": 0,
        "stored_fields_memory": "0b",
        "stored_fields_memory_in_bytes": 0,
        "term_vectors_memory": "0b",
        "term_vectors_memory_in_bytes": 0,
        "norms_memory": "0b",
        "norms_memory_in_bytes": 0,
        "points_memory": "0b",
        "points_memory_in_bytes": 0,
        "doc_values_memory": "0b",
        "doc_values_memory_in_bytes": 0,
        "index_writer_memory": "0b",
        "index_writer_memory_in_bytes": 0,
        "version_map_memory": "0b",
        "version_map_memory_in_bytes": 0,
        "fixed_bit_set": "0b",
        "fixed_bit_set_memory_in_bytes": 0,
        "max_unsafe_auto_id_timestamp": -1,
        "file_sizes": {}
      },
      "translog": {
        "operations": 0,
        "size": "770b",
        "size_in_bytes": 770,
        "uncommitted_operations": 0,
        "uncommitted_size": "770b",
        "uncommitted_size_in_bytes": 770,
        "earliest_last_modified_age": 3907380
      },
      "request_cache": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "evictions": 0,
        "hit_count": 0,
        "miss_count": 2
      },
      "recovery": {
        "current_as_source": 0,
        "current_as_target": 0,
        "throttle_time": "12.8m",
        "throttle_time_in_millis": 773597
      },
      "bulk": {
        "total_operations": 496849,
        "total_time": "1.8d",
        "total_time_in_millis": 161209047,
        "total_size_in_bytes": 1801491056117,
        "avg_time": "395ms",
        "avg_time_in_millis": 395,
        "avg_size_in_bytes": 3629146
      },
      "dense_vector": {
        "value_count": 0,
        "off_heap": {
          "total_size": "0b",
          "total_size_bytes": 0,
          "total_veb_size": "0b",
          "total_veb_size_bytes": 0,
          "total_vec_size": "0b",
          "total_vec_size_bytes": 0,
          "total_veq_size": "0b",
          "total_veq_size_bytes": 0,
          "total_vex_size": "0b",
          "total_vex_size_bytes": 0
        }
      },
      "sparse_vector": {
        "value_count": 0
      }
    }
  },
  "indices": {
    ".ds-logs-benchmark-dev-2025.09.11-000005": {
      "uuid": "e5nx78ioToqCKyf-zOoJsQ",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 197309927,
          "deleted": 0,
          "total_size": "26.7gb",
          "total_size_in_bytes": 28695110261
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.7gb",
          "size_in_bytes": 28695110678,
          "total_data_set_size": "26.7gb",
          "total_data_set_size_in_bytes": 28695110678,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 0,
          "index_time": "0s",
          "index_time_in_millis": 0,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0,
          "recent_write_load": 0,
          "peak_write_load": 0
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 0,
          "query_time": "0s",
          "query_time_in_millis": 0,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 0,
          "fetch_time": "0s",
          "fetch_time_in_millis": 0,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 5,
          "total_time": "1.9h",
          "total_time_in_millis": 6991303,
          "total_docs": 294245750,
          "total_size": "38.2gb",
          "total_size_in_bytes": 41101004671,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "13.8m",
          "total_throttled_time_in_millis": 833916,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 17,
          "total_time": "1.4s",
          "total_time_in_millis": 1435,
          "external_total": 8,
          "external_total_time": "1.6s",
          "external_total_time_in_millis": 1661,
          "listeners": 0
        },
        "flush": {
          "total": 5,
          "periodic": 4,
          "total_time": "13.3s",
          "total_time_in_millis": 13345,
          "total_time_excluding_waiting": "15.7s",
          "total_time_excluding_waiting_on_lock_in_millis": 15777
        },
        "warmer": {
          "current": 0,
          "total": 7,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 0,
          "hit_count": 0,
          "miss_count": 0,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 1,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 34854098
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "6.2m",
          "throttle_time_in_millis": 372758
        },
        "bulk": {
          "total_operations": 0,
          "total_time": "0s",
          "total_time_in_millis": 0,
          "total_size_in_bytes": 0,
          "avg_time": "0s",
          "avg_time_in_millis": 0,
          "avg_size_in_bytes": 0
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 394619854,
          "deleted": 0,
          "total_size": "53.4gb",
          "total_size_in_bytes": 57415199994
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.4gb",
          "size_in_bytes": 57415200828,
          "total_data_set_size": "53.4gb",
          "total_data_set_size_in_bytes": 57415200828,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 197309927,
          "index_time": "3.6h",
          "index_time_in_millis": 13018930,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.13015621121396306,
          "recent_write_load": 3.7059993403390092e-37,
          "peak_write_load": 0.3532440468228376
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 0,
          "query_time": "0s",
          "query_time_in_millis": 0,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 0,
          "fetch_time": "0s",
          "fetch_time_in_millis": 0,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 73,
          "total_time": "6h",
          "total_time_in_millis": 21648090,
          "total_docs": 857918492,
          "total_size": "109.9gb",
          "total_size_in_bytes": 118013007397,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "59.8m",
          "total_throttled_time_in_millis": 3589299,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 546,
          "total_time": "7.1m",
          "total_time_in_millis": 429028,
          "external_total": 42,
          "external_total_time": "10.5s",
          "external_total_time_in_millis": 10512,
          "listeners": 0
        },
        "flush": {
          "total": 498,
          "periodic": 495,
          "total_time": "1.1h",
          "total_time_in_millis": 4035840,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 4040277
        },
        "warmer": {
          "current": 0,
          "total": 39,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 0,
          "hit_count": 0,
          "miss_count": 0,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 2,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 34854098
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "6.2m",
          "throttle_time_in_millis": 372758
        },
        "bulk": {
          "total_operations": 49445,
          "total_time": "3.6h",
          "total_time_in_millis": 13307993,
          "total_size_in_bytes": 179267680832,
          "avg_time": "944ms",
          "avg_time_in_millis": 944,
          "avg_size_in_bytes": 3633617
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-2025.09.12-000007": {
      "uuid": "NAZMUgtYQf-tBWwHriJnkQ",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 18634346,
          "deleted": 0,
          "total_size": "2.3gb",
          "total_size_in_bytes": 2510672221
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "2.3gb",
          "size_in_bytes": 2510675794,
          "total_data_set_size": "2.3gb",
          "total_data_set_size_in_bytes": 2510675794,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 18634346,
          "index_time": "29m",
          "index_time_in_millis": 1745026,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.2502736530094059,
          "recent_write_load": 0.00004266927304987056,
          "peak_write_load": 0.6911987645392734
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 0,
          "query_time": "0s",
          "query_time_in_millis": 0,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 0,
          "fetch_time": "0s",
          "fetch_time_in_millis": 0,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 7,
          "total_time": "10.7m",
          "total_time_in_millis": 643388,
          "total_docs": 19880156,
          "total_size": "2.4gb",
          "total_size_in_bytes": 2643687862,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.2m",
          "total_throttled_time_in_millis": 253027,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 77,
          "total_time": "52.2s",
          "total_time_in_millis": 52287,
          "external_total": 27,
          "external_total_time": "6s",
          "external_total_time_in_millis": 6039,
          "listeners": 0
        },
        "flush": {
          "total": 47,
          "periodic": 47,
          "total_time": "6.8m",
          "total_time_in_millis": 408339,
          "total_time_excluding_waiting": "6.8m",
          "total_time_excluding_waiting_on_lock_in_millis": 408337
        },
        "warmer": {
          "current": 0,
          "total": 26,
          "total_time": "1ms",
          "total_time_in_millis": 1
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 0,
          "hit_count": 0,
          "miss_count": 0,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 33,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 3907380
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 4668,
          "total_time": "29.7m",
          "total_time_in_millis": 1784347,
          "total_size_in_bytes": 16928122370,
          "avg_time": "317ms",
          "avg_time_in_millis": 317,
          "avg_size_in_bytes": 3449672
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 37268692,
          "deleted": 0,
          "total_size": "4.6gb",
          "total_size_in_bytes": 5026139534
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "4.6gb",
          "size_in_bytes": 5026145180,
          "total_data_set_size": "4.6gb",
          "total_data_set_size_in_bytes": 5026145180,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 37268692,
          "index_time": "51.7m",
          "index_time_in_millis": 3102472,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.22248912839470614,
          "recent_write_load": 0.00003547934056772819,
          "peak_write_load": 0.6115825129969941
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 0,
          "query_time": "0s",
          "query_time_in_millis": 0,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 0,
          "fetch_time": "0s",
          "fetch_time_in_millis": 0,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 14,
          "total_time": "22.2m",
          "total_time_in_millis": 1337687,
          "total_docs": 40956230,
          "total_size": "5gb",
          "total_size_in_bytes": 5447275653,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "8.7m",
          "total_throttled_time_in_millis": 527403,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 151,
          "total_time": "1.6m",
          "total_time_in_millis": 98390,
          "external_total": 53,
          "external_total_time": "15.6s",
          "external_total_time_in_millis": 15645,
          "listeners": 0
        },
        "flush": {
          "total": 94,
          "periodic": 93,
          "total_time": "12.9m",
          "total_time_in_millis": 774072,
          "total_time_excluding_waiting": "12.9m",
          "total_time_excluding_waiting_on_lock_in_millis": 774070
        },
        "warmer": {
          "current": 0,
          "total": 51,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 0,
          "hit_count": 0,
          "miss_count": 0,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 51,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 3907380
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 9336,
          "total_time": "52.8m",
          "total_time_in_millis": 3170312,
          "total_size_in_bytes": 33856244740,
          "avg_time": "271ms",
          "avg_time_in_millis": 271,
          "avg_size_in_bytes": 3449672
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-2025.09.12-000006": {
      "uuid": "fPbRYudjRbWzqgAEh_dDLw",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 193191908,
          "deleted": 0,
          "total_size": "26.1gb",
          "total_size_in_bytes": 28115420543
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.1gb",
          "size_in_bytes": 28115420960,
          "total_data_set_size": "26.1gb",
          "total_data_set_size_in_bytes": 28115420960,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 0,
          "index_time": "0s",
          "index_time_in_millis": 0,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0,
          "recent_write_load": 0,
          "peak_write_load": 0
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 0,
          "query_time": "0s",
          "query_time_in_millis": 0,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 0,
          "fetch_time": "0s",
          "fetch_time_in_millis": 0,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 2,
          "total_time": "1.2h",
          "total_time_in_millis": 4635585,
          "total_docs": 243492148,
          "total_size": "31.7gb",
          "total_size_in_bytes": 34073509518,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "0s",
          "total_throttled_time_in_millis": 0,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 14,
          "total_time": "1.3s",
          "total_time_in_millis": 1351,
          "external_total": 7,
          "external_total_time": "1.4s",
          "external_total_time_in_millis": 1418,
          "listeners": 0
        },
        "flush": {
          "total": 4,
          "periodic": 3,
          "total_time": "8.2s",
          "total_time_in_millis": 8268,
          "total_time_excluding_waiting": "9.1s",
          "total_time_excluding_waiting_on_lock_in_millis": 9128
        },
        "warmer": {
          "current": 0,
          "total": 5,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 0,
          "hit_count": 0,
          "miss_count": 0,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 1,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 6140706
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "6.6m",
          "throttle_time_in_millis": 400838
        },
        "bulk": {
          "total_operations": 0,
          "total_time": "0s",
          "total_time_in_millis": 0,
          "total_size_in_bytes": 0,
          "avg_time": "0s",
          "avg_time_in_millis": 0,
          "avg_size_in_bytes": 0
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 386383816,
          "deleted": 0,
          "total_size": "52.3gb",
          "total_size_in_bytes": 56249023151
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "52.3gb",
          "size_in_bytes": 56249023985,
          "total_data_set_size": "52.3gb",
          "total_data_set_size_in_bytes": 56249023985,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 193191908,
          "index_time": "3.6h",
          "index_time_in_millis": 13002909,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.3102434622580324,
          "recent_write_load": 3.682121976411163e-8,
          "peak_write_load": 0.46971416129511967
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 0,
          "query_time": "0s",
          "query_time_in_millis": 0,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 0,
          "fetch_time": "0s",
          "fetch_time_in_millis": 0,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 70,
          "total_time": "5.2h",
          "total_time_in_millis": 18905072,
          "total_docs": 819444280,
          "total_size": "105gb",
          "total_size_in_bytes": 112772146752,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "48.2m",
          "total_throttled_time_in_millis": 2896525,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 530,
          "total_time": "7.1m",
          "total_time_in_millis": 431046,
          "external_total": 38,
          "external_total_time": "6s",
          "external_total_time_in_millis": 6075,
          "listeners": 0
        },
        "flush": {
          "total": 487,
          "periodic": 484,
          "total_time": "1.1h",
          "total_time_in_millis": 4030237,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 4031472
        },
        "warmer": {
          "current": 0,
          "total": 35,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 0,
          "hit_count": 0,
          "miss_count": 0,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 2,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 6140706
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "6.6m",
          "throttle_time_in_millis": 400838
        },
        "bulk": {
          "total_operations": 48405,
          "total_time": "3.6h",
          "total_time_in_millis": 13289849,
          "total_size_in_bytes": 175520036157,
          "avg_time": "241ms",
          "avg_time_in_millis": 241,
          "avg_size_in_bytes": 3634290
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-2025.09.11-000003": {
      "uuid": "q8u3CMhyTNaUkv8-d0MLfA",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 193364373,
          "deleted": 0,
          "total_size": "26.2gb",
          "total_size_in_bytes": 28231289423
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.2gb",
          "size_in_bytes": 28231289840,
          "total_data_set_size": "26.2gb",
          "total_data_set_size_in_bytes": 28231289840,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 193364373,
          "index_time": "5.5h",
          "index_time_in_millis": 19902696,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.16132207399800907,
          "recent_write_load": 7.85759789256403e-96,
          "peak_write_load": 1.1226759950521872
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 41,
          "query_time": "5.7s",
          "query_time_in_millis": 5741,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 4,
          "fetch_time": "45ms",
          "fetch_time_in_millis": 45,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 6.420120464196219e-69
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 75,
          "total_time": "4.2h",
          "total_time_in_millis": 15460248,
          "total_docs": 584898779,
          "total_size": "74.5gb",
          "total_size_in_bytes": 80035472726,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "37.1m",
          "total_throttled_time_in_millis": 2229573,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 517,
          "total_time": "6.7m",
          "total_time_in_millis": 406430,
          "external_total": 33,
          "external_total_time": "5.2s",
          "external_total_time_in_millis": 5283,
          "listeners": 0
        },
        "flush": {
          "total": 480,
          "periodic": 479,
          "total_time": "1h",
          "total_time_in_millis": 3943450,
          "total_time_excluding_waiting": "1h",
          "total_time_excluding_waiting_on_lock_in_millis": 3943940
        },
        "warmer": {
          "current": 0,
          "total": 32,
          "total_time": "1ms",
          "total_time_in_millis": 1
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 41,
          "hit_count": 0,
          "miss_count": 41,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 1,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 94272885
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 48456,
          "total_time": "5.6h",
          "total_time_in_millis": 20248320,
          "total_size_in_bytes": 175669537456,
          "avg_time": "360ms",
          "avg_time_in_millis": 360,
          "avg_size_in_bytes": 3630073
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 386728746,
          "deleted": 0,
          "total_size": "52.6gb",
          "total_size_in_bytes": 56479281097
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "52.6gb",
          "size_in_bytes": 56479281931,
          "total_data_set_size": "52.6gb",
          "total_data_set_size_in_bytes": 56479281931,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 386724746,
          "index_time": "9.1h",
          "index_time_in_millis": 32961721,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.13358564544798734,
          "recent_write_load": 6.622615422686725e-96,
          "peak_write_load": 0.8325931573057603
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 97,
          "query_time": "13.3s",
          "query_time_in_millis": 13374,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 15,
          "fetch_time": "107ms",
          "fetch_time_in_millis": 107,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 1.377449782293867e-68
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 144,
          "total_time": "8.1h",
          "total_time_in_millis": 29474845,
          "total_docs": 1128905116,
          "total_size": "143.6gb",
          "total_size_in_bytes": 154229520255,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.4h",
          "total_throttled_time_in_millis": 5102226,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1034,
          "total_time": "13.7m",
          "total_time_in_millis": 825694,
          "external_total": 66,
          "external_total_time": "11.9s",
          "external_total_time_in_millis": 11963,
          "listeners": 0
        },
        "flush": {
          "total": 962,
          "periodic": 959,
          "total_time": "2.1h",
          "total_time_in_millis": 7901498,
          "total_time_excluding_waiting": "2.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 7902593
        },
        "warmer": {
          "current": 0,
          "total": 63,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 97,
          "hit_count": 0,
          "miss_count": 97,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 2,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 94272204
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 96911,
          "total_time": "9.3h",
          "total_time_in_millis": 33598884,
          "total_size_in_bytes": 351335443082,
          "avg_time": "446ms",
          "avg_time_in_millis": 446,
          "avg_size_in_bytes": 3630185
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-2025.09.10-000001": {
      "uuid": "6J3QFIc5TLq_pVj2uHtJpA",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 195598935,
          "deleted": 0,
          "total_size": "26.4gb",
          "total_size_in_bytes": 28442907283
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.4gb",
          "size_in_bytes": 28442907700,
          "total_data_set_size": "26.4gb",
          "total_data_set_size_in_bytes": 28442907700,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 195598935,
          "index_time": "4.7h",
          "index_time_in_millis": 17149998,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.09464324690353387,
          "recent_write_load": 1.1223289869613504e-153,
          "peak_write_load": 1.092606093933559
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 2,
          "query_time": "14ms",
          "query_time_in_millis": 14,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 2,
          "fetch_time": "65ms",
          "fetch_time_in_millis": 65,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 4.026966532653795e-71
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 70,
          "total_time": "3.9h",
          "total_time_in_millis": 14360277,
          "total_docs": 564413031,
          "total_size": "71.6gb",
          "total_size_in_bytes": 76931437162,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "44.2m",
          "total_throttled_time_in_millis": 2656062,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 493,
          "total_time": "7.1m",
          "total_time_in_millis": 429137,
          "external_total": 9,
          "external_total_time": "5.5s",
          "external_total_time_in_millis": 5574,
          "listeners": 0
        },
        "flush": {
          "total": 480,
          "periodic": 479,
          "total_time": "1.1h",
          "total_time_in_millis": 3966818,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 3967525
        },
        "warmer": {
          "current": 0,
          "total": 7,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 2,
          "hit_count": 0,
          "miss_count": 2,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 1,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 151871345
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 49016,
          "total_time": "4.8h",
          "total_time_in_millis": 17499793,
          "total_size_in_bytes": 177704855494,
          "avg_time": "361ms",
          "avg_time_in_millis": 361,
          "avg_size_in_bytes": 3636235
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 391197870,
          "deleted": 0,
          "total_size": "52.9gb",
          "total_size_in_bytes": 56883812706
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "52.9gb",
          "size_in_bytes": 56883813540,
          "total_data_set_size": "52.9gb",
          "total_data_set_size_in_bytes": 56883813540,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 391197870,
          "index_time": "8.3h",
          "index_time_in_millis": 30226604,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "1.1m",
          "throttle_time_in_millis": 70367,
          "write_load": 0.08340370937666815,
          "recent_write_load": 9.99576795658341e-154,
          "peak_write_load": 0.8156577332661538
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 108,
          "query_time": "9.3s",
          "query_time_in_millis": 9373,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 74,
          "fetch_time": "556ms",
          "fetch_time_in_millis": 556,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 9.775813639200592e-69
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 138,
          "total_time": "7.8h",
          "total_time_in_millis": 28158969,
          "total_docs": 1123380853,
          "total_size": "142.5gb",
          "total_size_in_bytes": 153093744071,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.3h",
          "total_throttled_time_in_millis": 4827124,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 984,
          "total_time": "14.4m",
          "total_time_in_millis": 864853,
          "external_total": 18,
          "external_total_time": "6.3s",
          "external_total_time_in_millis": 6375,
          "listeners": 0
        },
        "flush": {
          "total": 960,
          "periodic": 958,
          "total_time": "2.2h",
          "total_time_in_millis": 8047859,
          "total_time_excluding_waiting": "2.2h",
          "total_time_excluding_waiting_on_lock_in_millis": 8050474
        },
        "warmer": {
          "current": 0,
          "total": 14,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 119,
          "hit_count": 0,
          "miss_count": 119,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 2,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 151868393
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 98032,
          "total_time": "8.5h",
          "total_time_in_millis": 30840121,
          "total_size_in_bytes": 355409710988,
          "avg_time": "360ms",
          "avg_time_in_millis": 360,
          "avg_size_in_bytes": 3636256
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-2025.09.11-000004": {
      "uuid": "RYXc4_LbR7ytmKoSeQie_A",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 194259761,
          "deleted": 0,
          "total_size": "26.6gb",
          "total_size_in_bytes": 28599562391
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.6gb",
          "size_in_bytes": 28599562808,
          "total_data_set_size": "26.6gb",
          "total_data_set_size_in_bytes": 28599562808,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 194259761,
          "index_time": "5.8h",
          "index_time_in_millis": 21082406,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.22292284769566809,
          "recent_write_load": 2.6090755000959357e-66,
          "peak_write_load": 1.3137122932486507
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 52,
          "query_time": "9.5s",
          "query_time_in_millis": 9596,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 16,
          "fetch_time": "251ms",
          "fetch_time_in_millis": 251,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 1.0083883692694147e-68
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 95,
          "total_time": "4.4h",
          "total_time_in_millis": 16091951,
          "total_docs": 596254755,
          "total_size": "76.2gb",
          "total_size_in_bytes": 81856961998,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "34.5m",
          "total_throttled_time_in_millis": 2073394,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 926,
          "total_time": "8.5m",
          "total_time_in_millis": 513861,
          "external_total": 430,
          "external_total_time": "1.4m",
          "external_total_time_in_millis": 85295,
          "listeners": 0
        },
        "flush": {
          "total": 491,
          "periodic": 490,
          "total_time": "1.1h",
          "total_time_in_millis": 4064701,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 4065885
        },
        "warmer": {
          "current": 0,
          "total": 428,
          "total_time": "17ms",
          "total_time_in_millis": 17
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1708,
          "hit_count": 0,
          "miss_count": 1708,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "279ms",
            "build_time_in_millis": 279
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 1,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 64872741
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 1
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 48666,
          "total_time": "5.9h",
          "total_time_in_millis": 21466393,
          "total_size_in_bytes": 176486955781,
          "avg_time": "347ms",
          "avg_time_in_millis": 347,
          "avg_size_in_bytes": 3630207
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 388519522,
          "deleted": 0,
          "total_size": "53.1gb",
          "total_size_in_bytes": 57094425327
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.1gb",
          "size_in_bytes": 57094426161,
          "total_data_set_size": "53.1gb",
          "total_data_set_size_in_bytes": 57094426161,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 388519522,
          "index_time": "9.4h",
          "index_time_in_millis": 33866873,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "write_load": 0.17905247833215943,
          "recent_write_load": 2.1354969413098098e-66,
          "peak_write_load": 0.9128692390802
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 100,
          "query_time": "13.6s",
          "query_time_in_millis": 13636,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 38,
          "fetch_time": "560ms",
          "fetch_time_in_millis": 560,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 1.4129727311665868e-68
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 177,
          "total_time": "8.4h",
          "total_time_in_millis": 30394883,
          "total_docs": 1166283587,
          "total_size": "148.8gb",
          "total_size_in_bytes": 159824530801,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.4h",
          "total_throttled_time_in_millis": 5056881,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1858,
          "total_time": "16.6m",
          "total_time_in_millis": 1001410,
          "external_total": 870,
          "external_total_time": "2.8m",
          "external_total_time_in_millis": 173936,
          "listeners": 0
        },
        "flush": {
          "total": 981,
          "periodic": 979,
          "total_time": "2.2h",
          "total_time_in_millis": 7953032,
          "total_time_excluding_waiting": "2.2h",
          "total_time_excluding_waiting_on_lock_in_millis": 7954543
        },
        "warmer": {
          "current": 0,
          "total": 867,
          "total_time": "41ms",
          "total_time_in_millis": 41
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 2546,
          "hit_count": 0,
          "miss_count": 2546,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "431ms",
            "build_time_in_millis": 431
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 2,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 64871623
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 2
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 97332,
          "total_time": "9.5h",
          "total_time_in_millis": 34536674,
          "total_size_in_bytes": 352973911562,
          "avg_time": "304ms",
          "avg_time_in_millis": 304,
          "avg_size_in_bytes": 3630215
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-2025.09.10-000002": {
      "uuid": "_WkR0Vr1S1WXNVDexotQ0A",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 194342533,
          "deleted": 0,
          "total_size": "26.3gb",
          "total_size_in_bytes": 28306539068
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.3gb",
          "size_in_bytes": 28306539485,
          "total_data_set_size": "26.3gb",
          "total_data_set_size_in_bytes": 28306539485,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 194342533,
          "index_time": "5.3h",
          "index_time_in_millis": 19171412,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "2.7m",
          "throttle_time_in_millis": 166875,
          "write_load": 0.125985053786228,
          "recent_write_load": 9.724750084378035e-125,
          "peak_write_load": 1.3552490843472897
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 44,
          "query_time": "5.1s",
          "query_time_in_millis": 5103,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 9,
          "fetch_time": "42ms",
          "fetch_time_in_millis": 42,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 5.386056892176532e-69
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 74,
          "total_time": "3.8h",
          "total_time_in_millis": 13873943,
          "total_docs": 518998217,
          "total_size": "65.5gb",
          "total_size_in_bytes": 70376396214,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "36.9m",
          "total_throttled_time_in_millis": 2214767,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 516,
          "total_time": "6.6m",
          "total_time_in_millis": 398611,
          "external_total": 31,
          "external_total_time": "8.8s",
          "external_total_time_in_millis": 8858,
          "listeners": 0
        },
        "flush": {
          "total": 481,
          "periodic": 480,
          "total_time": "1h",
          "total_time_in_millis": 3832375,
          "total_time_excluding_waiting": "1h",
          "total_time_excluding_waiting_on_lock_in_millis": 3832539
        },
        "warmer": {
          "current": 0,
          "total": 30,
          "total_time": "1ms",
          "total_time_in_millis": 1
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 44,
          "hit_count": 0,
          "miss_count": 44,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 1,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 123072502
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 48694,
          "total_time": "5.4h",
          "total_time_in_millis": 19502217,
          "total_size_in_bytes": 176564014378,
          "avg_time": "346ms",
          "avg_time_in_millis": 346,
          "avg_size_in_bytes": 3632281
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      },
      "total": {
        "docs": {
          "count": 388685066,
          "deleted": 0,
          "total_size": "52.7gb",
          "total_size_in_bytes": 56611972228
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "52.7gb",
          "size_in_bytes": 56611973062,
          "total_data_set_size": "52.7gb",
          "total_data_set_size_in_bytes": 56611973062,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 388685066,
          "index_time": "8.8h",
          "index_time_in_millis": 31859346,
          "index_current": 0,
          "index_failed": 0,
          "index_failed_due_to_version_conflict": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "2.7m",
          "throttle_time_in_millis": 166875,
          "write_load": 0.10468283573625327,
          "recent_write_load": 8.169713820129614e-125,
          "peak_write_load": 0.9565491404637985
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time_in_millis": 0,
          "exists_total": 0,
          "exists_time": "0s",
          "exists_time_in_millis": 0,
          "missing_total": 0,
          "missing_time": "0s",
          "missing_time_in_millis": 0,
          "current": 0
        },
        "search": {
          "open_contexts": 0,
          "query_total": 97,
          "query_time": "11.4s",
          "query_time_in_millis": 11471,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 15,
          "fetch_time": "84ms",
          "fetch_time_in_millis": 84,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 0,
          "scroll_time": "0s",
          "scroll_time_in_millis": 0,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 1.1708896845761554e-68
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 140,
          "total_time": "7.8h",
          "total_time_in_millis": 28221614,
          "total_docs": 1067621044,
          "total_size": "135.1gb",
          "total_size_in_bytes": 145154390452,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.4h",
          "total_throttled_time_in_millis": 5052620,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1029,
          "total_time": "14m",
          "total_time_in_millis": 840870,
          "external_total": 61,
          "external_total_time": "19.4s",
          "external_total_time_in_millis": 19457,
          "listeners": 0
        },
        "flush": {
          "total": 962,
          "periodic": 959,
          "total_time": "2.1h",
          "total_time_in_millis": 7852640,
          "total_time_excluding_waiting": "2.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 7854661
        },
        "warmer": {
          "current": 0,
          "total": 58,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 97,
          "hit_count": 0,
          "miss_count": 97,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "global_ordinals": {
            "build_time": "0s",
            "build_time_in_millis": 0
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 2,
          "memory": "0b",
          "memory_in_bytes": 0,
          "terms_memory": "0b",
          "terms_memory_in_bytes": 0,
          "stored_fields_memory": "0b",
          "stored_fields_memory_in_bytes": 0,
          "term_vectors_memory": "0b",
          "term_vectors_memory_in_bytes": 0,
          "norms_memory": "0b",
          "norms_memory_in_bytes": 0,
          "points_memory": "0b",
          "points_memory_in_bytes": 0,
          "doc_values_memory": "0b",
          "doc_values_memory_in_bytes": 0,
          "index_writer_memory": "0b",
          "index_writer_memory_in_bytes": 0,
          "version_map_memory": "0b",
          "version_map_memory_in_bytes": 0,
          "fixed_bit_set": "0b",
          "fixed_bit_set_memory_in_bytes": 0,
          "max_unsafe_auto_id_timestamp": -1,
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 123071931
        },
        "request_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0,
          "hit_count": 0,
          "miss_count": 0
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 97388,
          "total_time": "9h",
          "total_time_in_millis": 32465214,
          "total_size_in_bytes": 353128028756,
          "avg_time": "293ms",
          "avg_time_in_millis": 293,
          "avg_size_in_bytes": 3632281
        },
        "dense_vector": {
          "value_count": 0,
          "off_heap": {
            "total_size": "0b",
            "total_size_bytes": 0,
            "total_veb_size": "0b",
            "total_veb_size_bytes": 0,
            "total_vec_size": "0b",
            "total_vec_size_bytes": 0,
            "total_veq_size": "0b",
            "total_veq_size_bytes": 0,
            "total_vex_size": "0b",
            "total_vex_size_bytes": 0
          }
        },
        "sparse_vector": {
          "value_count": 0
        }
      }
    }
  }
}
```