import mongoose from "mongoose";

const direccionSchema = new mongoose.Schema({
    calle: mongoose.Schema.Types.String,
    numero: mongoose.Schema.Types.String,
    codigoPostal: {
        alias: "codigo_postal", // indica como se llevara la columna de la base de datos
        type: mongoose.Schema.Types.String,
    },
},{
    _id: false,

});

const usuarioSchema = new mongoose.Schema({
    nombre:  {
        type: mongoose.Schema.Types.String,
        required: true,
    },
    email:{
        type: mongoose.Schema.Types.String,
        unique:true,
        required:true,
    },
    password: {
        type: mongoose.Schema.Types.String,
        required:true,
    },
    direcciones: [direccionSchema],
},{
    timestamps: {
        createdAt:"fechaCreacion",
        updatedAt:"fechaActualizacion",
    },
});

export const Usuario = mongoose.model("usuarios", usuarioSchema);