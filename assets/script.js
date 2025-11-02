async function obtenerDatos() {
    const datos = await fetch("http://127.0.0.1:8000/");
    console.log(datos.json());
       
}

obtenerDatos()

/*
let galeria = document.getElementById("galeria")
let json = "assets/data.json"
let imagenes = "assets/img"

//Petición fetch que captura los datos

fetch(json)

    //Maneja el estado de la página por ejemplo ok:200

    .then(respuesta => {

        if(!respuesta.ok){
             throw new Error(respuesta.status);
             
        } else{
            console.log("Funcionando");
            console.log(respuesta.status);  
        }

        //Retorna los datos del json
        return respuesta.json()
    })
    
    //Maneja los datos de el json

    .then(datosjson => {
        console.log(datosjson);

    })

    .catch(error =>{
        console.error("Ha ocurrido un error : ",error);
        
    })
*/