# installing a package from its provider through puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
