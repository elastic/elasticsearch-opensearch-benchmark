#!/bin/bash
# this script build a multi arch image and pushes it to $TAG

export TAG=ugosan/logstash-custom:8.8.2-dev
export ARM_TAG="${TAG}-manifest-arm64v8"
export AMD_TAG="${TAG}-manifest-amd64"

docker buildx build --push -f Dockerfile --platform linux/arm64/v8 --tag $ARM_TAG . 
docker buildx build --push -f Dockerfile --platform linux/amd64 --tag $AMD_TAG .      

docker manifest create $TAG --amend $ARM_TAG --amend $AMD_TAG 
docker manifest push $TAG --purge

docker pull $TAG
