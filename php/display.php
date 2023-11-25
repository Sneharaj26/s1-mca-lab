<?php
$con= mysqli_connect('localhost','root', '','student');
if($con)
{
    echo"connection successful";
}
else{
    echo"connection failed";

}
$s= "select * from student";
$q=mysqli_query($con,$s);
if(mysqli_num_rows($q))
{ 
    echo"<table border=1><tr><th>rollno</th><th>name</th><th>mark</th></tr>";
      
    while($row=mysqli_fetch_assoc($q))
    {
        echo"<tr>";
        echo"<td>rollno=".$row["rollno"]."<br></td>";
        echo"<td>name=".$row["name"]."<br></td>";
        echo"<td>mark=".$row["mark"]."<br></td>";
        echo"</tr>";

    }

}
