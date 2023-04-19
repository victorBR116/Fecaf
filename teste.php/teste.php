<?php

require_once 'validacao.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $username = $_POST['username'];
    $password = $_POST['password'];

    $usuarios = array();
    if (file_exists('usuarios.json')) {
        $usuarios = json_decode(file_get_contents('usuarios.json'), true);
    }
    if (isset($usuarios[$username])) {
        header('Location: negado.html');     
          
        exit();
    } else {
        $validator = new Validador();
        if (!$validator->isValid($password)) {
            header('Location: senha-invalida.html');
            exit();
        }
        $usuarios[$username] = array('senha' => $password);
        file_put_contents('usuarios.json', json_encode($usuarios));
        header('Location: sucesso.html');
        
        exit();
    }
    $validator = new Validador();
    if (!$validator->isValidUsername($username)) {
    header('Location: usuarioInvalido.html');
    exit();
}

}
