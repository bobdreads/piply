import Link from "next/link";
import { 
  LayoutDashboard, 
  PieChart, 
  ArrowLeftRight, 
  FileText, 
  LifeBuoy, 
  Settings,
  LogOut 
} from "lucide-react";

const menuItems = [
  { icon: LayoutDashboard, label: "Visão Geral", href: "/dashboard" },
  { icon: ArrowLeftRight, label: "Meus Trades", href: "/dashboard/trades" },
  { icon: PieChart, label: "Estratégias", href: "/dashboard/strategies" },
  { icon: FileText, label: "Relatórios Fiscais", href: "/dashboard/tax-reports" },
  { icon: LifeBuoy, label: "Suporte", href: "/dashboard/support" },
];

export function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800 hidden md:flex flex-col h-screen fixed left-0 top-0">
      {/* Logo Area */}
      <div className="h-16 flex items-center px-6 border-b border-slate-800">
        <span className="text-xl font-bold text-white">
          PipLy <span className="text-emerald-500">App</span>
        </span>
      </div>

      {/* Navigation */}
      <nav className="flex-1 py-6 px-3 space-y-1">
        {menuItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="flex items-center gap-3 px-3 py-2.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded-lg transition-colors group"
          >
            <item.icon size={20} className="group-hover:text-emerald-400 transition-colors" />
            <span className="font-medium text-sm">{item.label}</span>
          </Link>
        ))}
      </nav>

      {/* Footer Area */}
      <div className="p-4 border-t border-slate-800 space-y-1">
        <button className="w-full flex items-center gap-3 px-3 py-2.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded-lg transition-colors">
          <Settings size={20} />
          <span className="font-medium text-sm">Configurações</span>
        </button>
        <button className="w-full flex items-center gap-3 px-3 py-2.5 text-red-400 hover:text-red-300 hover:bg-red-500/10 rounded-lg transition-colors">
          <LogOut size={20} />
          <span className="font-medium text-sm">Sair</span>
        </button>
      </div>
    </aside>
  );
}