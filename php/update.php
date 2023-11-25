<html>
    <head>
        <title>
            </title></head>
            <body>
                <form action="update.php" method="POST">
                    Username:<input type="text" name="name"/>
                    Password:<input type="password" name="password"/>
                    <button type="submit">Login</button>
                    <button type="submit">Reset</button>
                    
</form>
</body>
</html>

<?php
$con= mysqli_connect('localhost','root', '','student');
if($con)
{
    echo"connection successful";
}
else{
    echo"connection failed";

}
?>