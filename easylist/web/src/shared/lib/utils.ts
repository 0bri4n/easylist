import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
	return twMerge(clsx(inputs));
}

const getRandomColor = () =>
	`#${Array.from({ length: 6 }, () => "0123456789ABCDEF"[Math.floor(Math.random() * 16)]).join("")}`;
export const getRandomGradient = () =>
	`linear-gradient(135deg, ${getRandomColor()}, ${getRandomColor()})`;
