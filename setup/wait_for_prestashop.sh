#!/bin/bash

set -e

echo "Waiting for PrestaShop..."

until curl -s -I http://prestashop/administration/login?_token= | grep -q "200 OK"; do
  echo "Waiting for 200 OK response..."
  sleep 3
done

echo "PrestaShop is ready (got 200 OK)"