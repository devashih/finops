#!/bin/bash

echo "Stopping development EC2 instances..."

aws ec2 stop-instances \
--instance-ids i-1234567890abcdef0
