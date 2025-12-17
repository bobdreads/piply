import { Button } from "@/components/ui/Button"; // Reutilizando nosso componente!
import { Bell } from "lucide-react";

export function Header() {
  return (
    <header className="h-16 bg-slate-950 border-b border-slate-800 flex items-center justify-between px-6 sticky top-0 z-20">
      {/* Lado Esquerdo (Título ou Breadcrumb) */}
      <div>
        <h2 className="text-white font-semibold">Dashboard</h2>
      </div>

      {/* Lado Direito (Ações) */}
      <div className="flex items-center gap-4">
        <button className="text-slate-400 hover:text-white transition-colors relative">
          <Bell size={20} />
          <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-500 rounded-full border-2 border-slate-950"></span>
        </button>
        
        {/* Placeholder do Usuário */}
        <div className="flex items-center gap-3 pl-4 border-l border-slate-800">
          <div className="text-right hidden sm:block">
            <p className="text-sm font-medium text-white">Trader Pro</p>
            <p className="text-xs text-slate-400">Plano Basic</p>
          </div>
          <div className="w-8 h-8 rounded-full bg-emerald-600 flex items-center justify-center text-white font-bold text-xs">
            TP
          </div>
        </div>
      </div>
    </header>
  );
}