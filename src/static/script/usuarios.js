const correo = document.getElementById('mail')
const form_alta = document.getElementById('form_altausuario')

function validarCorreo() {
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
    if (!validarCorreo()) return false;
    return true;
}

form_alta.addEventListener('submit', (e)=>{
    if(validarFormulario()) {
        console.log("Campos validos -enviando");
        // alert("Su consulta/suscripción fue enviada.")
        // e.preventDefault();
    } else {
        e.preventDefault();
    }
})