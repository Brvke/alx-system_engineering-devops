# adjusting user limits
exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 2048\nholberton hard nofile 4096" >> /etc/security/limits.conf', 
  unless  => 'grep -q "holberton soft nofile 2048" /etc/security/limits.conf',
}
