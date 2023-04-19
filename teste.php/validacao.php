<?php

class Validador{
  public function isValid($password) {
    if (strlen($password) < 8) {
      return false;
    }

    if (!preg_match('/[A-Z]/', $password)) {
      return false;
    }

    if (!preg_match('/[a-z]/', $password)) {
      return false;
    }

    if (!preg_match('/[0-9]/', $password)) {
      return false;
    }

    return true;
  }
  public function isValidUsername($username) {
    if (strlen($username) < 3 || strlen($username) > 20) {
      return false;
    }
    
    if (!preg_match('/^[a-z0-9._]+$/', $username)) {
      return false;
    }
    
    if (preg_match('/(^\.|\.$|__|_\.)/', $username)) {
      return false;
    }
    
    return true;
  }
}

