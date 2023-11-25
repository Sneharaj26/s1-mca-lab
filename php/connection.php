<?php
$con= mysqli_connect('localhost','root', '','student');
if($con)
{
    echo"connection successful";
}
else{
    echo"connection failed";

}
$fname=$_POST['fname'];
$rollno=$_POST['rollno'];
$mark=$_POST['mark'];
$sq="insert into student values($rollno,'$fname',$mark)";
$p= mysqli_query($con,$sq);
if($p)
{
    echo"<script>
    alert('successfully inserted first row');
    </script>";
}

?>