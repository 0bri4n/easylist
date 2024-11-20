"use client";

import { AppSidebar } from "#/shared/components/modules/sidebar/app-sidebar";
import {
	Breadcrumb,
	BreadcrumbItem,
	BreadcrumbLink,
	BreadcrumbList,
	BreadcrumbPage,
	BreadcrumbSeparator,
} from "#/shared/components/ui/breadcrumb";
import { Separator } from "#/shared/components/ui/separator";
import {
	SidebarInset,
	SidebarProvider,
	SidebarTrigger,
} from "#/shared/components/ui/sidebar";
import { usePathname } from "next/navigation";

const SettingsLayout = ({ children }: { children: React.ReactNode }) => {
	const pathname = usePathname();
	const breadcrumb =
		pathname
			.split("/")
			.pop()
			?.replace(/^\w/, (c) => c.toUpperCase()) || "???";

	return (
		<SidebarProvider>
			<AppSidebar />
			<SidebarInset>
				<header className="flex h-16 shrink-0 items-center gap-2 px-4">
					<SidebarTrigger className="-ml-1" />
					<Separator orientation="vertical" className="mr-2 h-4" />
					<Breadcrumb>
						<BreadcrumbList>
							<BreadcrumbItem>
								<BreadcrumbLink href="AAA" className="pointer-events-none">
									S(ettings)
								</BreadcrumbLink>
							</BreadcrumbItem>

							<BreadcrumbSeparator />

							<BreadcrumbItem>
								<BreadcrumbPage>{breadcrumb}</BreadcrumbPage>
							</BreadcrumbItem>
						</BreadcrumbList>
					</Breadcrumb>
				</header>

				<div className="mt-8 px-12">{children}</div>
			</SidebarInset>
		</SidebarProvider>
	);
};

export default SettingsLayout;
