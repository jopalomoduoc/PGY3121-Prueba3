jQuery(document).ready(function () {

    $("#enviar").click(function () {

        var codigo = $("#id_ISBN").val();
        var nombreLibro = $("#id_nombreLibro").val();
        var descripcion = $("#id_descripcion").val();
        var categoria = $("#id_categoria").val();

        var mensaje = "";

        if (codigo !== "") {

            if (codigo.length !== 13) {

                mensaje += "ISBN no es correcto\n";
            }

        } else {

            mensaje += "Ingrese ISBN \n";
        }
        if (nombreLibro == "") {

            mensaje += "Ingrese Nombre del libro \n";

        }
        if (descripcion == "") {

            mensaje += "Ingrese descripcion \n";

        }
        if (categoria == "") {

            mensaje += "Seleccione categoria \n";

        }
        if (mensaje !== "") {

            alert(mensaje);
            return false;

        }

    });

    $("#enviarUsuario").click(function () {

        var nombre = $("#id_nombre").val();
        var apellido = $("#id_apellido").val();
        var correo = $("#id_correo").val();
        var comentario = $("#id_comentario").val();
        var contraseña = $("#id_password").val();
        var confContraseña = $("#id_repeatPassword").val();

        var mensaje = "";

        if (nombre == "") {

            mensaje += "Ingrese Nombre \n";

        }

        if (apellido == "") {

            mensaje += "Ingrese Apellido \n";

        }

        if (correo !== "") {

            if (correo.contains('@') || correo.contains('.')) {
                mensaje += "El correo electrónico introducido no es correcto.";
            }
        } else {
            mensaje += "Ingrese Correo \n";
        }
        if (contraseña == "") {

            mensaje += "Ingrese Contraseña \n";

        }
        if (confContraseña == "") {

            mensaje += "Ingrese Confirmacion Contraseña \n";

        }
        if (contraseña !== confContraseña) {

            mensaje += "Las Contraseñas no son iguales Corrígelas \n";

        }
        if (comentario == "") {

            mensaje += "Ingrese Comentario \n";

        }
        if (mensaje !== "") {

            alert(mensaje);
            return false;

        }

    });

});

