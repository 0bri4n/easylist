"use client";

import type { ColumnDef } from "@tanstack/react-table";
import { Checkbox } from "#/shared/components/ui/checkbox";
import type { Student } from "#/shared/lib/data/schema-student";

export const columns: ColumnDef<Student>[] = [
	{
		id: "select",
		header: ({ table }) => (
			<Checkbox
				checked={
					table.getIsAllPageRowsSelected() ||
					(table.getIsSomePageRowsSelected() && "indeterminate")
				}
				onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
				aria-label="Select all"
				className="translate-y-[2px]"
			/>
		),
		cell: ({ row }) => (
			<Checkbox
				checked={row.getIsSelected()}
				onCheckedChange={(value) => row.toggleSelected(!!value)}
				aria-label="Select row"
				className="translate-y-[2px]"
			/>
		),
		enableSorting: false,
		enableHiding: false,
	},
	{
		accessorKey: "name",
		header: "Nombre",
		cell: ({ row }) => <span>{row.original.name}</span>,
	},
	{
		accessorKey: "email",
		header: "Correo",
		cell: ({ row }) => <span>{row.original.email}</span>,
	},
	{
		accessorKey: "age",
		header: "Cedula",
		cell: ({ row }) => <span>{row.original.age}</span>,
	},
	{
		accessorKey: "cedula",
		header: "Cedula",
		cell: ({ row }) => <span>{row.original.cedula}</span>,
	},
	{
		accessorKey: "sex",
		header: "Genero",
		cell: ({ row }) => <span>{row.original.sex}</span>,
	},
];
