import express, { json } from "express";

const servidor = express();
// use sirve para agregar un middleware que validara la informacion 
servidor.use(json());

const productos = [
    {
        nombre:"pollada",
        precio: 15.5,
        disponible: true,
    },
    {
        nombre:"adobada",
        precio: 15.5,
        disponible: true,

    },
    {
        nombre: "chicharronada",
        precio: 17.5,
        disponible: true,
    },
    {
        nombre: "chuletada",
        precio:12.5,
        disponible: false,
    },
];

servidor.get("/",(req,res)=>{
    console.log("Entro aqui");
    res.status(200).json({
        message:"Bienvenido a mi Api de express",
    });
});
servidor
    .route("/productos")
    .get((req,res)=>{
    const productoDisponibles = productos.filter((producto) => {
        return producto.disponible === true;
        });
      res.status(200).json({
        content: productoDisponibles,
    });

})
.post((req, res) =>{
    console.log(req.body);
    const data = req.body;
    productos.push(data);
    res.status(201).json({
        message:"Producto creado exitosamente",
    });
});
servidor.listen(5000, ()=>{
    console.log(`Servidor corriendo exitosamente en el puerto 5000`);
});

