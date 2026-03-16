#!/bin/bash

set -e

echo "Waiting for PrestaShop..."

until docker compose exec -T prestashop curl -s -I http://localhost/administration/login?_token= | grep -q "200"; do
  echo "Waiting for 200 OK response..."
  sleep 3
done

echo "PrestaShop is ready (got 200 OK)"