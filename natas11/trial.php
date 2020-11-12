<?php
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";  
  
function xor_encrypt($in) {  
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
    $text = $in;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
function second_time($in1){
	$key = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq';
	$text = $in1;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}

// echo xor_encrypt(base64_decode($cookie));

$in1 = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"); 


echo base64_encode(second_time(json_encode($in1)));
?>
