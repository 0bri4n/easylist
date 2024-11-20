import studentsJSON from "#/shared/lib/data/students.json";
import { columns } from "#/shared/components/modules/students/table/columns";
import { DataTable } from "#/shared/components/modules/students/table/data-table";
import type { Student } from "#/shared/lib/data/schema-student";

const students: Student[] = studentsJSON.map((student) => ({
	...student,
	sex: ["M", "F", "O"].includes(student.sex)
		? (student.sex as "M" | "F" | "O")
		: "O",
}));

export default function StudentsPage() {
	return (
		<>
			<div className="flex justify-between items-center mb-16">
				<div>
					<h1 className="text-4xl font-bold">Estudiantes</h1>
					<span className="text-gray-400">
						Administra los estudiantes de tu curso aquí.
					</span>
				</div>
			</div>

			<DataTable columns={columns} data={students} />
		</>
	);
}
