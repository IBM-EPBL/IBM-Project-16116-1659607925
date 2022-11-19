<?php
    $n=$_POST['Name'];
    $p=$_POST['phonenumber'];
    $e=$_POST['Email'];
$con=mysqli_connect('localhost','root',"",'data');
$sql="INSERT INTO details ('Name','Phonenumber','Email')VALUES('$n','$c','$e')";
$r=$mysqli_query($con,$sql);

if($r)
{
    echo "Details inserted";
}
?>

