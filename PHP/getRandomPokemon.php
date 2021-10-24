<?php 
$str = file_get_contents('../JSON/mysql.json');
$json = json_decode($str, true);

echo $json;
    
?>