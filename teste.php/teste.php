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

?>

<form method="post">
    <label for="username">Nome de usuário:</label>
    <input type="text" name="username" id="username" required>
    <br>
    <label for="password">Senha:</label>
    <input type="password" name="password" id="password" required>
    <br>
    <input type="submit" value="Cadastrar">
</form>
