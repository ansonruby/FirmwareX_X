
<?php
/*
define('WP_USE_THEMES', false);
require('../wp-blog-header.php');
header("HTTP/1.1 200 OK");
header("Status: 200 All rosy");
*/
/*
$DATO_re = $_GET['Dato'];
	$fh = fopen('Dato_get.txt', 'a');
	fwrite($fh,$DATO_re."\n");
	echo 'OK';
	$fclose($fh);

echo 'anderson';
*/



///---- resepcion por get un dato
/*
if (isset($_GET["Dato"])) {
    http_response_code(200);
    #header('Content-type: text/html');

    echo 'La URI solicitada es: ';
    echo 'El valor del parámetro "foo" es: ';

    return ;
}

*/

///---- resepcion por post


$dato = json_decode(file_get_contents('php://input'), true);
http_response_code(200);
#print_r($dato);
echo '-----------'
echo $dato["data"][0];
echo $dato["data"][1];

#$fh = fopen('Dato_get.txt', 'a');
#fwrite($fh,$dato["data"][0]."\n");
#echo 'OK';
#$fclose($fh);



?>
