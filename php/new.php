<html>
    <head>
        <title>
            </title></head>
            <body>
                <form action="new.php" method="POST">
                    Name:<input type="text"  name="fname"/>
                    Rollno:<input type="number" name="rollno"/>
                    Mark:<input type="number" name="mark"/>
                    <input type="submit">
                </form>
            </body>
        </title>
   
</html>
<?php
$con= mysqli_connect('localhost','root', '','student');

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