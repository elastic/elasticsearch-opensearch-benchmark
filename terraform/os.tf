resource "google_container_cluster" "os_benchmarks_logging" {
  name                = "os-benchmarks-logging"
  location            = "us-central1-a"
  deletion_protection = false

  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "opensearch_nodes_16cpu_logging" {
  name       = "opensearch-nodepool-logging"
  cluster    = google_container_cluster.os_benchmarks_logging.id
  node_count = 6

  node_config {
    machine_type = "e2-standard-16"
    disk_size_gb = 50
  }
}

resource "google_container_node_pool" "dashboards_nodes_2cpu_logging" {
  name       = "dashboards-nodepool-logging"
  cluster    = google_container_cluster.os_benchmarks_logging.id
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 12
  }
}

resource "google_container_node_pool" "os_rally_node_logging" {
  name       = "os-rally-node-logging"
  cluster    = google_container_cluster.os_benchmarks_logging.id
  node_count = 1

  node_config {
    machine_type = "e2-standard-4"
    disk_size_gb = 25
  }
}
