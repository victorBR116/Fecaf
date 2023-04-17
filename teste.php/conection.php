<?php

$server = stream_socket_server("tcp://0.0.0.0:8080", $errno, $errstr);

if (!$server) {
    die("Erro ao criar o servidor: $errstr ($errno)");
}

while ($client = stream_socket_accept($server)) {
    $message = fread($client, 1024);
    echo "Mensagem recebida: $message" . PHP_EOL;
    $response = "Olá, cliente!";
    fwrite($client, $response);
    fclose($client);
}

fclose($server);
