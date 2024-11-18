"use client";

import type { Table } from "@tanstack/react-table";

import { Button } from "#/shared/components/ui/button";
import { Input } from "#/shared/components/ui/input";
import AddStudent from "../add-student";
import { SearchIcon } from "lucide-react";

export function DataTableToolbar<TData>({ table }: { table: Table<TData> }) {
	const isFiltered = table.getState().columnFilters.length > 0;

	return (
		<div className="flex items-center justify-between">
			<div className="flex flex-1 items-center space-x-2">				
				<Input
					placeholder="Buscar estudiantes..."
					value={(table.getColumn("name")?.getFilterValue() as string) ?? ""}
					onChange={(event) =>
						table.getColumn("name")?.setFilterValue(event.target.value)
					}
					className="h-8 w-[250px] lg:w-[444px]"
				/>

				{isFiltered && (
					<Button
						variant="ghost"
						onClick={() => table.resetColumnFilters()}
						className="h-8 px-2 lg:px-3"
					>
						Reiniciar
					</Button>
				)}
			</div>
			<AddStudent />
		</div>
	);
}
