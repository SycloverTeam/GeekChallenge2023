<?php
include('waf.php');
session_start();
show_source(__FILE__);
error_reporting(0);
$data=$_GET['data'];
if(waf($data)){
    eval($data);
}else{
    echo "no!";
}
?>