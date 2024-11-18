import { z } from "zod";

export const schemaStudent = z.object({
	id: z.string(),
	name: z.string(),
	email: z.string(),
	age: z.number(),
	cedula: z.string(),
	sex: z.enum(["M", "F", "O"]),
});

export type Student = z.infer<typeof schemaStudent>;
