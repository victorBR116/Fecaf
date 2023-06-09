<?php

require 'vendor/autoload.php';

use Mews\Purifier;

$purifier = new Purifier();

$text = "Esta é uma string com palavras ofensivas, como palavrão1 e palavrão2.";

$filteredText = $purifier->clean($text);

echo $filteredText;
