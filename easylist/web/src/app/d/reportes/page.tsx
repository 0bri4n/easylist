import ExportButton from "#/shared/components/modules/reports/export-button";

export default function ReportsPage() {
	return (
		<>
			<div className="flex justify-between items-center">
				<div>
					<h1 className="text-4xl font-bold">Reportes</h1>
					<span className="text-gray-400">
						Genera reportes de tus estudiantes aquí.
					</span>
				</div>
				<ExportButton />
			</div>
		</>
	);
}
