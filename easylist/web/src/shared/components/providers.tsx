import { ThemeProvider as NextThemeProvider } from "next-themes";
import { Toaster } from "./ui/toaster";

export default function Providers({ children }: { children: React.ReactNode }) {
	return (
		<NextThemeProvider
			attribute="class"
			defaultTheme="dark"
			disableTransitionOnChange
		>
			<Toaster />
			{children}
		</NextThemeProvider>
	);
}
