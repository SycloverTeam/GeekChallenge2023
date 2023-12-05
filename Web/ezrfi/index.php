<!DOCTYPE html>
<html>
<head>
  <title>来读文件玩吧</title>
</head>
<body>
  <img src="https://img.zcool.cn/community/01dcd059117b12a801216a3e9c4fd5.jpg@1280w_1l_2o_100sh.jpg" height="300px" width="400px">
<form action="index.php" method="GET">
  <label for="filename">filename:</label>
  <input type="text" id="file" name="file" required><br><br>
  <input type="submit" value="提交">
</form>
  <!-- you may be can find some information in the hint.py-->
</body>
</html>
<?php
error_reporting(0);
echo "what pythonfile do you want to read?please input the filename of python file"."<br>";
$file=$_GET['file'];
    $readfile=include($file.".py");
    if($readfile){
        var_dump($readfile);
    }else{
      if(!file_exists($file)){
        echo "no such file!!!";
      }else{
        echo "nonono.you only can read python file!!!."."<br>";
      }
    }

?>