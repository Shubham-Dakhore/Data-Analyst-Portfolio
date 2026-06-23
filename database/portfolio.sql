-- File: database/portfolio.sql

CREATE DATABASE IF NOT EXISTS portfolio_db;

USE portfolio_db;

-- ==========================================
-- USERS
-- ==========================================

CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(100) NOT NULL,

    email VARCHAR(150) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- PROJECTS
-- ==========================================

CREATE TABLE IF NOT EXISTS projects (

    id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(255) NOT NULL,

    description TEXT NOT NULL,

    technologies VARCHAR(255),

    github_url VARCHAR(255),

    live_url VARCHAR(255),

    image_url VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- CERTIFICATIONS
-- ==========================================

CREATE TABLE IF NOT EXISTS certifications (

    id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(255) NOT NULL,

    issuer VARCHAR(255),

    issue_date DATE,

    certificate_url VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- CONTACTS
-- ==========================================

CREATE TABLE IF NOT EXISTS contacts (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(150) NOT NULL,

    email VARCHAR(150) NOT NULL,

    subject VARCHAR(255) NOT NULL,

    message TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);