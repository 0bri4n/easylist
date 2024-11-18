import { Button } from "#/shared/components/ui/button";
import {
	Card,
	CardContent,
	CardDescription,
	CardHeader,
	CardTitle,
} from "#/shared/components/ui/card";
import { Input } from "#/shared/components/ui/input";
import { Label } from "#/shared/components/ui/label";
import Link from "next/link";

export default function LoginPage() {
	return (
		<div className="flex h-screen w-full items-center justify-center px-4">
			<Card className="mx-auto max-w-sm">
				<CardHeader>
					<CardTitle className="text-2xl">Iniciar sesión</CardTitle>
					<CardDescription>
						Ingresa tus credenciales para continuar.
					</CardDescription>
				</CardHeader>
				<CardContent>
					<div className="grid gap-4">
						<div className="grid gap-2">
							<Label htmlFor="email">Correo</Label>
							<Input
								id="email"
								type="email"
								placeholder="john@doe.com"
								required
							/>
						</div>
						<div className="grid gap-2">
							<div className="flex items-center">
								<Label htmlFor="password">Contraseña</Label>
							</div>
							<Input id="password" type="password" required />
						</div>
						<Button type="submit" className="w-full">
							Iniciar sesión
						</Button>
					</div>
					<div className="mt-4 text-center">
						<p className="px-4 text-center text-xs text-muted-foreground">
							<span className="underline text-white">Easylist</span> es un
							proyecto realizado con fines educativos por el grupo{" "}
							<span className="underline text-white">
								Los dueños de Python.
							</span>
						</p>
					</div>
				</CardContent>
			</Card>
		</div>
	);
}
