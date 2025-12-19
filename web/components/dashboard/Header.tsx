"use client";
import * as React from "react";
import Link from "next/link";
import Image from "next/image";
import { SearchIcon } from "@/components/icons/SearchIcon"; 

export function Header() {
  return (
    <header className='flex items-center px-8 py-8 bg-fback space-y-2'>
      <nav className="flex items-center justify-between w-full">
        <div className="flex gap-6 items-center">
          <img className="" src="/assets/Logo.svg"alt="Logo PipLy"/>

          {/* CAIXA DE BUSCA (Container) */}
          <div className="w-[360px] h-[48px] mx-4 my-3 rounded-[8px] flex items-center gap-2 px-4 py-3 border border-[var(--foundation-black-400)]transition-all duration-200 ease-in-out focus-within:border-primary-500 focus-within:border-2">
            
            <SearchIcon className="text-[var(--foundation-black-400)] w-6 h-6" />

            {/* INPUT DE TEXTO */}
            <input type="text" placeholder="Buscar..." className="bg-transparent border-none outline-none w-full h-full text-black-500 placeholder-black-500 focus:placeholder-transparent focus:text-white" />
          </div>
          <div className="px-14 py-4 h-auto flex items-center gap-6">
            <a href="#" className="text-[var(--foundation-black-300)] hover:text-primary-400 transition-colors duration-200">Link 1</a>
            <a href="#" className="text-[var(--foundation-black-300)] hover:text-[var(--foundation-blue-400)] transition-colors duration-200">Link 2</a>
            <a href="#" className="text-[var(--foundation-black-300)] hover:text-[var(--foundation-blue-400)] transition-colors duration-200">Link 3</a>
            <a href="#" className="text-[var(--foundation-black-300)] hover:text-[var(--foundation-blue-400)] transition-colors duration-200">Link 4</a>
            <a href="#" className="text-[var(--foundation-black-300)] hover:text-[var(--foundation-blue-400)] transition-colors duration-200">Link 5</a>
          </div>
        </div>
      </nav>
    </header>
  );
}