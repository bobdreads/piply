import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      // 1. AQUI ESTÃO NOSSAS FONTES OTIMIZADAS (Mantemos isso!)
      fontFamily: {
        sans: ["var(--font-banana)", "sans-serif"], 
      },
      
      // 2. AQUI ESTÃO AS CORES DO FIGMA (Limpei os nomes duplicados)
      colors: {
        // Tons de Preto/Cinza (Foundation Black)
        black: {
          50: "var(--foundation-blackblack-50)",
          100: "var(--foundation-blackblack-100)",
          200: "var(--foundation-blackblack-200)",
          300: "var(--foundationblackblack-300)", // Corrigi o nome variável
          400: "var(--foundationblackblack-400)",
          500: "var(--foundationblackblack-500)",
          600: "var(--foundation-blackblack-600)",
          700: "var(--foundation-blackblack-700)",
          800: "var(--foundation-blackblack-800)",
          900: "var(--foundation-blackblack-900)",
        },
        // Tons de Azul (Foundation Blue) -> Nossa cor Primária?
        primary: {
          50: "var(--foundation-blueblue-50)",
          100: "var(--foundationblueblue-100)",
          200: "var(--foundation-blueblue-200)",
          300: "var(--foundation-blueblue-300)",
          400: "var(--foundationblueblue-400)",
          500: "var(--foundation-blueblue-500)", // Provavelmente sua cor principal
          600: "var(--foundation-blueblue-600)",
          700: "var(--foundation-blueblue-700)",
          800: "var(--foundation-blueblue-800)",
          900: "var(--foundation-blueblue-900)",
        },
        // Tons de Verde (Foundation Green) -> Lucro/Sucesso
        success: {
          50: "var(--foundation-greengreen-50)",
          100: "var(--foundation-greengreen-100)",
          200: "var(--foundation-greengreen-200)",
          300: "var(--foundation-greengreen-300)",
          400: "var(--foundation-greengreen-400)",
          500: "var(--foundationgreengreen-500)",
          600: "var(--foundation-greengreen-600)",
          700: "var(--foundation-greengreen-700)",
          800: "var(--foundation-greengreen-800)",
          900: "var(--foundation-greengreen-900)",
        },
        // Tons de Vermelho (Foundation Red) -> Prejuízo/Erro
        danger: {
          50: "var(--foundation-redred-50)",
          100: "var(--foundation-redred-100)",
          200: "var(--foundation-redred-200)",
          300: "var(--foundation-redred-300)",
          400: "var(--foundation-redred-400)",
          500: "var(--foundation-redred-500)",
          600: "var(--foundation-redred-600)",
          700: "var(--foundation-redred-700)",
          800: "var(--foundation-redred-800)",
          900: "var(--foundation-redred-900)",
        },
        // Tons de Branco/Cinza Claro (Foundation White)
        white: {
           DEFAULT: "#ffffff",
           50: "var(--foundation-whitewhite-50)",
           // ... mapear o resto se necessário
           900: "var(--foundation-whitewhite-900)",
        },
        // Roxo (Foundation Purple)
        accent: {
          500: "var(--foundation-purplepurple-500)",
          // ... mapear outros se usar
        }
      },
    },
  },
  plugins: [],
};
export default config;