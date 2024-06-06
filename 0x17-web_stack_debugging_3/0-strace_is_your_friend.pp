# fix bad "phpp" to "php" in "wp-settings.php"

exec { 'fix-wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path => '/usr/local/bin/:/bin/'
<<<<<<< HEAD
}
=======
}
>>>>>>> 5a0a0725ed25b5d16b0e57953e499aff5612e0bf
