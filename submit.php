<?php 
    $first_name = $_POST['first_name'];
    $last_name = $_POST['last_name'];
    $email = $_POST['email'];
    $comment = $_POST['comment'];

    $from = 'Michael-Weisz.de Contact Form: '; 
    $to = 'mail@michael-weisz.de'; 
    $subject = "Message from <$first_name $last_name> via michael-weisz.de contact form.";

    $body = "First Name: $first_name\n Last Name: $last_name\n E-Mail: $email\n Message:\n $comment";

    mail ($to, $subject, $body, $from)
?>