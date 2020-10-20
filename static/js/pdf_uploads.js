function upload(){
    var error = false
    var branch = document.getElementById('branch');
    var regulation = document.getElementById('regulation');
    var year = document.getElementById('year')
    var semester = document.getElementById('semester');
    var subject = document.getElementById('subject');
    var file = document.getElementById('pdf').value;
    var fields_check = document.getElementById('fields_check');

    

    if (branch.selectedIndex == 0){
        error = true
    }
    if (regulation.selectedIndex == 0){
        error = true

    }
    if (year.selectedIndex == 0){
        error = true

    }
    if (semester.selectedIndex == 0){
        error = true

    }
    if (subject == ''){
        error = true
    }
    if (file == ''){
        error = true

    }
    if (error) {
        fields_check.innerHTML = "* please fill all the fields"
        fields_check.style.color = "red"
        return false
    }
    
    else{
        fields_check.innerHTML = ""
        return true
    }
}

function subjects(){
    var branch = document.getElementById('branch').value;
    var regulation = document.getElementById('regulation').value;
    var year = document.getElementById('year').value
    var semester = document.getElementById('semester').value;
    var data_list = document.getElementById('listOfSubjects')
    var str = ''

    // for mechanical
    if (branch == 'mech'){
        if (regulation == 'r-15'){
            if (year == 'firstyear'){
                if(semester == 'firstsemester'){
                    var optionArray = [
                        'ENGINEERING CHEMISTRY',
                        'ENVIRONMENT STUDIES',
                        'MATHEMATICS-I',
                        'COMPUTER PROGRAMMING',
                        'FUNCTIONAL ENGLISH',
                        'ENGINEERING MECHANICS',
                        'ENGINEERING CHEMISTRY LAB',
                        'COMPUTER PROGRAMMING LAB',
                        'ENGLISH LANGUAGE COMMUNICATION SKILLS LAB'
                    ]
                }
                else{
                    var optionArray = [
                        
                    ]
                }
            }
        }
        

    }

    for (var option in optionArray){
        str += '<option value="' + optionArray[option] + '" />'
    }

    data_list.innerHTML = str


    
}


