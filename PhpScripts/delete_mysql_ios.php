<?php
    //Setup connection variables and user arguments
    $hostname = "192.168.0.107";
    $username = $_POST['arg_usr'];
    $password = $_POST['arg_pwd'];
    $dbname = secuure;
    $usertable = data;
    $acc = $_POST['arg_del_acc'];
    $ws = $_POST['arg_del_ws'];
    $uid = 0;

    // Fetch user id
    // Connect to the database
    $connection = mysql_connect($hostname, $username, $password);
    mysql_select_db($dbname, $connection);

    $query = "SELECT id FROM users WHERE username='$username'";
    
    // Run the Query
    $result = mysql_query($query);
    
    // Find the id for a particular username
    if($result)
    {
        while($row = mysql_fetch_array($result))
        {
            $uid = $row[id];
        }
        
    }


    // Delete data
    // Create connection
    $conn = mysqli_connect($hostname, $username, $password, $dbname);
   
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    // Sends query to the database to delete entry
    $sql = "DELETE FROM `$usertable` WHERE `userid`='$uid' and `account`='$acc' and `website`='$ws'";

    if (mysqli_query($conn, $sql)) {
        echo "Record removed from database" . "\r\n";
    } else {
        echo "Error: " . $sql . " " . mysqli_error($conn);
    }

    mysqli_close($conn);
 
?>
