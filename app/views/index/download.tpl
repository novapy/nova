<form method="post">
    <div>
        <label>First Name</label>
        <input type="text" name="user.first_name" value="{% user.first_name %}" />
    </div>
    <div>
        <label>Last Name</label>
        <input type="text" name="user.last_name" value="{% user.last_name %}" />
    </div>
    <div>
        <label>Email</label>
        <input type="text" name="user.email" value="{% user.email %}" />
    </div>
    <div>
        <input type="submit" value="Signup" />
    </div>
</form>