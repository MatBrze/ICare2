document.addEventListener("DOMContentLoaded", function() {
        var user = document.getElementById("user");
        var userPlaceholder = user.firstElementChild;
        var pass = document.getElementById("pass");
        var passPlaceholder = pass.firstElementChild;
        userPlaceholder.placeholder = "Nazwa użytkownika";
        passPlaceholder.placeholder = "Hasło";
    });