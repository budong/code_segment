      <?php
      //连接mysql服务器
      $link=mysql_connect('localhost','root','mumayi') or die("Could not connect: ".mysql_error());
      //选择数据库
      //mysql_query("use yunbbs");
      mysql_select_db("yunbbs") or die("Could not select databases");
      //使用mysql_query()函数执行sql语句
      $sql="select * from yunbbs_users";
      $result=mysql_query($sql,$link) or die("Query failed:".mysql_error());
      //返回结果集中一个字段的值
      echo mysql_result($result,0,'name');
      //换回结果集中行的数
      echo mysql_num_rows($result);
      //换回结果集中字段的数
      echo mysql_num_fields($result);
      //删除数据
      $delete_one=mysql_query("delete from yunbbs_users where id=3",$link);
      //从结果集中取得一行作为数字数组
      print_r(mysql_fetch_row($result));
      while($row=mysql_fetch_row($result)){
          print_r($row);
          echo "<br />\n";
      }
      //从结果集中取得一行作为关联数组，或数字数组，或二者兼有
      print_r(mysql_fetch_array($result));
      while($row=mysql_fetch_array($result)){
          print_r($row);
          echo "<br />\n";
      }
      //分析表头
      while ($field=mysql_fetch_field($result)){
          echo "<tr>\n";
          echo "<td>".$field->name."</td>\n";
          echo "</tr>\n";
      }
      //分析表身
      while($row=mysql_fetch_row($result)){
          echo "<tr>\n";
          for($i=0;$i<count($row);$i++){
              echo "<td>".$row[$i]."</td>";
          }
          echo "</tr>\n";
      }
      //取得 MySQL 服务器信息
      print_r(mysql_get_server_info($link));

      //释放$result变量
      mysql_free_result($result);
      //释放数据库连接池
      mysql_close($link);

    $a = array( 
        "one" => 1, 
        "two" => 2, 
        "three" => 3, 
        "seventeen" => 17 
    ); 
    foreach ($a as $k => $v) { 
        echo $k;
        echo $v;
        echo "<br />";
    } 

    echo stripslashes("Who\'s John Adams?");

    $t=time();
    echo ($t ."<br />");
    echo(date("D F d Y",$t));

     //分割字符串，相当于python split
     $str = "I am budong";
     print_r(explode(" ",$str));
     //php header跳转，有点意思
     header('location: http://www.baidu.com');
?>
