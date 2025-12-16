import { ArrowRight } from "lucide-react";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-slate-950 text-white p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <h1 className="text-4xl font-bold text-emerald-400 mb-4">
          PipLy <span className="text-white">Financial</span>
        </h1>
      </div>
      
      <p className="mt-4 text-slate-400 text-lg text-center max-w-2xl">
        A plataforma definitiva para traders brasileiros operarem no mundo todo.
        Controle ações, futuros, forex e cripto com inteligência fiscal.
      </p>

      <button className="mt-8 px-6 py-3 bg-emerald-500 hover:bg-emerald-600 text-white rounded-lg font-semibold flex items-center gap-2 transition-all">
        Acessar Dashboard
        <ArrowRight size={20} />
      </button>
    </main>
  );
}