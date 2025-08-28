provider "google" {
  project = "inlaid-vehicle-462617-e1"    # project id, not the name
  region  = "us-central"              	  # the region
  credentials = file("credentials.json")  # your service account credentials
}
