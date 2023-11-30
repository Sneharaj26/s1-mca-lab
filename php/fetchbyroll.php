<html>
    <head>
        <title>
            </title></head>
            <body>
                <form action="fetchbyroll.php" method="POST">
                    Rollno:<input type="number" name="rollno"/>
                    <input type="submit" name="submit">
                    
</form>
</body>
</html>

<?php
$conn=mysqli_connect('localhost','root','','student');
if(isset($_POST['submit'])){
$roll=$_POST['rollno'];
//$mark=$_POST['mark'];
$s="select * from student where rollno='$roll'";
$q=mysqli_query($conn,$s);
if(mysqli_num_rows($q))
{
    echo "<html><body><form method='post' action=''>";
    while($row=mysqli_fetch_assoc($q))
    {
        echo "ROLLNO <input type='text' value=".$row['rollno']."  name='rollno' readonly>";
        echo "NAME <input type='text' value=".$row['name']." disabled>";
        echo "MARK <input type='text' value=".$row['mark']." name='mark'>";
    }
    echo "<input type='submit' value='update' name='Update'>";
    echo "</form></body></html";
}
}
if(isset($_POST['Update']))
{
    $rollno=$_POST['rollno'];
    $mark=$_POST['mark'];   
$up="update student set mark='$mark' where rollno='$rollno'";
echo $up;
$mq=mysqli_query($conn,$up);
if($mq)
{
    echo "Mark updated";

}
else{
    echo "Mark not updated";
}
}
?>