<?php
    //Setup connection variables and user arguments
    $hostname = "localhost";
    $username = $_POST['arg_usr'];
    $password = $_POST['arg_pwd'];
    $dbname = secuure;
    $usertable = data;
    $acc = $_POST['arg_edit_acc'];
    $ws = $_POST['arg_edit_ws'];
    $pwd = $_POST['arg_edit_pwd'];
    $note = $_POST['arg_edit_note'];
    $uid = 0;

    // Fetch user id
    //Connect to the database
    $connection = mysql_connect($hostname, $username, $password);
    mysql_select_db($dbname, $connection);

    $query = "SELECT id FROM users WHERE username='$username'";
    
    //Run the Query
    $result = mysql_query($query);
    
    //Find the id for a particular username
    if($result)
    {
        while($row = mysql_fetch_array($result))
        {
            $uid = $row[id];
        }
        
    }

    // Edit data
    // Create connection
    $conn = mysqli_connect($hostname, $username, $password, $dbname);
   
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    // Updates password and/notes depending on account name and website
    $sql = "UPDATE $usertable SET password='$pwd', notes='$note' WHERE userid='$uid' AND account='$acc' AND website='$ws'";

    if (mysqli_query($conn, $sql)) {
        echo "Record edited successfully" . "\r\n";
    } else {
        echo "Error: " . $sql . " " . mysqli_error($conn);
    }

    mysqli_close($conn);
 
?>
