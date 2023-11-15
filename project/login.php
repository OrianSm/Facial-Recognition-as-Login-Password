<?php

  // Data storing and managing images   
  $username = $_POST["Username"];
  $password; 
  // Database connection
  $connection = new mysqli('localhost','root','','users');

  if($connection->connect_error){
    die('Connection Failed : '.$connection->connect_error);
  }
  else{
      $query = "SELECT Username,Password FROM signup WHERE Username = '$username'";
      $statement = $connection->query($query);
      $result = mysqli_fetch_assoc($statement);
      if(isset($result["Username"])){
        $password =  $result["Password"];
        $temp = shell_exec("python C:/xampp/htdocs/project/Python/facerect.py '$password' ");
        
        if($temp){
          header("Location:final.html");
        }
        else{
          header("Location:loginFailed.html");
        }
      }
      else{
        header("Location:empty.html");
      }
      $connection->close(); 
    }
?>