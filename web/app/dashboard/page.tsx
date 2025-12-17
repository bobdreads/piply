import { Button } from "@/components/ui/Button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/Card"; // <--- Importação nova
import { PlusCircle, DollarSign, TrendingUp, Landmark } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      
      {/* Header da Página */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-white">Visão Geral</h1>
          <p className="text-slate-400">Bem-vindo de volta ao teu terminal financeiro.</p>
        </div>
        <Button>
          <PlusCircle className="mr-2 h-4 w-4" />
          Novo Trade
        </Button>
      </div>

      {/* Grid de Cards - Agora usando componentes! */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* Card 1: Saldo Total */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">
              Saldo Total
            </CardTitle>
            <Landmark className="h-4 w-4 text-slate-400" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-white">R$ 0,00</div>
            <p className="text-xs text-slate-500 mt-1">
              +0% em relação ao mês passado
            </p>
          </CardContent>
        </Card>

        {/* Card 2: Lucro Brasil */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">
              Lucro Mensal (BR)
            </CardTitle>
            <TrendingUp className="h-4 w-4 text-emerald-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-emerald-400">+ R$ 0,00</div>
            <p className="text-xs text-slate-500 mt-1">
              Isenção de 20k disponível
            </p>
          </CardContent>
        </Card>

        {/* Card 3: Exterior */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-slate-400">
              Provisão Exterior (USD)
            </CardTitle>
            <DollarSign className="h-4 w-4 text-blue-400" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-blue-400">$ 0.00</div>
            <p className="text-xs text-slate-500 mt-1">
              PTAX automática ativa
            </p>
          </CardContent>
        </Card>

      </div>

      {/* Área do Gráfico (Usando o mesmo componente Card!) */}
      <Card className="h-96 border-dashed bg-slate-900/50 flex items-center justify-center">
        <p className="text-slate-500">Gráfico de Performance (Em breve)</p>
      </Card>

    </div>
  );
}