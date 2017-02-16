$('#contact_form').submit(function(e){
  
    e.preventDefault(); // Prevent Default Submission

    // Recheck inputs
    if ($("#first_name_input").val() == "" 
        || $("#last_name_input").val() == ""
        || $("#email_input").val() == ""
        || $("#comment_input").val() == "") {
        return;
    }

    $.ajax({
 url: 'submit.php',
 type: 'POST',
 data: $(this).serialize(), // it will serialize the form data
        dataType: 'html'
    })
    .done(function(data){
        $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...

     $('#form-content').fadeOut('slow', function(){
          $('#form-content').fadeIn('slow').html(data);
        });
    })
    .fail(function(){
 alert('Ajax Submit Failed ...'); 
    });
});


// Decrypted email
<!--
// Email obfuscator script 2.1 by Tim Williams, University of Arizona
// Random encryption key feature coded by Andrew Moulden
// This code is freeware provided these four comment lines remain intact
// A wizard to generate this code is at http://www.jottings.com/obfuscator/
 coded = "Y3Zb@YZvl3xb-SxZn1.Ex"
  key = "GkJpOzfUvFRX0eAEbMYgS79rai1BVKW6Dsx5hNTLtjIo23ZyucCPHqn8dlQm4w"
  shift=coded.length
  link=""
  for (i=0; i<coded.length; i++) {
    if (key.indexOf(coded.charAt(i))==-1) {
      ltr = coded.charAt(i)
      link += (ltr)
    }
    else {     
      ltr = (key.indexOf(coded.charAt(i))-shift+key.length) % key.length
      link += (key.charAt(ltr))
    }
  }
$("#mail_link").attr('href', 'mailto:'+link)
