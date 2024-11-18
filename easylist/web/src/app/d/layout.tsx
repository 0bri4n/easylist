"use client";

import { AppSidebar } from "#/shared/components/modules/sidebar/app-sidebar";
import { DATA_NAVBAR } from "#/shared/components/modules/sidebar/nav-sidebar";
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

const DashboardLayout = ({ children }: { children: React.ReactNode }) => {
	const pathname = usePathname();
	const breadcrumb = getBreadcrumb(pathname);

	return (
		<SidebarProvider>
			<AppSidebar />
			<SidebarInset>
				<header className="flex h-16 shrink-0 items-center gap-2 px-4">
					<SidebarTrigger className="-ml-1" />
					<Separator orientation="vertical" className="mr-2 h-4" />
					<Breadcrumb>
						<BreadcrumbList>
							{breadcrumb.parent && (
								<BreadcrumbItem>
									<BreadcrumbLink
										href={breadcrumb.parent.url}
										className="pointer-events-none"
									>
										{breadcrumb.parent.title}
									</BreadcrumbLink>
								</BreadcrumbItem>
							)}

							{breadcrumb.parent && <BreadcrumbSeparator />}

							<BreadcrumbItem>
								<BreadcrumbPage>{breadcrumb.current}</BreadcrumbPage>
							</BreadcrumbItem>
						</BreadcrumbList>
					</Breadcrumb>
				</header>

				<div className="mt-8 px-12">{children}</div>
			</SidebarInset>
		</SidebarProvider>
	);
};

export default DashboardLayout;

const getBreadcrumb = (pathname: string) => {
	const section = pathname.split("/")[2];
	const allSections = Object.entries(DATA_NAVBAR);

	for (const [parentKey, items] of allSections) {
		const parent = parentKey.charAt(0).toUpperCase() + parentKey.slice(1);
		const foundItem = items.find((item) => item.url.endsWith(section));

		if (foundItem) {
			return {
				parent: { title: parent, url: `/d/${parentKey}` },
				current: foundItem.title,
			};
		}
	}

	return { parent: null, current: "Dashboard" };
};
