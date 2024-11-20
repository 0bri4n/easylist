"use client";

import { useState } from "react";
import { Loader2, MoreHorizontal } from "lucide-react";
import { toast } from "#/shared/hooks/use-toast";
import {
	AlertDialog,
	AlertDialogCancel,
	AlertDialogContent,
	AlertDialogDescription,
	AlertDialogFooter,
	AlertDialogHeader,
	AlertDialogTitle,
	AlertDialogTrigger,
} from "#/shared/components/ui/alert-dialog";
import { Button } from "#/shared/components/ui/button";
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuTrigger,
} from "#/shared/components/ui/dropdown-menu";
import {
	Dialog,
	DialogContent,
	DialogTrigger,
} from "#/shared/components/ui/dialog";
import type { Row } from "@tanstack/react-table";
import { schemaStudent } from "#/shared/lib/data/schema-student";

interface DataTableRowActionsProps<TData> {
	row: Row<TData>;
}

export function DataTableRowActions<TData>({
	row,
}: DataTableRowActionsProps<TData>) {
	const student = schemaStudent.parse(row.original);

	const [isDialogOpen, setIsDialogOpen] = useState<boolean>(false);
	const [isLoaderRequest, setIsLoaderRequest] = useState<boolean>(false);
	const [open, setOpen] = useState<boolean>(false);

	const onSubmit = async () => {
		/** WIP: Simulamos el timeout de una peticion */
		setIsLoaderRequest(true);
		await new Promise((resolve) => setTimeout(resolve, 2000));

		toast({
			title: "Estudiante eliminado con exito",
			description: `El estudiante ${student.name} ha sido eliminado correctamente`,
		});

		setIsLoaderRequest(false);
		setIsDialogOpen(false);
	};

	return (
		<DropdownMenu>
			<DropdownMenuTrigger asChild>
				<Button
					variant="ghost"
					className="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
				>
					<MoreHorizontal />
				</Button>
			</DropdownMenuTrigger>
			<DropdownMenuContent align="end" className="w-[160px]">
				<Dialog open={open} onOpenChange={setOpen}>
					<DialogTrigger asChild>
						<Button
							variant="ghost"
							className="w-full text-sm h-8 justify-start"
						>
							Editar
						</Button>
					</DialogTrigger>
					<DialogContent
						className="sm:max-w-[425px]"
						aria-describedby="Form create student"
					>
						A
					</DialogContent>
				</Dialog>

				<AlertDialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
					<AlertDialogTrigger asChild>
						<Button
							variant="ghost"
							className="w-full text-sm h-8 justify-start"
						>
							Eliminar
						</Button>
					</AlertDialogTrigger>
					<AlertDialogContent>
						<AlertDialogHeader>
							<AlertDialogTitle>¿Estás totalmente seguro?</AlertDialogTitle>
							<AlertDialogDescription>
								Seguro que quiere eliminar a{" "}
								<span className="text-white">{student.name}</span>, una vez
								eliminado no podrá recuperar su información.
								<span className="text-white">
									{" "}
									¿Estás seguro de que deseas continuar?
								</span>
							</AlertDialogDescription>
						</AlertDialogHeader>
						<AlertDialogFooter>
							<AlertDialogCancel onClick={() => setIsDialogOpen(false)}>
								Cancelar
							</AlertDialogCancel>
							<Button variant="destructive" onClick={() => onSubmit()}>
								{isLoaderRequest ? (
									<>
										<Loader2 className="animate-spin" />
										Eliminando...
									</>
								) : (
									"Eliminar"
								)}
							</Button>
						</AlertDialogFooter>
					</AlertDialogContent>
				</AlertDialog>
			</DropdownMenuContent>
		</DropdownMenu>
	);
}
