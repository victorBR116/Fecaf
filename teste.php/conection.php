<?php

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);


socket_bind($socket, '0.0.0.0', 8080);

socket_listen($socket);

while (true) {
    $client = socket_accept($socket);
    
    $message = socket_read($client, 1024);

    echo "Mensagem recebida: $message" . PHP_EOL;

    $response = "Olá, cliente!";
    socket_write($client, $response, strlen($response));

    socket_close($client);
}
