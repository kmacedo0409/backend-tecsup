import express from "express";
import mongoose from "mongoose";
import { usuarioRouter } from "./routes/usuarioRoute.js";

const server = express();
const PORT =process.env.PORT ?? 5000;

server.use(express.json());
server.use(usuarioRouter);

server.listen(PORT, async ()=>{
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
    try{
        mongoose.set("strictQuery", false);
        await mongoose.connect(process.env.MONGO_URI,{});
        console.log("conexion exitosa a la base de datos");

    }catch (error) {
        console.log("Error al conectarse a la base de datos");
    }
});
