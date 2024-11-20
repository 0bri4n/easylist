"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import {
	Dialog,
	DialogClose,
	DialogContent,
	DialogFooter,
	DialogHeader,
	DialogTrigger,
} from "../../ui/dialog";
import { Button } from "../../ui/button";
import { Loader2, Plus } from "lucide-react";
import { useState } from "react";
import {
	Form,
	FormControl,
	FormDescription,
	FormField,
	FormItem,
	FormLabel,
	FormMessage,
} from "../../ui/form";
import { Input } from "../../ui/input";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "../../ui/select";
import { toast } from "#/shared/hooks/use-toast";

const formSchema = z.object({
	name: z
		.string()
		.min(2, "El nombre debe tener al menos 2 caracteres")
		.max(30, "El nombre debe tener menos de 30 caracteres"),
	age: z.number().min(1, "La edad debe ser positiva"),
	email: z.string().email("Correo inválido"),
	sex: z.enum(["M", "F", "O"]),
	cedula: z
		.string()
		.regex(/^(\d{3}-\d{7}-\d{1})$/, "Formato de cédula inválida"),
});

type FormValues = z.infer<typeof formSchema>;

export default function AddStudent() {
	const [open, setOpen] = useState<boolean>(false);

	const form = useForm<FormValues>({
		resolver: zodResolver(formSchema),
		defaultValues: {
			name: "",
			age: undefined,
			email: "",
			sex: "M",
			cedula: "",
		},
	});

	const onSubmit = async (values: FormValues) => {
		/** WIP: Simulamos el timeout de una peticion */
		await new Promise((resolve) => setTimeout(resolve, 2000))
		
		toast({
			title: "Estudiante creado con éxito",
			description: `El estudiante ${values.name} ha sido creado correctamente`,
		});

		setOpen(false);
		form.reset()
	};

	return (
		<Dialog open={open} onOpenChange={setOpen}>
			<DialogTrigger asChild>
				<Button>
					<Plus className="size-4" aria-hidden="true" />
					Add student
				</Button>
			</DialogTrigger>
			<DialogContent
				className="sm:max-w-[425px]"
				aria-describedby="Form create student"
			>
				<DialogHeader>
					<h2 className="text-xl font-semibold">Crear estudiante</h2>
				</DialogHeader>
				<Form {...form}>
					<form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
						<div className="flex flex-col gap-4">
							<FormField
								control={form.control}
								name="name"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Nombre completo</FormLabel>
										<FormControl>
											<Input placeholder="(e.g. John Doe)" {...field} />
										</FormControl>
										<FormMessage className="text-red-500" />
									</FormItem>
								)}
							/>

							<FormField
								control={form.control}
								name="age"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Edad</FormLabel>
										<FormControl>
											<Input
												type="number"
												placeholder="(e.g. 25)"
												value={field.value || ""}
												onChange={(e) => field.onChange(Number(e.target.value))}
											/>
										</FormControl>
										<FormMessage className="text-red-500" />
									</FormItem>
								)}
							/>

							<FormField
								control={form.control}
								name="email"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Correo electrónico</FormLabel>
										<FormControl>
											<Input
												type="email"
												placeholder="(e.g. john@doe.com)"
												{...field}
											/>
										</FormControl>
										<FormMessage className="text-red-500" />
									</FormItem>
								)}
							/>

							<FormField
								control={form.control}
								name="sex"
								defaultValue="M"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Género</FormLabel>
										<FormControl>
											<Select {...field}>
												<SelectTrigger>
													<SelectValue />
												</SelectTrigger>
												<SelectContent>
													<SelectItem value="M">Masculino</SelectItem>
													<SelectItem value="F">Femenino</SelectItem>
													<SelectItem value="O">Otro</SelectItem>
												</SelectContent>
											</Select>
										</FormControl>
										<FormMessage className="text-red-500" />
									</FormItem>
								)}
							/>

							<FormField
								control={form.control}
								name="cedula"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Cédula</FormLabel>
										<FormControl>
											<Input placeholder="(e.g. 001-0164336-9)" {...field} />
										</FormControl>
										<FormDescription>
											La cédula debe seguir el formato e incluir guiones.
										</FormDescription>
										<FormMessage className="text-red-500" />
									</FormItem>
								)}
							/>
						</div>

						<DialogFooter className="mt-4">
							<DialogClose asChild>
								<Button type="button" variant="outline">
									Cerrar
								</Button>
							</DialogClose>
							<Button type="submit" disabled={form.formState.isSubmitting}>
								{form.formState.isSubmitting ? (
									<>
										<Loader2 className="animate-spin" />
										Creando...
									</>
								) : (
									"Crear"
								)}
							</Button>
						</DialogFooter>
					</form>
				</Form>
			</DialogContent>
		</Dialog>
	);
}
