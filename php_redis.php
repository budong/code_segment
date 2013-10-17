<?php
$redis = new Redis();
try{
    $redis->connect('127.0.0.1',6379);
}
catch (Exception $e){
    die("Cannot connect to redis server:".$e->getMessage() );
}

$redis->set('name','peiqiang');
echo $redis->get('name');
?>
