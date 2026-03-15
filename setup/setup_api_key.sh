#!/bin/bash

set -euo pipefail

PS_CONTAINER="prestashop"

API_KEY=$(openssl rand -hex 16)
echo "Generated API key: $API_KEY"

echo "Setting up Webservice and API key via PHP..."

docker exec -i -e API_KEY="$API_KEY" "$PS_CONTAINER" php <<'EOF'
<?php
require_once '/var/www/html/config/config.inc.php';

// 1. Start Webservice
Configuration::updateValue('PS_WEBSERVICE', 1);

// Get token from environment variable
$apiKey = getenv('API_KEY');
if (!$apiKey) {
    echo "Error: API_KEY environment variable not set.\n";
    exit(1);
}

// 2. Create an API key
$account = new WebserviceKey();
$account->key = $apiKey;
$account->description = 'Autotest API key';
$account->active = 1;

if ($account->save()) {
    // 3. Grant permissions to the key
    $permissions = [
        'products' => ['GET' => 1, 'POST' => 1, 'PUT' => 1, 'DELETE' => 1],
        'categories' => ['GET' => 1, 'POST' => 1, 'PUT' => 1, 'DELETE' => 1],
        'customers' => ['GET' => 1, 'POST' => 1, 'PUT' => 1, 'DELETE' => 1],
        'orders' => ['GET' => 1, 'POST' => 1, 'PUT' => 1, 'DELETE' => 1],
        'addresses' => ['GET' => 1, 'POST' => 1, 'PUT' => 1, 'DELETE' => 1],
        'carts' => ['GET' => 1, 'POST' => 1, 'PUT' => 1, 'DELETE' => 1],
        'cart_rules' => ['GET' => 1, 'POST' => 1, 'PUT' => 1],
        'order_histories' => ['GET' => 1, 'POST' => 1, 'PUT' => 1]
    ];
    
    WebserviceKey::setPermissionForAccount($account->id, $permissions);
    echo "Webservice enabled and API key configured successfully! (ID: {$account->id})\n";
} else {
    echo "Error: Failed to create API key in PrestaShop.\n";
    exit(1); // stop execution with an error
}
EOF

echo "Saving .env file..."

cat > .env <<EOL
API_KEY=$API_KEY
# Changed to internal Docker URL so tests can access the API!
BASE_URL=http://prestashop/api
EOL

echo "Setup complete."