
try
{
    function validatebusinessinfo()
    {
        let businessname = document.forms.businessinfo.businessname.value;
        let registrationno = document.forms.businessinfo.registrationno.value;
        let email = document.forms.businessinfo.email.value;
        let phone = document.forms.businessinfo.phone.value;
       // let businessaddress = document.forms.businessinfo.businessaddress.value;
        let country = document.forms.businessinfo.country.value;
        let state = document.forms.businessinfo.state.value;
        let city = document.forms.businessinfo.city.value;   
        let pwd = document.forms.businessinfo.pwd.value;
        let cpwd = document.forms.businessinfo.cpwd.value; 
        
        if(!businessname)
        {
            document.getElementById('businessnameerr').innerHTML = " *Business name is required";
            //document.forms.businessinfo.businessname.focus();
            //return false;
        }
        if(!registrationno)
        {
            document.getElementById('registrationnoerr').innerHTML = " *Required Field";
            //return false;
        }
        if(!email)
        {
            document.getElementById('emailerr').innerHTML = " *Required Field";
        }
        if(!phone)
        {
            document.getElementById('phoneerr').innerHTML = " *Required Field";
        }
        if(!country)
        {
            document.getElementById('countryerr').innerHTML = " * Required Field";
        }
        if(!state)
        {
            document.getElementById('stateerr').innerHTML = " * Required Field";
        }
        if(!city)
        {
            document.getElementById('cityerr').innerHTML = " * Required Field";
            return false;
        }
        if(!pwd)
        {
            document.getElementById('pwderr').innerHTML = " * Required Field";
        }
        if(!cpwd)
        {
            document.getElementById('cpwderr').innerHTML = " * Required Field";
        }

    }

    function validatepwd()
    {
        let namepattern = /^[A-Za-z\s]/;//need to add pattern for special character, digits and range
        let pwd = document.forms.businessinfo.pwd.value;
        if(pwd)
        {
            let x = namepattern.test(pwd);
            if(x == false)
            {
                document.getElementById('pwderr').innerHTML = " Incorrect password pattern";
            }
            else
            {
                document.getElementById('pwderr').innerHTML = " ";
            }
        }
    }

    function validatebusinesssignin()
    {
        let username = document.forms.businesssignin.username.value;
        let pwd = document.forms.businesssignin.pwd.value;
        document.getElementById('usernamepwderr').style.border = "none";
        if(!username)
        {
            
            document.getElementById('usernamepwderr').innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>* Username or Password is incorrect!</small>";
            return false;
        }
        if(!pwd)
        {
            //document.getElementById('usernamepwderr').style.border = "none";
            document.getElementById('usernamepwderr').innerHTML = " * Username or Password is incorrect";  
            return false;
        }
    }
}

catch(err)
{
    window.alert(err.message)
}
