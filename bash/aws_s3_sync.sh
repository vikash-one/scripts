#!/bin/bash
# Usage: ./aws_s3_sync.sh <local-folder> <s3-bucket-name>
aws s3 sync "$1" "s3://$2" --delete
