# fix config file for wordpress, fix a filename
exec { 'sed':
  command => 'sed -i "s|.phpp|.php|" /var/www/html/wp-settings.php',
  path    => '/bin/'
}
