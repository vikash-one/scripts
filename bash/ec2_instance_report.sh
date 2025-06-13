#!/bin/bash
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,Tags[?Key=='Name']|[0].Value]" \
  --output table
