import React from 'react'
import NavbarItem from './NavbarItem'

const Navbar = () => {
  return (
    <nav className='w-full fixed z-40'>
        <div className='px-4 md:px-16 py-6 flex flex-row items-center transition duration-500 bg-zinc-900 bg-opacity-90'>
            <img src="/images/logo.png" alt="" className='h-4 block lg:h-7'/>
            <div className='flex-row ml-8 gap-7 hidden  lg:flex'>
                <NavbarItem label='Home'/>
                <NavbarItem label='Sries'/>
                <NavbarItem label='Films'/>
                <NavbarItem label='New Popular'/>
                <NavbarItem label='Broswer by languages'/>
                
            </div>
            <div className='lg:hidden flex flex-row items-center gap-2 ml-8 cursor-pointer relative'>
                <p className='text-white text-sm'>Browse</p>
            </div>
        </div>
    </nav>
  )
}

export default Navbar