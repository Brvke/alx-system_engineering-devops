#adjust user limits and pam configuration
exec { 'set-soft-limit':
  command => '/bin/echo "holberton soft nofile 2048" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton soft nofile 2048" /etc/security/limits.conf',
}

exec { 'set-hard-limit':
  command => '/bin/echo "holberton hard nofile 4096" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton hard nofile 4096" /etc/security/limits.conf',
}

exec { 'add-pam-limits-common-session':
  command => '/bin/echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  unless  => '/bin/grep -q "session required pam_limits.so" /etc/pam.d/common-session',
}

exec { 'add-pam-limits-common-session-noninteractive':
  command => '/bin/echo "session required pam_limits.so" >> /etc/pam.d/common-session-noninteractive',
  unless  => '/bin/grep -q "session required pam_limits.so" /etc/pam.d/common-session-noninteractive',
}
