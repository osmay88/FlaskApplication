# FlaskApplication

<p>In order to run this application you will need to set three environment variables:<p>
<ul>
    <li><strong>CONNECTION_STRING</strong> the database connection string</li>
    <li><strong>MAIL_USERNAME</strong> email username</li>
    <li><strong>MAIL_PASSWORD</strong> email password</li>
    <li><strong>ENV_SETTINGS</strong> settings to be used when running the application. Values: Development, Production</li>
</ul>

<p> The API consist of 4 endpoints</p>
<ul>
    <li>
        <i>/register</i> Register a new user to the system. The user data is a json that contains 3 values:
        <ul>
            <li>username</li>
            <li>email</li>
            <li>password</li>
        </ul>
        After the user is register, a email is send with a confirmation link.
    </li>
    <li>
        <i>/confirm/+activationlink</i> Activate the user in the database.
    </li>
    <li>
        <i>/login</i> Login a user to the system. The user data is a json that contains 2 values:
        <ul>
            <li>username</li>
            <li>password</li>
        </ul>
        If the login success a bearer token is return.
    </li>
    <li>
        <i>/generatekey</i> Generate an api key, requires authentification.
    </li>
    <li>
        <i>/update</i> Update the user password, required athentification. The user data is a json that contains 2 values:
        <ul>
            <li>oldpassword</li>
            <li>newpassword</li>
        </ul>
    </li>
</ul>
