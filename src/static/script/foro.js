const nombre = document.getElementById('nombre')
const mensaje = document.getElementById('mensaje')
const form_mensaje = document.getElementById('form_mensaje')

function validarNombre() {
    //
    if (nombre.value === "" || nombre.value === null){
        alert("El nombre no puede estar vacío");
        return false;
    }
    return true;
}

function validarMensaje() {
    //
    if (mensaje.value === "" || mensaje.value === null){
        alert("El Mensaje no puede estar vacío!");
        return false;
    }
    return true;
}

function validarTyc() {
    //
    if (correo.value === "" || correo.value === null){
        alert("El correo no puede estar vacío");
        return false;
    }
    const _valido = (correo) => {
        return String(correo)
            .toLowerCase()
            .match(/^\S+@\S+\.\S+$/);
        
    };
    if (!_valido(correo.value)) {
        alert("Revise el correo, debe ser ejemplo@server.org");
        return false;
    }
    return true;
}

function validarFormulario(){
    if (!validarNombre()) return false;
    if (!validarMensaje()) return false;

    return true;
}

form_mensaje.addEventListener('submit', (e)=>{
    if(validarFormulario()) {
        console.log("Campos validos -enviando");
        // alert("Su consulta/suscripción fue enviada.")
        // e.preventDefault();
    } else {
        e.preventDefault();
    }
})