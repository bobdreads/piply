import { Header } from "@/components/dashboard/Header";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    // IMPORTANTE: 'relative overflow-hidden' impede que o SVG crie barras de scroll laterais
    <div className="min-h-screen dashboard-bg flex flex-col font-sans relative overflow-hidden">
      <div className="relative z-10 flex flex-col flex-1">
        <Header />
        <main className="flex-1 p-6 max-w-[1600px] w-full mx-auto">
          {children}
        </main>
      </div>
    </div>
  );
}