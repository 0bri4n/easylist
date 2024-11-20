"use client";

import { useState } from "react";
import { Button } from "#/shared/components/ui/button";
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuTrigger,
} from "#/shared/components/ui/dropdown-menu";
import { FileSpreadsheet, FileText, Loader2, Plus } from "lucide-react";
import { toast } from "#/shared/hooks/use-toast";

export default function CompactExportButton() {
	const [isLoading, setIsLoading] = useState(false);

	const handleExport = async (format: "csv" | "pdf") => {
		setIsLoading(true);
		try {
			await new Promise((resolve) => setTimeout(resolve, 1000));

			toast({
				description: `Exportado como ${format.toUpperCase()}`,
				duration: 2000,
			});
		} catch (error) {
			toast({
				description: "Error en la exportación",
				variant: "destructive",
				duration: 2000,
			});
		} finally {
			setIsLoading(false);
		}
	};

	return (
		<DropdownMenu>
			<DropdownMenuTrigger asChild>
				<Button disabled={isLoading} className="flex items-center">
					{isLoading ? (
						<Loader2 className="size-4 animate-spin" />
					) : (
						<Plus className="size" />
					)}
					<span className="font-semibold">Exportar</span>
				</Button>
			</DropdownMenuTrigger>
			<DropdownMenuContent align="end">
				<DropdownMenuItem onClick={() => handleExport("csv")}>
					<FileSpreadsheet className="mr-2 size-4" />
					<span>CSV</span>
				</DropdownMenuItem>
				<DropdownMenuItem onClick={() => handleExport("pdf")}>
					<FileText className="mr-2 size-4" />
					<span>PDF</span>
				</DropdownMenuItem>
			</DropdownMenuContent>
		</DropdownMenu>
	);
}
