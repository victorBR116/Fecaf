<?php

class Aleatoria{
  public static function gerarSenha($tamanho = 12) {
      $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}[]<>?';
      $password = '';
      for ($i = 0; $i < $tamanho; $i++) {
          $password .= $chars[mt_rand(0, strlen($chars)-1)];
      }
      return $password;
  }
}

$usuario = new Aleatoria();
echo $usuario->gerarSenha();