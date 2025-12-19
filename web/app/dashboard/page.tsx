import { Card } from "@/components/ui/Card";
import { ArrowUpRight, Calendar, BarChart3, PieChart, Activity, LayoutGrid } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      
      {/* Abas de Navegação Interna */}
      <div className="flex items-center gap-6 mb-8 border-b border-black-400 pb-1">
        <TabItem active icon={LayoutGrid} label="Overview" />
        <TabItem icon={Activity} label="Time Metrics" />
        <TabItem icon={BarChart3} label="Analytics" />
        <TabItem icon={Calendar} label="Calendar" />
      </div>

      {/* GRID PRINCIPAL: Gráfico (2/3) + Lista Lateral (1/3) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* --- COLUNA ESQUERDA: GRÁFICO (Ocupa 8 colunas) --- */}
        <div className="lg:col-span-8">
          <Card className="h-[500px] bg-black-400 border-black-300/50 p-8 flex flex-col justify-between relative overflow-hidden group">
            
            {/* Header do Gráfico */}
            <div className="flex justify-between items-start z-10">
              <div>
                <h2 className="text-4xl font-bold text-white tracking-tight">$5,394.62</h2>
                <div className="flex items-center gap-2 mt-2">
                  <ArrowUpRight size={20} className="text-success-500" />
                  <span className="text-success-500 font-bold text-lg">+$267 (+5,2%)</span>
                  <span className="text-black-200 text-sm ml-2">Today 16:25PM</span>
                </div>
              </div>
              
              {/* Toggle de Gráfico */}
              <div className="flex bg-black-500 p-1 rounded-lg border border-black-300">
                 <button className="p-2 rounded text-black-200 hover:text-white"><BarChart3 size={18} /></button>
                 <button className="p-2 rounded bg-purple-500 text-white shadow-lg"><Activity size={18} /></button>
              </div>
            </div>

            {/* Placeholder Visual do Gráfico (Simulando a linha da imagem) */}
            <div className="absolute inset-0 top-32 px-4 pointer-events-none">
               <svg className="w-full h-full" viewBox="0 0 100 50" preserveAspectRatio="none">
                  {/* Gradiente de Fundo */}
                  <defs>
                    <linearGradient id="chartGradient" x1="0" x2="0" y1="0" y2="1">
                      <stop offset="0%" stopColor="#4ADE80" stopOpacity="0.1" />
                      <stop offset="100%" stopColor="#4ADE80" stopOpacity="0" />
                    </linearGradient>
                  </defs>
                  
                  {/* Linha do Gráfico */}
                  <path 
                    d="M0,40 Q10,38 20,35 T40,20 T60,25 T80,30 T100,10" 
                    fill="url(#chartGradient)" 
                    stroke="none"
                  />
                  <path 
                    d="M0,40 Q10,38 20,35 T40,20 T60,25 T80,30 T100,10" 
                    fill="none" 
                    stroke="#A1E8B1" 
                    strokeWidth="0.5"
                    className="drop-shadow-[0_0_10px_rgba(74,222,128,0.5)]"
                  />
               </svg>
            </div>

            {/* Eixo X (Datas) */}
            <div className="flex justify-between text-xs text-black-200 mt-auto pt-4 border-t border-black-300/30 z-10">
               <span>16/10/2025</span>
               <span>20/10/2025</span>
               <span>22/10/2025</span>
            </div>
            
            {/* Eixo Y (Valores) - Absoluto na esquerda */}
            <div className="absolute left-6 top-40 flex flex-col gap-8 text-xs text-black-200 pointer-events-none">
              <span>$0</span>
              <span>$40</span>
              <span>$80</span>
              <span>$120</span>
              <span>$160</span>
            </div>

          </Card>
        </div>

        {/* --- COLUNA DIREITA: ACCURACY RANKING (Ocupa 4 colunas) --- */}
        <div className="lg:col-span-4">
          <Card className="h-[500px] bg-black-400 border-black-300/50 p-6 flex flex-col">
            <h3 className="text-lg font-medium text-black-100 mb-6">Accuracy Ranking</h3>
            
            <div className="space-y-6 flex-1 overflow-y-auto pr-2 custom-scrollbar">
               {/* Lista de Ativos */}
               <RankingItem symbol="EUR/USD" type="Forex" percentage={87} color="text-success-500" />
               <RankingItem symbol="GBP/USD" type="Forex" percentage={82} color="text-success-500" />
               <RankingItem symbol="XAU/USD" type="Commodities" percentage={72} color="text-success-500" />
               <RankingItem symbol="US30" type="Futures" percentage={61} color="text-danger-500" />
               <RankingItem symbol="AUD/NZD" type="Forex" percentage={53} color="text-danger-500" />
               <RankingItem symbol="INTC" type="Stocks" percentage={48} color="text-danger-500" />
            </div>
          </Card>
        </div>

      </div>
    </div>
  );
}

// --- SUB-COMPONENTES PARA ORGANIZAÇÃO ---

function TabItem({ icon: Icon, label, active }: { icon: any, label: string, active?: boolean }) {
    return (
        <button className={`flex items-center gap-2 pb-3 text-sm font-medium transition-all border-b-2 ${active ? 'text-white border-white' : 'text-black-200 border-transparent hover:text-white'}`}>
            <Icon size={16} />
            {label}
        </button>
    )
}

function RankingItem({ symbol, type, percentage, color }: { symbol: string, type: string, percentage: number, color: string }) {
    return (
        <div className="flex items-center justify-between group cursor-pointer">
            <div>
                <p className="text-sm font-bold text-white group-hover:text-primary-500 transition-colors">{symbol}</p>
                <p className="text-[10px] text-black-200 uppercase tracking-wider">{type}</p>
            </div>
            <div className="text-right">
                <span className={`text-sm font-bold ${color}`}>{percentage}%</span>
            </div>
        </div>
    )
}