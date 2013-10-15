<?php
echo getcwd() . "\n";
if (chdir('/data/')) {
    echo "True" . "\n";
} else {
   echo "False" . "\n";
}

$fp=fopen("test.txt","w+");
$str="This is a test";
fputs($fp,$str);
fclose($fp);

echo getcwd() . "\n";
?>
