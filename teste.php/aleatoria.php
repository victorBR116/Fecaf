<?php

class Aleatoria {
  public static function gerarSenha($tamanho = 12) {
      $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*+?';
      $password = '';
      for ($i = 0; $i < $tamanho; $i++) {
          $password .= $chars[mt_rand(0, strlen($chars)-1)];
      }
      return $password;
  }

  public static function gerarUsuario($tamanho = 8) {
      $chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
      $usuario = '';
      for ($i = 0; $i < $tamanho; $i++) {
          $usuario .= $chars[mt_rand(0, strlen($chars)-1)];
      }
      return $usuario;
  }
}

