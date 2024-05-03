document.addEventListener('DOMContentLoaded', function() {
    var togglePassword = document.getElementById('togglePassword');
    var passwordField = document.querySelector('input[type="password"]');

    togglePassword.addEventListener('click', function() {
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
        } else {
            passwordField.type = 'password';
        }
    });
});