import mongoose from "mongoose";
import express from "express";
const productoSchema = new mongoose.Schema({
    nombre: {
    type: mongoose.Schema.Types.String,
    unique:true,
    maxLength:50,
    required:true,
    },
    precio:{
        type:mongoose.Schema.Types.Decimal128,
        max:100.0,
    },
});
const Producto = mongoose.model("productos", productoSchema);

const servidor =express();
const PORT =process.env.PORT ?? 5000;
servidor.listen(PORT, async()=>{

    console.log(`servidor corriendo exitosamente en el puerto ${PORT}`);
    try{
        await mongoose.connect('mongodb://127.0.0.1:027017/express');
        console.log("Conexion a la base de datos");
    }catch (e){
        console.log("Error al conectarse a la base de datos");
    }
});