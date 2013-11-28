<?php
print_r($_SERVER);
/*
一般做訪客計數器時，
    大多都會利用PHP的$SERVER['REMOTE_ADDR']來抓取訪客的IP位址；
    可是在書上發現REMOTE_ADDR不能抓取到有經過proxy(代理伺服器)訪客的真實IP，
    所以搭配利用$SERVER['HTTP_X_FORWARDED_FOR']
    它可以將所有訪客主機經過的代理主機IP記錄下來
    便可以抓到有經過proxy訪客的真實IP
 */
//先判斷HTTP_X_FORWARDED_FOR是否存在
//if(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
//　　//存在的話將HTTP_X_FORWARDED_FOR拆解取出第一個IP即可
//　　$proxy_ip = split(',',$_SERVER['HTTP_X_FORWARDED_FOR']);
//　　$ip = $proxy_ip[0];
//}else
//{
//　　//不存在則使用REMOTE_ADDR來得到訪客IP
//　　$ip = $_SERVER['REMOTE_ADDR'];
//}

?>
