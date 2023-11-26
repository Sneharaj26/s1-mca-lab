<?php
include 'conn1.php';
if($_POST)
{
    $username=$_POST['rname'];
    $password=$_POST['rpass'];
    $chckpass=$_POST['rpass2'];
    $fname=$_POST['fname'];
    $lname=$_POST['lname'];
    if($con)
    {
        $rq="insert into accounts values('','$username','$password','$fname','$lname')";
        $rs=mysqli_query($con,$rq);
        if($rs)
        {
            $res="Account Created";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <center>
        <h2><?php
                echo "$res";
                ?></h2>
                <a href="signin.php">Go to Sign in Page</a>
</center>
</body>
</html>

</body>
</html>