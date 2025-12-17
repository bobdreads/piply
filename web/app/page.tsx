import { ArrowRight, TrendingUp, ShieldCheck, Globe } from "lucide-react";
import Link from "next/link";
import { Button } from "@/components/ui/Button"; // <--- Importamos o nosso componente

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-slate-950 text-slate-50 relative overflow-hidden">
      {/* ... (Fundo e Header mantêm-se iguais) ... */}
      
      <div className="z-10 max-w-5xl w-full flex flex-col items-center text-center px-6">
        
        {/* ... (Badge e Títulos mantêm-se iguais) ... */}
        <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6 bg-gradient-to-br from-white to-slate-400 bg-clip-text text-transparent">
          PipLy <span className="text-emerald-500">Financial</span>
        </h1>
        
        <p className="mt-4 text-slate-400 text-lg md:text-xl max-w-2xl leading-relaxed mb-10">
          A plataforma definitiva para traders brasileiros operarem no mundo todo.
          Controle ações, futuros, forex e cripto com 
          <strong className="text-slate-200 font-medium"> cálculo automático de impostos</strong>.
        </p>

        {/* --- AQUI USAMOS OS NOVOS COMPONENTES --- */}
        <div className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
          
          {/* Botão Primário (Envolvido num Link pois navega para outra página) */}
          <Link href="/dashboard">
            <Button variant="primary" size="lg" className="w-full sm:w-auto">
              Acessar Dashboard
              <ArrowRight size={20} className="ml-2" />
            </Button>
          </Link>
          
          {/* Botão Secundário */}
          <Button variant="secondary" size="lg" className="w-full sm:w-auto">
            <Globe size={20} className="mr-2" />
            Documentação
          </Button>

        </div>
        {/* ---------------------------------------- */}

        {/* ... (Estatísticas mantêm-se iguais) ... */}
         <div className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8 text-slate-400 border-t border-slate-800 pt-10 w-full">
          {/* Podes manter o resto do código igual ao anterior */}
          <div className="flex flex-col items-center">
            <span className="text-3xl font-bold text-white mb-1">B3 & Exterior</span>
            <span className="text-sm">Integração Híbrida</span>
          </div>
          <div className="flex flex-col items-center">
            <span className="text-3xl font-bold text-white mb-1 flex items-center gap-2">
              <TrendingUp size={24} className="text-emerald-500" />
              Automático
            </span>
            <span className="text-sm">Cotação do Dólar (PTAX)</span>
          </div>
          <div className="flex flex-col items-center">
            <span className="text-3xl font-bold text-white mb-1">100%</span>
            <span className="text-sm">Conformidade Fiscal</span>
          </div>
        </div>
      </div>
    </main>
  );
}