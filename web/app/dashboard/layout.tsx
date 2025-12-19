import { Header } from "@/components/dashboard/Header";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-black-500 flex flex-col font-sans">
      {/* Header Fixo no Topo (Inclui KPIs) */}
      <Header />

      {/* Conteúdo Principal */}
      <main className="flex-1 p-6 max-w-[1600px] w-full mx-auto">
        {children}
      </main>
    </div>
  );
}