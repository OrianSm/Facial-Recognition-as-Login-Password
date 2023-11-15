<?php

  // Data storing and managing images   

  $fullName = $_POST['Fullname'];
  $userName = $_POST['Username'];
  $email = $_POST['Email'];

  if(isset($_FILES['Photo'])){
    $extension = "";
    if($_FILES['Photo']['type']=="image/png"){
    $extension = ".png";
    }
    else if ($_FILES['Photo']['type']=="image/jpeg"){
    $extension = ".jpeg";
    }
    else if ($_FILES['Photo']['type']=="image/jpg"){
      $extension = ".jpg";
    }
    $tempName = $_FILES['Photo']['tmp_name'];
    $dest = "./Signuppwd/";
    move_uploaded_file($tempName,$dest.$userName.$extension);
  }

  $password = $userName.$extension;
  
  // Connection and storing data in database

 $connection = new mysqli('localhost','root','','users');

 $query = "SELECT Username FROM signup WHERE Username = '$userName'";
 $statement = $connection->query($query);
 $result = mysqli_fetch_assoc($statement);
 if(isset($result["Username"])){
  header('Location:conflict.html');   
}
else{
  if($connection->connect_error){
    die('Connection Failed : '.$connection->connect_error);
  }
  else{
    $query = "insert into signup(Fullname,Username,Email,Password) values('$fullName' ,'$userName','$email','$password')";
    mysqli_query($connection,$query);
    $connection->close();
    header('Location:sign-upSuccess.html');
  }
}

?>