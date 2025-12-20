import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-banana)", "sans-serif"], 
      },
      colors: {
        // CORRIGIDO: Mapeia para --foundation-black-* (apaguei os 'blackblack')
        black: {
          50: "var(--foundation-black-50)",
          100: "var(--foundation-black-100)",
          200: "var(--foundation-black-200)",
          300: "var(--foundation-black-300)",
          400: "var(--foundation-black-400)",
          500: "var(--foundation-black-500)",
          600: "var(--foundation-black-btn)",
          DEFAULT: "var(--foundation-black-500)",
        },
        
        // CORRIGIDO: Mapeia para --foundation-blue-* (apaguei os 'blueblue')
        primary: {
          50: "var(--foundation-blue-50)",
          100: "var(--foundation-blue-100)",
          200: "var(--foundation-blue-200)",
          300: "var(--foundation-blue-300)",
          400: "var(--foundation-blue-400)", // <--- AQUI ESTAVA O ERRO!
          500: "var(--foundation-blue-500)",
          600: "var(--foundation-blue-600)",
          700: "var(--foundation-blue-700)",
          800: "var(--foundation-blue-800)",
          900: "var(--foundation-blue-900)",
          DEFAULT: "var(--foundation-blue-500)",
        },

        // CORRIGIDO: Mapeia para --foundation-green-*
        success: {
          50: "var(--foundation-green-50)",
          100: "var(--foundation-green-100)",
          200: "var(--foundation-green-200)",
          300: "var(--foundation-green-300)",
          400: "var(--foundation-green-400)",
          500: "var(--foundation-green-500)",
          DEFAULT: "var(--foundation-green-500)",
        },

        // CORRIGIDO: Mapeia para --foundation-red-*
        danger: {
          50: "var(--foundation-red-50)",
          100: "var(--foundation-red-100)",
          200: "var(--foundation-red-200)",
          300: "var(--foundation-red-300)",
          400: "var(--foundation-red-400)",
          500: "var(--foundation-red-500)",
          DEFAULT: "var(--foundation-red-500)",
        },
        
        white: {
           DEFAULT: "var(--foundation-white-500)",
           500: "var(--foundation-white-500)",
           900: "var(--foundation-white-900)",
        },
        
        purple: {
          500: "var(--foundation-purple-500)",
        }
      },
    },
  },
  plugins: [],
};
export default config;