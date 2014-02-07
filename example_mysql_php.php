<?php
header('Content-Type:text/html;charset=utf-8');
include(dirname(__FILE__) . 'include/config.php');
include(dirname(__FILE__) . 'include/db_mysql.class.php');

$db=new dbstuff();
$db->connect(DBHOST,DBUSER,DBPASSWD,DBNAME);

$sql="select * from yunbbs_users";
$result = $db->fetch_first($sql);
echo $result;
?>
