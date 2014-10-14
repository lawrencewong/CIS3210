<div class="container">
  <h2><a href="https://docs.python.org/2/library/cookie.html" style="color: #000000;">Cookies and Mako Templates</a></h2>
  <h5>This is an web application that uses a RESTful API and jQuery's AJAX to mimic a user managment web application with a database.
      Play with the user's functions and see what the returns from the server side are. All user functions work. The server side has been
      updated to work with a running MySQL database. Cookies are stored on the server side to handle the web site's states.
  </h5>
</div>

<div class="container">
  <div class="rest-form">
    <div class="row">
      <div>
	<label style="color: BLUE;" id="loggedInUser">Logged in as: </label>
      </div>
      <div class="span6">
	<div>
	  <input type="text" id="userName" placeholder="Username">
	</div>
	<div>
	  <input type="password" id="password" placeholder="Password">
	</div>
	<div>
	  <input type="text" id="firstName" placeholder="First Name">
	</div>
	<div>
	  <input type="text" id="lastName" placeholder="Last Name">
	</div>
      </div>
      <div class="span6">
	<label for="status-box" class="rest-labels">User Functions:</label>
	<div>
	  <button class="btn btn-success btn-small" id="addUser">Add User</button>
	  <button class="btn btn-warning btn-small" id="changeName">Edit User</button>
	  <button class="btn btn-info btn-small" id="checkUser">User Check</button>
	  <button class="btn btn-danger btn-small" id="removeUser">Remove User</button>
	  <button class="btn btn-primary btn-small" id="logOut">Log Out</button>
	</div>
      </div>
    </div>
  </div>
</div>

<div class="user-forms">
  <label for="status-box"  class="rest-labels">Status / Returns:</label>
  <textarea readonly id="status-box" placeholder="Status and data that will be returned."></textarea>
</div>
<script type="text/javascript">
      $('#addUser').on('click', function(event) {
	  if($('#userName').val()=="" || $('#firstName').val()=="" || $('#lastName').val()=="" || $('#password').val()==""){
	     $('#status-box').val("Username, password, first and last names required.");
	  }else{
	    $.ajax({
	      type: "GET",
	      url: "/users/existingUser/" + $('#userName').val(),
	    })
	    .done(function( data ) {
	      var obj = jQuery.parseJSON( data );
	      if( obj.hasOwnProperty('error')){;
		$('#status-box').val("ERROR: " + obj.error);
	      }else{
		 $.ajax({
		  type: "POST",
		  url: "/users/addUser",
		  data: {firstName:$('#firstName').val(), lastName:$('#lastName').val(), password:$('#password').val(), userName:$('#userName').val()}
		})
		.done(function( data ) {
		  $('#status-box').val("Added User: " + data);
		});
	      }
	    });
	  }
	});

      $('#changeName').on('click', function(event) {
        if($('#userName').val()=="" || $('#firstName').val()=="" || $('#lastName').val()=="" || $('#password').val()==""){
          $('#status-box').val("Username, password, first and last names required.");
        }else{
          $.ajax({
            type: "PUT",
            url: "/users/editUser/" + $('#userName').val(),
            data: {firstName:$('#firstName').val(), lastName:$('#lastName').val(), password:$('#password').val(), userName:$('#userName').val()}
          })
          .done(function( data ) {
            var obj = jQuery.parseJSON( data );
            if( obj.hasOwnProperty('error')){
              $('#status-box').val("ERROR: " + obj.error);
            }else{
              $('#status-box').val("Edited User: " + data);
            }
          });
        }
      });

      $('#checkUser').on('click', function(event) {
        if($('#userName').val()==""){
          $('#status-box').val("Username required.");
        }else{
          $.ajax({
            type: "GET",
            url: "/users/userCheck/" + $('#userName').val()
          })
          .done(function( data ) {
            var obj = jQuery.parseJSON( data );
            if( obj.hasOwnProperty('error')){
              $('#status-box').val("ERROR: " + obj.error);
            }else{
              $('#status-box').val("Found User: " + data);
            }
          });
        }
      });

      $('#removeUser').on('click', function(event) {
        if($('#userName').val()==""){
            $('#status-box').val("Username required.");
          }else{
            event.preventDefault();
            if (window.confirm("Are you sure?")) {
              $.ajax({
                type: "DELETE",
                url: "/users/removeUser/" + $('#userName').val(),
              })
              .done(function( data ) {
                var obj = jQuery.parseJSON( data );
                if( obj.hasOwnProperty('error')){;
                  $('#status-box').val("ERROR: " + obj.error);
                }else{
                  $('#status-box').val("Removing User: " + data);
                }
              });
            }
          }
      });

      $('#logOut').on('click', function(event) {
	$.ajax({
	  type: "POST",
	  url: "/users/logout"
	})
	.done(function( data ) {
	   $('#placeholder').html(data);
	});
      });
</script>