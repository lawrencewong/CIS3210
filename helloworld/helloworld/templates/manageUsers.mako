<div class="container">
        <h2><a href="http://www.mysql.com/" style="color: #000000;">MySQL</a></h2>
	<h5>This is an web application that uses a RESTful API and jQuery's AJAX to mimic a user managment web application with a database.
	    Play with the user's functions and see what the returns from the server side are. All user functions work. The server side has been
	    updated to work with a running MySQL databse.
	</h5>
      </div>

      <div class="container">
        <div class="rest-form">
          <div class="row">
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
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="user-forms">
        <label for="status-box"  class="rest-labels">Status / Returns:</label>
        <textarea readonly id="status-box" placeholder="Status and data that will be returned."></textarea>
      </div>