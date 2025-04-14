provider "google" {
  project = "benchmark-project"           # project id, not the name
  region  = "us-central"              	  # the region
  credentials = file("credentials.json")  # your service account credentials
}

resource "google_container_cluster" "my_cluster" {
  name           	= "my-benchmark-cluster"  # your cluster name
  location       	= "us-central1-a"

  remove_default_node_pool = true           	 
  initial_node_count   	= 1
}

resource "google_container_node_pool" "elasticsearch_nodes_32cpu" {
  name   	= "elasticsearch-nodepool-32"
  cluster	= google_container_cluster.my_cluster.id
  node_count = 1

  node_config {
	machine_type = "n2-custom-36-81920" # 36 CPUs, 80GB RAM, 64GB for data + 16GB for utilities
	disk_size_gb = 3600
  }
}

resource "google_container_node_pool" "opensearch_nodes_32cpu" {
  name   	= "opensearch-nodepool-32"
  cluster	= google_container_cluster.my_cluster.id
  node_count = 1

  node_config {
	machine_type = "n2-custom-36-81920" # 36 CPUs, 80GB RAM, 64GB for data + 16GB for utilities
	disk_size_gb = 3600
  }
}
resource "google_container_node_pool" "rally_nodes" {
  name   	= "rally-nodes"
  cluster	= google_container_cluster.my_cluster.id
  node_count = 2

  node_config {
	machine_type = "n2-standard-16"
	disk_size_gb = 40
  }
}
