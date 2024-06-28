$(document).ready(function () {
    console.log('a');
    $('form.needs-validation').submit(function (event) {
        var nombre = $('#nombre').val();
        var apellido = $('#apellido').val();
        var email = $('#Email').val();
        var confirmarEmail = $('#ConfirmEmail').val(); // Cambiado a ConfirmEmail
        var contraseña = $('#contraseña').val(); // Cambiado a contraseña
        var repetirContraseña = $('#repetirContraseña').val(); // Cambiado a repetirContraseña
        var regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (nombre.trim() === '') {
            alert('Introduce tu nombre.');
            event.preventDefault();
            return;
        }

        if (apellido.trim() === '') {
            alert('Introduce tu apellido.');
            event.preventDefault();
            return;
        }

        if (email.trim() === '' || !regexEmail.test(email)) {
            alert('Introduce una dirección de correo electrónico válida.');
            event.preventDefault();
            return;
        }

        if (confirmarEmail.trim() !== email.trim()) {
            alert('Las direcciones de correo electrónico no coinciden.');
            event.preventDefault();
            return;
        }

        if (contraseña.trim() === '') {
            alert('Introduce tu contraseña.');
            event.preventDefault();
            return;
        }

        if (repetirContraseña.trim() === '') {
            alert('Repite tu contraseña.');
            event.preventDefault();
            return;
        }

        if (repetirContraseña.trim() !== contraseña.trim()) {
            alert('Las contraseñas no coinciden.');
            event.preventDefault();
            return;
        }
    });
});
