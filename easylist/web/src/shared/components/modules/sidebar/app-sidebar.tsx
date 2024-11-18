"use client";

import { Command } from "lucide-react";
import { NavSidebar } from "./nav-sidebar";
import {
	Sidebar,
	SidebarHeader,
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem,
} from "#/shared/components/ui/sidebar";
import { CourseSwitcher } from "./course-switch";

const COURSES = [
	{ name: "Programacion", logo: Command, members: "25 estudiantes" },
	{ name: "Matematicas", logo: Command, members: "25 estudiantes" },
];

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
	return (
		<Sidebar variant="floating" collapsible="icon" {...props}>
			<SidebarHeader>
				<SidebarMenu>
					<SidebarMenuItem>
						<SidebarMenuButton size="lg" asChild>
							<CourseSwitcher courses={COURSES} />
						</SidebarMenuButton>
					</SidebarMenuItem>
				</SidebarMenu>
			</SidebarHeader>

			<NavSidebar />
		</Sidebar>
	);
}
