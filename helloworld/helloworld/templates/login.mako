<div class="container">
  <h1 style="font-size: 75px;">Hi there.</h1>
  <div class="rest-form">
    <div class="row">
      <div class="span12">
	<h3>Log in</h3>
	<label id="errorPlaceHolder" style="color: RED;"></label>
	<div>
	  <input type="text" id="loginUserName" placeholder="Username">
	</div>
	<div>
	  <input type="password" id="loginPassword" placeholder="Password">
	</div>
	<div>
	  <button class="btn btn-info btn-small" id="Submit">Submit</button>
	</div>
      </div>
    </div>
  </div>
</div>
<script type="text/javascript">
  $('#Submit').on('click', function(event) {
    $.ajax({
      type: "POST",
      url: "/users/login",
      data: {password:$('#loginPassword').val(), userName:$('#loginUserName').val()}
    })
    .done(function( data ) {
      var obj = jQuery.parseJSON( data );
      if( obj.hasOwnProperty('error')){
	$('#errorPlaceHolder').html("ERROR: " + obj.error);
      }else{;
	var username = $('#loginUserName').val()
	$('#placeholder').html(obj.code);
	$('#loggedInUser').append(username);
      }
    });
  });
</script>