# installing a package using puppet
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
