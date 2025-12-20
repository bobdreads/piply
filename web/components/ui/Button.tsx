import * as React from "react";
import { Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

// Definimos as variantes disponíveis (igual às Properties do Figma)
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "danger" | "notification" | "profile";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean; // Para mostrar spinner de carregamento
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = "primary", size = "md", isLoading, children, disabled, ...props }, ref) => {
    
    // Estilos Base (Aplicados a todos os botões)
    const baseStyles = "inline-flex items-center justify-center rounded-lg font-sans transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 disabled:pointer-events-none disabled:opacity-50 active:scale-95";
    
    // Variantes de Estilo (Cores)
    const variants = {
      primary: "bg-white text-black-500 hover:bg-primary-400 font-sans px",
      danger: "bg-danger-500/10 text-danger-500 hover:bg-danger-500/20 border border-danger-500/20",
      notification:"p-8 bg-[#1d1d1d] text-white hover:text-primary-400",
      profile: "w-10 h-10 overflow-hidden",
    };

    // Variantes de Tamanho
    const sizes = {
      sm: "h-9 px-3 text-xs",
      md: "p-2 text-base",
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