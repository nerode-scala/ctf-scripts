<?php
    $text="nerode";

    for($i=0; $i<5; $i++){
        $encoded=strrev(base64_encode($text));
    }
    echo $encoded;
?>