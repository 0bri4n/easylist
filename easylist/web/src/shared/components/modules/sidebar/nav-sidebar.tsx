"use client";

import {
	CalendarCheck,
	LibraryBig,
	LifeBuoy,
	ListOrdered,
	MessageCircleWarning,
	Newspaper,
	PieChart,
	Send,
	TableOfContents,
	Users,
} from "lucide-react";
import {
	SidebarContent,
	SidebarFooter,
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem,
	SidebarGroup,
	SidebarGroupLabel,
	SidebarGroupContent,
} from "#/shared/components/ui/sidebar";
import { NavUser } from "./nav-user";
import { BASE_URL_API } from "#/shared/lib/consts";

const TEACHER_DATA = {
	name: "Waldis Yael",
	email: "waldistaveras@gmail.com",
	avatar: "/avatars/waldis.jpg",
};

export const DATA_NAVBAR = {
	plataforma: [
		{ title: "Estudiantes", url: "/d/estudiantes", icon: Users },
		{ title: "Asistencia", url: "/d/asistencia", icon: ListOrdered },
		{ title: "Programacion", url: "/d/programacion", icon: CalendarCheck },
		{ title: "Exámenes", url: "/d/examenes", icon: Newspaper },
	],
	analitica: [
		{ title: "Calificaciones", url: "/d/calificaciones", icon: LibraryBig },
		{ title: "Estadisticas", url: "/d/estadisticas", icon: PieChart },
		{ title: "Reportes", url: "/d/reportes", icon: MessageCircleWarning },
	],
	otros: [
		{
			title: "API docs",
			url: BASE_URL_API.replace("/api/v1", "/docs"),
			icon: TableOfContents,
		},
	],
	secundarios: [
		{ title: "Soporte", url: "#", icon: LifeBuoy },
		{ title: "Feedback", url: "#", icon: Send },
	],
};

export const NavSidebar = () => {
	return (
		<>
			<SidebarContent>
				<SidebarGroup>
					<SidebarGroupLabel>Plataforma</SidebarGroupLabel>
					<SidebarMenu>
						{DATA_NAVBAR.plataforma.map((item) => (
							<SidebarMenuButton asChild key={item.title}>
								<a href={item.url}>
									<item.icon />
									<span>{item.title}</span>
								</a>
							</SidebarMenuButton>
						))}
					</SidebarMenu>
				</SidebarGroup>

				<SidebarGroup>
					<SidebarGroupLabel>Analitica</SidebarGroupLabel>
					<SidebarMenu>
						{DATA_NAVBAR.analitica.map((item) => (
							<SidebarMenuButton asChild key={item.title}>
								<a href={item.url}>
									<item.icon />
									<span>{item.title}</span>
								</a>
							</SidebarMenuButton>
						))}
					</SidebarMenu>
				</SidebarGroup>

				<SidebarGroup>
					<SidebarGroupLabel>Otros</SidebarGroupLabel>
					<SidebarMenu>
						{DATA_NAVBAR.otros.map((item) => (
							<SidebarMenuButton asChild key={item.title}>
								<a href={item.url}>
									<item.icon />
									<span>{item.title}</span>
								</a>
							</SidebarMenuButton>
						))}
					</SidebarMenu>
				</SidebarGroup>

				<SidebarGroup className="mt-auto">
					<SidebarGroupContent>
						<SidebarMenu>
							{DATA_NAVBAR.secundarios.map((item) => (
								<SidebarMenuItem key={item.title}>
									<SidebarMenuButton asChild size="sm">
										<a href={item.url}>
											<item.icon />
											<span>{item.title}</span>
										</a>
									</SidebarMenuButton>
								</SidebarMenuItem>
							))}
						</SidebarMenu>
					</SidebarGroupContent>
				</SidebarGroup>
			</SidebarContent>

			<SidebarFooter>
				<NavUser user={TEACHER_DATA} />
			</SidebarFooter>
		</>
	);
};
