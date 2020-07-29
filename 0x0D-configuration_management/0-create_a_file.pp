# A resource declaration
file { '/tmp/codingschool':
  ensure  => file,
  path    => '/tmp/codingschool',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
