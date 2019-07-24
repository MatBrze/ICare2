document.addEventListener("DOMContentLoaded", function() {
        var user = document.getElementById("user");
        var userPlaceholder = user.firstElementChild;
        var email = document.getElementById("email");
        var emailPlaceholder = email.firstElementChild;
        var pass1 = document.getElementById("pass1");
        var pass1Placeholder = pass1.firstElementChild;
        var pass2 = document.getElementById("pass2");
        var pass2Placeholder = pass2.firstElementChild;
        userPlaceholder.placeholder = "Nazwa użytkownika";
        emailPlaceholder.placeholder = "Email";
        pass1Placeholder.placeholder = "Hasło";
        pass2Placeholder.placeholder = "Powtórz hasło";
    });