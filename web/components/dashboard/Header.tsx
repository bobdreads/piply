"use client";
import * as React from "react";
import Link from "next/link";
import Image from "next/image";
import { SearchIcon } from "@/components/icons/SearchIcon";
import { NotificationIcon } from "@/components/icons/NotificationIcon";
import { Button } from "@/components/ui/Button"; 

export function Header() {
  return (
    <header className='flex items-center px-8 py-8 bg-fback space-y-2'>
      <nav className="flex items-center justify-between w-full">
        <div className="flex gap-6 items-center">
          <img className="" src="/assets/Logo.svg"alt="Logo PipLy"/>

          {/* CAIXA DE BUSCA (Container) */}
          <div className="w-[360px] h-[48px] mx-4 my-3 rounded-[8px] flex items-center gap-2 px-4 py-3 border border-black-400 transition-all duration-200 ease-in-out focus-within:border-primary-500 focus-within:border-2">
            
            <SearchIcon className="text-black-400 w-6 h-6" />

            {/* INPUT DE TEXTO */}
            <input type="text" placeholder="Buscar..." className="bg-transparent border-none outline-none w-full h-full text-black-400 placeholder-black-400 focus:placeholder-transparent focus:text-white" />
          </div>
          <div className="px-14 py-4 h-auto flex items-center gap-14">
            <a href="#" className="text-black-300 hover:text-primary-400 transition-colors duration-200">PipLy</a>
            <a href="#" className="text-black-300 hover:text-primary-400 transition-colors duration-200">Trades</a>
            <a href="#" className="text-black-300 hover:text-primary-400 transition-colors duration-200">Journal</a>
            <a href="#" className="text-black-300 hover:text-primary-400 transition-colors duration-200">Wallet</a>
            <a href="#" className="text-black-300 hover:text-primary-400 transition-colors duration-200">Tools</a>
          </div>
        </div>
        <div className="flex gap-2">
          <Button variant="primary" size="md">+ Adicionar Trade</Button>
          <Button variant="notification" size="md"><NotificationIcon className="w-6 h-6" /></Button>
          <Button variant="profile">
            <img 
              src="/assets/perfilimg.jpg"  /* <--- MUDAR AQUI (Coloca o nome exato do teu arquivo) */
              alt="Perfil" 
              className="w-full h-full object-cover"
            />
          </Button>
        </div>
      </nav>
    </header>
  );
}