function validation() {
    var state = false
    var roll_number = document.getElementById('roll_number').value;
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confPassword = document.getElementById('confPassword').value;
    roll_number_check = document.getElementById('roll_number_check');
    username_check = document.getElementById('username_check');
    email_check = document.getElementById('email_check');
    password_check = document.getElementById('password_check');
    confPassword_check = document.getElementById('confPassword_check')
    // verifying the roll number
    if (roll_number != ''){
        
        if (roll_number.match(/^[0-9]{4}(1|5)(A|a)0[12345]{1}[0-6]{1}[0-9]{1}$/) == null ){
            roll_number_check.innerHTML = "* invalid roll number"
            roll_number_check.style.color = 'red'
            state = false
        }
        else {
            roll_number_check.innerHTML = "done"
            roll_number_check.style.color = 'green'
            state = true
        }
    }
    else {
        roll_number_check.innerHTML = "* please enter the roll number"
        roll_number_check.style.color = 'red'
        state = false
    }

    // verifying the username
    if (username != ''){
        
            username_check.innerHTML = "done"
            username_check.style.color = 'green'
            state = true
    }
    else {
        username_check.innerHTML = "* please enter the username"
        username_check.style.color = 'red'
        state = false
    }

    // verifying the email
    if (email != ''){
        
        if (email.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/) == null ){
            email_check.innerHTML = "* invalid email address"
            email_check.style.color = 'red'
            state = false
        }
        else {
            email_check.innerHTML = "done"
            email_check.style.color = 'green'
            state = true
        }
    }
    else {
        email_check.innerHTML = "* please enter the email address"
        email_check.style.color = 'red'
        state = false
    }
    // verifying the password
    if (password != ''){
        
        if (password.length < 6 ){
            password_check.innerHTML = "* password should have min 6 characters"
            password_check.style.color = 'red'
            state = false
        }
        else if (confPassword != password){
            confPassword_check.innerHTML = "* password not matched"
            password_check.innerHTML = ""
            confPassword_check.style.color = 'red'
            state = false
        }
        else {
            password_check.innerHTML = "done"
            password_check.style.color = 'green'
            confPassword_check.innerHTML = "done"
            confPassword_check.style.color = 'green'
            state = true
        }
    }
    else {
        password_check.innerHTML = "* please enter the password"
        password_check.style.color = 'red'
        state = false
    }
    
    return state
    
}