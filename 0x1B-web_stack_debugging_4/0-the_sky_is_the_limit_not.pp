# 0-the_sky_is_the_limit_not.pp
exec { 'fix--for-nginx':
    command => '/usr/sbin/nginx -s reload',
    path    => '/usr/bin:/usr/sbin:/bin:/sbin',
    onlyif  => '/usr/sbin/nginx -t',
}