import * as React from "react";
import { Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

// Definimos as variantes disponíveis (igual às Properties do Figma)
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "outline" | "ghost" | "danger";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean; // Para mostrar spinner de carregamento
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = "primary", size = "md", isLoading, children, disabled, ...props }, ref) => {
    
    // Estilos Base (Aplicados a todos os botões)
    const baseStyles = "inline-flex items-center justify-center rounded-xl font-medium transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 disabled:pointer-events-none disabled:opacity-50 active:scale-95";
    
    // Variantes de Estilo (Cores)
    const variants = {
      primary: "bg-emerald-600 text-white hover:bg-emerald-500 shadow-lg shadow-emerald-900/20",
      secondary: "bg-slate-800 text-slate-200 hover:bg-slate-700 border border-slate-700",
      outline: "border-2 border-slate-700 bg-transparent hover:bg-slate-800 text-slate-200",
      ghost: "hover:bg-slate-800 text-slate-400 hover:text-white",
      danger: "bg-red-500/10 text-red-400 hover:bg-red-500/20 border border-red-500/20",
    };

    // Variantes de Tamanho
    const sizes = {
      sm: "h-9 px-3 text-xs",
      md: "h-11 px-8 py-2 text-sm",
      lg: "h-14 px-10 text-base",
    };

    return (
      <button
        ref={ref}
        disabled={disabled || isLoading}
        className={cn(
          baseStyles,
          variants[variant],
          sizes[size],
          className // Permite passar classes extra se necessário
        )}
        {...props}
      >
        {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
        {children}
      </button>
    );
  }
);

Button.displayName = "Button";

export { Button };