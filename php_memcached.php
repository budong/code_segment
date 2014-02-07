<?php
      //实例化一个memcache对象
      $mem=new Memcache;
      //链接一台memcahe服务
      $mem->connect('localhost','11211');
      //准备SQL语句
      $sql="select * from yunbbs_users limit 1";
      //设置一个键名
      $key=md5($sql);
      $data=$mem->get($key);
      //第二次之后的查询
      if(!$data){
          try{
      //连接mysql服务器
      $link=mysql_connect('localhost','root','mumayi') or die("Could not connect: ".mysql_error());
      //选择数据库
      mysql_select_db("yunbbs") or die("Could not select databases");
      //使用mysql_query()函数执行sql语句
      $result=mysql_query($sql,$link) or die("Query failed:".mysql_error());
      //就一条记录，直接一个数组就取出来了,没while循环去取了
      $data=mysql_fetch_array($result);
      //把数据存储到memcache中(第一次查询)
      $mem->add($key,$data);
      //释放$result变量
      mysql_free_result($result);
      //释放数据库连接池
      mysql_close($link);
          }
      catch(Exception $e){
          echo "error";
      }
          }

       $mem->close();
       print_r($data);
?>
