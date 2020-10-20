function validation() {
    var state = false
    var roll_number = document.getElementById('roll_number').value;
    var password = document.getElementById('password').value;
    var roll_Number_check = document.getElementById('roll_number_check')
    var password_check = document.getElementById('password_check')
    if (roll_number == ''){
        roll_Number_check.innerHTML = "* please enter the roll number"
        roll_Number_check.style.color = "red"
        state = false
    }
    else{
        roll_Number_check.innerHTML = "done"
        roll_Number_check.style.color = "green"
    }
    if (password == ''){
        password_check.innerHTML = "* please enter the password"
        password_check.style.color = "red"
        state = false
    }
    else {
        password_check.innerHTML = "done"
        password_check.style.color = "green"
        state = true
    }
    return state
}