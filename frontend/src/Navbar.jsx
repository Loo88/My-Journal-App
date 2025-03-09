import React from 'react';
import './navbar.css';

const Navbar = () => {
    return (
        
        
<nav className='navbar'>
    <div className='navbar-left'>
        <a href='/' className='logo'>
            Clear
        </a>
    </div>
    <div className='navbar-centre'>
        <ul className='nav-links'>
            <li>
                <a href='/my_journal'>My Journal</a>
            </li>
            <li>
                <a href='/add_new_entry'>Add New Entry</a>
            </li>
            <li>
                <a href='/about_us'>About Us</a>
            </li>
            <li>
                <a href='/sign_up'>Sign Up</a>
            </li>
            <li>
                <a href='/log_in'>Log In</a>
            </li>
        </ul>
    </div>
    <div className='navbar-right'>
        <a href='/account' className='user-icon'>
            <i className='fas fa-user'></i>
        </a>
    </div>
</nav>    
);
};

export default Navbar;
