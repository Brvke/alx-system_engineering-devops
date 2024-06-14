#adjusting limit configuration and pam file
exec { 'set-soft-limit':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton soft nofile 4096" /etc/security/limits.conf',
}

exec { 'set-hard-limit':
  command => 'echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton hard nofile 8192" /etc/security/limits.conf',
}

exec { 'add-pam-limits-common-session':
  command => 'echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  unless  => '/bin/grep -q "session required pam_limits.so" /etc/pam.d/common-session',
}

exec { 'add-pam-limits-common-session-noninteractive':
  command => 'echo "session required pam_limits.so" >> /etc/pam.d/common-session-noninteractive',
  unless  => '/bin/grep -q "session required pam_limits.so" /etc/pam.d/common-session-noninteractive',
}
