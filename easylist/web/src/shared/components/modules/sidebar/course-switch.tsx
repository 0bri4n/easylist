"use client";

import { ChevronsUpDown, Loader2, Plus } from "lucide-react";
import { useState, type FC } from "react";
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuLabel,
	DropdownMenuSeparator,
	DropdownMenuShortcut,
	DropdownMenuTrigger,
} from "#/shared/components/ui/dropdown-menu";
import {
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem,
	useSidebar,
} from "#/shared/components/ui/sidebar";
import { z } from "zod";
import { getRandomGradient } from "#/shared/lib/utils";
import { cn } from "#/shared/lib/utils";
import {
	Dialog,
	DialogClose,
	DialogContent,
	DialogFooter,
	DialogHeader,
	DialogTitle,
} from "../../ui/dialog";
import {
	Form,
	FormControl,
	FormField,
	FormItem,
	FormLabel,
	FormMessage,
} from "../../ui/form";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "../../ui/input";
import { Button } from "../../ui/button";
import { toast } from "#/shared/hooks/use-toast";

export interface Course {
	name: string;
	logo: React.ElementType;
	members: string;
}

export interface CourseSwitcherProps {
	courses: Course[];
	onCourseChange?: (course: Course) => void;
}

const formSchema = z.object({
	nombre: z
		.string()
		.min(6, "El curso debe tener al menos 6 caracteres")
		.max(40, "El curso debe tener menos de 40 caracteres"),
});

export const CourseSwitcher: FC<CourseSwitcherProps> = ({
	courses,
	onCourseChange,
}) => {
	const { isMobile } = useSidebar();
	const [activeCourse, setActiveCourse] = useState(courses[0]);
	const [isDialogOpen, setIsDialogOpen] = useState(false);

	const form = useForm<z.infer<typeof formSchema>>({
		resolver: zodResolver(formSchema),
		defaultValues: {
			nombre: "",
		},
	});

	const onSubmit = async (data: z.infer<typeof formSchema>) => {
		/** WIP: Simulamos el timeout de una peticion */
		await new Promise((resolve) => setTimeout(resolve, 2000))
		
		toast({
			title: "Curso creado con éxito",
			description: `El curso ${data.nombre} ha sido creado correctamente`,
		});

		setIsDialogOpen(false);
		form.reset();		
	};

	const handleCourseSelect = (course: Course) => {
		setActiveCourse(course);
		onCourseChange?.(course);
	};

	return (
		<SidebarMenu>
			<SidebarMenuItem>
				<DropdownMenu>
					<DropdownMenuTrigger asChild>
						<SidebarMenuButton
							size="lg"
							className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
						>
							<div className="flex items-center">
								<CourseLogo />
							</div>
							<div className="grid flex-1 text-left text-sm leading-tight">
								<span className="truncate font-semibold">
									{activeCourse.name}
								</span>
								<span className="truncate text-xs">{activeCourse.members}</span>
							</div>
							<ChevronsUpDown className="ml-auto" />
						</SidebarMenuButton>
					</DropdownMenuTrigger>
					<DropdownMenuContent
						className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
						align="start"
						side={isMobile ? "bottom" : "right"}
						sideOffset={4}
					>
						<DropdownMenuLabel className="text-xs text-muted-foreground">
							Cursos
						</DropdownMenuLabel>
						{courses.map((course, index) => (
							<DropdownMenuItem
								key={course.name}
								onClick={() => handleCourseSelect(course)}
								className="gap-2 p-2"
							>
								<CourseLogo className="size-6" />
								{course.name}
								<DropdownMenuShortcut>
									[{index + 1}/{courses.length}]
								</DropdownMenuShortcut>
							</DropdownMenuItem>
						))}
						<DropdownMenuSeparator />
						<DropdownMenuItem
							className="gap-2 p-2"
							onClick={() => setIsDialogOpen(true)}
						>
							<AddCourseAction />
						</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
			</SidebarMenuItem>
			<Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
				<DialogContent>
					<DialogHeader>
						<DialogTitle>Agregar nuevo curso</DialogTitle>
					</DialogHeader>
					<Form {...form}>
						<form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
							<div className="flex flex-col gap-4">
								<FormField
									control={form.control}
									name="nombre"
									render={({ field }) => (
										<FormItem>
											<FormLabel>Nombre del curso</FormLabel>
											<FormControl>
												<Input
													placeholder="(e.g. Ciencias sociales)"
													{...field}
												/>
											</FormControl>
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
		</SidebarMenu>
	);
};

const CourseLogo: FC<{ className?: string }> = ({ className }) => (
	<div
		className={cn(
			"flex size-8 items-center justify-center rounded-sm",
			className,
		)}
		style={{ background: getRandomGradient() }}
	/>
);

const AddCourseAction: FC = () => (
	<>
		<div className="flex size-6 items-center justify-center rounded-md border bg-background">
			<Plus className="size-4" />
		</div>
		<div className="font-medium text-muted-foreground">Agregar curso</div>
	</>
);
