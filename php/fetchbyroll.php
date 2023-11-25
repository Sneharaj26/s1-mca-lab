<html>
    <head>
        <title>
            </title></head>
            <body>
                <form action="fetchbyroll.php" method="POST">
                    Rollno:<input type="number" name="rollno"/>
                    <input type="submit">
                    <button input type="submit">Update</button>
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
$rollno= $_POST["rollno"];
$s= "select * from student where rollno='$rollno'";
$q=mysqli_query($con,$s);
if(mysqli_num_rows($q))
{ 
    

while($row=mysqli_fetch_assoc($q))
   {    
        echo"Rollno:<input type='text' value=' ".$row["rollno"]." 'disabled name='roll1'>";
        echo"Name:<input type='text' value=' ".$row["name"]." 'disabled name='name1'>";
        echo"Mark:<input type='text' value=' ".$row["mark"]." 'name='mark1'>";
   }
}

