resource "google_container_cluster" "es_benchmarks_logging" {
  name                = "es-benchmarks-logging"
  location            = "us-central1-a"
  deletion_protection = false

  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "elasticsearch_nodes_16cpu_logging" {
  name       = "elasticsearch-nodepool-logging"
  cluster    = google_container_cluster.es_benchmarks_logging.id
  node_count = 6

  node_config {
    machine_type = "e2-standard-16"
    disk_size_gb = 50
  }
}

resource "google_container_node_pool" "kibana_nodes_2cpu_logging" {
  name       = "kibana-nodepool-logging"
  cluster    = google_container_cluster.es_benchmarks_logging.id
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 12
  }
}

resource "google_container_node_pool" "es_rally_node_logging" {
  name       = "es-rally-node-logging"
  cluster    = google_container_cluster.es_benchmarks_logging.id
  node_count = 1

  node_config {
    machine_type = "e2-standard-4"
    disk_size_gb = 25
  }
}
