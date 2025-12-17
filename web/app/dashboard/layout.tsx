import { Sidebar } from "@/components/dashboard/Sidebar";
import { Header } from "@/components/dashboard/Header";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-950 flex">
      {/* Sidebar Fixa */}
      <Sidebar />

      {/* Área de Conteúdo (Deslocada para a direita para não ficar baixo da sidebar) */}
      <div className="flex-1 md:ml-64 flex flex-col min-h-screen">
        <Header />
        
        {/* Onde o conteúdo das páginas vai entrar */}
        <main className="flex-1 p-6 overflow-y-auto">
          {children}
        </main>
      </div>
    </div>
  );
}