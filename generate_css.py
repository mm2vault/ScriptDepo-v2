#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_css():
    return """
:root, [data-theme="dark"] {
  --bg-primary: #070816;
  --bg-card: rgba(255, 255, 255, 0.03);
  --bg-card-hover: rgba(255, 255, 255, 0.06);
  --bg-modal: #0d0e26;
  --bg-input: rgba(255, 255, 255, 0.05);
  --text-primary: #f0eeff;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --border-color: rgba(167, 139, 250, 0.15);
  --border-hover: rgba(167, 139, 250, 0.4);
  --accent: #7c3aed;
  --accent-light: #a78bfa;
  --accent-gradient: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
  --gold: #fbbf24;
  --gold-gradient: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  --green: #10b981;
  --green-gradient: linear-gradient(135deg, #059669 0%, #10b981 100%);
  --red: #ef4444;
  --shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  --radius-card: 28px;
  --radius-modal: 40px;
  --radius-btn: 60px;
}

[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-card: rgba(255, 255, 255, 0.85);
  --bg-card-hover: #ffffff;
  --bg-modal: #ffffff;
  --bg-input: rgba(0, 0, 0, 0.04);
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  --border-color: rgba(124, 58, 237, 0.15);
  --border-hover: rgba(124, 58, 237, 0.35);
  --accent: #7c3aed;
  --accent-light: #6d28d9;
  --accent-gradient: linear-gradient(135deg, #7c3aed 0%, #9333ea 100%);
  --gold: #d97706;
  --gold-gradient: linear-gradient(135deg, #d97706 0%, #f59e0b 100%);
  --green: #059669;
  --green-gradient: linear-gradient(135deg, #047857 0%, #10b981 100%);
  --red: #dc2626;
  --shadow: 0 10px 25px rgba(124, 58, 237, 0.08);
}

[data-theme="blue"] {
  --bg-primary: #050d1a;
  --bg-card: rgba(15, 23, 42, 0.65);
  --bg-card-hover: rgba(30, 41, 59, 0.8);
  --bg-modal: #09172e;
  --bg-input: rgba(255, 255, 255, 0.06);
  --text-primary: #e0f2fe;
  --text-secondary: #93c5fd;
  --text-muted: #60a5fa;
  --border-color: rgba(56, 189, 248, 0.2);
  --border-hover: rgba(56, 189, 248, 0.45);
  --accent: #0284c7;
  --accent-light: #38bdf8;
  --accent-gradient: linear-gradient(135deg, #0284c7 0%, #06b6d4 100%);
  --gold: #f59e0b;
  --gold-gradient: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  --green: #10b981;
  --green-gradient: linear-gradient(135deg, #059669 0%, #10b981 100%);
  --red: #f43f5e;
  --shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
}

[data-theme="green"] {
  --bg-primary: #04140b;
  --bg-card: rgba(6, 30, 17, 0.65);
  --bg-card-hover: rgba(10, 45, 26, 0.8);
  --bg-modal: #072314;
  --bg-input: rgba(255, 255, 255, 0.06);
  --text-primary: #ecfdf5;
  --text-secondary: #a7f3d0;
  --text-muted: #34d399;
  --border-color: rgba(52, 211, 153, 0.2);
  --border-hover: rgba(52, 211, 153, 0.45);
  --accent: #059669;
  --accent-light: #34d399;
  --accent-gradient: linear-gradient(135deg, #059669 0%, #10b981 100%);
  --gold: #fbbf24;
  --gold-gradient: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
  --green: #10b981;
  --green-gradient: linear-gradient(135deg, #059669 0%, #10b981 100%);
  --red: #f43f5e;
  --shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  -webkit-tap-highlight-color: transparent;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* Background Ambient Glows */
.ambient-glow {
  position: fixed;
  border-radius: 50%;
  filter: blur(100px);
  pointer-events: none;
  z-index: 0;
  opacity: 0.16;
  will-change: transform;
  transform: translate3d(0, 0, 0);
}
.glow-1 {
  width: 500px;
  height: 500px;
  background: var(--accent);
  top: -100px;
  left: 10%;
}
.glow-2 {
  width: 450px;
  height: 450px;
  background: #06b6d4;
  bottom: 10%;
  right: 5%;
}

/* Base Utility Classes */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: var(--radius-btn);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  user-select: none;
  text-decoration: none;
}
.btn:hover {
  transform: scale(1.03);
}
.btn:active {
  transform: scale(0.98);
}
.btn-primary {
  background: var(--accent-gradient);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(124, 58, 237, 0.35);
}
.btn-green {
  background: var(--green-gradient);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}
.btn-gold {
  background: var(--gold-gradient);
  color: #000000;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
}
.btn-outline {
  background: var(--bg-card);
  border-color: var(--border-color);
  color: var(--text-primary);
  backdrop-filter: blur(10px);
}
.btn-outline:hover {
  border-color: var(--accent-light);
  background: var(--bg-card-hover);
}
.btn-icon {
  width: 40px;
  height: 40px;
  padding: 0;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Header */
header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(7, 8, 22, 0.75);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-color);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
[data-theme="light"] header {
  background: rgba(255, 255, 255, 0.85);
}
[data-theme="blue"] header {
  background: rgba(5, 13, 26, 0.85);
}
[data-theme="green"] header {
  background: rgba(4, 20, 11, 0.85);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
  cursor: pointer;
}
.header-logo {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  object-fit: cover;
  border: 2px solid var(--accent-light);
}
.header-titles h1 {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: var(--text-primary);
}
.header-titles span {
  font-size: 12px;
  color: var(--text-muted);
  display: block;
}

.header-center {
  flex: 1;
  max-width: 500px;
  position: relative;
}
.search-input-wrapper {
  position: relative;
  width: 100%;
}
.search-input-wrapper i {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 14px;
}
.search-input {
  width: 100%;
  padding: 11px 16px 11px 42px;
  border-radius: var(--radius-btn);
  background: var(--bg-input);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  font-size: 14px;
  outline: none;
  transition: all 0.2s ease;
}
.search-input:focus {
  border-color: var(--accent-light);
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.2);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: flex-end;
}

/* Coin indicator */
.coin-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(251, 191, 36, 0.12);
  border: 1px solid rgba(251, 191, 36, 0.3);
  border-radius: var(--radius-btn);
  font-weight: 700;
  color: var(--gold);
  cursor: pointer;
  font-size: 14px;
  transition: transform 0.2s ease;
}
.coin-badge:hover {
  transform: scale(1.05);
}
.coin-pulse {
  animation: pulseCoin 0.4s ease;
}
@keyframes pulseCoin {
  0% { transform: scale(1); }
  50% { transform: scale(1.25); filter: drop-shadow(0 0 10px #fbbf24); }
  100% { transform: scale(1); }
}

/* Theme picker */
.theme-picker {
  display: flex;
  gap: 6px;
  background: var(--bg-card);
  padding: 4px;
  border-radius: 40px;
  border: 1px solid var(--border-color);
}
.theme-dot {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid transparent;
  cursor: pointer;
  transition: transform 0.2s;
}
.theme-dot:hover {
  transform: scale(1.15);
}
.theme-dot.active {
  border-color: #ffffff;
}
.dot-dark { background: #7c3aed; }
.dot-light { background: #cbd5e1; }
.dot-blue { background: #0284c7; }
.dot-green { background: #10b981; }

/* Lang switch */
.lang-btn {
  font-weight: 700;
  font-size: 12px;
  padding: 6px 12px;
  border-radius: 20px;
}

/* Notification Bell */
.notif-bell-btn {
  position: relative;
}
.notif-badge-dot {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 8px;
  height: 8px;
  background: var(--red);
  border-radius: 50%;
  display: none;
}
.notif-badge-dot.show {
  display: block;
}

/* Dropdown */
.notif-dropdown {
  position: absolute;
  top: 68px;
  right: 20px;
  width: 320px;
  background: var(--bg-modal);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  box-shadow: var(--shadow);
  padding: 16px;
  display: none;
  flex-direction: column;
  gap: 10px;
  z-index: 105;
  backdrop-filter: blur(20px);
}
.notif-dropdown.active {
  display: flex;
  animation: slideUp 0.2s ease;
}
.notif-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 8px;
}
.notif-list {
  max-height: 300px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.notif-item {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  padding: 8px 10px;
  border-radius: 12px;
  background: var(--bg-card);
  font-size: 13px;
}
.notif-item i {
  color: var(--accent-light);
  margin-top: 3px;
}
.notif-empty {
  text-align: center;
  color: var(--text-muted);
  padding: 20px 0;
  font-size: 13px;
}

/* Container */
.main-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px 20px 80px 20px;
  position: relative;
  z-index: 1;
}

/* Daily Tasks Section */
.daily-tasks-banner {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  padding: 20px 24px;
  margin-bottom: 24px;
  backdrop-filter: blur(20px);
  display: none;
}
.daily-tasks-banner.visible {
  display: block;
}
.tasks-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  flex-wrap: wrap;
  gap: 12px;
}
.tasks-title-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}
.tasks-title-wrap h2 {
  font-size: 18px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
}
.tasks-counter {
  font-size: 13px;
  font-weight: 600;
  color: var(--gold);
  background: rgba(251, 191, 36, 0.1);
  padding: 4px 12px;
  border-radius: 20px;
  border: 1px solid rgba(251, 191, 36, 0.25);
}
.tasks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px;
}
.task-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  transition: all 0.2s;
}
.task-card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-hover);
}
.task-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.task-icon {
  width: 38px;
  height: 38px;
  border-radius: 12px;
  background: rgba(124, 58, 237, 0.15);
  color: var(--accent-light);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
}
.task-details h4 {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 2px;
}
.task-details p {
  font-size: 12px;
  color: var(--text-muted);
}
.task-reward {
  color: var(--gold);
  font-size: 12px;
  font-weight: 700;
  margin-top: 3px;
  display: flex;
  align-items: center;
  gap: 4px;
}
.task-btn {
  font-size: 12px;
  padding: 6px 14px;
  border-radius: 14px;
}

/* Categories Carousel */
.categories-wrapper {
  margin-bottom: 24px;
  overflow-x: auto;
  scrollbar-width: thin;
  padding-bottom: 6px;
}
.categories-wrapper::-webkit-scrollbar {
  height: 4px;
}
.categories-wrapper::-webkit-scrollbar-thumb {
  background: var(--border-color);
  border-radius: 4px;
}
.categories-list {
  display: flex;
  gap: 10px;
  min-width: max-content;
}
.category-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 30px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-secondary);
  transition: all 0.2s;
  user-select: none;
  backdrop-filter: blur(10px);
}
.category-pill img {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  object-fit: cover;
}
.category-pill i {
  font-size: 14px;
  color: var(--accent-light);
}
.category-pill:hover {
  color: var(--text-primary);
  border-color: var(--accent-light);
  transform: translateY(-2px);
}
.category-pill.active {
  background: var(--accent-gradient);
  border-color: transparent;
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
}
.category-pill.active i {
  color: #ffffff;
}
.category-pill.games-pill {
  border-color: rgba(16, 185, 129, 0.4);
  color: var(--green);
}
.category-pill.games-pill.active {
  background: var(--green-gradient);
  color: #ffffff;
}

/* Filter Bar */
.filter-bar {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  padding: 12px 18px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  backdrop-filter: blur(20px);
}
.filter-group {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.filter-label {
  font-size: 13px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 5px;
}
.custom-select {
  background: var(--bg-input);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 7px 14px;
  border-radius: 20px;
  font-size: 13px;
  outline: none;
  cursor: pointer;
}
.custom-select option {
  background: var(--bg-modal);
  color: var(--text-primary);
}

/* Script & Games Grid */
.scripts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 22px;
}

/* Script Card */
.script-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
  backdrop-filter: blur(20px);
  position: relative;
}
.script-card:hover {
  transform: translateY(-6px);
  border-color: var(--border-hover);
  box-shadow: var(--shadow);
}
.script-card-img-wrap {
  width: 100%;
  height: 160px;
  position: relative;
  overflow: hidden;
  background: #0d0f2b;
}
.script-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.script-card:hover .script-card-img {
  transform: scale(1.05);
}
.card-floating-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 700;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 5px;
}
.badge-premium {
  background: rgba(124, 58, 237, 0.85);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.badge-community {
  background: rgba(6, 182, 212, 0.85);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.badge-price {
  position: absolute;
  bottom: 12px;
  right: 12px;
  background: rgba(0, 0, 0, 0.7);
  color: var(--gold);
  border: 1px solid rgba(251, 191, 36, 0.4);
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  gap: 5px;
}
.btn-fav {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  backdrop-filter: blur(10px);
}
.btn-fav:hover {
  transform: scale(1.15);
  color: #f43f5e;
}
.btn-fav.active {
  color: #f43f5e;
  background: rgba(244, 63, 94, 0.2);
  border-color: #f43f5e;
}

.script-card-body {
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}
.card-header-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 8px;
}
.card-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.3;
}
.card-category-tag {
  font-size: 12px;
  color: var(--accent-light);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
}
.card-desc {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card-features {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.feature-tag {
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 8px;
  background: rgba(167, 139, 250, 0.1);
  color: var(--accent-light);
  border: 1px solid rgba(167, 139, 250, 0.2);
}
.card-stats-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  color: var(--text-muted);
  border-top: 1px solid var(--border-color);
  padding-top: 10px;
}
.rating-stars {
  color: var(--gold);
  display: flex;
  align-items: center;
  gap: 3px;
  cursor: pointer;
}

.card-owner-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
}
.owner-info {
  display: flex;
  align-items: center;
  gap: 8px;
}
.owner-avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  object-fit: cover;
}
.owner-badge {
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 6px;
  background: rgba(124, 58, 237, 0.2);
  color: var(--accent-light);
}

/* Comments accordion / preview */
.card-comments-box {
  background: rgba(0, 0, 0, 0.18);
  border-radius: 14px;
  padding: 10px;
  font-size: 12px;
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.comment-single {
  display: flex;
  gap: 6px;
  line-height: 1.3;
}
.comment-author {
  font-weight: 700;
  color: var(--accent-light);
}
.comment-form {
  display: flex;
  gap: 6px;
  margin-top: 4px;
}
.comment-input {
  flex: 1;
  background: var(--bg-input);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 6px 10px;
  color: var(--text-primary);
  font-size: 12px;
  outline: none;
}
.comment-submit-btn {
  padding: 6px 10px;
  border-radius: 12px;
  font-size: 11px;
}

/* Card Footer */
.script-card-footer {
  padding: 14px 20px;
  background: rgba(0, 0, 0, 0.15);
  border-top: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
.footer-left {
  display: flex;
  align-items: center;
  gap: 6px;
}
.unlocked-badge {
  font-size: 11px;
  font-weight: 700;
  color: var(--green);
  display: flex;
  align-items: center;
  gap: 4px;
}
.btn-get {
  min-width: 90px;
}

/* Games Grid Item */
.game-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
  backdrop-filter: blur(20px);
}
.game-card:hover {
  transform: translateY(-6px);
  border-color: var(--green);
}
.game-card-img {
  width: 100%;
  height: 160px;
  object-fit: cover;
}
.game-card-body {
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}
.game-card-footer {
  padding: 14px 20px;
  border-top: 1px solid var(--border-color);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  background: var(--bg-card);
  border-radius: var(--radius-card);
  border: 1px dashed var(--border-color);
  margin-top: 20px;
}
.empty-state i {
  font-size: 48px;
  color: var(--text-muted);
  margin-bottom: 16px;
}
.empty-state h3 {
  font-size: 18px;
  margin-bottom: 8px;
}
.empty-state p {
  color: var(--text-muted);
  font-size: 14px;
}

/* Pagination */
.pagination-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 36px;
}

/* Modals Overlay */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(12px);
  z-index: 200;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.modal-overlay.active {
  display: flex;
}
.modal-container {
  background: var(--bg-modal);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-modal);
  width: 100%;
  max-width: 580px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow);
  animation: slideUp 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  position: relative;
}
.modal-container.modal-lg {
  max-width: 820px;
}
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.modal-header {
  padding: 24px 28px 16px 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-color);
}
.modal-title {
  font-size: 20px;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 10px;
}
.modal-close-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 20px;
  cursor: pointer;
  padding: 6px;
  border-radius: 50%;
  transition: color 0.2s;
}
.modal-close-btn:hover {
  color: var(--text-primary);
}
.modal-body {
  padding: 24px 28px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* Forms in modal */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.form-group label {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
}
.form-input, .form-textarea, .form-select {
  background: var(--bg-input);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 12px 16px;
  color: var(--text-primary);
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}
.form-textarea {
  min-height: 110px;
  resize: vertical;
  font-family: monospace;
}
.form-input:focus, .form-textarea:focus, .form-select:focus {
  border-color: var(--accent-light);
}

/* Code block view */
.code-viewer {
  background: #050614;
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 16px;
  font-family: 'JetBrains Mono', Consolas, monospace; line-height: 1.6;
  font-size: 13px;
  color: #38bdf8;
  max-height: 320px;
  overflow-y: auto;
  white-space: pre-wrap;
  word-break: break-all;
}

/* Unlock options */
.unlock-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 10px;
}
.unlock-box {
  background: var(--bg-card);
  border: 2px solid var(--border-color);
  border-radius: 20px;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.unlock-box:hover {
  border-color: var(--accent-light);
  transform: translateY(-4px);
}
.unlock-box i {
  font-size: 32px;
  margin-bottom: 6px;
}
.unlock-box.coin-box i { color: var(--gold); }
.unlock-box.tasks-box i { color: var(--green); }

/* Task Countdown in Modal */
.task-step {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 14px 18px;
}
.step-timer {
  font-weight: 800;
  color: var(--gold);
  font-size: 15px;
}

/* Password strength */
.password-meter {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 4px;
  height: 5px;
  margin-top: 4px;
}
.meter-bar {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  height: 100%;
}
.meter-bar.active-red { background: #ef4444; }
.meter-bar.active-yellow { background: #f59e0b; }
.meter-bar.active-green { background: #10b981; }

/* Cosmetic frames */
.avatar-frame-gold {
  box-shadow: 0 0 0 3px #fbbf24, 0 0 15px #f59e0b;
}
.avatar-frame-rainbow {
  box-shadow: 0 0 0 3px #a855f7, 0 0 15px #06b6d4;
}
.name-purple {
  color: #c084fc !important;
  font-weight: 700;
}
.name-gold {
  color: #fbbf24 !important;
  font-weight: 700;
}

/* Chat Floating Button & Widget */
.chat-fab {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 65px;
  height: 65px;
  border-radius: 50%;
  background: var(--accent-gradient);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4);
  z-index: 99;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
}
.chat-fab:hover {
  transform: scale(1.08);
}
.chat-fab.open {
  background: #ef4444;
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}
.chat-iframe-modal {
  position: fixed;
  bottom: 100px;
  right: 24px;
  width: 400px;
  height: 600px;
  max-width: calc(100vw - 40px);
  max-height: calc(100vh - 120px);
  background: var(--bg-modal);
  border: 1px solid var(--border-color);
  border-radius: 28px;
  box-shadow: var(--shadow);
  z-index: 99;
  overflow: hidden;
  display: none;
  flex-direction: column;
}
.chat-iframe-modal.show {
  display: flex;
  animation: slideUp 0.3s ease;
}
.chat-iframe-header {
  padding: 12px 18px;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  font-weight: 700;
}
.chat-iframe-content {
  width: 100%;
  height: 100%;
  border: none;
}

/* Scroll to top button */
.scroll-top-btn {
  position: fixed;
  bottom: 24px;
  left: 24px;
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  display: none;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 90;
  backdrop-filter: blur(10px);
  transition: all 0.2s;
}
.scroll-top-btn.show {
  display: flex;
}

/* Toast Container */
.toast-container {
  position: fixed;
  bottom: 24px;
  right: 100px;
  z-index: 300;
  display: flex;
  flex-direction: column;
  gap: 10px;
  pointer-events: none;
}
.toast {
  background: var(--bg-modal);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 12px 20px;
  box-shadow: var(--shadow);
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  animation: toastIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: auto;
  min-width: 250px;
}
@keyframes toastIn {
  from { opacity: 0; transform: translateX(50px); }
  to { opacity: 1; transform: translateX(0); }
}

/* Cookie banner */
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--bg-modal);
  border-top: 1px solid var(--border-color);
  padding: 16px 24px;
  z-index: 150;
  display: none;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  backdrop-filter: blur(20px);
}
.cookie-banner.show {
  display: flex;
}

/* Tabs */
.tab-nav {
  display: flex;
  gap: 10px;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 12px;
}
.tab-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  padding: 6px 14px;
  border-radius: 12px;
  transition: all 0.2s;
}
.tab-btn.active {
  color: var(--text-primary);
  background: var(--bg-card-hover);
  border: 1px solid var(--border-color);
}

/* Responsive */
@media (max-width: 768px) {
  header {
    flex-direction: column;
    align-items: stretch;
    padding: 14px;
  }
  .header-left {
    justify-content: space-between;
  }
  .header-right {
    justify-content: space-between;
    margin-top: 4px;
  }
  .search-input-wrapper {
    max-width: 100%;
  }
  .filter-bar {
    flex-direction: column;
    align-items: stretch;
  }
  .filter-group {
    justify-content: space-between;
    width: 100%;
  }
  .chat-iframe-modal {
    width: calc(100vw - 30px);
    right: 15px;
    bottom: 95px;
  }
  .toast-container {
    right: 20px;
    bottom: 95px;
  }
}

@media (max-width: 480px) {
  .scripts-grid {
    grid-template-columns: 1fr;
  }
  .unlock-options {
    grid-template-columns: 1fr;
  }
  .tasks-grid {
    grid-template-columns: 1fr;
  }
}

/* ==================== SOCIAL BUTTONS ==================== */
.btn-social-discord {
  background: #5865F2 !important;
  color: #ffffff !important;
  border: none !important;
  padding: 6px 12px !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  border-radius: 60px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}
.btn-social-discord:hover {
  filter: brightness(1.15) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 15px rgba(88, 101, 242, 0.4) !important;
}

.btn-social-youtube {
  background: #FF0000 !important;
  color: #ffffff !important;
  border: none !important;
  padding: 6px 12px !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  border-radius: 60px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}
.btn-social-youtube:hover {
  filter: brightness(1.15) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4) !important;
}

.btn-social-tiktok {
  background: linear-gradient(135deg, #00f2fe 0%, #fe0979 100%) !important;
  color: #ffffff !important;
  border: none !important;
  padding: 6px 12px !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  border-radius: 60px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}
.btn-social-tiktok:hover {
  filter: brightness(1.15) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 15px rgba(0, 242, 254, 0.4) !important;
}

/* ==================== EXECUTOR BADGES ==================== */
.executor-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin: 6px 0;
}
.badge-executor {
  background: rgba(124, 58, 237, 0.12);
  color: var(--accent-light);
  border: 1px solid rgba(124, 58, 237, 0.25);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 6px;
  letter-spacing: 0.3px;
}

/* ==================== STATUS PILLS ==================== */
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 9px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.2px;
}
.status-working {
  background: rgba(16, 185, 129, 0.15);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.35);
}
.status-patched {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.35);
}

/* ==================== LUA SYNTAX HIGHLIGHTER ==================== */
.code-viewer {
  background: #090a1a !important;
  border: 1px solid rgba(124, 58, 237, 0.25) !important;
  border-radius: 16px !important;
  padding: 14px !important;
  font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace !important;
  font-size: 13px !important;
  line-height: 1.6 !important;
  max-height: 380px !important;
  overflow-y: auto !important;
  overflow-x: auto !important;
  white-space: pre !important;
}
.code-line {
  display: flex;
  align-items: flex-start;
  min-height: 20px;
}
.code-line:hover {
  background: rgba(255, 255, 255, 0.03);
}
.line-num {
  width: 38px;
  color: #475569;
  user-select: none;
  text-align: right;
  padding-right: 14px;
  font-size: 11px;
}
.line-content {
  flex: 1;
  color: #e2e8f0;
}
.lua-kw {
  color: #c084fc;
  font-weight: 700;
}
.lua-string {
  color: #34d399;
}
.lua-comment {
  color: #64748b;
  font-style: italic;
}
.lua-num {
  color: #fbbf24;
}

/* ==================== PROMO CODE MODAL ==================== */
.promo-box {
  background: rgba(251, 191, 36, 0.08);
  border: 1px dashed rgba(251, 191, 36, 0.4);
  border-radius: 16px;
  padding: 14px;
  margin-top: 14px;
}
.promo-chip {
  display: inline-block;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-color);
  padding: 4px 10px;
  border-radius: 8px;
  font-family: monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--gold);
  cursor: pointer;
  transition: all 0.2s ease;
  margin: 3px;
}
.promo-chip:hover {
  background: rgba(251, 191, 36, 0.2);
  transform: scale(1.04);
}

/* ==================== MOBILE BOTTOM NAVIGATION ==================== */
.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 62px;
  background: rgba(7, 8, 22, 0.94);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid var(--border-color);
  z-index: 999;
  justify-content: space-around;
  align-items: center;
  padding: 0 8px;
}
[data-theme="light"] .mobile-bottom-nav {
  background: rgba(255, 255, 255, 0.94);
}
.mobile-nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 10px;
  font-weight: 700;
  cursor: pointer;
  padding: 6px 12px;
  border-radius: 12px;
  transition: all 0.2s ease;
  gap: 3px;
  min-width: 58px;
  min-height: 48px;
}
.mobile-nav-item i {
  font-size: 18px;
  transition: transform 0.2s;
}
.mobile-nav-item.active {
  color: var(--accent-light);
}
.mobile-nav-item.active i {
  transform: translateY(-2px);
  color: var(--accent-light);
}

@media (max-width: 768px) {
  body {
    padding-bottom: 74px !important;
  }
  .mobile-bottom-nav {
    display: flex !important;
  }
  .social-btn-text {
    display: none !important;
  }
  .chat-widget-btn {
    bottom: 74px !important;
  }
  .chat-iframe-modal {
    bottom: 135px !important;
  }
  .toast-container {
    bottom: 74px !important;
  }
}


/* ==================== PLATFORM INTRO & HERO BANNER ==================== */
.platform-hero {
  background: radial-gradient(ellipse at 50% -20%, rgba(124, 58, 237, 0.25) 0%, rgba(15, 17, 43, 0.7) 60%, rgba(7, 8, 22, 0.9) 100%);
  border: 1px solid rgba(167, 139, 250, 0.22);
  border-radius: 26px;
  padding: 24px;
  margin-bottom: 24px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  transition: all 0.3s ease;
}
[data-theme="light"] .platform-hero {
  background: radial-gradient(ellipse at 50% -20%, rgba(124, 58, 237, 0.12) 0%, rgba(255, 255, 255, 0.95) 70%);
  border: 1px solid rgba(124, 58, 237, 0.18);
  box-shadow: 0 12px 32px rgba(124, 58, 237, 0.08);
}

.hero-top-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
}
.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(124, 58, 237, 0.16);
  border: 1px solid rgba(167, 139, 250, 0.35);
  padding: 4px 12px;
  border-radius: 30px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.8px;
  color: var(--accent-light);
}
.hero-collapse-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border-color);
  color: var(--text-muted);
  border-radius: 20px;
  padding: 4px 12px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.hero-collapse-btn:hover {
  background: rgba(255, 255, 255, 0.12);
  color: var(--text-primary);
}

.hero-title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: var(--text-primary);
  margin-bottom: 8px;
  line-height: 1.25;
}
.hero-subtitle {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.6;
  max-width: 860px;
  margin-bottom: 20px;
}

.hero-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 14px;
  margin-bottom: 20px;
}
.hero-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 16px;
  display: flex;
  gap: 14px;
  align-items: flex-start;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.hero-card:hover {
  background: rgba(255, 255, 255, 0.07);
  border-color: var(--border-hover);
  transform: translateY(-3px);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.3);
}
.hero-card-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}
.hero-card-info h4 {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--text-primary);
}
.hero-card-info p {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.45;
  margin-bottom: 6px;
}
.hero-card-link {
  font-size: 11px;
  font-weight: 700;
  color: var(--accent-light);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
}

/* ==================== GUIDE MODAL STYLING ==================== */
.guide-step-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 18px;
  margin-bottom: 14px;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}
.guide-step-num {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: var(--accent-gradient);
  color: #fff;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
  box-shadow: 0 4px 14px rgba(124, 58, 237, 0.4);
}
.guide-step-content h4 {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 6px;
  color: var(--text-primary);
}
.guide-step-content p {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.55;
  margin-bottom: 6px;
}
.guide-step-content code {
  background: rgba(0, 0, 0, 0.35);
  padding: 2px 6px;
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  color: var(--gold);
  font-size: 12px;
}

.tip-box {
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.25);
  border-radius: 14px;
  padding: 12px 16px;
  margin: 10px 0;
  font-size: 12px;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 10px;
}
.warning-box {
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: 14px;
  padding: 12px 16px;
  margin: 10px 0;
  font-size: 12px;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 10px;
}

.faq-item {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  margin-bottom: 10px;
  overflow: hidden;
}
.faq-question {
  padding: 14px 18px;
  font-size: 14px;
  font-weight: 700;
  color: var(--text-primary);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  user-select: none;
}
.faq-question:hover {
  background: rgba(255, 255, 255, 0.04);
}
.faq-answer {
  padding: 0 18px 14px 18px;
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.6;
  display: none;
}
.faq-item.active .faq-answer {
  display: block;
}
.faq-item.active .faq-question i {
  transform: rotate(180deg);
  color: var(--accent-light);
}

/* Script Card Glow Enhancement */
.script-card {
  transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.28s, border-color 0.28s;
}
.script-card:hover {
  transform: translateY(-5px);
  border-color: rgba(167, 139, 250, 0.45);
  box-shadow: 0 18px 38px rgba(0, 0, 0, 0.4), 0 0 24px rgba(124, 58, 237, 0.18);
}


/* Desktop & Mobile Display Helpers */
.desktop-only {
  display: inline-flex !important;
}
.theme-picker.desktop-only {
  display: flex !important;
}
.mobile-menu-btn {
  display: none !important;
}
.code-modal-top-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  gap: 10px;
}
.code-btn-group {
  display: flex;
  gap: 8px;
}


/* ==================== COMPREHENSIVE RESPONSIVE MOBILE OVERHAUL ==================== */
@media (max-width: 768px) {
  /* Helper classes */
  .desktop-only {
    display: none !important;
  }
  .mobile-menu-btn {
    display: inline-flex !important;
  }
  body {
    padding-bottom: calc(76px + env(safe-area-inset-bottom, 0px)) !important;
  }
  .main-container {
    padding: 12px 12px calc(80px + env(safe-area-inset-bottom, 0px)) 12px !important;
  }

  /* Header Clean Mobile 2-Row Layout */
  header {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 10px 14px !important;
    gap: 8px !important;
  }
  .header-left {
    order: 1 !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
  }
  .header-logo {
    width: 36px !important;
    height: 36px !important;
    border-radius: 10px !important;
  }
  .header-titles h1 {
    font-size: 17px !important;
  }
  .header-titles span {
    font-size: 11px !important;
  }
  .header-right {
    order: 2 !important;
    display: flex !important;
    align-items: center !important;
    gap: 6px !important;
    flex-wrap: nowrap !important;
    margin: 0 !important;
  }
  .coin-badge {
    padding: 6px 10px !important;
    font-size: 12px !important;
    border-radius: 20px !important;
    gap: 6px !important;
  }
  .header-guide-btn {
    padding: 6px 10px !important;
    font-size: 12px !important;
  }
  .guide-btn-text {
    display: none !important;
  }
  .btn-icon {
    width: 36px !important;
    height: 36px !important;
    font-size: 14px !important;
  }
  .header-center {
    order: 3 !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-top: 2px !important;
  }
  .search-input {
    padding: 9px 14px 9px 38px !important;
    font-size: 13px !important;
    border-radius: 12px !important;
  }
  .search-input-wrapper i {
    left: 12px !important;
    font-size: 13px !important;
  }

  /* Chat Floating Button (Never overlaps bottom navigation!) */
  .chat-fab {
    bottom: 76px !important;
    right: 14px !important;
    width: 48px !important;
    height: 48px !important;
    font-size: 19px !important;
    box-shadow: 0 4px 16px rgba(124, 58, 237, 0.45) !important;
    z-index: 990 !important;
  }
  .chat-iframe-modal {
    bottom: 132px !important;
    right: 12px !important;
    left: 12px !important;
    width: auto !important;
    max-width: 100% !important;
    height: 420px !important;
    max-height: calc(100vh - 160px) !important;
  }

  /* Platform Hero Banner */
  .platform-hero {
    padding: 16px 14px !important;
    border-radius: 18px !important;
    margin-bottom: 16px !important;
  }
  .hero-top-row {
    margin-bottom: 10px !important;
  }
  .hero-tag {
    font-size: 10px !important;
    padding: 3px 8px !important;
  }
  .hero-collapse-btn {
    padding: 4px 10px !important;
    font-size: 11px !important;
  }
  .hero-title {
    font-size: 17px !important;
    line-height: 1.35 !important;
    margin-bottom: 6px !important;
  }
  .hero-subtitle {
    font-size: 12px !important;
    line-height: 1.5 !important;
    margin-bottom: 12px !important;
  }
  .hero-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 8px !important;
    margin-bottom: 12px !important;
  }
  .hero-card {
    padding: 10px 12px !important;
    gap: 10px !important;
    border-radius: 12px !important;
  }
  .hero-card-icon {
    width: 36px !important;
    height: 36px !important;
    font-size: 14px !important;
    border-radius: 10px !important;
    flex-shrink: 0 !important;
  }
  .hero-card-info h4 {
    font-size: 13px !important;
    margin-bottom: 2px !important;
  }
  .hero-card-info p {
    font-size: 11px !important;
    line-height: 1.35 !important;
  }
  .hero-actions {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    width: 100% !important;
  }
  .hero-actions .btn {
    width: 100% !important;
    justify-content: center !important;
    padding: 10px 14px !important;
    font-size: 13px !important;
  }

  /* Daily Tasks Section */
  .daily-tasks-banner {
    padding: 14px !important;
    border-radius: 16px !important;
    margin-bottom: 16px !important;
  }
  .tasks-header {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 10px !important;
  }
  .tasks-header .btn {
    width: 100% !important;
    justify-content: center !important;
  }
  .tasks-grid {
    grid-template-columns: 1fr !important;
    gap: 8px !important;
  }
  .task-card {
    padding: 10px 12px !important;
    gap: 10px !important;
  }
  .task-title {
    font-size: 12px !important;
  }
  .task-reward {
    font-size: 11px !important;
  }

  /* Compact Filter Bar */
  .filter-bar {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 8px !important;
    padding: 12px !important;
    border-radius: 16px !important;
    margin-bottom: 16px !important;
  }
  .filter-group {
    width: 100% !important;
    margin: 0 !important;
    gap: 4px !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
  }
  .filter-label {
    font-size: 11px !important;
    color: var(--text-muted) !important;
  }
  .custom-select {
    width: 100% !important;
    padding: 7px 10px !important;
    font-size: 12px !important;
    border-radius: 10px !important;
  }
  .filter-group:last-child {
    grid-column: span 2 !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    gap: 8px !important;
    margin-top: 4px !important;
  }
  .filter-group:last-child .btn {
    flex: 1 !important;
    justify-content: center !important;
    font-size: 12px !important;
    padding: 8px 10px !important;
  }

  /* Categories Touch Scroll */
  .categories-wrapper {
    margin-left: -12px !important;
    margin-right: -12px !important;
    padding-left: 12px !important;
    padding-right: 12px !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    margin-bottom: 16px !important;
  }
  .categories-wrapper::-webkit-scrollbar {
    display: none !important;
  }
  .category-pill {
    padding: 7px 13px !important;
    font-size: 12px !important;
  }

  /* Scripts & Games Grid */
  .scripts-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }
  .script-card-img-wrap {
    height: 150px !important;
  }
  .script-card-body {
    padding: 14px !important;
    gap: 8px !important;
  }
  .card-title {
    font-size: 15px !important;
  }

  /* Modals Mobile Bottom Sheet Styling */
  .modal-overlay {
    padding: 8px !important;
    align-items: flex-end !important;
  }
  .modal-container {
    max-height: 88vh !important;
    border-radius: 22px 22px 10px 10px !important;
    width: 100% !important;
  }
  .modal-header {
    padding: 14px 16px 12px 16px !important;
  }
  .modal-title {
    font-size: 16px !important;
  }
  .modal-body {
    padding: 14px 16px 24px 16px !important;
  }
  .tab-nav {
    overflow-x: auto !important;
    flex-wrap: nowrap !important;
    white-space: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    gap: 6px !important;
    padding-bottom: 6px !important;
    margin-bottom: 12px !important;
  }
  .tab-nav::-webkit-scrollbar {
    display: none !important;
  }
  .tab-btn {
    padding: 6px 12px !important;
    font-size: 12px !important;
    flex-shrink: 0 !important;
  }
  .code-modal-top-row {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 8px !important;
    margin-bottom: 8px !important;
  }
  .code-btn-group {
    display: flex !important;
    gap: 8px !important;
    width: 100% !important;
  }
  .code-btn-group .btn {
    flex: 1 !important;
    justify-content: center !important;
  }
  .code-viewer {
    max-height: 220px !important;
    font-size: 11px !important;
    padding: 12px !important;
  }
  .unlock-options {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }
  .unlock-box {
    padding: 14px !important;
  }
  .notif-dropdown {
    position: fixed !important;
    top: 56px !important;
    left: 10px !important;
    right: 10px !important;
    width: auto !important;
    max-width: calc(100vw - 20px) !important;
    z-index: 1001 !important;
  }
  .toast-container {
    bottom: 76px !important;
    left: 12px !important;
    right: 12px !important;
    align-items: center !important;
  }
  .toast {
    width: 100% !important;
    max-width: 360px !important;
    text-align: center !important;
  }

  /* Mobile Bottom Nav */
  .mobile-bottom-nav {
    display: flex !important;
    height: calc(62px + env(safe-area-inset-bottom, 0px)) !important;
    padding-bottom: env(safe-area-inset-bottom, 0px) !important;
    background: rgba(7, 8, 22, 0.94) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
  }
  .mobile-nav-item.active {
    background: rgba(124, 58, 237, 0.12) !important;
    border-radius: 14px !important;
  }

  /* Mobile Drawer Bottom Sheet */
  #mobileDrawerModal {
    align-items: flex-end !important;
    padding: 0 !important;
  }
  #mobileDrawerModal .modal-container {
    max-height: 85vh !important;
    border-radius: 24px 24px 0 0 !important;
    margin-bottom: 0 !important;
    width: 100% !important;
    box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.7) !important;
    animation: slideUpDrawer 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }
}

@keyframes slideUpDrawer {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}

/* Mobile Drawer Components */
.mobile-drawer-sheet {
  max-width: 520px;
  width: 100%;
}
.drawer-user-card {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(124, 58, 237, 0.1);
  border: 1px solid rgba(167, 139, 250, 0.25);
  border-radius: 16px;
  padding: 12px 14px;
  margin-bottom: 14px;
  cursor: pointer;
  transition: all 0.2s;
}
.drawer-user-card:hover {
  background: rgba(124, 58, 237, 0.16);
  border-color: var(--accent-light);
}
.drawer-user-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 18px;
  flex-shrink: 0;
}
.drawer-user-info {
  flex: 1;
}
.drawer-user-info h4 {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 2px;
}
.drawer-user-info span {
  font-size: 11px;
  color: var(--text-muted);
}
.drawer-section-title {
  font-size: 11px;
  font-weight: 800;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin: 14px 0 8px 0;
}
.drawer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}
.drawer-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 12px 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s;
  color: var(--text-primary);
}
.drawer-btn i {
  font-size: 18px;
}
.drawer-btn span {
  font-size: 11px;
  font-weight: 700;
  white-space: nowrap;
}
.drawer-btn:active {
  transform: scale(0.96);
  background: var(--bg-card-hover);
}
.drawer-settings-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.drawer-setting-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 10px 14px;
}
.drawer-setting-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  font-weight: 600;
}
.drawer-setting-label i {
  color: var(--accent-light);
  width: 16px;
  text-align: center;
}
.drawer-socials {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
}
.drawer-socials .btn {
  width: 100%;
  justify-content: center;
  padding: 10px;
  font-size: 13px;
}


/* ==================== POLISHED UI & MODERN SCRIPT CARDS ==================== */

/* Search enhancements */
.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
}
.search-clear-btn {
  position: absolute;
  right: 12px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-color);
  color: var(--text-muted);
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  cursor: pointer;
  transition: all 0.2s;
  z-index: 2;
}
.search-clear-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
  border-color: rgba(239, 68, 68, 0.4);
}
.search-kbd-hint {
  position: absolute;
  right: 12px;
  font-size: 10px;
  font-weight: 700;
  font-family: monospace;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-color);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--text-muted);
  pointer-events: none;
}
.search-input-wrapper:focus-within .search-kbd-hint {
  display: none;
}

/* Quick Filter Chips */
.quick-filters-scroll {
  width: 100%;
  overflow-x: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
  padding: 4px 0 16px 0;
  margin-bottom: 2px;
}
.quick-filters-scroll::-webkit-scrollbar {
  display: none;
}
.quick-filters-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
}
.quick-filter-chip {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 8px 16px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 700;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
}
.quick-filter-chip:hover {
  background: rgba(124, 58, 237, 0.14);
  border-color: var(--accent-light);
  color: var(--text-primary);
  transform: translateY(-2px);
}
.quick-filter-chip.active {
  background: var(--accent-gradient);
  border-color: var(--accent-light);
  color: #ffffff;
  box-shadow: 0 4px 18px rgba(124, 58, 237, 0.4);
}

/* Script Cards Uniform Grid */
.scripts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 22px;
  align-items: stretch;
}
.script-card {
  background: rgba(14, 16, 40, 0.68);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(167, 139, 250, 0.16);
  border-radius: 20px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.28s, box-shadow 0.28s;
  position: relative;
}
.script-card:hover {
  transform: translateY(-6px);
  border-color: rgba(167, 139, 250, 0.45);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45), 0 0 24px rgba(124, 58, 237, 0.22);
}

/* Card Image Wrap */
.script-card-img-wrap {
  position: relative;
  width: 100%;
  height: 165px;
  overflow: hidden;
  background: #08091a;
  cursor: pointer;
}
.script-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.45s ease;
}
.script-card:hover .script-card-img {
  transform: scale(1.05);
}
.script-card-img-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(10, 11, 28, 0.95) 0%, rgba(10, 11, 28, 0.3) 50%, transparent 100%);
  pointer-events: none;
}

/* Floating Badges */
.card-badge-top-left {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
  z-index: 3;
}
.card-badge-top-right {
  position: absolute;
  top: 10px;
  right: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
  z-index: 3;
}
.card-badge-bottom-left {
  position: absolute;
  bottom: 8px;
  left: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
  z-index: 3;
}
.card-badge-bottom-right {
  position: absolute;
  bottom: 8px;
  right: 12px;
  z-index: 3;
}

.status-pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  display: inline-block;
  box-shadow: 0 0 8px currentColor;
  animation: pulseDotAnim 1.6s infinite ease-in-out;
}
@keyframes pulseDotAnim {
  0% { transform: scale(0.9); opacity: 0.8; }
  50% { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.8; }
}

.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  backdrop-filter: blur(8px);
}
.status-working {
  background: rgba(16, 185, 129, 0.22);
  border: 1px solid rgba(16, 185, 129, 0.45);
  color: #34d399;
}
.status-patched {
  background: rgba(239, 68, 68, 0.22);
  border: 1px solid rgba(239, 68, 68, 0.45);
  color: #f87171;
}

.badge-premium-star {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 800;
  background: rgba(251, 191, 36, 0.22);
  border: 1px solid rgba(251, 191, 36, 0.5);
  color: #fbbf24;
  backdrop-filter: blur(8px);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.badge-keyless {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 9px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 800;
  background: rgba(56, 189, 248, 0.22);
  border: 1px solid rgba(56, 189, 248, 0.5);
  color: #38bdf8;
  backdrop-filter: blur(8px);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.btn-fav {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: rgba(255, 255, 255, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-fav:hover {
  color: #ef4444;
  background: rgba(239, 68, 68, 0.2);
  border-color: rgba(239, 68, 68, 0.4);
  transform: scale(1.1);
}
.btn-fav.active {
  color: #ef4444;
  background: rgba(239, 68, 68, 0.25);
  border-color: rgba(239, 68, 68, 0.6);
  animation: heartPopAnim 0.35s ease;
}
@keyframes heartPopAnim {
  0% { transform: scale(1); }
  50% { transform: scale(1.3); }
  100% { transform: scale(1); }
}

.card-game-pill {
  font-size: 11px;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #e2e8f0;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
.card-version-pill {
  font-size: 10px;
  font-weight: 700;
  padding: 3px 7px;
  border-radius: 8px;
  background: rgba(124, 58, 237, 0.25);
  border: 1px solid rgba(167, 139, 250, 0.3);
  color: var(--accent-light);
}
.card-price-pill {
  font-size: 11px;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 8px;
  background: rgba(251, 191, 36, 0.2);
  border: 1px solid rgba(251, 191, 36, 0.4);
  color: #fbbf24;
  backdrop-filter: blur(6px);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.card-price-free {
  background: rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.4);
  color: #34d399;
}

/* Card Body */
.script-card-body {
  padding: 14px 16px 10px 16px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  flex: 1;
}
.card-title-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 8px;
}
.card-title {
  font-size: 16px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.3;
  cursor: pointer;
  transition: color 0.2s;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.card-title:hover {
  color: var(--accent-light);
}
.card-desc {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  min-height: 35px;
}

/* Feature tags */
.card-features {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.feature-tag {
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

/* Executor tags */
.executor-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  align-items: center;
}
.badge-executor {
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 5px;
  background: rgba(124, 58, 237, 0.15);
  border: 1px solid rgba(167, 139, 250, 0.25);
  color: var(--accent-light);
}

/* Working Vote Bar */
.card-vote-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  padding: 4px 8px;
}
.vote-bar-track {
  flex: 1;
  height: 6px;
  background: rgba(239, 68, 68, 0.35);
  border-radius: 4px;
  overflow: hidden;
}
.vote-bar-fill {
  height: 100%;
  background: #10b981;
  border-radius: 4px;
  transition: width 0.3s ease;
}
.vote-btns-group {
  display: flex;
  align-items: center;
  gap: 4px;
}
.vote-btn-mini {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 2px 6px;
  font-size: 10px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 3px;
  color: var(--text-secondary);
  transition: all 0.18s;
}
.vote-btn-mini:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--text-primary);
}
.vote-up:hover {
  color: #10b981;
  border-color: rgba(16, 185, 129, 0.4);
}
.vote-down:hover {
  color: #ef4444;
  border-color: rgba(239, 68, 68, 0.4);
}

/* Card Meta Row */
.card-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text-muted);
  padding-top: 4px;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
}
.owner-info {
  display: flex;
  align-items: center;
  gap: 6px;
}
.owner-avatar {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--bg-card);
}
.owner-name {
  font-weight: 600;
  color: var(--text-secondary);
}
.card-stats-right {
  display: flex;
  align-items: center;
  gap: 8px;
}
.rating-badge, .views-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-weight: 700;
  cursor: pointer;
}
.rating-badge:hover {
  color: var(--gold);
}

/* Card Footer */
.script-card-footer {
  padding: 10px 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(0, 0, 0, 0.16);
  border-radius: 0 0 20px 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.card-buttons-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}
.btn-quick-copy {
  background: var(--accent-gradient);
  border: 1px solid var(--accent-light);
  color: #ffffff;
  padding: 9px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.btn-quick-copy:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(124, 58, 237, 0.4);
}
.btn-quick-copy:active {
  transform: translateY(0);
}
.btn-view-code {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 9px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-view-code:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--accent-light);
  transform: translateY(-2px);
}
.btn-locked-unlock {
  grid-column: span 2;
  background: var(--gold-gradient);
  color: #000;
  font-weight: 800;
  padding: 10px;
  border-radius: 12px;
  border: none;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-locked-unlock:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4);
}

.card-footer-sub {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 4px;
}
.btn-toggle-comments {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: color 0.18s;
  padding: 2px 0;
}
.btn-toggle-comments:hover {
  color: var(--accent-light);
}
.chevron-icon {
  font-size: 9px;
  transition: transform 0.25s ease;
}

/* Comments Drawer Inside Card */
.card-comments-box {
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.35s ease, opacity 0.25s ease, margin 0.25s ease;
  margin-top: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 10px;
  padding: 0 10px;
}
.card-comments-box.expanded {
  max-height: 380px;
  opacity: 1;
  margin-top: 8px;
  padding: 10px;
}
.comments-box-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 4px;
}
.comment-single {
  font-size: 11px;
  padding: 4px 6px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 6px;
  display: flex;
  gap: 6px;
}
.comment-author {
  font-weight: 700;
  color: var(--accent-light);
}
.comment-body {
  color: var(--text-secondary);
  word-break: break-word;
}
.comment-empty {
  font-size: 11px;
  color: var(--text-muted);
  text-align: center;
  padding: 6px 0;
}
.comment-notice {
  font-size: 11px;
  color: var(--gold);
  text-align: center;
  padding: 6px 0;
}

/* Modal Execution Guidance */
.code-execution-guide {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-top: 12px;
  margin-bottom: 10px;
}
.exec-step-item {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 10px 12px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}
.step-badge {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--accent-gradient);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.step-text {
  font-size: 11px;
  color: var(--text-secondary);
  line-height: 1.35;
}
.step-text strong {
  color: var(--text-primary);
  display: block;
}

@media (max-width: 768px) {
  .code-execution-guide {
    grid-template-columns: 1fr;
    gap: 6px;
  }
  .scripts-grid {
    grid-template-columns: 1fr;
  }
}

/* ==================== PERFORMANCE & THEME COMPATIBILITY PATCHES ==================== */

/* Instant Owner Avatar Badge (Zero network latency) */
.owner-avatar-badge {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 800;
  color: #ffffff;
  flex-shrink: 0;
  box-shadow: 0 2px 6px rgba(124, 58, 237, 0.3);
}

/* Header layout fixes: prevent ugly multi-row wrapping on desktop/laptops */
.header-right {
  flex-wrap: nowrap !important;
}

@media (max-width: 1200px) {
  .social-btn-text, .guide-btn-text {
    display: none !important;
  }
  .btn-social-discord, .btn-social-youtube, .btn-social-tiktok, .header-guide-btn {
    padding: 8px !important;
    min-width: 36px !important;
    height: 36px !important;
  }
  .header-titles span {
    display: none !important;
  }
}

/* Mobile bottom nav clearance: prevent fixed nav from hiding pagination or footer */
@media (max-width: 768px) {
  main {
    padding-bottom: 84px !important;
  }
  /* Center modals properly on mobile instead of awkward cut-off bottom sheets */
  .modal-overlay {
    padding: 12px !important;
    align-items: center !important;
  }
  .modal-container {
    max-height: 92vh !important;
    border-radius: 20px !important;
    width: 100% !important;
  }
}

/* Smooth Horizontal Scroll for Categories and Quick Filters */
.categories-wrapper, .quick-filters-scroll {
  -webkit-overflow-scrolling: touch;
  scroll-behavior: smooth;
}

/* Light Mode Card and Component Contrast Fixes */
[data-theme="light"] .script-card {
  background: #ffffff !important;
  border-color: rgba(0, 0, 0, 0.08) !important;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.05) !important;
}
[data-theme="light"] .script-card:hover {
  border-color: var(--accent-light) !important;
  box-shadow: 0 12px 28px rgba(124, 58, 237, 0.12) !important;
}
[data-theme="light"] .script-card-img-wrap {
  background: #f1f5f9 !important;
}
[data-theme="light"] .script-card-img-overlay {
  background: linear-gradient(to top, rgba(255, 255, 255, 0.96) 0%, rgba(255, 255, 255, 0.25) 45%, transparent 100%) !important;
}
[data-theme="light"] .card-title {
  color: #0f172a !important;
}
[data-theme="light"] .card-title:hover {
  color: var(--accent) !important;
}
[data-theme="light"] .card-desc {
  color: #475569 !important;
}
[data-theme="light"] .script-card-footer {
  background: #f8fafc !important;
  border-color: rgba(0, 0, 0, 0.06) !important;
}
[data-theme="light"] .card-comments-box {
  background: #f1f5f9 !important;
}
[data-theme="light"] .card-vote-bar {
  background: #f8fafc !important;
  border-color: rgba(0, 0, 0, 0.08) !important;
}
[data-theme="light"] .feature-tag {
  background: #f1f5f9 !important;
  border-color: rgba(0, 0, 0, 0.08) !important;
  color: #334155 !important;
}
[data-theme="light"] .btn-view-code {
  background: #ffffff !important;
  border-color: rgba(0, 0, 0, 0.12) !important;
  color: #0f172a !important;
}
[data-theme="light"] .btn-view-code:hover {
  background: #f1f5f9 !important;
  border-color: var(--accent) !important;
}
[data-theme="light"] .comment-single {
  background: #ffffff !important;
  border: 1px solid rgba(0, 0, 0, 0.06) !important;
}
[data-theme="light"] .quick-filter-chip {
  background: #ffffff !important;
  border-color: rgba(0, 0, 0, 0.1) !important;
  color: #475569 !important;
}
[data-theme="light"] .quick-filter-chip.active {
  background: var(--accent-gradient) !important;
  color: #ffffff !important;
  border-color: var(--accent) !important;
}
[data-theme="light"] .exec-step-item {
  background: #ffffff !important;
  border-color: rgba(0, 0, 0, 0.08) !important;
}
[data-theme="light"] .owner-name {
  color: #334155 !important;
}

/* Blue & Green Themes Card Support */
[data-theme="blue"] .script-card {
  background: rgba(15, 23, 42, 0.75);
  border-color: rgba(56, 189, 248, 0.18);
}
[data-theme="green"] .script-card {
  background: rgba(6, 30, 18, 0.75);
  border-color: rgba(16, 185, 129, 0.18);
}

/* ==================== SCRIPT CARD CSS GRID LAYOUT ==================== */
.script-card {
  display: grid !important;
  grid-template-rows: auto 1fr auto !important;
  grid-template-areas:
    "card-banner"
    "card-body"
    "card-footer" !important;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  overflow: hidden;
  transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.28s, border-color 0.28s;
  height: 100%;
  box-sizing: border-box;
}

.script-card-img-wrap {
  grid-area: card-banner !important;
  position: relative;
  width: 100%;
  height: 165px;
  overflow: hidden;
  background: #08091a;
  cursor: pointer;
}

.script-card-body {
  grid-area: card-body !important;
  padding: 16px 18px 12px 18px !important;
  display: grid !important;
  grid-template-rows: auto auto auto auto auto auto !important;
  grid-template-areas:
    "card-title"
    "card-desc"
    "card-features"
    "card-executors"
    "card-vote"
    "card-meta" !important;
  gap: 10px !important;
  box-sizing: border-box;
}

.card-title-row {
  grid-area: card-title !important;
}

.card-desc {
  grid-area: card-desc !important;
  margin: 0 !important;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.45;
}

.card-features {
  grid-area: card-features !important;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
}

.executor-tags {
  grid-area: card-executors !important;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 5px;
  margin: 2px 0 !important;
}

.card-vote-bar {
  grid-area: card-vote !important;
}

.card-meta-row {
  grid-area: card-meta !important;
}

.card-comments-box {
  grid-column: 1 / -1;
  margin-top: 4px;
}

.script-card-footer {
  grid-area: card-footer !important;
  padding: 12px 16px !important;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(0, 0, 0, 0.16);
  display: grid !important;
  grid-template-rows: auto auto !important;
  grid-template-areas:
    "footer-actions"
    "footer-sub" !important;
  gap: 10px !important;
  box-sizing: border-box;
}

.card-buttons-row {
  grid-area: footer-actions !important;
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 8px !important;
  width: 100% !important;
}

.card-footer-sub {
  grid-area: footer-sub !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding-top: 4px !important;
}

/* ==================== MOBILE OPTIMIZATIONS (SPACING & BUTTONS) ==================== */
@media (max-width: 768px) {
  .script-grid {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }

  .script-card {
    border-radius: 16px !important;
  }

  .script-card-img-wrap {
    height: 145px !important;
  }

  .script-card-body {
    padding: 12px 14px 10px 14px !important;
    gap: 8px !important;
  }

  .card-title {
    font-size: 15px !important;
    line-height: 1.35 !important;
  }

  .card-desc {
    font-size: 12px !important;
    -webkit-line-clamp: 2 !important;
  }

  .script-card-footer {
    padding: 10px 12px !important;
    gap: 8px !important;
  }

  .card-buttons-row .btn-quick-copy,
  .card-buttons-row .btn-view-code,
  .card-buttons-row .btn-locked-unlock {
    min-height: 42px !important;
    padding: 8px 10px !important;
    font-size: 12px !important;
    white-space: nowrap !important;
    text-overflow: ellipsis !important;
    overflow: hidden !important;
  }
}

@media (max-width: 480px) {
  .script-card-img-wrap {
    height: 135px !important;
  }

  .card-buttons-row {
    grid-template-columns: 1fr 1fr !important;
    gap: 6px !important;
  }

  .card-buttons-row .btn-quick-copy span,
  .card-buttons-row .btn-view-code span {
    font-size: 11px !important;
  }
}

/* ==================== MODALS CSS GRID & BUTTON OVERLAP PREVENTION ==================== */
.modal-container {
  display: grid !important;
  grid-template-rows: auto 1fr auto !important;
  grid-template-areas:
    "modal-header"
    "modal-body"
    "modal-footer" !important;
  max-height: 88vh !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
}

.modal-header {
  grid-area: modal-header !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 16px 20px !important;
  border-bottom: 1px solid var(--border-color) !important;
}

.modal-body {
  grid-area: modal-body !important;
  overflow-y: auto !important;
  padding: 18px 20px !important;
  box-sizing: border-box !important;
  -webkit-overflow-scrolling: touch;
}

.modal-footer {
  grid-area: modal-footer !important;
  padding: 14px 20px !important;
  border-top: 1px solid var(--border-color) !important;
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)) !important;
  gap: 10px !important;
  align-items: center !important;
}

/* Ensure no button in modals ever overlaps or breaks layout */
.modal-container button,
.modal-container .btn {
  flex-shrink: 0 !important;
  min-height: 40px !important;
  box-sizing: border-box !important;
  word-break: normal !important;
  white-space: nowrap !important;
}

/* Script Code Modal Actions Layout */
.code-modal-top-row {
  display: grid !important;
  grid-template-columns: 1fr auto !important;
  grid-template-areas: "code-label code-actions" !important;
  align-items: center !important;
  gap: 12px !important;
  margin-bottom: 10px !important;
}

.code-modal-top-row > span {
  grid-area: code-label !important;
}

.code-btn-group {
  grid-area: code-actions !important;
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, auto)) !important;
  gap: 8px !important;
}

@media (max-width: 640px) {
  .modal-container {
    width: 94% !important;
    max-height: 90vh !important;
    border-radius: 18px !important;
  }

  .modal-header {
    padding: 14px 16px !important;
  }

  .modal-body {
    padding: 14px 16px !important;
  }

  .code-modal-top-row {
    grid-template-columns: 1fr !important;
    grid-template-areas:
      "code-label"
      "code-actions" !important;
    gap: 8px !important;
  }

  .code-btn-group {
    grid-template-columns: repeat(3, 1fr) !important;
    width: 100% !important;
    gap: 6px !important;
  }

  .code-btn-group .btn {
    padding: 8px 6px !important;
    font-size: 11px !important;
    justify-content: center !important;
  }
}

@media (max-width: 420px) {
  .code-btn-group {
    grid-template-columns: 1fr !important;
    gap: 6px !important;
  }

  .code-btn-group .btn {
    width: 100% !important;
  }
}

/* Task steps in Tasks Countdown Modal */
.task-step {
  display: grid !important;
  grid-template-columns: 1fr auto !important;
  grid-template-areas: "task-info task-action" !important;
  align-items: center !important;
  gap: 12px !important;
  background: var(--bg-card) !important;
  border: 1px solid var(--border-color) !important;
  border-radius: 14px !important;
  padding: 12px 16px !important;
  margin-bottom: 10px !important;
  box-sizing: border-box !important;
}

.task-step > div:first-child {
  grid-area: task-info !important;
}

.task-step > div:last-child {
  grid-area: task-action !important;
}

@media (max-width: 520px) {
  .task-step {
    grid-template-columns: 1fr !important;
    grid-template-areas:
      "task-info"
      "task-action" !important;
    gap: 10px !important;
  }

  .task-step > div:last-child {
    display: flex !important;
    width: 100% !important;
  }

  .task-step .btn {
    width: 100% !important;
    justify-content: center !important;
    min-height: 42px !important;
  }
}

/* Unlock Choice Modal */
.unlock-options {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 14px !important;
  margin-top: 12px !important;
}

@media (max-width: 520px) {
  .unlock-options {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }
}

/* Edit profile and modal bottom button pairs */
.modal-body div[style*="justify-content: flex-end"],
.modal-body div[style*="display: flex; gap: 10px; margin-top"],
.modal-body div[style*="display: flex; gap: 8px"] {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)) !important;
  gap: 8px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

.modal-body div[style*="justify-content: flex-end"] button,
.modal-body div[style*="display: flex; gap: 10px; margin-top"] button {
  width: 100% !important;
  min-height: 42px !important;
  justify-content: center !important;
}

/* ==================== RBLXSCRIPTS.NET TOP NAV & EXECUTOR CARDS ==================== */
.rblx-top-nav-wrap {
  width: 100%;
  background: rgba(13, 14, 28, 0.95);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  position: sticky;
  top: 64px;
  z-index: 90;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}

.rblx-top-nav-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 8px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  overflow-x: auto;
  scrollbar-width: none;
}

.rblx-top-nav-inner::-webkit-scrollbar {
  display: none;
}

.rblx-nav-links {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.rblx-nav-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: var(--text-secondary);
  padding: 8px 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.rblx-nav-btn:hover {
  background: rgba(124, 58, 237, 0.15);
  border-color: var(--accent-light);
  color: #ffffff;
  transform: translateY(-1px);
}

.rblx-nav-btn.active {
  background: var(--accent-gradient);
  border-color: var(--accent-light);
  color: #ffffff;
  box-shadow: 0 0 16px rgba(124, 58, 237, 0.4);
}

.rblx-badge-hot {
  background: #ef4444;
  color: #ffffff;
  font-size: 9px;
  font-weight: 900;
  padding: 2px 6px;
  border-radius: 6px;
  letter-spacing: 0.5px;
}

.rblx-live-status-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.25);
  color: #10b981;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
}

/* Executor Hub Cards Grid */
.executor-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.28s, box-shadow 0.28s;
  box-sizing: border-box;
}

.executor-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent-light);
  box-shadow: 0 12px 30px rgba(124, 58, 237, 0.2);
}

.executor-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.executor-card-title-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.executor-icon-box {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}

.executor-unc-badge {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.3);
  color: #10b981;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 800;
  white-space: nowrap;
}

.badge-status-dot-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(16, 185, 129, 0.12);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.25);
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 700;
}

.platform-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

@media (max-width: 768px) {
  .rblx-top-nav-wrap {
    top: 56px;
  }

  .rblx-top-nav-inner {
    padding: 6px 12px;
  }

  .rblx-nav-btn {
    padding: 6px 10px;
    font-size: 12px;
  }
}






/* ==================== RBLXSCRIPTS.NET ENHANCED STYLING ==================== */
.brand-logo-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: linear-gradient(135deg, #7c3aed, #06b6d4);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-size: 18px;
  box-shadow: 0 0 16px rgba(124, 58, 237, 0.4);
  flex-shrink: 0;
}

.brand-accent {
  color: #a855f7;
  font-weight: 900;
  letter-spacing: -0.5px;
}

.brand-white {
  color: #ffffff;
  font-weight: 800;
  letter-spacing: -0.5px;
}

.brand-net-pill {
  font-size: 11px;
  font-weight: 800;
  background: rgba(124, 58, 237, 0.25);
  color: #38bdf8;
  padding: 2px 6px;
  border-radius: 6px;
  border: 1px solid rgba(56, 189, 248, 0.3);
  margin-left: 6px;
  vertical-align: middle;
}

.live-dot {
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  margin-right: 4px;
  animation: livePulse 1.8s infinite;
}

@keyframes livePulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.6; }
}

.hero-quick-tags {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-top: 14px;
}

.hero-quick-label {
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 5px;
}

.hero-quick-pill {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-color);
  padding: 4px 12px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.hero-quick-pill:hover {
  background: rgba(124, 58, 237, 0.2);
  border-color: var(--accent);
  color: #ffffff;
  transform: translateY(-1px);
}

.rblx-stats-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-top: 16px;
  padding: 14px;
  background: rgba(14, 16, 38, 0.7);
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.rblx-stats-bar .stat-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.rblx-stats-bar .stat-num {
  font-size: 20px;
  font-weight: 800;
  font-family: 'JetBrains Mono', monospace;
  line-height: 1.2;
}

.rblx-stats-bar .stat-label {
  font-size: 11px;
  color: var(--text-muted);
  font-weight: 600;
  margin-top: 2px;
}

.card-action-btns {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 8px;
  width: 100%;
}

.btn-copy-loadstring {
  background: linear-gradient(135deg, #7c3aed, #6366f1);
  color: #ffffff;
  font-weight: 700;
  font-size: 13px;
  border: none;
  border-radius: 8px;
  padding: 8px 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(124, 58, 237, 0.25);
}

.btn-copy-loadstring:hover {
  background: linear-gradient(135deg, #8b5cf6, #4f46e5);
  box-shadow: 0 6px 16px rgba(124, 58, 237, 0.4);
  transform: translateY(-1px);
}

.btn-copied-success {
  background: #10b981 !important;
  color: #ffffff !important;
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.5) !important;
}

.btn-view-code {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  font-weight: 600;
  font-size: 13px;
  border-radius: 8px;
  padding: 8px 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.2s ease;
}

.btn-view-code:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--text-muted);
  color: #ffffff;
}

@media (max-width: 640px) {
  .rblx-stats-bar {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
}

"""

if __name__ == "__main__":
    pass
