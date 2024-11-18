"use client";

import { ChevronsUpDown, Plus } from "lucide-react";
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
import { getRandomGradient } from "#/shared/lib/utils";
import { cn } from "#/shared/lib/utils";

export interface Course {
	name: string;
	logo: React.ElementType;
	members: string;
}

interface CourseSwitcherProps {
	courses: Course[];
	onCourseChange?: (course: Course) => void;
}

export const CourseSwitcher: FC<CourseSwitcherProps> = ({
	courses,
	onCourseChange,
}) => {
	const { isMobile } = useSidebar();
	const [activeCourse, setActiveCourse] = useState(courses[0]);

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
						<DropdownMenuItem className="gap-2 p-2">
							<AddCourseButton />
						</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
			</SidebarMenuItem>
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

const AddCourseButton: FC = () => (
	<>
		<div className="flex size-6 items-center justify-center rounded-md border bg-background">
			<Plus className="size-4" />
		</div>
		<div className="font-medium text-muted-foreground">Agregar curso</div>
	</>
);
