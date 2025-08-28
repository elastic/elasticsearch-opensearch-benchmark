resource "google_container_cluster" "es_benchmarks_big5" {
  name                = "es-benchmarks-big5"
  location            = "us-central1-a"
  deletion_protection = false

  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "elasticsearch_nodes_16cpu_big5" {
  name       = "elasticsearch-nodepool-big5"
  cluster    = google_container_cluster.es_benchmarks_big5.id
  node_count = 6

  node_config {
    machine_type = "e2-standard-16"
    disk_size_gb = 50
  }
}

resource "google_container_node_pool" "kibana_nodes_2cpu_big5" {
  name       = "kibana-nodepool-big5"
  cluster    = google_container_cluster.es_benchmarks_big5.id
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 12
  }
}

resource "google_container_node_pool" "es_rally_node_big5" {
  name       = "es-rally-node-big5"
  cluster    = google_container_cluster.es_benchmarks_big5.id
  node_count = 1

  node_config {
    machine_type = "e2-standard-4"
    disk_size_gb = 25
  }
}
