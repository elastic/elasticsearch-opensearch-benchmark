# Index stats

```
GET logs-benchmark-dev/_stats?human
```

```json
{
  "_shards": {
    "total": 20,
    "successful": 20,
    "failed": 0
  },
  "_all": {
    "primaries": {
      "docs": {
        "count": 1186701783,
        "deleted": 0,
        "total_size": "239.3gb",
        "total_size_in_bytes": 256989631207
      },
      "shard_stats": {
        "total_count": 10
      },
      "store": {
        "size": "239.3gb",
        "size_in_bytes": 256989638026,
        "total_data_set_size": "239.3gb",
        "total_data_set_size_in_bytes": 256989638026,
        "reserved": "0b",
        "reserved_in_bytes": 0
      },
      "indexing": {
        "index_total": 1186701783,
        "index_time": "19.3h",
        "index_time_in_millis": 69828161,
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
        "write_load": 0.008663780103807181,
        "recent_write_load": 0,
        "peak_write_load": 0.3384333176712392
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
        "query_total": 10318734,
        "query_time": "7.9d",
        "query_time_in_millis": 690779591,
        "query_current": 0,
        "query_failure": 0,
        "fetch_total": 4855198,
        "fetch_time": "1.9h",
        "fetch_time_in_millis": 7126693,
        "fetch_current": 0,
        "fetch_failure": 0,
        "scroll_total": 178405,
        "scroll_time": "23.4h",
        "scroll_time_in_millis": 84354333,
        "scroll_current": 0,
        "suggest_total": 0,
        "suggest_time": "0s",
        "suggest_time_in_millis": 0,
        "suggest_current": 0,
        "recent_search_load": 0.4653212554980746
      },
      "merges": {
        "current": 0,
        "current_docs": 0,
        "current_size": "0b",
        "current_size_in_bytes": 0,
        "total": 391,
        "total_time": "1.3d",
        "total_time_in_millis": 115852537,
        "total_docs": 3424197741,
        "total_size": "657.3gb",
        "total_size_in_bytes": 705821519952,
        "total_stopped_time": "0s",
        "total_stopped_time_in_millis": 0,
        "total_throttled_time": "13.6h",
        "total_throttled_time_in_millis": 49194525,
        "total_auto_throttle": "50mb",
        "total_auto_throttle_in_bytes": 52428800
      },
      "refresh": {
        "total": 4654,
        "total_time": "24.4m",
        "total_time_in_millis": 1466042,
        "external_total": 340,
        "external_total_time": "1.4m",
        "external_total_time_in_millis": 89958,
        "listeners": 0
      },
      "flush": {
        "total": 4268,
        "periodic": 4259,
        "total_time": "5.6h",
        "total_time_in_millis": 20484830,
        "total_time_excluding_waiting": "5.6h",
        "total_time_excluding_waiting_on_lock_in_millis": 20510084
      },
      "warmer": {
        "current": 0,
        "total": 322,
        "total_time": "20ms",
        "total_time_in_millis": 20
      },
      "query_cache": {
        "memory_size": "1.1mb",
        "memory_size_in_bytes": 1215056,
        "total_count": 16949306,
        "hit_count": 0,
        "miss_count": 16949306,
        "cache_size": 33,
        "cache_count": 33,
        "evictions": 0
      },
      "fielddata": {
        "memory_size": "9.1kb",
        "memory_size_in_bytes": 9408,
        "evictions": 282,
        "global_ordinals": {
          "build_time": "221ms",
          "build_time_in_millis": 221
        }
      },
      "completion": {
        "size": "0b",
        "size_in_bytes": 0
      },
      "segments": {
        "count": 37,
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
        "size": "550b",
        "size_in_bytes": 550,
        "uncommitted_operations": 0,
        "uncommitted_size": "550b",
        "uncommitted_size_in_bytes": 550,
        "earliest_last_modified_age": 682435628
      },
      "request_cache": {
        "memory_size": "235.4kb",
        "memory_size_in_bytes": 241064,
        "evictions": 0,
        "hit_count": 1553098,
        "miss_count": 99
      },
      "recovery": {
        "current_as_source": 0,
        "current_as_target": 0,
        "throttle_time": "0s",
        "throttle_time_in_millis": 0
      },
      "bulk": {
        "total_operations": 297583,
        "total_time": "19.7h",
        "total_time_in_millis": 71197773,
        "total_size_in_bytes": 1078141202468,
        "avg_time": "241ms",
        "avg_time_in_millis": 241,
        "avg_size_in_bytes": 3632338
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
        "total_size": "478.5gb",
        "total_size_in_bytes": 513847749340
      },
      "shard_stats": {
        "total_count": 20
      },
      "store": {
        "size": "478.5gb",
        "size_in_bytes": 513847761277,
        "total_data_set_size": "478.5gb",
        "total_data_set_size_in_bytes": 513847761277,
        "reserved": "0b",
        "reserved_in_bytes": 0
      },
      "indexing": {
        "index_total": 2373403566,
        "index_time": "1.4d",
        "index_time_in_millis": 123151689,
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
        "write_load": 0.007639855259423382,
        "recent_write_load": 0,
        "peak_write_load": 0.29766056406123326
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
        "query_total": 16453326,
        "query_time": "12.5d",
        "query_time_in_millis": 1081754820,
        "query_current": 0,
        "query_failure": 0,
        "fetch_total": 7591610,
        "fetch_time": "3.6h",
        "fetch_time_in_millis": 12990183,
        "fetch_current": 0,
        "fetch_failure": 0,
        "scroll_total": 282000,
        "scroll_time": "1.5d",
        "scroll_time_in_millis": 133539990,
        "scroll_current": 0,
        "suggest_total": 0,
        "suggest_time": "0s",
        "suggest_time_in_millis": 0,
        "suggest_current": 0,
        "recent_search_load": 0.6664557741511277
      },
      "merges": {
        "current": 0,
        "current_docs": 0,
        "current_size": "0b",
        "current_size_in_bytes": 0,
        "total": 776,
        "total_time": "2.6d",
        "total_time_in_millis": 231312006,
        "total_docs": 6832679355,
        "total_size": "1.2tb",
        "total_size_in_bytes": 1408259034351,
        "total_stopped_time": "0s",
        "total_stopped_time_in_millis": 0,
        "total_throttled_time": "1.1d",
        "total_throttled_time_in_millis": 101068406,
        "total_auto_throttle": "100mb",
        "total_auto_throttle_in_bytes": 104857600
      },
      "refresh": {
        "total": 9311,
        "total_time": "47.2m",
        "total_time_in_millis": 2832598,
        "external_total": 699,
        "external_total_time": "3.2m",
        "external_total_time_in_millis": 193897,
        "listeners": 0
      },
      "flush": {
        "total": 8543,
        "periodic": 8522,
        "total_time": "11.1h",
        "total_time_in_millis": 40228202,
        "total_time_excluding_waiting": "11.1h",
        "total_time_excluding_waiting_on_lock_in_millis": 40266623
      },
      "warmer": {
        "current": 0,
        "total": 666,
        "total_time": "39ms",
        "total_time_in_millis": 39
      },
      "query_cache": {
        "memory_size": "1.1mb",
        "memory_size_in_bytes": 1215056,
        "total_count": 21531429,
        "hit_count": 0,
        "miss_count": 21531429,
        "cache_size": 33,
        "cache_count": 33,
        "evictions": 0
      },
      "fielddata": {
        "memory_size": "12kb",
        "memory_size_in_bytes": 12328,
        "evictions": 557,
        "global_ordinals": {
          "build_time": "454ms",
          "build_time_in_millis": 454
        }
      },
      "completion": {
        "size": "0b",
        "size_in_bytes": 0
      },
      "segments": {
        "count": 57,
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
        "size": "1kb",
        "size_in_bytes": 1100,
        "uncommitted_operations": 0,
        "uncommitted_size": "1kb",
        "uncommitted_size_in_bytes": 1100,
        "earliest_last_modified_age": 682433494
      },
      "request_cache": {
        "memory_size": "470.9kb",
        "memory_size_in_bytes": 482208,
        "evictions": 0,
        "hit_count": 2576558,
        "miss_count": 200
      },
      "recovery": {
        "current_as_source": 0,
        "current_as_target": 0,
        "throttle_time": "0s",
        "throttle_time_in_millis": 0
      },
      "bulk": {
        "total_operations": 595166,
        "total_time": "1.4d",
        "total_time_in_millis": 125655835,
        "total_size_in_bytes": 2156282404936,
        "avg_time": "207ms",
        "avg_time_in_millis": 207,
        "avg_size_in_bytes": 3632339
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
    ".ds-logs-benchmark-dev-2025.08.16-000008": {
      "uuid": "GuvU2ilqQX2SDsNH4S67bw",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 126127097,
          "deleted": 0,
          "total_size": "25.4gb",
          "total_size_in_bytes": 27300585988
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "25.4gb",
          "size_in_bytes": 27300586405,
          "total_data_set_size": "25.4gb",
          "total_data_set_size_in_bytes": 27300586405,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 126127097,
          "index_time": "2.6h",
          "index_time_in_millis": 9630750,
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
          "write_load": 0.013053770089204749,
          "recent_write_load": 0,
          "peak_write_load": 0.427965555776882
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
          "query_total": 1490403,
          "query_time": "1.3d",
          "query_time_in_millis": 120780608,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 709845,
          "fetch_time": "18.1m",
          "fetch_time_in_millis": 1091637,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 26550,
          "scroll_time": "3.5h",
          "scroll_time_in_millis": 12637852,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.07217254865495823
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 45,
          "total_time": "3.4h",
          "total_time_in_millis": 12491949,
          "total_docs": 358324559,
          "total_size": "68.6gb",
          "total_size_in_bytes": 73683783218,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.2h",
          "total_throttled_time_in_millis": 4555085,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 498,
          "total_time": "3.8m",
          "total_time_in_millis": 230250,
          "external_total": 34,
          "external_total_time": "6.4s",
          "external_total_time_in_millis": 6445,
          "listeners": 0
        },
        "flush": {
          "total": 460,
          "periodic": 459,
          "total_time": "44.6m",
          "total_time_in_millis": 2681160,
          "total_time_excluding_waiting": "44.6m",
          "total_time_excluding_waiting_on_lock_in_millis": 2681509
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
          "total_count": 1131177,
          "hit_count": 0,
          "miss_count": 1131177,
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
          "earliest_last_modified_age": 711072170
        },
        "request_cache": {
          "memory_size": "23.2kb",
          "memory_size_in_bytes": 23776,
          "evictions": 0,
          "hit_count": 232633,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 31628,
          "total_time": "2.7h",
          "total_time_in_millis": 9809253,
          "total_size_in_bytes": 114591176131,
          "avg_time": "291ms",
          "avg_time_in_millis": 291,
          "avg_size_in_bytes": 3635649
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
          "count": 252254194,
          "deleted": 0,
          "total_size": "50.7gb",
          "total_size_in_bytes": 54536927019
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "50.7gb",
          "size_in_bytes": 54536927852,
          "total_data_set_size": "50.7gb",
          "total_data_set_size_in_bytes": 54536927852,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 252254194,
          "index_time": "4h",
          "index_time_in_millis": 14689196,
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
          "write_load": 0.00995506340947181,
          "recent_write_load": 0,
          "peak_write_load": 0.3281405687367808
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
          "query_total": 1642483,
          "query_time": "1.7d",
          "query_time_in_millis": 151357926,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 761700,
          "fetch_time": "20.4m",
          "fetch_time_in_millis": 1227458,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13348405,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.09164807964845542
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 86,
          "total_time": "6.8h",
          "total_time_in_millis": 24511067,
          "total_docs": 717740791,
          "total_size": "137.5gb",
          "total_size_in_bytes": 147672719572,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.8h",
          "total_throttled_time_in_millis": 10339528,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 993,
          "total_time": "5.6m",
          "total_time_in_millis": 340030,
          "external_total": 67,
          "external_total_time": "13.8s",
          "external_total_time_in_millis": 13852,
          "listeners": 0
        },
        "flush": {
          "total": 920,
          "periodic": 918,
          "total_time": "1.2h",
          "total_time_in_millis": 4556478,
          "total_time_excluding_waiting": "1.2h",
          "total_time_excluding_waiting_on_lock_in_millis": 4558028
        },
        "warmer": {
          "current": 0,
          "total": 63,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245555,
          "hit_count": 0,
          "miss_count": 1245555,
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
          "earliest_last_modified_age": 711072170
        },
        "request_cache": {
          "memory_size": "47kb",
          "memory_size_in_bytes": 48152,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 63256,
          "total_time": "4.1h",
          "total_time_in_millis": 14979190,
          "total_size_in_bytes": 229182352262,
          "avg_time": "246ms",
          "avg_time_in_millis": 246,
          "avg_size_in_bytes": 3635648
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
    ".ds-logs-benchmark-dev-2025.08.16-000007": {
      "uuid": "bYauE9C0S6K8zzgCdB4rvg",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 132072438,
          "deleted": 0,
          "total_size": "26.5gb",
          "total_size_in_bytes": 28561461679
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.5gb",
          "size_in_bytes": 28561462096,
          "total_data_set_size": "26.5gb",
          "total_data_set_size_in_bytes": 28561462096,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 132072438,
          "index_time": "1.8h",
          "index_time_in_millis": 6780660,
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
          "write_load": 0.008866210626778984,
          "recent_write_load": 0,
          "peak_write_load": 0.29892036753145285
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
          "query_total": 748280,
          "query_time": "1.2h",
          "query_time_in_millis": 4494513,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 309250,
          "fetch_time": "8.3m",
          "fetch_time_in_millis": 498134,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 12370,
          "scroll_time": "1.6h",
          "scroll_time_in_millis": 5940326,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.0004317858009525683
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 42,
          "total_time": "3.3h",
          "total_time_in_millis": 12149780,
          "total_docs": 376996211,
          "total_size": "72.2gb",
          "total_size_in_bytes": 77612665551,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.5h",
          "total_throttled_time_in_millis": 5696893,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 510,
          "total_time": "2m",
          "total_time_in_millis": 124010,
          "external_total": 35,
          "external_total_time": "11.8s",
          "external_total_time_in_millis": 11818,
          "listeners": 0
        },
        "flush": {
          "total": 470,
          "periodic": 469,
          "total_time": "33.3m",
          "total_time_in_millis": 1999233,
          "total_time_excluding_waiting": "33.3m",
          "total_time_excluding_waiting_on_lock_in_millis": 2000306
        },
        "warmer": {
          "current": 0,
          "total": 33,
          "total_time": "1ms",
          "total_time_in_millis": 1
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 548044,
          "hit_count": 0,
          "miss_count": 548044,
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
          "earliest_last_modified_age": 737472975
        },
        "request_cache": {
          "memory_size": "23.4kb",
          "memory_size_in_bytes": 23968,
          "evictions": 0,
          "hit_count": 118008,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 33120,
          "total_time": "1.9h",
          "total_time_in_millis": 6937098,
          "total_size_in_bytes": 119999047666,
          "avg_time": "221ms",
          "avg_time_in_millis": 221,
          "avg_size_in_bytes": 3633059
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
          "count": 264144876,
          "deleted": 0,
          "total_size": "53.1gb",
          "total_size_in_bytes": 57102250795
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.1gb",
          "size_in_bytes": 57102251629,
          "total_data_set_size": "53.1gb",
          "total_data_set_size_in_bytes": 57102251629,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 264144876,
          "index_time": "3.4h",
          "index_time_in_millis": 12519001,
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
          "write_load": 0.008184758642010084,
          "recent_write_load": 0,
          "peak_write_load": 0.2799607030761065
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
          "query_total": 1642482,
          "query_time": "1.1d",
          "query_time_in_millis": 96130957,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 704998,
          "fetch_time": "14.3m",
          "fetch_time_in_millis": 859999,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13354308,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.05902047578294526
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 83,
          "total_time": "6.6h",
          "total_time_in_millis": 24030362,
          "total_docs": 745819591,
          "total_size": "142.8gb",
          "total_size_in_bytes": 153387060086,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "3.3h",
          "total_throttled_time_in_millis": 12008093,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1011,
          "total_time": "4.3m",
          "total_time_in_millis": 262624,
          "external_total": 68,
          "external_total_time": "22.3s",
          "external_total_time_in_millis": 22305,
          "listeners": 0
        },
        "flush": {
          "total": 936,
          "periodic": 934,
          "total_time": "1.1h",
          "total_time_in_millis": 4115773,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 4117201
        },
        "warmer": {
          "current": 0,
          "total": 65,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245554,
          "hit_count": 0,
          "miss_count": 1245554,
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
          "earliest_last_modified_age": 737472975
        },
        "request_cache": {
          "memory_size": "47.3kb",
          "memory_size_in_bytes": 48480,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 66240,
          "total_time": "3.5h",
          "total_time_in_millis": 12797762,
          "total_size_in_bytes": 239998095332,
          "avg_time": "186ms",
          "avg_time_in_millis": 186,
          "avg_size_in_bytes": 3633059
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
    ".ds-logs-benchmark-dev-2025.08.15-000004": {
      "uuid": "kFoUm7K0RQeNW8nFV_l19Q",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 132131365,
          "deleted": 0,
          "total_size": "26.7gb",
          "total_size_in_bytes": 28673520463
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.7gb",
          "size_in_bytes": 28673520879,
          "total_data_set_size": "26.7gb",
          "total_data_set_size_in_bytes": 28673520879,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 132131365,
          "index_time": "1.8h",
          "index_time_in_millis": 6760622,
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
          "write_load": 0.007987735224449625,
          "recent_write_load": 0,
          "peak_write_load": 0.290128603609268
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
          "query_total": 949900,
          "query_time": "22.3h",
          "query_time_in_millis": 80426157,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 470016,
          "fetch_time": "9.4m",
          "fetch_time_in_millis": 568596,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 17779,
          "scroll_time": "2.3h",
          "scroll_time_in_millis": 8471913,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.02875719447607324
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 41,
          "total_time": "3.4h",
          "total_time_in_millis": 12390009,
          "total_docs": 385572379,
          "total_size": "74.1gb",
          "total_size_in_bytes": 79634551119,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.6h",
          "total_throttled_time_in_millis": 5835483,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 502,
          "total_time": "2.1m",
          "total_time_in_millis": 128040,
          "external_total": 33,
          "external_total_time": "11.2s",
          "external_total_time_in_millis": 11248,
          "listeners": 0
        },
        "flush": {
          "total": 464,
          "periodic": 463,
          "total_time": "34.3m",
          "total_time_in_millis": 2059564,
          "total_time_excluding_waiting": "34.3m",
          "total_time_excluding_waiting_on_lock_in_millis": 2062127
        },
        "warmer": {
          "current": 0,
          "total": 31,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 745516,
          "hit_count": 0,
          "miss_count": 745516,
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
          "earliest_last_modified_age": 819375329
        },
        "request_cache": {
          "memory_size": "23.8kb",
          "memory_size_in_bytes": 24392,
          "evictions": 0,
          "hit_count": 134427,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 33135,
          "total_time": "1.9h",
          "total_time_in_millis": 6883005,
          "total_size_in_bytes": 120038139988,
          "avg_time": "236ms",
          "avg_time_in_millis": 236,
          "avg_size_in_bytes": 3632375
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
          "count": 264262730,
          "deleted": 0,
          "total_size": "53.4gb",
          "total_size_in_bytes": 57348108829
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.4gb",
          "size_in_bytes": 57348109661,
          "total_data_set_size": "53.4gb",
          "total_data_set_size_in_bytes": 57348109661,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 264262730,
          "index_time": "3.3h",
          "index_time_in_millis": 11915740,
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
          "write_load": 0.007039249833346172,
          "recent_write_load": 0,
          "peak_write_load": 0.2547936024948092
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
          "query_total": 1642483,
          "query_time": "1.2d",
          "query_time_in_millis": 110441605,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 761400,
          "fetch_time": "22.3m",
          "fetch_time_in_millis": 1342675,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13355109,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.06536049710316283
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 81,
          "total_time": "6.9h",
          "total_time_in_millis": 25157028,
          "total_docs": 770832099,
          "total_size": "148.2gb",
          "total_size_in_bytes": 159222802667,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "3.2h",
          "total_throttled_time_in_millis": 11857955,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1004,
          "total_time": "4.1m",
          "total_time_in_millis": 250031,
          "external_total": 67,
          "external_total_time": "19.3s",
          "external_total_time_in_millis": 19340,
          "listeners": 0
        },
        "flush": {
          "total": 930,
          "periodic": 927,
          "total_time": "1.1h",
          "total_time_in_millis": 4067101,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 4070808
        },
        "warmer": {
          "current": 0,
          "total": 63,
          "total_time": "5ms",
          "total_time_in_millis": 5
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245555,
          "hit_count": 0,
          "miss_count": 1245555,
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
          "earliest_last_modified_age": 819075007
        },
        "request_cache": {
          "memory_size": "47kb",
          "memory_size_in_bytes": 48192,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 66270,
          "total_time": "3.3h",
          "total_time_in_millis": 12150314,
          "total_size_in_bytes": 240076279976,
          "avg_time": "193ms",
          "avg_time_in_millis": 193,
          "avg_size_in_bytes": 3632375
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
    ".ds-logs-benchmark-dev-2025.08.16-000006": {
      "uuid": "jnI7W4VkS26OxUDk1lWWZQ",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 131219400,
          "deleted": 0,
          "total_size": "26.6gb",
          "total_size_in_bytes": 28609541756
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.6gb",
          "size_in_bytes": 28609542173,
          "total_data_set_size": "26.6gb",
          "total_data_set_size_in_bytes": 28609542173,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 131219400,
          "index_time": "2h",
          "index_time_in_millis": 7257404,
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
          "write_load": 0.0091590494473027,
          "recent_write_load": 0,
          "peak_write_load": 0.32143553174912265
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
          "query_total": 1101606,
          "query_time": "17.8h",
          "query_time_in_millis": 64425018,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 496895,
          "fetch_time": "7.9m",
          "fetch_time_in_millis": 476078,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 19876,
          "scroll_time": "2.6h",
          "scroll_time_in_millis": 9363586,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.037964463549517755
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 44,
          "total_time": "3.6h",
          "total_time_in_millis": 13039973,
          "total_docs": 369630837,
          "total_size": "71gb",
          "total_size_in_bytes": 76312521024,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.5h",
          "total_throttled_time_in_millis": 5441421,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 520,
          "total_time": "2.3m",
          "total_time_in_millis": 141842,
          "external_total": 33,
          "external_total_time": "10.3s",
          "external_total_time_in_millis": 10337,
          "listeners": 0
        },
        "flush": {
          "total": 481,
          "periodic": 480,
          "total_time": "35.7m",
          "total_time_in_millis": 2145173,
          "total_time_excluding_waiting": "35.8m",
          "total_time_excluding_waiting_on_lock_in_millis": 2151284
        },
        "warmer": {
          "current": 0,
          "total": 31,
          "total_time": "4ms",
          "total_time_in_millis": 4
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 826827,
          "hit_count": 0,
          "miss_count": 826827,
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
          "earliest_last_modified_age": 764474817
        },
        "request_cache": {
          "memory_size": "23.1kb",
          "memory_size_in_bytes": 23696,
          "evictions": 0,
          "hit_count": 171995,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 32898,
          "total_time": "2h",
          "total_time_in_millis": 7396237,
          "total_size_in_bytes": 119208434776,
          "avg_time": "220ms",
          "avg_time_in_millis": 220,
          "avg_size_in_bytes": 3634193
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
          "count": 262438800,
          "deleted": 0,
          "total_size": "53.2gb",
          "total_size_in_bytes": 57201876390
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.2gb",
          "size_in_bytes": 57201877224,
          "total_data_set_size": "53.2gb",
          "total_data_set_size_in_bytes": 57201877224,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 262438800,
          "index_time": "4.2h",
          "index_time_in_millis": 15305423,
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
          "write_load": 0.009657941420264467,
          "recent_write_load": 0,
          "peak_write_load": 0.3310552779585224
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
          "query_total": 1642481,
          "query_time": "1.4d",
          "query_time_in_millis": 124467966,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 704995,
          "fetch_time": "17.6m",
          "fetch_time_in_millis": 1060540,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13354956,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.0769722788208573
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 90,
          "total_time": "7.4h",
          "total_time_in_millis": 26770533,
          "total_docs": 758063719,
          "total_size": "145.8gb",
          "total_size_in_bytes": 156644509016,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "3h",
          "total_throttled_time_in_millis": 10804562,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1037,
          "total_time": "6.4m",
          "total_time_in_millis": 386398,
          "external_total": 65,
          "external_total_time": "24.2s",
          "external_total_time_in_millis": 24209,
          "listeners": 0
        },
        "flush": {
          "total": 963,
          "periodic": 961,
          "total_time": "1.3h",
          "total_time_in_millis": 4965419,
          "total_time_excluding_waiting": "1.3h",
          "total_time_excluding_waiting_on_lock_in_millis": 4972299
        },
        "warmer": {
          "current": 0,
          "total": 61,
          "total_time": "5ms",
          "total_time_in_millis": 5
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245553,
          "hit_count": 0,
          "miss_count": 1245553,
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
          "earliest_last_modified_age": 764474817
        },
        "request_cache": {
          "memory_size": "46.9kb",
          "memory_size_in_bytes": 48040,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 65796,
          "total_time": "4.3h",
          "total_time_in_millis": 15605126,
          "total_size_in_bytes": 238416869552,
          "avg_time": "239ms",
          "avg_time_in_millis": 239,
          "avg_size_in_bytes": 3634239
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
    ".ds-logs-benchmark-dev-2025.08.14-000001": {
      "uuid": "sWUirOTvTLWF50h-hSAIqw",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 132504311,
          "deleted": 0,
          "total_size": "26.6gb",
          "total_size_in_bytes": 28614957036
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.6gb",
          "size_in_bytes": 28614957452,
          "total_data_set_size": "26.6gb",
          "total_data_set_size_in_bytes": 28614957452,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 132504311,
          "index_time": "1.7h",
          "index_time_in_millis": 6443865,
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
          "write_load": 0.0069408140366535144,
          "recent_write_load": 0,
          "peak_write_load": 0.3142933506236424
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
          "query_total": 1251759,
          "query_time": "22h",
          "query_time_in_millis": 79235412,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 886047,
          "fetch_time": "18.7m",
          "fetch_time_in_millis": 1126877,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 22504,
          "scroll_time": "2.9h",
          "scroll_time_in_millis": 10614570,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.05923405870852763
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 41,
          "total_time": "3.7h",
          "total_time_in_millis": 13486910,
          "total_docs": 385152128,
          "total_size": "73.8gb",
          "total_size_in_bytes": 79348327960,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.4h",
          "total_throttled_time_in_millis": 5256380,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 527,
          "total_time": "2.1m",
          "total_time_in_millis": 129334,
          "external_total": 48,
          "external_total_time": "10.9s",
          "external_total_time_in_millis": 10942,
          "listeners": 0
        },
        "flush": {
          "total": 474,
          "periodic": 473,
          "total_time": "34.3m",
          "total_time_in_millis": 2060619,
          "total_time_excluding_waiting": "34.4m",
          "total_time_excluding_waiting_on_lock_in_millis": 2067175
        },
        "warmer": {
          "current": 0,
          "total": 46,
          "total_time": "4ms",
          "total_time_in_millis": 4
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 980168,
          "hit_count": 0,
          "miss_count": 980168,
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
          "earliest_last_modified_age": 900674546
        },
        "request_cache": {
          "memory_size": "24.4kb",
          "memory_size_in_bytes": 25032,
          "evictions": 0,
          "hit_count": 177132,
          "miss_count": 13
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 33235,
          "total_time": "1.8h",
          "total_time_in_millis": 6571313,
          "total_size_in_bytes": 120381775444,
          "avg_time": "196ms",
          "avg_time_in_millis": 196,
          "avg_size_in_bytes": 3632298
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
          "count": 265008622,
          "deleted": 0,
          "total_size": "53.2gb",
          "total_size_in_bytes": 57227624980
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.2gb",
          "size_in_bytes": 57227625813,
          "total_data_set_size": "53.2gb",
          "total_data_set_size_in_bytes": 57227625813,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 265008622,
          "index_time": "3.2h",
          "index_time_in_millis": 11785071,
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
          "write_load": 0.0063469671301476195,
          "recent_write_load": 0,
          "peak_write_load": 0.29676144598315213
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
          "query_total": 1670987,
          "query_time": "1.1d",
          "query_time_in_millis": 98954934,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 1133525,
          "fetch_time": "24.2m",
          "fetch_time_in_millis": 1455610,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13355243,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.05981901171825176
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 82,
          "total_time": "7.4h",
          "total_time_in_millis": 26797840,
          "total_docs": 768175072,
          "total_size": "147.4gb",
          "total_size_in_bytes": 158275026159,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.9h",
          "total_throttled_time_in_millis": 10579259,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1049,
          "total_time": "4.3m",
          "total_time_in_millis": 263283,
          "external_total": 93,
          "external_total_time": "23.6s",
          "external_total_time_in_millis": 23674,
          "listeners": 0
        },
        "flush": {
          "total": 949,
          "periodic": 947,
          "total_time": "1.1h",
          "total_time_in_millis": 4166537,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 4175333
        },
        "warmer": {
          "current": 0,
          "total": 89,
          "total_time": "8ms",
          "total_time_in_millis": 8
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245597,
          "hit_count": 0,
          "miss_count": 1245597,
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
          "earliest_last_modified_age": 900674318
        },
        "request_cache": {
          "memory_size": "48.9kb",
          "memory_size_in_bytes": 50080,
          "evictions": 0,
          "hit_count": 283304,
          "miss_count": 27
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 66470,
          "total_time": "3.3h",
          "total_time_in_millis": 12022907,
          "total_size_in_bytes": 240763550888,
          "avg_time": "180ms",
          "avg_time_in_millis": 180,
          "avg_size_in_bytes": 3632298
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
    ".ds-logs-benchmark-dev-2025.08.17-000009": {
      "uuid": "Ar4seJuZRUCqgKZDV-9Nwg",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 128792467,
          "deleted": 0,
          "total_size": "25.9gb",
          "total_size_in_bytes": 27904026329
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "25.9gb",
          "size_in_bytes": 27904026746,
          "total_data_set_size": "25.9gb",
          "total_data_set_size_in_bytes": 27904026746,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 128792467,
          "index_time": "2.7h",
          "index_time_in_millis": 9795102,
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
          "write_load": 0.013769243974900171,
          "recent_write_load": 0,
          "peak_write_load": 0.454857980327503
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
          "query_total": 826051,
          "query_time": "1d",
          "query_time_in_millis": 91901862,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 340250,
          "fetch_time": "15.1m",
          "fetch_time_in_millis": 907703,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 13610,
          "scroll_time": "1.8h",
          "scroll_time_in_millis": 6502839,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.06173766522400786
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 47,
          "total_time": "3.6h",
          "total_time_in_millis": 13087606,
          "total_docs": 386582440,
          "total_size": "74.2gb",
          "total_size_in_bytes": 79768148004,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.3h",
          "total_throttled_time_in_millis": 4835392,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 506,
          "total_time": "3.8m",
          "total_time_in_millis": 231993,
          "external_total": 32,
          "external_total_time": "8.6s",
          "external_total_time_in_millis": 8648,
          "listeners": 0
        },
        "flush": {
          "total": 470,
          "periodic": 469,
          "total_time": "45.3m",
          "total_time_in_millis": 2720649,
          "total_time_excluding_waiting": "45.4m",
          "total_time_excluding_waiting_on_lock_in_millis": 2724082
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
          "total_count": 609295,
          "hit_count": 0,
          "miss_count": 609295,
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
          "earliest_last_modified_age": 684071085
        },
        "request_cache": {
          "memory_size": "23.8kb",
          "memory_size_in_bytes": 24416,
          "evictions": 0,
          "hit_count": 138757,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 32299,
          "total_time": "2.7h",
          "total_time_in_millis": 9979495,
          "total_size_in_bytes": 117010762845,
          "avg_time": "300ms",
          "avg_time_in_millis": 300,
          "avg_size_in_bytes": 3637280
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
          "count": 257584934,
          "deleted": 0,
          "total_size": "51.9gb",
          "total_size_in_bytes": 55798113815
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "51.9gb",
          "size_in_bytes": 55798114649,
          "total_data_set_size": "51.9gb",
          "total_data_set_size_in_bytes": 55798114649,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 257584934,
          "index_time": "4.1h",
          "index_time_in_millis": 15056687,
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
          "write_load": 0.010582803241926854,
          "recent_write_load": 0,
          "peak_write_load": 0.34276568868458307
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
          "query_total": 1642480,
          "query_time": "1.5d",
          "query_time_in_millis": 133575071,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 704997,
          "fetch_time": "23.7m",
          "fetch_time_in_millis": 1424440,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13354332,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.08499809959491472
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 90,
          "total_time": "6.9h",
          "total_time_in_millis": 25116159,
          "total_docs": 752769029,
          "total_size": "144.5gb",
          "total_size_in_bytes": 155168699213,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.9h",
          "total_throttled_time_in_millis": 10635874,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1012,
          "total_time": "5.8m",
          "total_time_in_millis": 350072,
          "external_total": 63,
          "external_total_time": "20s",
          "external_total_time_in_millis": 20003,
          "listeners": 0
        },
        "flush": {
          "total": 943,
          "periodic": 941,
          "total_time": "1.2h",
          "total_time_in_millis": 4652941,
          "total_time_excluding_waiting": "1.2h",
          "total_time_excluding_waiting_on_lock_in_millis": 4657045
        },
        "warmer": {
          "current": 0,
          "total": 59,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245552,
          "hit_count": 0,
          "miss_count": 1245552,
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
          "earliest_last_modified_age": 684070227
        },
        "request_cache": {
          "memory_size": "47.1kb",
          "memory_size_in_bytes": 48320,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 64598,
          "total_time": "4.2h",
          "total_time_in_millis": 15363502,
          "total_size_in_bytes": 234021525690,
          "avg_time": "255ms",
          "avg_time_in_millis": 255,
          "avg_size_in_bytes": 3637284
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
    ".ds-logs-benchmark-dev-2025.08.15-000005": {
      "uuid": "IXxa4N6ESGy5xPAxeGvAKg",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 132818201,
          "deleted": 0,
          "total_size": "26.7gb",
          "total_size_in_bytes": 28767747864
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.7gb",
          "size_in_bytes": 28767748281,
          "total_data_set_size": "26.7gb",
          "total_data_set_size_in_bytes": 28767748281,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 132818201,
          "index_time": "1.8h",
          "index_time_in_millis": 6783525,
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
          "write_load": 0.00827890125508557,
          "recent_write_load": 0,
          "peak_write_load": 0.2943960817859761
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
          "query_total": 1253332,
          "query_time": "22.6h",
          "query_time_in_millis": 81617017,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 559374,
          "fetch_time": "12.9m",
          "fetch_time_in_millis": 777519,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 22375,
          "scroll_time": "2.9h",
          "scroll_time_in_millis": 10591785,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.04995729204404346
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 41,
          "total_time": "3.5h",
          "total_time_in_millis": 12785553,
          "total_docs": 387710068,
          "total_size": "74.4gb",
          "total_size_in_bytes": 79968705876,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.7h",
          "total_throttled_time_in_millis": 6129398,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 505,
          "total_time": "2m",
          "total_time_in_millis": 120308,
          "external_total": 32,
          "external_total_time": "8.5s",
          "external_total_time_in_millis": 8552,
          "listeners": 0
        },
        "flush": {
          "total": 469,
          "periodic": 468,
          "total_time": "33m",
          "total_time_in_millis": 1983126,
          "total_time_excluding_waiting": "33.1m",
          "total_time_excluding_waiting_on_lock_in_millis": 1987264
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
          "total_count": 976492,
          "hit_count": 0,
          "miss_count": 976492,
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
          "earliest_last_modified_age": 792070507
        },
        "request_cache": {
          "memory_size": "23.9kb",
          "memory_size_in_bytes": 24488,
          "evictions": 0,
          "hit_count": 176406,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 33304,
          "total_time": "1.9h",
          "total_time_in_millis": 6938547,
          "total_size_in_bytes": 120669894410,
          "avg_time": "235ms",
          "avg_time_in_millis": 235,
          "avg_size_in_bytes": 3632207
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
          "count": 265636402,
          "deleted": 0,
          "total_size": "53.5gb",
          "total_size_in_bytes": 57513940542
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.5gb",
          "size_in_bytes": 57513941375,
          "total_data_set_size": "53.5gb",
          "total_data_set_size_in_bytes": 57513941375,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 265636402,
          "index_time": "3.3h",
          "index_time_in_millis": 12014750,
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
          "write_load": 0.007331657276782205,
          "recent_write_load": 0,
          "peak_write_load": 0.2584766720834451
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
          "query_total": 1642482,
          "query_time": "1d",
          "query_time_in_millis": 89163274,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 704999,
          "fetch_time": "20.3m",
          "fetch_time_in_millis": 1218631,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13354215,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.053177072491317146
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 82,
          "total_time": "7.1h",
          "total_time_in_millis": 25776404,
          "total_docs": 770811479,
          "total_size": "148gb",
          "total_size_in_bytes": 158956013978,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "3.3h",
          "total_throttled_time_in_millis": 12038631,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1007,
          "total_time": "4m",
          "total_time_in_millis": 240216,
          "external_total": 65,
          "external_total_time": "15.7s",
          "external_total_time_in_millis": 15798,
          "listeners": 0
        },
        "flush": {
          "total": 935,
          "periodic": 933,
          "total_time": "1.1h",
          "total_time_in_millis": 3968484,
          "total_time_excluding_waiting": "1.1h",
          "total_time_excluding_waiting_on_lock_in_millis": 3977772
        },
        "warmer": {
          "current": 0,
          "total": 61,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245554,
          "hit_count": 0,
          "miss_count": 1245554,
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
          "earliest_last_modified_age": 792070507
        },
        "request_cache": {
          "memory_size": "47.2kb",
          "memory_size_in_bytes": 48400,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 66608,
          "total_time": "3.4h",
          "total_time_in_millis": 12286131,
          "total_size_in_bytes": 241339788820,
          "avg_time": "187ms",
          "avg_time_in_millis": 187,
          "avg_size_in_bytes": 3632207
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
    ".ds-logs-benchmark-dev-2025.08.14-000002": {
      "uuid": "G_XntVaoRuizjDVFAD_ghg",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 129377605,
          "deleted": 0,
          "total_size": "26gb",
          "total_size_in_bytes": 27988547074
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26gb",
          "size_in_bytes": 27988547491,
          "total_data_set_size": "26gb",
          "total_data_set_size_in_bytes": 27988547491,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 129377605,
          "index_time": "2.5h",
          "index_time_in_millis": 9357319,
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
          "write_load": 0.01038576455567479,
          "recent_write_load": 0,
          "peak_write_load": 0.41533417227029273
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
          "query_total": 929852,
          "query_time": "1.1d",
          "query_time_in_millis": 99523424,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 362600,
          "fetch_time": "14.4m",
          "fetch_time_in_millis": 869252,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 14504,
          "scroll_time": "1.8h",
          "scroll_time_in_millis": 6795007,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.0978440764965544
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 45,
          "total_time": "3.7h",
          "total_time_in_millis": 13456629,
          "total_docs": 387057057,
          "total_size": "74.3gb",
          "total_size_in_bytes": 79800337249,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.4h",
          "total_throttled_time_in_millis": 5297043,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 506,
          "total_time": "3.9m",
          "total_time_in_millis": 234161,
          "external_total": 32,
          "external_total_time": "7.1s",
          "external_total_time_in_millis": 7184,
          "listeners": 0
        },
        "flush": {
          "total": 470,
          "periodic": 469,
          "total_time": "45.9m",
          "total_time_in_millis": 2758157,
          "total_time_excluding_waiting": "45.9m",
          "total_time_excluding_waiting_on_lock_in_millis": 2758514
        },
        "warmer": {
          "current": 0,
          "total": 31,
          "total_time": "1ms",
          "total_time_in_millis": 1
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 717873,
          "hit_count": 0,
          "miss_count": 717873,
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
          "earliest_last_modified_age": 873673973
        },
        "request_cache": {
          "memory_size": "23.8kb",
          "memory_size_in_bytes": 24400,
          "evictions": 0,
          "hit_count": 121065,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 32443,
          "total_time": "2.6h",
          "total_time_in_millis": 9515093,
          "total_size_in_bytes": 117536622810,
          "avg_time": "299ms",
          "avg_time_in_millis": 299,
          "avg_size_in_bytes": 3632590
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
          "count": 258755210,
          "deleted": 0,
          "total_size": "52gb",
          "total_size_in_bytes": 55937802166
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "52gb",
          "size_in_bytes": 55937803000,
          "total_data_set_size": "52gb",
          "total_data_set_size_in_bytes": 55937803000,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 258755210,
          "index_time": "3.9h",
          "index_time_in_millis": 14355285,
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
          "write_load": 0.007966203646787564,
          "recent_write_load": 0,
          "peak_write_load": 0.3156218518825318
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
          "query_total": 1642484,
          "query_time": "1.7d",
          "query_time_in_millis": 150222576,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 705000,
          "fetch_time": "29.5m",
          "fetch_time_in_millis": 1771688,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13356184,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.10613437600156111
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 87,
          "total_time": "7h",
          "total_time_in_millis": 25475495,
          "total_docs": 757217942,
          "total_size": "145.3gb",
          "total_size_in_bytes": 156019104633,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "3h",
          "total_throttled_time_in_millis": 11107142,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1016,
          "total_time": "5.7m",
          "total_time_in_millis": 344610,
          "external_total": 65,
          "external_total_time": "14.7s",
          "external_total_time_in_millis": 14762,
          "listeners": 0
        },
        "flush": {
          "total": 944,
          "periodic": 941,
          "total_time": "1.2h",
          "total_time_in_millis": 4650259,
          "total_time_excluding_waiting": "1.2h",
          "total_time_excluding_waiting_on_lock_in_millis": 4651427
        },
        "warmer": {
          "current": 0,
          "total": 64,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245556,
          "hit_count": 0,
          "miss_count": 1245556,
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
          "earliest_last_modified_age": 873673973
        },
        "request_cache": {
          "memory_size": "47.6kb",
          "memory_size_in_bytes": 48792,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 20
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 64886,
          "total_time": "4h",
          "total_time_in_millis": 14622918,
          "total_size_in_bytes": 235073245620,
          "avg_time": "223ms",
          "avg_time_in_millis": 223,
          "avg_size_in_bytes": 3632590
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
    ".ds-logs-benchmark-dev-2025.08.15-000003": {
      "uuid": "uNUxmWHCQ9qCFvVQU2WZng",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 133612021,
          "deleted": 0,
          "total_size": "26.9gb",
          "total_size_in_bytes": 28924332082
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "26.9gb",
          "size_in_bytes": 28924332499,
          "total_data_set_size": "26.9gb",
          "total_data_set_size_in_bytes": 28924332499,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 133612021,
          "index_time": "1.8h",
          "index_time_in_millis": 6526219,
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
          "write_load": 0.007467279592037897,
          "recent_write_load": 0,
          "peak_write_load": 0.27837913846254564
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
          "query_total": 676713,
          "query_time": "16.8h",
          "query_time_in_millis": 60595308,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 259675,
          "fetch_time": "6.2m",
          "fetch_time_in_millis": 377011,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 10387,
          "scroll_time": "1.3h",
          "scroll_time_in_millis": 4881489,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.04756495332164846
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 42,
          "total_time": "3.5h",
          "total_time_in_millis": 12707432,
          "total_docs": 381134043,
          "total_size": "73.1gb",
          "total_size_in_bytes": 78491549450,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.6h",
          "total_throttled_time_in_millis": 5990298,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 522,
          "total_time": "1.8m",
          "total_time_in_millis": 109942,
          "external_total": 35,
          "external_total_time": "7.3s",
          "external_total_time_in_millis": 7316,
          "listeners": 0
        },
        "flush": {
          "total": 482,
          "periodic": 481,
          "total_time": "32.3m",
          "total_time_in_millis": 1942724,
          "total_time_excluding_waiting": "32.3m",
          "total_time_excluding_waiting_on_lock_in_millis": 1943399
        },
        "warmer": {
          "current": 0,
          "total": 33,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 516323,
          "hit_count": 0,
          "miss_count": 516323,
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
          "earliest_last_modified_age": 846072988
        },
        "request_cache": {
          "memory_size": "23.4kb",
          "memory_size_in_bytes": 23992,
          "evictions": 0,
          "hit_count": 116835,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 33503,
          "total_time": "1.8h",
          "total_time_in_millis": 6665341,
          "total_size_in_bytes": 121396451983,
          "avg_time": "199ms",
          "avg_time_in_millis": 199,
          "avg_size_in_bytes": 3632975
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
          "count": 267224042,
          "deleted": 0,
          "total_size": "53.8gb",
          "total_size_in_bytes": 57860121153
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "53.8gb",
          "size_in_bytes": 57860121987,
          "total_data_set_size": "53.8gb",
          "total_data_set_size_in_bytes": 57860121987,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 267224042,
          "index_time": "4h",
          "index_time_in_millis": 14698408,
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
          "write_load": 0.008408939811900861,
          "recent_write_load": 0,
          "peak_write_load": 0.3166596260501427
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
          "query_total": 1642484,
          "query_time": "1.3d",
          "query_time_in_millis": 117301138,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 705000,
          "fetch_time": "25.3m",
          "fetch_time_in_millis": 1522100,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13356560,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.05944109258567582
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 89,
          "total_time": "7.4h",
          "total_time_in_millis": 26975953,
          "total_docs": 774473750,
          "total_size": "148.5gb",
          "total_size_in_bytes": 159549351301,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "3.1h",
          "total_throttled_time_in_millis": 11224050,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 1068,
          "total_time": "6.1m",
          "total_time_in_millis": 368120,
          "external_total": 94,
          "external_total_time": "28.2s",
          "external_total_time_in_millis": 28243,
          "listeners": 0
        },
        "flush": {
          "total": 966,
          "periodic": 964,
          "total_time": "1.3h",
          "total_time_in_millis": 4833660,
          "total_time_excluding_waiting": "1.3h",
          "total_time_excluding_waiting_on_lock_in_millis": 4835162
        },
        "warmer": {
          "current": 0,
          "total": 91,
          "total_time": "4ms",
          "total_time_in_millis": 4
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1245586,
          "hit_count": 0,
          "miss_count": 1245586,
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
          "earliest_last_modified_age": 846072988
        },
        "request_cache": {
          "memory_size": "47.3kb",
          "memory_size_in_bytes": 48528,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 20
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 67006,
          "total_time": "4.1h",
          "total_time_in_millis": 14999111,
          "total_size_in_bytes": 242792903966,
          "avg_time": "212ms",
          "avg_time_in_millis": 212,
          "avg_size_in_bytes": 3632975
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
    ".ds-logs-benchmark-dev-2025.08.17-000010": {
      "uuid": "sQD2z1CRQfybc39yHa-aLA",
      "health": "green",
      "status": "open",
      "primaries": {
        "docs": {
          "count": 8046878,
          "deleted": 0,
          "total_size": "1.5gb",
          "total_size_in_bytes": 1644910936
        },
        "shard_stats": {
          "total_count": 1
        },
        "store": {
          "size": "1.5gb",
          "size_in_bytes": 1644914004,
          "total_data_set_size": "1.5gb",
          "total_data_set_size_in_bytes": 1644914004,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 8046878,
          "index_time": "8.2m",
          "index_time_in_millis": 492695,
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
          "write_load": 0.0007199196188690346,
          "recent_write_load": 0,
          "peak_write_load": 0.3053950880610038
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
          "query_total": 1090838,
          "query_time": "2.1h",
          "query_time_in_millis": 7780272,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 461246,
          "fetch_time": "7.2m",
          "fetch_time_in_millis": 433886,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 18450,
          "scroll_time": "2.3h",
          "scroll_time_in_millis": 8554966,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.009657217221791041
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 3,
          "total_time": "4.2m",
          "total_time_in_millis": 256696,
          "total_docs": 6038019,
          "total_size": "1.1gb",
          "total_size_in_bytes": 1200930501,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.6m",
          "total_throttled_time_in_millis": 157132,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880
        },
        "refresh": {
          "total": 58,
          "total_time": "16.1s",
          "total_time_in_millis": 16162,
          "external_total": 26,
          "external_total_time": "7.4s",
          "external_total_time_in_millis": 7468,
          "listeners": 0
        },
        "flush": {
          "total": 28,
          "periodic": 28,
          "total_time": "2.2m",
          "total_time_in_millis": 134425,
          "total_time_excluding_waiting": "2.2m",
          "total_time_excluding_waiting_on_lock_in_millis": 134424
        },
        "warmer": {
          "current": 0,
          "total": 25,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "1.1mb",
          "memory_size_in_bytes": 1215056,
          "total_count": 9897591,
          "hit_count": 0,
          "miss_count": 9897591,
          "cache_size": 33,
          "cache_count": 33,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "9.1kb",
          "memory_size_in_bytes": 9408,
          "evictions": 282,
          "global_ordinals": {
            "build_time": "221ms",
            "build_time_in_millis": 221
          }
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 28,
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
          "earliest_last_modified_age": 682435628
        },
        "request_cache": {
          "memory_size": "22.3kb",
          "memory_size_in_bytes": 22904,
          "evictions": 0,
          "hit_count": 165840,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 2018,
          "total_time": "8.3m",
          "total_time_in_millis": 502391,
          "total_size_in_bytes": 7308896415,
          "avg_time": "186ms",
          "avg_time_in_millis": 186,
          "avg_size_in_bytes": 3447120
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
          "count": 16093756,
          "deleted": 0,
          "total_size": "3gb",
          "total_size_in_bytes": 3320983651
        },
        "shard_stats": {
          "total_count": 2
        },
        "store": {
          "size": "3gb",
          "size_in_bytes": 3320988087,
          "total_data_set_size": "3gb",
          "total_data_set_size_in_bytes": 3320988087,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 16093756,
          "index_time": "13.5m",
          "index_time_in_millis": 812128,
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
          "write_load": 0.0005933363417328822,
          "recent_write_load": 0,
          "peak_write_load": 0.2522707969618881
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
          "query_total": 1642480,
          "query_time": "2.8h",
          "query_time_in_millis": 10139373,
          "query_current": 0,
          "query_failure": 0,
          "fetch_total": 704996,
          "fetch_time": "18.4m",
          "fetch_time_in_millis": 1107042,
          "fetch_current": 0,
          "fetch_failure": 0,
          "scroll_total": 28200,
          "scroll_time": "3.7h",
          "scroll_time_in_millis": 13350678,
          "scroll_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "recent_search_load": 0.009884790403986208
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 6,
          "total_time": "11.6m",
          "total_time_in_millis": 701165,
          "total_docs": 16775883,
          "total_size": "3.1gb",
          "total_size_in_bytes": 3363747726,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "7.8m",
          "total_throttled_time_in_millis": 473312,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760
        },
        "refresh": {
          "total": 114,
          "total_time": "27.2s",
          "total_time_in_millis": 27214,
          "external_total": 52,
          "external_total_time": "11.7s",
          "external_total_time_in_millis": 11711,
          "listeners": 0
        },
        "flush": {
          "total": 57,
          "periodic": 56,
          "total_time": "4.1m",
          "total_time_in_millis": 251550,
          "total_time_excluding_waiting": "4.1m",
          "total_time_excluding_waiting_on_lock_in_millis": 251548
        },
        "warmer": {
          "current": 0,
          "total": 50,
          "total_time": "4ms",
          "total_time_in_millis": 4
        },
        "query_cache": {
          "memory_size": "1.1mb",
          "memory_size_in_bytes": 1215056,
          "total_count": 10321367,
          "hit_count": 0,
          "miss_count": 10321367,
          "cache_size": 33,
          "cache_count": 33,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "12kb",
          "memory_size_in_bytes": 12328,
          "evictions": 557,
          "global_ordinals": {
            "build_time": "454ms",
            "build_time_in_millis": 454
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
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 682433494
        },
        "request_cache": {
          "memory_size": "44.1kb",
          "memory_size_in_bytes": 45224,
          "evictions": 0,
          "hit_count": 254806,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        },
        "bulk": {
          "total_operations": 4036,
          "total_time": "13.8m",
          "total_time_in_millis": 828874,
          "total_size_in_bytes": 14617792830,
          "avg_time": "163ms",
          "avg_time_in_millis": 163,
          "avg_size_in_bytes": 3447120
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
