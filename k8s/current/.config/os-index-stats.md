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
        "deleted": 0
      },
      "store": {
        "size": "241.7gb",
        "size_in_bytes": 259574154522,
        "reserved": "0b",
        "reserved_in_bytes": 0
      },
      "indexing": {
        "index_total": 1144051933,
        "index_time": "1.1d",
        "index_time_in_millis": 100433772,
        "index_current": 0,
        "index_failed": 0,
        "delete_total": 0,
        "delete_time": "0s",
        "delete_time_in_millis": 0,
        "delete_current": 0,
        "noop_update_total": 0,
        "is_throttled": false,
        "throttle_time": "0s",
        "throttle_time_in_millis": 0,
        "doc_status": {}
      },
      "get": {
        "total": 0,
        "getTime": "0s",
        "time": "0s",
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
        "query_total": 8158548,
        "query_time": "1.4d",
        "query_time_in_millis": 127844939,
        "query_current": 0,
        "concurrent_query_total": 1195212,
        "concurrent_query_time": "8.4m",
        "concurrent_query_time_in_millis": 505708,
        "concurrent_query_current": 0,
        "concurrent_avg_slice_count": 1.1848400116464695,
        "fetch_total": 3925992,
        "fetch_time": "2.7h",
        "fetch_time_in_millis": 9739384,
        "fetch_current": 0,
        "scroll_total": 142936,
        "scroll_time": "21.3h",
        "scroll_time_in_millis": 76911463,
        "scroll_current": 0,
        "point_in_time_total": 0,
        "point_in_time_time": "0s",
        "point_in_time_time_in_millis": 0,
        "point_in_time_current": 0,
        "suggest_total": 0,
        "suggest_time": "0s",
        "suggest_time_in_millis": 0,
        "suggest_current": 0,
        "search_idle_reactivate_count_total": 0
      },
      "merges": {
        "current": 0,
        "current_docs": 0,
        "current_size": "0b",
        "current_size_in_bytes": 0,
        "total": 1002,
        "total_time": "1.2d",
        "total_time_in_millis": 104768822,
        "total_docs": 3374025801,
        "total_size": "688.8gb",
        "total_size_in_bytes": 739688182565,
        "total_stopped_time": "0s",
        "total_stopped_time_in_millis": 0,
        "total_throttled_time": "20.2h",
        "total_throttled_time_in_millis": 73020406,
        "total_auto_throttle": "50.4mb",
        "total_auto_throttle_in_bytes": 52905425,
        "unreferenced_file_cleanups_performed": 0
      },
      "refresh": {
        "total": 2508,
        "total_time": "9.1m",
        "total_time_in_millis": 546278,
        "external_total": 278,
        "external_total_time": "1m",
        "external_total_time_in_millis": 63815,
        "listeners": 0
      },
      "flush": {
        "total": 2187,
        "periodic": 2186,
        "total_time": "2.6h",
        "total_time_in_millis": 9386293
      },
      "warmer": {
        "current": 0,
        "total": 268,
        "total_time": "12ms",
        "total_time_in_millis": 12
      },
      "query_cache": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "total_count": 15477641,
        "hit_count": 0,
        "miss_count": 15477641,
        "cache_size": 0,
        "cache_count": 0,
        "evictions": 0
      },
      "fielddata": {
        "memory_size": "35kb",
        "memory_size_in_bytes": 35864,
        "evictions": 0
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
        "remote_store": {
          "upload": {
            "total_upload_size": {
              "started": "0b",
              "started_bytes": 0,
              "succeeded": "0b",
              "succeeded_bytes": 0,
              "failed": "0b",
              "failed_bytes": 0
            },
            "refresh_size_lag": {
              "total": "0b",
              "total_bytes": 0,
              "max": "0b",
              "max_bytes": 0
            },
            "max_refresh_time_lag": "0s",
            "max_refresh_time_lag_in_millis": 0,
            "total_time_spent": "0s",
            "total_time_spent_in_millis": 0,
            "pressure": {
              "total_rejections": 0
            }
          },
          "download": {
            "total_download_size": {
              "started": "0b",
              "started_bytes": 0,
              "succeeded": "0b",
              "succeeded_bytes": 0,
              "failed": "0b",
              "failed_bytes": 0
            },
            "total_time_spent": "0s",
            "total_time_spent_in_millis": 0
          }
        },
        "segment_replication": {
          "max_bytes_behind": 0,
          "total_bytes_behind": 0,
          "max_replication_lag": 0
        },
        "file_sizes": {}
      },
      "translog": {
        "operations": 0,
        "size": "550b",
        "size_in_bytes": 550,
        "uncommitted_operations": 0,
        "uncommitted_size": "550b",
        "uncommitted_size_in_bytes": 550,
        "earliest_last_modified_age": 676543176,
        "remote_store": {
          "upload": {
            "total_uploads": {
              "started": 0,
              "failed": 0,
              "succeeded": 0
            },
            "total_upload_size": {
              "started": "0b",
              "started_bytes": 0,
              "failed": "0b",
              "failed_bytes": 0,
              "succeeded": "0b",
              "succeeded_bytes": 0
            }
          }
        }
      },
      "request_cache": {
        "memory_size": "623.6kb",
        "memory_size_in_bytes": 638616,
        "evictions": 0,
        "hit_count": 1195121,
        "miss_count": 98
      },
      "recovery": {
        "current_as_source": 0,
        "current_as_target": 0,
        "throttle_time": "0s",
        "throttle_time_in_millis": 0
      }
    },
    "total": {
      "docs": {
        "count": 2373403566,
        "deleted": 0
      },
      "store": {
        "size": "483.4gb",
        "size_in_bytes": 519109581275,
        "reserved": "0b",
        "reserved_in_bytes": 0
      },
      "indexing": {
        "index_total": 2286866194,
        "index_time": "2.1d",
        "index_time_in_millis": 183713982,
        "index_current": 0,
        "index_failed": 0,
        "delete_total": 0,
        "delete_time": "0s",
        "delete_time_in_millis": 0,
        "delete_current": 0,
        "noop_update_total": 0,
        "is_throttled": false,
        "throttle_time": "0s",
        "throttle_time_in_millis": 0,
        "doc_status": {}
      },
      "get": {
        "total": 0,
        "getTime": "0s",
        "time": "0s",
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
        "query_total": 17489992,
        "query_time": "3.9d",
        "query_time_in_millis": 343561882,
        "query_current": 0,
        "concurrent_query_total": 2730000,
        "concurrent_query_time": "17.3m",
        "concurrent_query_time_in_millis": 1038623,
        "concurrent_query_current": 0,
        "concurrent_avg_slice_count": 1.2967032967032968,
        "fetch_total": 8249979,
        "fetch_time": "5.5h",
        "fetch_time_in_millis": 20129188,
        "fetch_current": 0,
        "scroll_total": 300000,
        "scroll_time": "1.8d",
        "scroll_time_in_millis": 162427880,
        "scroll_current": 0,
        "point_in_time_total": 0,
        "point_in_time_time": "0s",
        "point_in_time_time_in_millis": 0,
        "point_in_time_current": 0,
        "suggest_total": 0,
        "suggest_time": "0s",
        "suggest_time_in_millis": 0,
        "suggest_current": 0,
        "search_idle_reactivate_count_total": 0
      },
      "merges": {
        "current": 0,
        "current_docs": 0,
        "current_size": "0b",
        "current_size_in_bytes": 0,
        "total": 1972,
        "total_time": "2.4d",
        "total_time_in_millis": 210199061,
        "total_docs": 6760877386,
        "total_size": "1.3tb",
        "total_size_in_bytes": 1481737766955,
        "total_stopped_time": "0s",
        "total_stopped_time_in_millis": 0,
        "total_throttled_time": "1.7d",
        "total_throttled_time_in_millis": 147143077,
        "total_auto_throttle": "100.4mb",
        "total_auto_throttle_in_bytes": 105334225,
        "unreferenced_file_cleanups_performed": 0
      },
      "refresh": {
        "total": 5012,
        "total_time": "19m",
        "total_time_in_millis": 1144561,
        "external_total": 555,
        "external_total_time": "2m",
        "external_total_time_in_millis": 124726,
        "listeners": 0
      },
      "flush": {
        "total": 4390,
        "periodic": 4384,
        "total_time": "5.2h",
        "total_time_in_millis": 18891693
      },
      "warmer": {
        "current": 0,
        "total": 536,
        "total_time": "24ms",
        "total_time_in_millis": 24
      },
      "query_cache": {
        "memory_size": "0b",
        "memory_size_in_bytes": 0,
        "total_count": 28842472,
        "hit_count": 0,
        "miss_count": 28842472,
        "cache_size": 0,
        "cache_count": 0,
        "evictions": 0
      },
      "fielddata": {
        "memory_size": "65.3kb",
        "memory_size_in_bytes": 66944,
        "evictions": 0
      },
      "completion": {
        "size": "0b",
        "size_in_bytes": 0
      },
      "segments": {
        "count": 58,
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
        "remote_store": {
          "upload": {
            "total_upload_size": {
              "started": "0b",
              "started_bytes": 0,
              "succeeded": "0b",
              "succeeded_bytes": 0,
              "failed": "0b",
              "failed_bytes": 0
            },
            "refresh_size_lag": {
              "total": "0b",
              "total_bytes": 0,
              "max": "0b",
              "max_bytes": 0
            },
            "max_refresh_time_lag": "0s",
            "max_refresh_time_lag_in_millis": 0,
            "total_time_spent": "0s",
            "total_time_spent_in_millis": 0,
            "pressure": {
              "total_rejections": 0
            }
          },
          "download": {
            "total_download_size": {
              "started": "0b",
              "started_bytes": 0,
              "succeeded": "0b",
              "succeeded_bytes": 0,
              "failed": "0b",
              "failed_bytes": 0
            },
            "total_time_spent": "0s",
            "total_time_spent_in_millis": 0
          }
        },
        "segment_replication": {
          "max_bytes_behind": 0,
          "total_bytes_behind": 0,
          "max_replication_lag": 0
        },
        "file_sizes": {}
      },
      "translog": {
        "operations": 0,
        "size": "1kb",
        "size_in_bytes": 1100,
        "uncommitted_operations": 0,
        "uncommitted_size": "1kb",
        "uncommitted_size_in_bytes": 1100,
        "earliest_last_modified_age": 676242032,
        "remote_store": {
          "upload": {
            "total_uploads": {
              "started": 0,
              "failed": 0,
              "succeeded": 0
            },
            "total_upload_size": {
              "started": "0b",
              "started_bytes": 0,
              "failed": "0b",
              "failed_bytes": 0,
              "succeeded": "0b",
              "succeeded_bytes": 0
            }
          }
        }
      },
      "request_cache": {
        "memory_size": "1.2mb",
        "memory_size_in_bytes": 1275045,
        "evictions": 0,
        "hit_count": 2729817,
        "miss_count": 193
      },
      "recovery": {
        "current_as_source": 0,
        "current_as_target": 0,
        "throttle_time": "0s",
        "throttle_time_in_millis": 0
      }
    }
  },
  "indices": {
    ".ds-logs-benchmark-dev-000009": {
      "uuid": "4fBLQWP3S2O8Ax3tvHQGGg",
      "primaries": {
        "docs": {
          "count": 124543860,
          "deleted": 0
        },
        "store": {
          "size": "25.3gb",
          "size_in_bytes": 27254321009,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 124543860,
          "index_time": "3.7h",
          "index_time_in_millis": 13388787,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 633370,
          "query_time": "27.5m",
          "query_time_in_millis": 1655603,
          "query_current": 0,
          "concurrent_query_total": 120914,
          "concurrent_query_time": "57.7s",
          "concurrent_query_time_in_millis": 57774,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 351323,
          "fetch_time": "15.4m",
          "fetch_time_in_millis": 929683,
          "fetch_current": 0,
          "scroll_total": 14053,
          "scroll_time": "2h",
          "scroll_time_in_millis": 7322632,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 117,
          "total_time": "3.2h",
          "total_time_in_millis": 11829442,
          "total_docs": 370864072,
          "total_size": "75.8gb",
          "total_size_in_bytes": 81435301815,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.1h",
          "total_throttled_time_in_millis": 7740759,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 271,
          "total_time": "1.1m",
          "total_time_in_millis": 70774,
          "external_total": 31,
          "external_total_time": "5.5s",
          "external_total_time_in_millis": 5502,
          "listeners": 0
        },
        "flush": {
          "total": 236,
          "periodic": 236,
          "total_time": "18.6m",
          "total_time_in_millis": 1116601
        },
        "warmer": {
          "current": 0,
          "total": 30,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 461182,
          "hit_count": 0,
          "miss_count": 461182,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 690615693,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "62.6kb",
          "memory_size_in_bytes": 64107,
          "evictions": 0,
          "hit_count": 120905,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 249087720,
          "deleted": 0
        },
        "store": {
          "size": "50.7gb",
          "size_in_bytes": 54486214040,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 249087720,
          "index_time": "5.9h",
          "index_time_in_millis": 21494579,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1739997,
          "query_time": "7.9h",
          "query_time_in_millis": 28618319,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.7m",
          "concurrent_query_time_in_millis": 102959,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 749996,
          "fetch_time": "29.7m",
          "fetch_time_in_millis": 1786676,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16243082,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 219,
          "total_time": "6.3h",
          "total_time_in_millis": 22734381,
          "total_docs": 729874942,
          "total_size": "149.1gb",
          "total_size_in_bytes": 160108759327,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.3h",
          "total_throttled_time_in_millis": 15540323,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 545,
          "total_time": "2.3m",
          "total_time_in_millis": 142485,
          "external_total": 65,
          "external_total_time": "11.4s",
          "external_total_time_in_millis": 11425,
          "listeners": 0
        },
        "flush": {
          "total": 473,
          "periodic": 473,
          "total_time": "35.1m",
          "total_time_in_millis": 2108275
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
          "total_count": 1770016,
          "hit_count": 0,
          "miss_count": 1770016,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 690615693,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.4kb",
          "memory_size_in_bytes": 127473,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000008": {
      "uuid": "kEl5TQUpR1-6QLYP9N6vcw",
      "primaries": {
        "docs": {
          "count": 123817973,
          "deleted": 0
        },
        "store": {
          "size": "25.2gb",
          "size_in_bytes": 27092705284,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 123817973,
          "index_time": "3.7h",
          "index_time_in_millis": 13381583,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 577560,
          "query_time": "38.1m",
          "query_time_in_millis": 2287786,
          "query_current": 0,
          "concurrent_query_total": 105728,
          "concurrent_query_time": "59.5s",
          "concurrent_query_time_in_millis": 59520,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 295339,
          "fetch_time": "13.2m",
          "fetch_time_in_millis": 795444,
          "fetch_current": 0,
          "scroll_total": 11333,
          "scroll_time": "1.6h",
          "scroll_time_in_millis": 6093611,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 114,
          "total_time": "3.3h",
          "total_time_in_millis": 12173830,
          "total_docs": 374717306,
          "total_size": "76.5gb",
          "total_size_in_bytes": 82200614676,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.2h",
          "total_throttled_time_in_millis": 8070773,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 265,
          "total_time": "1.2m",
          "total_time_in_millis": 72768,
          "external_total": 27,
          "external_total_time": "6.4s",
          "external_total_time_in_millis": 6435,
          "listeners": 0
        },
        "flush": {
          "total": 234,
          "periodic": 234,
          "total_time": "18.4m",
          "total_time_in_millis": 1108794
        },
        "warmer": {
          "current": 0,
          "total": 26,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 418745,
          "hit_count": 0,
          "miss_count": 418745,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 717177085,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "62.5kb",
          "memory_size_in_bytes": 64035,
          "evictions": 0,
          "hit_count": 105719,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 247635946,
          "deleted": 0
        },
        "store": {
          "size": "50.4gb",
          "size_in_bytes": 54162127273,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 247635946,
          "index_time": "5.9h",
          "index_time_in_millis": 21294443,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1740000,
          "query_time": "8.8h",
          "query_time_in_millis": 31831135,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.8m",
          "concurrent_query_time_in_millis": 112850,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 809999,
          "fetch_time": "30.4m",
          "fetch_time_in_millis": 1824053,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16241981,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 215,
          "total_time": "6.4h",
          "total_time_in_millis": 23269371,
          "total_docs": 741635116,
          "total_size": "151.3gb",
          "total_size_in_bytes": 162549485854,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.5h",
          "total_throttled_time_in_millis": 16344923,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 534,
          "total_time": "2m",
          "total_time_in_millis": 123237,
          "external_total": 54,
          "external_total_time": "13.8s",
          "external_total_time_in_millis": 13806,
          "listeners": 0
        },
        "flush": {
          "total": 474,
          "periodic": 473,
          "total_time": "34.7m",
          "total_time_in_millis": 2082587
        },
        "warmer": {
          "current": 0,
          "total": 52,
          "total_time": "1ms",
          "total_time_in_millis": 1
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1770019,
          "hit_count": 0,
          "miss_count": 1770019,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 717177085,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.3kb",
          "memory_size_in_bytes": 127329,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000007": {
      "uuid": "zLSMDN_BTS672hAwfRyh2A",
      "primaries": {
        "docs": {
          "count": 124866936,
          "deleted": 0
        },
        "store": {
          "size": "25.4gb",
          "size_in_bytes": 27294022515,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 124866936,
          "index_time": "2.5h",
          "index_time_in_millis": 9141889,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 762391,
          "query_time": "28.3m",
          "query_time_in_millis": 1700563,
          "query_current": 0,
          "concurrent_query_total": 136533,
          "concurrent_query_time": "48.5s",
          "concurrent_query_time_in_millis": 48547,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 343632,
          "fetch_time": "15.1m",
          "fetch_time_in_millis": 907487,
          "fetch_current": 0,
          "scroll_total": 13739,
          "scroll_time": "2h",
          "scroll_time_in_millis": 7467142,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 97,
          "total_time": "2.9h",
          "total_time_in_millis": 10720948,
          "total_docs": 355452379,
          "total_size": "72.4gb",
          "total_size_in_bytes": 77770585793,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2h",
          "total_throttled_time_in_millis": 7499150,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 273,
          "total_time": "51.6s",
          "total_time_in_millis": 51670,
          "external_total": 31,
          "external_total_time": "6.7s",
          "external_total_time_in_millis": 6752,
          "listeners": 0
        },
        "flush": {
          "total": 238,
          "periodic": 238,
          "total_time": "17.3m",
          "total_time_in_millis": 1038628
        },
        "warmer": {
          "current": 0,
          "total": 30,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 555369,
          "hit_count": 0,
          "miss_count": 555369,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 743685334,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "62.6kb",
          "memory_size_in_bytes": 64115,
          "evictions": 0,
          "hit_count": 136524,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 249733872,
          "deleted": 0
        },
        "store": {
          "size": "50.8gb",
          "size_in_bytes": 54597588371,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 249733872,
          "index_time": "4.7h",
          "index_time_in_millis": 17060822,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1739996,
          "query_time": "8h",
          "query_time_in_millis": 28910400,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.6m",
          "concurrent_query_time_in_millis": 96999,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 779994,
          "fetch_time": "31.6m",
          "fetch_time_in_millis": 1900424,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16239698,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 192,
          "total_time": "6h",
          "total_time_in_millis": 21731990,
          "total_docs": 711873649,
          "total_size": "145gb",
          "total_size_in_bytes": 155781050992,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.2h",
          "total_throttled_time_in_millis": 15259257,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 546,
          "total_time": "1.8m",
          "total_time_in_millis": 111744,
          "external_total": 62,
          "external_total_time": "10.4s",
          "external_total_time_in_millis": 10425,
          "listeners": 0
        },
        "flush": {
          "total": 478,
          "periodic": 477,
          "total_time": "34.6m",
          "total_time_in_millis": 2080617
        },
        "warmer": {
          "current": 0,
          "total": 60,
          "total_time": "4ms",
          "total_time_in_millis": 4
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1770015,
          "hit_count": 0,
          "miss_count": 1770015,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 743684485,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.3kb",
          "memory_size_in_bytes": 127385,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000006": {
      "uuid": "kj7jT2IdTWG-QYTbNvNXTQ",
      "primaries": {
        "docs": {
          "count": 123639568,
          "deleted": 0
        },
        "store": {
          "size": "25.2gb",
          "size_in_bytes": 27097954254,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 123639568,
          "index_time": "2.5h",
          "index_time_in_millis": 9231508,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 982963,
          "query_time": "7.6h",
          "query_time_in_millis": 27558489,
          "query_current": 0,
          "concurrent_query_total": 151793,
          "concurrent_query_time": "41.4s",
          "concurrent_query_time_in_millis": 41421,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 410035,
          "fetch_time": "12.2m",
          "fetch_time_in_millis": 736960,
          "fetch_current": 0,
          "scroll_total": 15208,
          "scroll_time": "2.2h",
          "scroll_time_in_millis": 8032700,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 105,
          "total_time": "3.1h",
          "total_time_in_millis": 11183286,
          "total_docs": 371334785,
          "total_size": "75.7gb",
          "total_size_in_bytes": 81301222951,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.3h",
          "total_throttled_time_in_millis": 8408679,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 271,
          "total_time": "45.9s",
          "total_time_in_millis": 45948,
          "external_total": 32,
          "external_total_time": "4.3s",
          "external_total_time_in_millis": 4305,
          "listeners": 0
        },
        "flush": {
          "total": 235,
          "periodic": 235,
          "total_time": "15.6m",
          "total_time_in_millis": 937912
        },
        "warmer": {
          "current": 0,
          "total": 31,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1218224,
          "hit_count": 0,
          "miss_count": 1218224,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 770210328,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "62.5kb",
          "memory_size_in_bytes": 64019,
          "evictions": 0,
          "hit_count": 151784,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 247279136,
          "deleted": 0
        },
        "store": {
          "size": "50.4gb",
          "size_in_bytes": 54221341691,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 247275136,
          "index_time": "5.7h",
          "index_time_in_millis": 20647466,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1740001,
          "query_time": "8.4h",
          "query_time_in_millis": 30479697,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.7m",
          "concurrent_query_time_in_millis": 106747,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 780000,
          "fetch_time": "28.9m",
          "fetch_time_in_millis": 1738731,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16241718,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 219,
          "total_time": "6.5h",
          "total_time_in_millis": 23605783,
          "total_docs": 751915821,
          "total_size": "153.4gb",
          "total_size_in_bytes": 164778709317,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.5h",
          "total_throttled_time_in_millis": 16479068,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 547,
          "total_time": "1.9m",
          "total_time_in_millis": 118981,
          "external_total": 65,
          "external_total_time": "10.6s",
          "external_total_time_in_millis": 10614,
          "listeners": 0
        },
        "flush": {
          "total": 475,
          "periodic": 474,
          "total_time": "34.3m",
          "total_time_in_millis": 2059922
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
          "total_count": 1770020,
          "hit_count": 0,
          "miss_count": 1770020,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 770209881,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.4kb",
          "memory_size_in_bytes": 127409,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000005": {
      "uuid": "PP1CPNk5RXOPFLYwBk5Mxw",
      "primaries": {
        "docs": {
          "count": 124154805,
          "deleted": 0
        },
        "store": {
          "size": "25.2gb",
          "size_in_bytes": 27128586059,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 124154805,
          "index_time": "2.6h",
          "index_time_in_millis": 9606938,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 906246,
          "query_time": "5.6h",
          "query_time_in_millis": 20471097,
          "query_current": 0,
          "concurrent_query_total": 121694,
          "concurrent_query_time": "43.5s",
          "concurrent_query_time_in_millis": 43535,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 392927,
          "fetch_time": "11.8m",
          "fetch_time_in_millis": 708325,
          "fetch_current": 0,
          "scroll_total": 14589,
          "scroll_time": "2.2h",
          "scroll_time_in_millis": 7922656,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 106,
          "total_time": "3h",
          "total_time_in_millis": 11053422,
          "total_docs": 368128212,
          "total_size": "75.1gb",
          "total_size_in_bytes": 80656194230,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.2h",
          "total_throttled_time_in_millis": 8232887,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 274,
          "total_time": "45.3s",
          "total_time_in_millis": 45320,
          "external_total": 32,
          "external_total_time": "5.6s",
          "external_total_time_in_millis": 5623,
          "listeners": 0
        },
        "flush": {
          "total": 238,
          "periodic": 238,
          "total_time": "15.6m",
          "total_time_in_millis": 939601
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
          "total_count": 1131986,
          "hit_count": 0,
          "miss_count": 1131986,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 796721701,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "62.5kb",
          "memory_size_in_bytes": 64043,
          "evictions": 0,
          "hit_count": 121685,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 248309610,
          "deleted": 0
        },
        "store": {
          "size": "50.5gb",
          "size_in_bytes": 54272067443,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 248309610,
          "index_time": "5.8h",
          "index_time_in_millis": 21071904,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1740000,
          "query_time": "12.1h",
          "query_time_in_millis": 43616831,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.8m",
          "concurrent_query_time_in_millis": 113466,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 779999,
          "fetch_time": "30.2m",
          "fetch_time_in_millis": 1817184,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16242319,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 224,
          "total_time": "6.4h",
          "total_time_in_millis": 23314017,
          "total_docs": 743539532,
          "total_size": "151.7gb",
          "total_size_in_bytes": 162926931171,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.5h",
          "total_throttled_time_in_millis": 16273605,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 543,
          "total_time": "1.9m",
          "total_time_in_millis": 118954,
          "external_total": 60,
          "external_total_time": "16.9s",
          "external_total_time_in_millis": 16981,
          "listeners": 0
        },
        "flush": {
          "total": 477,
          "periodic": 476,
          "total_time": "34.2m",
          "total_time_in_millis": 2052244
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
          "total_count": 1770019,
          "hit_count": 0,
          "miss_count": 1770019,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 796721701,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.3kb",
          "memory_size_in_bytes": 127345,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000004": {
      "uuid": "I2ecRTtwQdWc5CiL9KdhsA",
      "primaries": {
        "docs": {
          "count": 124063934,
          "deleted": 0
        },
        "store": {
          "size": "25.3gb",
          "size_in_bytes": 27198987539,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 124063934,
          "index_time": "2.6h",
          "index_time_in_millis": 9383509,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 512127,
          "query_time": "1.7h",
          "query_time_in_millis": 6184669,
          "query_current": 0,
          "concurrent_query_total": 103218,
          "concurrent_query_time": "43s",
          "concurrent_query_time_in_millis": 43030,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 268051,
          "fetch_time": "9.5m",
          "fetch_time_in_millis": 571112,
          "fetch_current": 0,
          "scroll_total": 10717,
          "scroll_time": "1.5h",
          "scroll_time_in_millis": 5572544,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 105,
          "total_time": "3.2h",
          "total_time_in_millis": 11556119,
          "total_docs": 378859285,
          "total_size": "77.3gb",
          "total_size_in_bytes": 83025688199,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.3h",
          "total_throttled_time_in_millis": 8518127,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 273,
          "total_time": "55.3s",
          "total_time_in_millis": 55366,
          "external_total": 30,
          "external_total_time": "8.4s",
          "external_total_time_in_millis": 8403,
          "listeners": 0
        },
        "flush": {
          "total": 238,
          "periodic": 238,
          "total_time": "16m",
          "total_time_in_millis": 961098
        },
        "warmer": {
          "current": 0,
          "total": 29,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 376413,
          "hit_count": 0,
          "miss_count": 376413,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 823152697,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "61.8kb",
          "memory_size_in_bytes": 63358,
          "evictions": 0,
          "hit_count": 103209,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 248127868,
          "deleted": 0
        },
        "store": {
          "size": "50.6gb",
          "size_in_bytes": 54390566136,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 248127868,
          "index_time": "4.7h",
          "index_time_in_millis": 17132368,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1739999,
          "query_time": "9.1h",
          "query_time_in_millis": 32946434,
          "query_current": 0,
          "concurrent_query_total": 270001,
          "concurrent_query_time": "1.6m",
          "concurrent_query_time_in_millis": 100283,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 809996,
          "fetch_time": "33m",
          "fetch_time_in_millis": 1980613,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16241276,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 204,
          "total_time": "6.3h",
          "total_time_in_millis": 22797475,
          "total_docs": 757301261,
          "total_size": "154.5gb",
          "total_size_in_bytes": 165915580394,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.6h",
          "total_throttled_time_in_millis": 16879094,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 540,
          "total_time": "1.7m",
          "total_time_in_millis": 107362,
          "external_total": 59,
          "external_total_time": "15.4s",
          "external_total_time_in_millis": 15466,
          "listeners": 0
        },
        "flush": {
          "total": 474,
          "periodic": 474,
          "total_time": "32.6m",
          "total_time_in_millis": 1958064
        },
        "warmer": {
          "current": 0,
          "total": 57,
          "total_time": "4ms",
          "total_time_in_millis": 4
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1770019,
          "hit_count": 0,
          "miss_count": 1770019,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 823152697,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "125.3kb",
          "memory_size_in_bytes": 128314,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 20
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000003": {
      "uuid": "ImHhOhl7QdaESbigMWq9Fg",
      "primaries": {
        "docs": {
          "count": 124531395,
          "deleted": 0
        },
        "store": {
          "size": "25.3gb",
          "size_in_bytes": 27261773548,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 124531395,
          "index_time": "3.3h",
          "index_time_in_millis": 12023156,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 788727,
          "query_time": "1.3h",
          "query_time_in_millis": 4699879,
          "query_current": 0,
          "concurrent_query_total": 111759,
          "concurrent_query_time": "1m",
          "concurrent_query_time_in_millis": 61438,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 386907,
          "fetch_time": "19.6m",
          "fetch_time_in_millis": 1176083,
          "fetch_current": 0,
          "scroll_total": 15470,
          "scroll_time": "2.3h",
          "scroll_time_in_millis": 8421695,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 112,
          "total_time": "3h",
          "total_time_in_millis": 11152203,
          "total_docs": 350861417,
          "total_size": "71.7gb",
          "total_size_in_bytes": 77065410141,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2h",
          "total_throttled_time_in_millis": 7301053,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 274,
          "total_time": "1m",
          "total_time_in_millis": 62479,
          "external_total": 32,
          "external_total_time": "7.1s",
          "external_total_time_in_millis": 7181,
          "listeners": 0
        },
        "flush": {
          "total": 238,
          "periodic": 238,
          "total_time": "17.4m",
          "total_time_in_millis": 1045709
        },
        "warmer": {
          "current": 0,
          "total": 31,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 565556,
          "hit_count": 0,
          "miss_count": 565556,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 849351054,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "62.5kb",
          "memory_size_in_bytes": 64091,
          "evictions": 0,
          "hit_count": 111750,
          "miss_count": 10
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 249062790,
          "deleted": 0
        },
        "store": {
          "size": "50.7gb",
          "size_in_bytes": 54500154642,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 249062790,
          "index_time": "5.5h",
          "index_time_in_millis": 19896268,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1739999,
          "query_time": "9.5h",
          "query_time_in_millis": 34325236,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.8m",
          "concurrent_query_time_in_millis": 109701,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 779998,
          "fetch_time": "31.4m",
          "fetch_time_in_millis": 1885425,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16243984,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 215,
          "total_time": "6.1h",
          "total_time_in_millis": 22055751,
          "total_docs": 711391177,
          "total_size": "145.3gb",
          "total_size_in_bytes": 156074843722,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.2h",
          "total_throttled_time_in_millis": 15332114,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 551,
          "total_time": "2.2m",
          "total_time_in_millis": 133019,
          "external_total": 63,
          "external_total_time": "13.4s",
          "external_total_time_in_millis": 13473,
          "listeners": 0
        },
        "flush": {
          "total": 482,
          "periodic": 482,
          "total_time": "33.5m",
          "total_time_in_millis": 2015645
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
          "total_count": 1770018,
          "hit_count": 0,
          "miss_count": 1770018,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 849349524,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.4kb",
          "memory_size_in_bytes": 127449,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000002": {
      "uuid": "kj47HFzdRLuzR4XX_BG1fw",
      "primaries": {
        "docs": {
          "count": 124688820,
          "deleted": 0
        },
        "store": {
          "size": "25.4gb",
          "size_in_bytes": 27277282976,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 124688820,
          "index_time": "3.2h",
          "index_time_in_millis": 11786405,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1083901,
          "query_time": "5.4h",
          "query_time_in_millis": 19510891,
          "query_current": 0,
          "concurrent_query_total": 123730,
          "concurrent_query_time": "1m",
          "concurrent_query_time_in_millis": 64757,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 497548,
          "fetch_time": "24.8m",
          "fetch_time_in_millis": 1491151,
          "fetch_current": 0,
          "scroll_total": 19902,
          "scroll_time": "2.9h",
          "scroll_time_in_millis": 10642230,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 111,
          "total_time": "3.1h",
          "total_time_in_millis": 11345555,
          "total_docs": 366948856,
          "total_size": "74.9gb",
          "total_size_in_bytes": 80475615974,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.1h",
          "total_throttled_time_in_millis": 7746050,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 274,
          "total_time": "1.1m",
          "total_time_in_millis": 68686,
          "external_total": 32,
          "external_total_time": "13.5s",
          "external_total_time_in_millis": 13515,
          "listeners": 0
        },
        "flush": {
          "total": 238,
          "periodic": 238,
          "total_time": "18m",
          "total_time_in_millis": 1081146
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
          "total_count": 872472,
          "hit_count": 0,
          "miss_count": 872472,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 875492199,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "61.7kb",
          "memory_size_in_bytes": 63206,
          "evictions": 0,
          "hit_count": 123721,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 249377640,
          "deleted": 0
        },
        "store": {
          "size": "50.7gb",
          "size_in_bytes": 54537792982,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 249377640,
          "index_time": "5.5h",
          "index_time_in_millis": 19812002,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1739999,
          "query_time": "11.3h",
          "query_time_in_millis": 40743246,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "1.8m",
          "concurrent_query_time_in_millis": 111778,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 749998,
          "fetch_time": "33m",
          "fetch_time_in_millis": 1985602,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16244712,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 212,
          "total_time": "6.2h",
          "total_time_in_millis": 22604556,
          "total_docs": 737485966,
          "total_size": "150.5gb",
          "total_size_in_bytes": 161607711097,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "4.5h",
          "total_throttled_time_in_millis": 16229523,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 548,
          "total_time": "2.1m",
          "total_time_in_millis": 127225,
          "external_total": 62,
          "external_total_time": "18.3s",
          "external_total_time_in_millis": 18304,
          "listeners": 0
        },
        "flush": {
          "total": 480,
          "periodic": 480,
          "total_time": "34.6m",
          "total_time_in_millis": 2076331
        },
        "warmer": {
          "current": 0,
          "total": 60,
          "total_time": "3ms",
          "total_time_in_millis": 3
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1770018,
          "hit_count": 0,
          "miss_count": 1770018,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 875490785,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "124.1kb",
          "memory_size_in_bytes": 127153,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000001": {
      "uuid": "LP5wRza6TMOdXhq5TKHsjQ",
      "primaries": {
        "docs": {
          "count": 124779252,
          "deleted": 0
        },
        "store": {
          "size": "25.4gb",
          "size_in_bytes": 27300786739,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 82129402,
          "index_time": "2.1h",
          "index_time_in_millis": 7565121,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 934560,
          "query_time": "9.9h",
          "query_time_in_millis": 35970103,
          "query_current": 0,
          "concurrent_query_total": 146202,
          "concurrent_query_time": "1.1m",
          "concurrent_query_time_in_millis": 67387,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 597865,
          "fetch_time": "26.7m",
          "fetch_time_in_millis": 1606550,
          "fetch_current": 0,
          "scroll_total": 13827,
          "scroll_time": "2.1h",
          "scroll_time_in_millis": 7734242,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 77,
          "total_time": "2.4h",
          "total_time_in_millis": 8667004,
          "total_docs": 306883417,
          "total_size": "62.5gb",
          "total_size_in_bytes": 67154302757,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.4h",
          "total_throttled_time_in_millis": 5269134,
          "total_auto_throttle": "5.4mb",
          "total_auto_throttle_in_bytes": 5719505,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 174,
          "total_time": "47.2s",
          "total_time_in_millis": 47291,
          "external_total": 6,
          "external_total_time": "2.6s",
          "external_total_time_in_millis": 2656,
          "listeners": 0
        },
        "flush": {
          "total": 161,
          "periodic": 160,
          "total_time": "11m",
          "total_time_in_millis": 660474
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
          "total_count": 932710,
          "hit_count": 0,
          "miss_count": 932710,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 901643303,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "63.3kb",
          "memory_size_in_bytes": 64876,
          "evictions": 0,
          "hit_count": 146192,
          "miss_count": 11
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 249558504,
          "deleted": 0
        },
        "store": {
          "size": "50.8gb",
          "size_in_bytes": 54591228135,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 163025132,
          "index_time": "4h",
          "index_time_in_millis": 14458834,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1830000,
          "query_time": "17.6h",
          "query_time_in_millis": 63619877,
          "query_current": 0,
          "concurrent_query_total": 299999,
          "concurrent_query_time": "2.2m",
          "concurrent_query_time_in_millis": 134609,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 1,
          "fetch_total": 1229999,
          "fetch_time": "54.1m",
          "fetch_time_in_millis": 3247237,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16247335,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 152,
          "total_time": "4.9h",
          "total_time_in_millis": 17978412,
          "total_docs": 621397235,
          "total_size": "126.5gb",
          "total_size_in_bytes": 135894581681,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.9h",
          "total_throttled_time_in_millis": 10694287,
          "total_auto_throttle": "10.4mb",
          "total_auto_throttle_in_bytes": 10962385,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 342,
          "total_time": "1.5m",
          "total_time_in_millis": 95870,
          "external_total": 13,
          "external_total_time": "5.9s",
          "external_total_time_in_millis": 5982,
          "listeners": 0
        },
        "flush": {
          "total": 317,
          "periodic": 315,
          "total_time": "23.2m",
          "total_time_in_millis": 1392759
        },
        "warmer": {
          "current": 0,
          "total": 11,
          "total_time": "0s",
          "total_time_in_millis": 0
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 1800024,
          "hit_count": 0,
          "miss_count": 1800024,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "evictions": 0
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 901641633,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "125.8kb",
          "memory_size_in_bytes": 128907,
          "evictions": 0,
          "hit_count": 299979,
          "miss_count": 21
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    },
    ".ds-logs-benchmark-dev-000010": {
      "uuid": "CbWAste9SZuPpBrBw3KGtw",
      "primaries": {
        "docs": {
          "count": 67615240,
          "deleted": 0
        },
        "store": {
          "size": "13.6gb",
          "size_in_bytes": 14667734599,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 67615240,
          "index_time": "1.3h",
          "index_time_in_millis": 4924876,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 976703,
          "query_time": "2.1h",
          "query_time_in_millis": 7805859,
          "query_current": 0,
          "concurrent_query_total": 73641,
          "concurrent_query_time": "18.2s",
          "concurrent_query_time_in_millis": 18299,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 4,
          "fetch_total": 382365,
          "fetch_time": "13.6m",
          "fetch_time_in_millis": 816589,
          "fetch_current": 0,
          "scroll_total": 14098,
          "scroll_time": "2.1h",
          "scroll_time_in_millis": 7702011,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 58,
          "total_time": "1.4h",
          "total_time_in_millis": 5087013,
          "total_docs": 129976072,
          "total_size": "26.6gb",
          "total_size_in_bytes": 28603246029,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "1.1h",
          "total_throttled_time_in_millis": 4233794,
          "total_auto_throttle": "5mb",
          "total_auto_throttle_in_bytes": 5242880,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 159,
          "total_time": "25.9s",
          "total_time_in_millis": 25976,
          "external_total": 25,
          "external_total_time": "3.4s",
          "external_total_time_in_millis": 3443,
          "listeners": 0
        },
        "flush": {
          "total": 131,
          "periodic": 131,
          "total_time": "8.2m",
          "total_time_in_millis": 496330
        },
        "warmer": {
          "current": 0,
          "total": 24,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 8944984,
          "hit_count": 0,
          "miss_count": 8944984,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "35kb",
          "memory_size_in_bytes": 35864,
          "evictions": 0
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 19,
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "55b",
          "size_in_bytes": 55,
          "uncommitted_operations": 0,
          "uncommitted_size": "55b",
          "uncommitted_size_in_bytes": 55,
          "earliest_last_modified_age": 676543176,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "61.2kb",
          "memory_size_in_bytes": 62766,
          "evictions": 0,
          "hit_count": 73632,
          "miss_count": 9
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      },
      "total": {
        "docs": {
          "count": 135230480,
          "deleted": 0
        },
        "store": {
          "size": "27.3gb",
          "size_in_bytes": 29350500562,
          "reserved": "0b",
          "reserved_in_bytes": 0
        },
        "indexing": {
          "index_total": 135230480,
          "index_time": "3h",
          "index_time_in_millis": 10845296,
          "index_current": 0,
          "index_failed": 0,
          "delete_total": 0,
          "delete_time": "0s",
          "delete_time_in_millis": 0,
          "delete_current": 0,
          "noop_update_total": 0,
          "is_throttled": false,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0,
          "doc_status": {}
        },
        "get": {
          "total": 0,
          "getTime": "0s",
          "time": "0s",
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
          "query_total": 1740001,
          "query_time": "2.3h",
          "query_time_in_millis": 8470707,
          "query_current": 0,
          "concurrent_query_total": 270000,
          "concurrent_query_time": "49.2s",
          "concurrent_query_time_in_millis": 49231,
          "concurrent_query_current": 0,
          "concurrent_avg_slice_count": 4,
          "fetch_total": 780000,
          "fetch_time": "32.7m",
          "fetch_time_in_millis": 1963243,
          "fetch_current": 0,
          "scroll_total": 30000,
          "scroll_time": "4.5h",
          "scroll_time_in_millis": 16241775,
          "scroll_current": 0,
          "point_in_time_total": 0,
          "point_in_time_time": "0s",
          "point_in_time_time_in_millis": 0,
          "point_in_time_current": 0,
          "suggest_total": 0,
          "suggest_time": "0s",
          "suggest_time_in_millis": 0,
          "suggest_current": 0,
          "search_idle_reactivate_count_total": 0
        },
        "merges": {
          "current": 0,
          "current_docs": 0,
          "current_size": "0b",
          "current_size_in_bytes": 0,
          "total": 120,
          "total_time": "2.8h",
          "total_time_in_millis": 10107325,
          "total_docs": 254462687,
          "total_size": "52.2gb",
          "total_size_in_bytes": 56100113400,
          "total_stopped_time": "0s",
          "total_stopped_time_in_millis": 0,
          "total_throttled_time": "2.2h",
          "total_throttled_time_in_millis": 8110883,
          "total_auto_throttle": "10mb",
          "total_auto_throttle_in_bytes": 10485760,
          "unreferenced_file_cleanups_performed": 0
        },
        "refresh": {
          "total": 316,
          "total_time": "1m",
          "total_time_in_millis": 65684,
          "external_total": 52,
          "external_total_time": "8.2s",
          "external_total_time_in_millis": 8250,
          "listeners": 0
        },
        "flush": {
          "total": 260,
          "periodic": 260,
          "total_time": "17.7m",
          "total_time_in_millis": 1065249
        },
        "warmer": {
          "current": 0,
          "total": 50,
          "total_time": "2ms",
          "total_time_in_millis": 2
        },
        "query_cache": {
          "memory_size": "0b",
          "memory_size_in_bytes": 0,
          "total_count": 12882304,
          "hit_count": 0,
          "miss_count": 12882304,
          "cache_size": 0,
          "cache_count": 0,
          "evictions": 0
        },
        "fielddata": {
          "memory_size": "65.3kb",
          "memory_size_in_bytes": 66944,
          "evictions": 0
        },
        "completion": {
          "size": "0b",
          "size_in_bytes": 0
        },
        "segments": {
          "count": 40,
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
          "remote_store": {
            "upload": {
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "refresh_size_lag": {
                "total": "0b",
                "total_bytes": 0,
                "max": "0b",
                "max_bytes": 0
              },
              "max_refresh_time_lag": "0s",
              "max_refresh_time_lag_in_millis": 0,
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0,
              "pressure": {
                "total_rejections": 0
              }
            },
            "download": {
              "total_download_size": {
                "started": "0b",
                "started_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0
              },
              "total_time_spent": "0s",
              "total_time_spent_in_millis": 0
            }
          },
          "segment_replication": {
            "max_bytes_behind": 0,
            "total_bytes_behind": 0,
            "max_replication_lag": 0
          },
          "file_sizes": {}
        },
        "translog": {
          "operations": 0,
          "size": "110b",
          "size_in_bytes": 110,
          "uncommitted_operations": 0,
          "uncommitted_size": "110b",
          "uncommitted_size_in_bytes": 110,
          "earliest_last_modified_age": 676242032,
          "remote_store": {
            "upload": {
              "total_uploads": {
                "started": 0,
                "failed": 0,
                "succeeded": 0
              },
              "total_upload_size": {
                "started": "0b",
                "started_bytes": 0,
                "failed": "0b",
                "failed_bytes": 0,
                "succeeded": "0b",
                "succeeded_bytes": 0
              }
            }
          }
        },
        "request_cache": {
          "memory_size": "123.3kb",
          "memory_size_in_bytes": 126281,
          "evictions": 0,
          "hit_count": 269982,
          "miss_count": 19
        },
        "recovery": {
          "current_as_source": 0,
          "current_as_target": 0,
          "throttle_time": "0s",
          "throttle_time_in_millis": 0
        }
      }
    }
  }
}
```
