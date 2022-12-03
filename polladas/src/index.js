import  express, {json} from "express";

const servidor= express();
// este json lo uso cuando me envien body en formato JSON express lo pueda leer y transformar a un formato legible
servidor.use(json());
// estos son las variables de entorno en formato JSON
// Nullish coalescing operator 
const PORT = process.env.PORT ?? 5000;

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
