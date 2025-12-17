import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { cn } from "@/lib/utils";

// Configuração da Banana Grotesk
const bananaGrotesk = localFont({
  src: [
    {
      path: './fonts/banana-grotesk-light.otf',
      weight: '300', // Quando usar font-light
      style: 'normal',
    },
    {
      path: './fonts/banana-grotesk-regular.otf',
      weight: '400', // O padrão (font-normal)
      style: 'normal',
    },
    {
      path: './fonts/banana-grotesk-semibold.otf',
      weight: '600', // Quando usar font-semibold
      style: 'normal',
    },
    {
      path: './fonts/banana-grotesk-bold.otf',
      weight: '700', // Quando usar font-bold
      style: 'normal',
    },
    {
      path: './fonts/banana-grotesk-extrabold.otf',
      weight: '800', // Quando usar font-extrabold
      style: 'normal',
    },
  ],
  variable: '--font-banana', // Nome da variável CSS
  display: 'swap',
});

export const metadata: Metadata = {
  title: "PipLy Financial",
  description: "Plataforma de Trading Inteligente",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body className={cn(
        "min-h-screen bg-slate-950 font-sans antialiased", 
        bananaGrotesk.variable // Injeta a variável aqui
      )}>
        {children}
      </body>
    </html>
  );
}