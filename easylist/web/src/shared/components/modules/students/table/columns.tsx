"use client";

import type { ColumnDef } from "@tanstack/react-table";
import { Checkbox } from "#/shared/components/ui/checkbox";
import type { Student } from "#/shared/lib/data/schema-student";
import { Badge } from "#/shared/components/ui/badge";
import { DataTableColumnHeader } from "./data-table-header";
import { DataTableRowActions } from "./data-table-row-actions";

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
		accessorKey: "id",
		header: "ID",
		cell: ({ row }) => <span>{row.getValue("id")}</span>,
		enableHiding: false,
	},
	{
		accessorKey: "name",
		header: ({ column }) => (
			<DataTableColumnHeader column={column} title="Nombre" />
		),
		cell: ({ row }) => <span>{row.getValue("name")}</span>,
	},
	{
		accessorKey: "email",
		header: "Correo",
		cell: ({ row }) => <span>{row.getValue("email")}</span>,
	},
	{
		accessorKey: "age",
		header: "Edad",
		cell: ({ row }) => <span>{row.getValue("age")}</span>,
	},
	{
		accessorKey: "cedula",
		header: "Cedula",
		cell: ({ row }) => <span>{row.getValue("cedula")}</span>,
	},
	{
		accessorKey: "sex",
		header: "Género",
		cell: ({ row }) => <Badge variant="outline">{row.getValue("sex")}</Badge>,
	},
	{
		id: "actions",
		cell: ({ row }) => <DataTableRowActions row={row} />,
	},
];
