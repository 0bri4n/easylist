import type { Metadata } from "next";
import { Bricolage_Grotesque } from "next/font/google";
import { cn } from "#/shared/lib/utils";
import Providers from "#/shared/components/providers";
import "./globals.css";

const bricolage = Bricolage_Grotesque({
	subsets: ["latin"],
	weight: ["400", "700"],
});

export const metadata: Metadata = {
	title: "Easylist",
	description: "Easylist - maneja tus estudiantes de una manera sencilla.",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en" suppressHydrationWarning>
			<body
				className={cn(
					"bg-background antialiased selection:bg-white selection:text-black",
					bricolage.className,
				)}
			>
				<Providers>{children}</Providers>
			</body>
		</html>
	);
}
