import prisma from "@prisma/client";
//  este sera la conexion a nuestra base de datos
// usando el patron singleton solamente generamos una conexion para todo nuestro proyecto
export const Prisma = new prisma.PrismaClient();