## Logging Rally Track

This repository contains a Logging track for benchmarking Elasticsearch using Rally. The "Logging" track focuses on queries that are essential in logging use cases.

### Prerequisites

Before using this repository, ensure you have the following installed:

- [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html) (v7.x or later)
- [Rally](https://esrally.readthedocs.io/en/stable/quickstart.html) (v2.x or later)
- An existing datastream with data generated using the open-source tool [Elastic Integration Corpus Generator Tool](https://github.com/elastic/elastic-integration-corpus-generator-tool). The data should follow the expected document structure mentioned below.

### Data Document Structure

The datastream must already exist and the data be generated using the open-source tool [Elastic Integration Corpus Generator Tool](https://github.com/elastic/elastic-integration-corpus-generator-tool). The expected structure of the documents is specified in the "Data Document Structure" section of this README.

```json
{
    "message": "2023-04-30T21:48:56.160Z Apr 30 21:48:56 ip-66-221-134-40 journal: donkey glazer fly shark whip servant thornfalcon",
    "process": {
        "name": "journal"
    },
    "aws.cloudwatch": {
        "ingestion_time": "2023-04-30T21:48:56.160Z",
        "log_group": "/var/log/messages",
        "log_stream": "luckcrafter"
    },
    "tags": [
        "preserve_original_event"
    ],
    "meta": {
        "file": "2023-01-02/1682891301-gotext.ndjson.gz"
    },
    "cloud": {
        "region": "eu-central-1"
    },
    "@timestamp": "2023-01-02T22:02:34.000Z",
    "input": {
        "type": "aws-cloudwatch"
    },
    "metrics": {
        "tmin": 849,
        "size": 1981
    },
    "log.file.path": "/var/log/messages/luckcrafter",
    "event": {
        "id": "sunsetmark",
        "dataset": "generic",
        "ingested": "2023-07-20T03:36:30.223806Z"
    },
    "agent": {
        "id": "c315dc22-3ea6-44dc-8d56-fd02f675367b",
        "name": "fancydancer",
        "ephemeral_id": "c315dc22-3ea6-44dc-8d56-fd02f675367b",
        "type": "filebeat",
        "version": "8.8.0"
    }
}

```
