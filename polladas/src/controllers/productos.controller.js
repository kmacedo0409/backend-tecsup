import {Prisma} from "../prisma.js";

export const crearProducto = async (req, res) =>{
    const data = req.body;

try{


    const nuevoProducto = await Prisma.producto.create({
        data,
        //nombre: data.nombre,
        //precio: data.precio,
        //cantidad: data.cantidad,
        //disponibilidad: data.disponibilidad,

    });
    console.log("hola");
    res.status(201).json({
        message: "producto creado exitosamente",
        content: nuevoProducto,

    });
}catch (error){
    console.log(error);
    res.status(400).json({
        message: "Error al crear el producto",

    });
    }
};