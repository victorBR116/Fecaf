<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $username = $_POST['username'];
    $password = $_POST['password'];

    $usuarios = array();
    if (file_exists('usuarios.json')) {
        $usuarios = json_decode(file_get_contents('usuarios.json'), true);
    }
    if (isset($usuarios[$username])) {
        echo "Usuário já cadastrado.";
    } else {
        $usuarios[$username] = array('senha' => $password);
        file_put_contents('usuarios.json', json_encode($usuarios));
        echo "Usuário cadastrado com sucesso.";
    }
}
