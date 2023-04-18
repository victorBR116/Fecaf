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
}