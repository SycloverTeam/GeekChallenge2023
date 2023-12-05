<?php

function waf($data){ 
    if(preg_match('/[b-df-km-uw-z0-9\+\~\{\}]+/i',$data)){
        return False;
    }else{
        return True;
    }
}
echo "你猜猜我禁用了什么";
