#!/usr/bin/env python3

def get_html():
    return """
  <!-- Ambient Background Glows -->
  <div class="ambient-glow glow-1"></div>
  <div class="ambient-glow glow-2"></div>

  <!-- Header -->
  <header>
    <div class="header-left" onclick="resetFilters()" title="Ana Sayfaya Dön">
      <div class="brand-logo-icon">
        <i class="fa-solid fa-bolt"></i>
      </div>
      <div class="header-titles">
        <h1 id="appTitle"><span class="brand-accent">SCRIPT</span><span class="brand-white">DEPO</span><span class="brand-net-pill">.NET</span></h1>
        <span id="appSubtitle"><span class="live-dot"></span> 120+ Doğrulanmış Script &amp; Oyun</span>
      </div>
    </div>

    <div class="header-center">
      <div class="search-input-wrapper">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" id="searchInput" class="search-input" placeholder="Script, oyun, executor veya özellik ara..." oninput="handleSearchDebounce(event)" />
        <button type="button" class="search-clear-btn" id="searchClearBtn" onclick="clearSearchInput()" title="Aramayı Temizle" style="display: none;">
          <i class="fa-solid fa-xmark"></i>
        </button>
        <span class="search-kbd-hint desktop-only" title="Hızlı arama için klavyede / tuşuna basın">/</span>
      </div>
    </div>

    <div class="header-right">
      <!-- Coin Display (Visible on all devices) -->
      <div class="coin-badge" id="headerCoinBadge" onclick="openCoinStoreModal('scripts')" title="Coin Bakiyen">
        <i class="fa-solid fa-coins"></i>
        <span id="headerCoinCount">50</span>
      </div>

      <!-- Guide / Rehber Button (Visible on all devices) -->
      <button class="btn btn-outline btn-sm header-guide-btn" id="btnOpenGuide" onclick="openGuideModal('howtouse')" title="Nasıl Kullanılır? & Detaylı Rehber">
        <i class="fa-solid fa-book-open"></i>
        <span class="guide-btn-text">Rehber</span>
      </button>

      <!-- Notification Bell (Visible on all devices) -->
      <div style="position: relative;" class="notif-wrapper">
        <button class="btn btn-outline btn-icon notif-bell-btn" id="notifBellBtn" onclick="toggleNotifDropdown()" title="Bildirimler">
          <i class="fa-solid fa-bell"></i>
          <span class="notif-badge-dot" id="notifBadgeDot"></span>
        </button>

        <!-- Notification Dropdown -->
        <div class="notif-dropdown" id="notifDropdown">
          <div class="notif-header">
            <span style="font-weight: 700; font-size: 14px;" id="notifTitle">Bildirimler</span>
            <button style="background: none; border: none; color: var(--accent-light); font-size: 12px; cursor: pointer;" onclick="clearAllNotifications()" id="notifClearBtn">Temizle</button>
          </div>
          <div class="notif-list" id="notifList">
            <!-- Dynamic notifications -->
          </div>
        </div>
      </div>

      <!-- Mobile Menu Hamburger Button (ONLY visible on Mobile) -->
      <button class="btn btn-outline btn-icon mobile-menu-btn" id="mobileMenuBtn" onclick="toggleMobileDrawer()" title="Hızlı Menü & Ayarlar">
        <i class="fa-solid fa-bars"></i>
      </button>

      <!-- Desktop Only Items -->
      <a href="https://discord.gg/Bpn6bYFHsm" target="_blank" rel="noopener noreferrer" class="btn btn-social-discord btn-sm desktop-only" title="Discord Sunucumuza Katıl">
        <i class="fa-brands fa-discord"></i>
        <span class="social-btn-text">Discord</span>
      </a>
      <a href="https://youtube.com/@mm2_ultimatehub" target="_blank" rel="noopener noreferrer" class="btn btn-social-youtube btn-sm desktop-only" title="YouTube Kanalımız">
        <i class="fa-brands fa-youtube"></i>
        <span class="social-btn-text">YouTube</span>
      </a>
      <a href="https://www.tiktok.com/@mm2_ultimatehub" target="_blank" rel="noopener noreferrer" class="btn btn-social-tiktok btn-sm desktop-only" title="TikTok Sayfamız">
        <i class="fa-brands fa-tiktok"></i>
        <span class="social-btn-text">TikTok</span>
      </a>

      <!-- Sound Toggle (Desktop) -->
      <button class="btn btn-outline btn-icon desktop-only" id="soundToggleBtn" onclick="toggleSound()" title="Ses Efektleri Aç/Kapat">
        <i class="fa-solid fa-volume-high" id="soundToggleIcon"></i>
      </button>

      <!-- Promo Code Button (Desktop) -->
      <button class="btn btn-gold btn-sm desktop-only" id="btnOpenPromo" onclick="openPromoCodeModal()" title="Kupon / Promosyon Kodu Kullan">
        <i class="fa-solid fa-gift"></i>
        <span>Kupon</span>
      </button>

      <!-- Coin Store Button (Desktop) -->
      <button class="btn btn-outline btn-icon desktop-only" id="storeBtn" title="Mağaza" onclick="openCoinStoreModal('scripts')">
        <i class="fa-solid fa-store"></i>
      </button>

      <!-- Theme Switcher (Desktop) -->
      <div class="theme-picker desktop-only" title="Tema Değiştir">
        <div class="theme-dot dot-dark active" onclick="switchTheme('dark')" title="Dark"></div>
        <div class="theme-dot dot-light" onclick="switchTheme('light')" title="Light"></div>
        <div class="theme-dot dot-blue" onclick="switchTheme('blue')" title="Blue"></div>
        <div class="theme-dot dot-green" onclick="switchTheme('green')" title="Green"></div>
      </div>

      <!-- Lang Selector (Desktop) -->
      <button class="btn btn-outline lang-btn desktop-only" id="langSwitchBtn" onclick="toggleLanguage()" title="Dil Değiştir">
        <span id="langLabel">TR</span>
      </button>

      <!-- User Profile / Login (Desktop) -->
      <button class="btn btn-outline desktop-only" id="authProfileBtn" onclick="handleAuthOrProfileClick()">
        <i class="fa-solid fa-user"></i>
        <span id="authProfileBtnText">Giriş Yap</span>
      </button>

      <!-- Add Script (Desktop) -->
      <button class="btn btn-primary desktop-only" onclick="openAddScriptModal()" id="btnAddScript">
        <i class="fa-solid fa-code"></i>
        <span>Script Ekle</span>
      </button>

      <!-- Add Game (Desktop) -->
      <button class="btn btn-green desktop-only" onclick="openAddGameModal()" id="btnAddGame">
        <i class="fa-solid fa-gamepad"></i>
        <span>Oyun Ekle</span>
      </button>

      <!-- Collection (Desktop) -->
      <button class="btn btn-gold desktop-only" onclick="openCoinStoreModal('inventory')" id="btnCollection" title="Koleksiyon">
        <i class="fa-solid fa-box-open"></i>
      </button>

      <!-- Admin Button (Hidden by default) -->
      <button class="btn btn-outline desktop-only" id="adminBtn" style="display: none; border-color: #ef4444; color: #ef4444;" onclick="openAdminModal()">
        <i class="fa-solid fa-wrench"></i>
        <span>Admin</span>
      </button>
    </div>
  </header>

  <!-- SCRIPTDEPO TOP NAVIGATION BAR -->
  <div class="rblx-top-nav-wrap">
    <div class="rblx-top-nav-inner">
      <div class="rblx-nav-links">
        <button class="rblx-nav-btn active" id="rblxNav_all" onclick="selectCategory('all')">
          <i class="fa-solid fa-layer-group"></i>
          <span>Tüm Scriptler</span>
        </button>
        <button class="rblx-nav-btn" id="rblxNav_popular" onclick="selectQuickFilter('popular')">
          <i class="fa-solid fa-fire" style="color: #f97316;"></i>
          <span>Trending & Popüler</span>
        </button>
        <button class="rblx-nav-btn" id="rblxNav_keyless" onclick="selectQuickFilter('keyless')">
          <i class="fa-solid fa-bolt" style="color: var(--gold);"></i>
          <span>Keyless Scriptler</span>
        </button>
        <button class="rblx-nav-btn" id="rblxNav_executors" onclick="selectCategory('executors')">
          <i class="fa-solid fa-microchip" style="color: var(--accent-light);"></i>
          <span>Executors Hub</span>
          <span class="rblx-badge-hot">YENİ</span>
        </button>
        <button class="rblx-nav-btn" id="rblxNav_games" onclick="selectCategory('games')">
          <i class="fa-solid fa-gamepad" style="color: #38bdf8;"></i>
          <span>Oyunlar</span>
        </button>
        <button class="rblx-nav-btn" id="rblxNav_rewards" onclick="openTasksCountdownModal()">
          <i class="fa-solid fa-gift" style="color: #ec4899;"></i>
          <span>Ücretsiz Script Aç (+3 Görev)</span>
        </button>
        <button class="rblx-nav-btn" id="rblxNav_guide" onclick="openGuideModal('howtouse')">
          <i class="fa-solid fa-book-open" style="color: #10b981;"></i>
          <span>Nasıl Çalıştırılır?</span>
        </button>
      </div>
      <div class="rblx-live-status-pill desktop-only">
        <span class="status-pulse-dot" style="background: #10b981;"></span>
        <span>120+ İçerik • Topluluk tarafından test ediliyor</span>
      </div>
    </div>
  </div>

  <!-- Main Container -->
  <main class="main-container">
    <!-- Platform Intro & Explanatory Hero Banner -->
    <section class="platform-hero" id="platformIntroHero">
      <div class="hero-top-row">
        <div class="hero-tag">
          <i class="fa-solid fa-bolt" style="color: var(--gold);"></i>
          <span>SCRIPTDEPO 2026 EDITION</span>
        </div>
        <button class="hero-collapse-btn" onclick="toggleHeroIntro()" id="btnToggleHero" title="Paneli Gizle/Göster">
          <i class="fa-solid fa-chevron-up" id="heroToggleIcon"></i>
          <span id="heroToggleText">Gizle</span>
        </button>
      </div>

      <div class="hero-content" id="heroMainContent">
        <div class="hero-text-wrap">
          <h2 class="hero-title">Roblox Script & Oyun Dünyasının En Güvenli Merkezi</h2>
          <p class="hero-subtitle">
            Roblox topluluğu için düzenli olarak güncellenen MM2, Blox Fruits, Da Hood ve 90+ Roblox oyunu scripti. Görevleri tamamlayarak veya kupon girerek bedava Coin kazan, script detaylarını hızlıca incele!
          </p>
        </div>

        <!-- 4 Explanatory Bento Cards -->
        <div class="hero-cards-grid">
          <div class="hero-card" onclick="openGuideModal('executors')">
            <div class="hero-card-icon" style="background: rgba(124, 58, 237, 0.15); color: var(--accent-light);">
              <i class="fa-solid fa-microchip"></i>
            </div>
            <div class="hero-card-info">
              <h4>1. Executor Nedir?</h4>
              <p>Delta, Wave, Solara, Hydrogen. Roblox'ta Lua scriptlerini çalıştıran güvenli programlardır.</p>
              <span class="hero-card-link">Detayları Gör <i class="fa-solid fa-arrow-right"></i></span>
            </div>
          </div>

          <div class="hero-card" onclick="openGuideModal('coins')">
            <div class="hero-card-icon" style="background: rgba(251, 191, 36, 0.15); color: var(--gold);">
              <i class="fa-solid fa-coins"></i>
            </div>
            <div class="hero-card-info">
              <h4>2. Coin Nasıl Kazanılır?</h4>
              <p>Günlük görevlerle (+100'e kadar), sponsor takipleriyle ve kuponlarla ücretsiz Coin topla!</p>
              <span class="hero-card-link">Taktikleri Oku <i class="fa-solid fa-arrow-right"></i></span>
            </div>
          </div>

          <div class="hero-card" onclick="openGuideModal('safety')">
            <div class="hero-card-icon" style="background: rgba(16, 185, 129, 0.15); color: var(--green);">
              <i class="fa-solid fa-shield-halved"></i>
            </div>
            <div class="hero-card-info">
              <h4>3. Güvenlik & Oylama</h4>
              <p>Her scriptin altında canlı topluluk oyu (%98 Çalışıyor). Oy vererek sen de +2 Coin kazan!</p>
              <span class="hero-card-link">Güvenlik Rehberi <i class="fa-solid fa-arrow-right"></i></span>
            </div>
          </div>

          <div class="hero-card" onclick="openGuideModal('howtouse')">
            <div class="hero-card-icon" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8;">
              <i class="fa-solid fa-terminal"></i>
            </div>
            <div class="hero-card-info">
              <h4>4. 3 Adımda Çalıştır</h4>
              <p>Scripti Aç & Kodu Kopyala -> Oyunu Başlat -> Executor'a Yapıştırıp "Execute" Butonuna Bas!</p>
              <span class="hero-card-link">Adım Adım İzle <i class="fa-solid fa-arrow-right"></i></span>
            </div>
          </div>
        </div>

        <div class="hero-actions">
          <button class="btn btn-primary" onclick="openGuideModal('howtouse')">
            <i class="fa-solid fa-book-open"></i>
            <span>Detaylı Kullanım Rehberi & SSS</span>
          </button>
          <button class="btn btn-gold" onclick="openPromoCodeModal()">
            <i class="fa-solid fa-gift"></i>
            <span>Ücretsiz Kupon Kodu Kullan (+100 🪙)</span>
          </button>
          <a href="https://discord.gg/Bpn6bYFHsm" target="_blank" rel="noopener noreferrer" class="btn btn-social-discord">
            <i class="fa-brands fa-discord"></i>
            <span>Discord Yardım & Topluluk</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Daily Tasks Section -->
    <section class="daily-tasks-banner" id="dailyTasksSection">
      <div class="tasks-header">
        <div class="tasks-title-wrap">
          <h2 id="dailyTasksTitle">
            <i class="fa-solid fa-bullseye" style="color: var(--accent-light);"></i>
            <span>Günlük Görevler</span>
          </h2>
          <span class="tasks-counter" id="tasksCounterDisplay">
            <i class="fa-solid fa-coins"></i> +0 coin (0/8)
          </span>
        </div>
        <button class="btn btn-gold" onclick="claimAllCompletedTasks()" id="btnClaimAllTasks">
          <i class="fa-solid fa-gift"></i>
          <span>Tümünü Topla</span>
        </button>
      </div>
      <div class="tasks-grid" id="tasksGrid">
        <!-- 8 Daily Tasks injected by JS -->
      </div>
    </section>

    <!-- Categories Horizontal Scroll -->
    <div class="categories-wrapper">
      <div class="categories-list" id="categoriesList">
        <!-- Injected by JS -->
      </div>
    </div>

    <!-- Quick Filters Chips Bar -->
    <div class="quick-filters-scroll">
      <div class="quick-filters-bar" id="quickFiltersBar">
        <button class="quick-filter-chip active" data-filter="all" onclick="selectQuickFilter('all')">
          <i class="fa-solid fa-list-ul"></i> <span>Tümü</span>
        </button>
        <button class="quick-filter-chip" data-filter="popular" onclick="selectQuickFilter('popular')">
          <i class="fa-solid fa-fire" style="color: #f97316;"></i> <span>En Popüler</span>
        </button>
        <button class="quick-filter-chip" data-filter="keyless" onclick="selectQuickFilter('keyless')">
          <i class="fa-solid fa-bolt" style="color: var(--gold);"></i> <span>Keyless (Anahtarsız)</span>
        </button>
        <button class="quick-filter-chip" data-filter="mobile" onclick="selectQuickFilter('mobile')">
          <i class="fa-solid fa-mobile-screen" style="color: #38bdf8;"></i> <span>Mobil Uyumlu</span>
        </button>
        <button class="quick-filter-chip" data-filter="pc" onclick="selectQuickFilter('pc')">
          <i class="fa-solid fa-desktop" style="color: #a78bfa;"></i> <span>PC Uyumlu</span>
        </button>
        <button class="quick-filter-chip" data-filter="working" onclick="selectQuickFilter('working')">
          <i class="fa-solid fa-circle-check" style="color: #10b981;"></i> <span>%80+ Çalışıyor</span>
        </button>
        <button class="quick-filter-chip" data-filter="new" onclick="selectQuickFilter('new')">
          <i class="fa-solid fa-sparkles" style="color: #ec4899;"></i> <span>Yeni Çıkanlar</span>
        </button>
        <button class="quick-filter-chip" data-filter="favs" onclick="selectQuickFilter('favs')">
          <i class="fa-solid fa-heart" style="color: #ef4444;"></i> <span>Favorilerim</span>
        </button>
      </div>
    </div>

    <!-- Filter Bar -->
    <div class="filter-bar">
      <div class="filter-group">
        <div class="filter-label">
          <i class="fa-solid fa-arrow-down-short-wide"></i>
          <span id="sortLabelText">Sırala:</span>
        </div>
        <select class="custom-select" id="sortSelect" onchange="applyFilters()">
          <option value="default" id="optSortDefault">Varsayılan</option>
          <option value="az" id="optSortAZ">A-Z</option>
          <option value="za" id="optSortZA">Z-A</option>
          <option value="popular" id="optSortPopular">Popüler (Görüntülenme)</option>
          <option value="new" id="optSortNew">Yeni</option>
        </select>
      </div>

      <div class="filter-group">
        <div class="filter-label">
          <i class="fa-solid fa-filter"></i>
          <span id="typeLabelText">Tip:</span>
        </div>
        <select class="custom-select" id="typeSelect" onchange="applyFilters()">
          <option value="all" id="optTypeAll">Tümü</option>
          <option value="premium" id="optTypePremium">Premium</option>
          <option value="community" id="optTypeCommunity">Topluluk</option>
        </select>
      </div>

      <div class="filter-group">
        <div class="filter-label">
          <i class="fa-solid fa-star"></i>
          <span id="ratingLabelText">Puan:</span>
        </div>
        <select class="custom-select" id="ratingSelect" onchange="applyFilters()">
          <option value="all" id="optRatingAll">Tümü</option>
          <option value="4" id="optRating4">4+ Yıldız</option>
          <option value="3" id="optRating3">3+ Yıldız</option>
        </select>
      </div>

      <div class="filter-group">
        <div class="filter-label">
          <i class="fa-solid fa-microchip"></i>
          <span id="executorLabelText">Executor:</span>
        </div>
        <select class="custom-select" id="executorSelect" onchange="applyFilters()">
          <option value="all">Tümü</option>
          <option value="Delta">Delta</option>
          <option value="Wave">Wave</option>
          <option value="Hydrogen">Hydrogen</option>
          <option value="Solara">Solara</option>
          <option value="Codex">Codex</option>
        </select>
      </div>

      <div class="filter-group">
        <!-- Backup Button -->
        <button class="btn btn-outline" onclick="exportDataBackup()" title="Yedekle (JSON)">
          <i class="fa-solid fa-floppy-disk"></i>
          <span id="btnBackupText">Yedekle</span>
        </button>
        <!-- Leaderboard Button -->
        <button class="btn btn-outline" onclick="openLeaderboardModal()" title="Liderlik Tablosu">
          <i class="fa-solid fa-trophy" style="color: var(--gold);"></i>
          <span id="btnLeaderboardText">Liderlik</span>
        </button>
      </div>
    </div>

    <!-- Active Filter Status / Section Heading -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
      <h3 id="currentSectionTitle" style="font-size: 18px; font-weight: 700;">Tüm Scriptler</h3>
      <span id="itemsCountDisplay" style="font-size: 13px; color: var(--text-muted);">0 script bulundu</span>
    </div>

    <!-- Scripts Grid / Games Grid -->
    <div class="scripts-grid" id="mainGridContainer">
      <!-- Cards injected by JS -->
    </div>

    <!-- Empty State -->
    <div class="empty-state" id="emptyState" style="display: none;">
      <i class="fa-solid fa-box-open"></i>
      <h3 id="emptyTitle">Sonuç bulunamadı</h3>
      <p id="emptyDesc">Aramanıza veya seçtiğiniz filtrelere uygun içerik bulunamadı.</p>
    </div>

    <!-- Pagination Controls -->
    <div class="pagination-wrapper" id="paginationWrapper" style="display: none;">
      <button class="btn btn-outline" id="prevPageBtn" onclick="changePage(-1)">
        <i class="fa-solid fa-chevron-left"></i>
      </button>
      <span id="pageIndicator" style="font-weight: 700; font-size: 14px;">1 / 1</span>
      <button class="btn btn-outline" id="nextPageBtn" onclick="changePage(1)">
        <i class="fa-solid fa-chevron-right"></i>
      </button>
    </div>
  </main>

  <!-- Footer -->
  <footer style="border-top: 1px solid var(--border-color); padding: 30px 20px; text-align: center; color: var(--text-muted); font-size: 13px;">
    <p>&copy; 2025 ScriptHub. Roblox topluluğu için script ve oyun platformu.</p>
    <div style="display: flex; justify-content: center; gap: 16px; margin-top: 8px;">
      <a href="javascript:void(0)" onclick="openPrivacyModal()" style="color: var(--accent-light); text-decoration: none;">Gizlilik Politikası</a>
      <span>&bull;</span>
      <a href="javascript:void(0)" onclick="exportDataBackup()" style="color: var(--accent-light); text-decoration: none;">Yedek İndir (JSON)</a>
      <span>&bull;</span>
      <a href="https://roblox.com" target="_blank" rel="noopener noreferrer" style="color: var(--accent-light); text-decoration: none;">Roblox</a>
    </div>
  </footer>

  <!-- Floating Chat Button & Widget -->
  <button class="chat-fab" id="chatFabBtn" onclick="toggleChatWidget()" title="Topluluk Sohbeti">
    <i class="fa-solid fa-comment-dots" id="chatFabIcon"></i>
  </button>
  <div class="chat-iframe-modal" id="chatIframeModal">
    <div class="chat-iframe-header">
      <span><i class="fa-solid fa-comments"></i> ScriptHub Chat</span>
      <button class="modal-close-btn" onclick="toggleChatWidget()"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <iframe src="https://scripthub.mm2ultimatehub.workers.dev/" class="chat-iframe-content" title="ScriptHub Chat Widget"></iframe>
  </div>

  <!-- Scroll to top button -->
  <button class="scroll-top-btn" id="scrollTopBtn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Yukarı Çık">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- Toast Container -->
  <div class="toast-container" id="toastContainer"></div>

  <!-- Cookie Consent Banner -->
  <div class="cookie-banner" id="cookieBanner">
    <div>
      <h4 style="font-size: 14px; font-weight: 700; margin-bottom: 4px;">🍪 Çerez Bildirimi</h4>
      <p style="font-size: 12px; color: var(--text-secondary);">Deneyiminizi geliştirmek ve tercihlerinizi hatırlamak için çerezleri ve yerel depolamayı kullanıyoruz.</p>
    </div>
    <button class="btn btn-primary" onclick="acceptCookieConsent()">Kabul Et</button>
  </div>

  <!-- ==================== MODALS ==================== -->

  <!-- Auth Modal -->
  <div class="modal-overlay" id="authModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title" id="authModalTitle"><i class="fa-solid fa-user-lock"></i> Hesap İşlemleri</h3>
        <button class="modal-close-btn" onclick="closeModal('authModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div class="tab-nav">
          <button class="tab-btn active" id="tabSignInBtn" onclick="switchAuthTab('signin')">Giriş Yap</button>
          <button class="tab-btn" id="tabSignUpBtn" onclick="switchAuthTab('signup')">Kayıt Ol</button>
        </div>

        <!-- Sign In Form -->
        <div id="signInFormWrap">
          <form onsubmit="handleSignInSubmit(event)" style="display: flex; flex-direction: column; gap: 14px;">
            <div class="form-group">
              <label>E-posta</label>
              <input type="email" id="signInEmail" class="form-input" placeholder="ornek@mail.com" required />
            </div>
            <div class="form-group">
              <label>Şifre</label>
              <input type="password" id="signInPassword" class="form-input" placeholder="••••••••" required />
            </div>
            <div id="signInError" style="color: var(--red); font-size: 13px; display: none;"></div>
            <button type="submit" class="btn btn-primary" style="margin-top: 8px;">
              <i class="fa-solid fa-rocket"></i> <span>Giriş Yap</span>
            </button>
          </form>
        </div>

        <!-- Sign Up Form -->
        <div id="signUpFormWrap" style="display: none;">
          <form onsubmit="handleSignUpSubmit(event)" style="display: flex; flex-direction: column; gap: 14px;">
            <div class="form-group">
              <label>Kullanıcı Adı (min 3 karakter)</label>
              <input type="text" id="signUpUsername" class="form-input" placeholder="RobloxUstasi" minlength="3" required />
            </div>
            <div class="form-group">
              <label>E-posta</label>
              <input type="email" id="signUpEmail" class="form-input" placeholder="ornek@mail.com" required />
            </div>
            <div class="form-group">
              <label>Şifre (min 6 karakter)</label>
              <input type="password" id="signUpPassword" class="form-input" placeholder="••••••••" minlength="6" oninput="calculatePasswordStrength(this.value)" required />
              <div class="password-meter">
                <div class="meter-bar" id="pwdBar1"></div>
                <div class="meter-bar" id="pwdBar2"></div>
                <div class="meter-bar" id="pwdBar3"></div>
                <div class="meter-bar" id="pwdBar4"></div>
              </div>
            </div>

            <!-- Avatar Selection -->
            <div class="form-group">
              <label>Avatar Seçimi</label>
              <div style="display: flex; gap: 12px; align-items: center; margin-top: 4px;">
                <img src="https://api.dicebear.com/7.x/bottts/svg?seed=RobloxHero" id="signUpAvatarPreview" style="width: 48px; height: 48px; border-radius: 50%; border: 2px solid var(--accent-light);" />
                <button type="button" class="btn btn-outline" style="font-size: 12px; padding: 6px 12px;" onclick="generateRandomSignUpAvatar()">
                  <i class="fa-solid fa-dice"></i> Yeni Avatar
                </button>
              </div>
            </div>

            <div id="signUpError" style="color: var(--red); font-size: 13px; display: none;"></div>
            <div id="signUpSuccess" style="color: var(--green); font-size: 13px; display: none;"></div>

            <button type="submit" class="btn btn-primary" style="margin-top: 8px;">
              <i class="fa-solid fa-user-plus"></i> <span>Kayıt Ol</span>
            </button>
          </form>
        </div>

        <div style="text-align: center; color: var(--text-muted); font-size: 13px; margin: 6px 0;">veya</div>

        <button class="btn btn-outline" style="width: 100%;" onclick="handleGoogleAuth()">
          <i class="fa-brands fa-google"></i> <span>Google ile Devam Et</span>
        </button>

        <button class="btn btn-outline" style="width: 100%; margin-top: 8px;" onclick="handleDiscordAuth()">
          <i class="fa-brands fa-discord"></i> <span>Discord ile Devam Et</span>
        </button>

        

        <button class="btn btn-outline" style="width: 100%; border-color: rgba(251, 191, 36, 0.4); color: var(--gold);" onclick="handleGuestDemoLogin()">
          <i class="fa-solid fa-bolt"></i> <span>Misafir / Demo Olarak Giriş Yap</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Unlock Choice Modal -->
  <div class="modal-overlay" id="unlockChoiceModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-unlock-keyhole"></i> <span id="unlockModalTitle">Scripti Aç</span></h3>
        <button class="modal-close-btn" onclick="closeModal('unlockChoiceModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div style="text-align: center;">
          <h4 id="unlockScriptName" style="font-size: 18px; margin-bottom: 6px; color: var(--accent-light);">Script Adı</h4>
          <p style="font-size: 14px; color: var(--text-muted);">Bu scripti açmak için 2 seçeneğin var:</p>
        </div>

        <div class="unlock-options">
          <div class="unlock-box coin-box" onclick="confirmCoinUnlock()">
            <i class="fa-solid fa-coins"></i>
            <h4 style="font-size: 16px; font-weight: 700;">Coin ile Aç</h4>
            <span style="font-weight: 800; color: var(--gold);" id="unlockCoinPriceLabel">30 coin</span>
            <span style="font-size: 11px; color: var(--text-muted);">Anında açılır</span>
          </div>

          <div class="unlock-box tasks-box" onclick="startTasksUnlock()">
            <i class="fa-solid fa-list-check"></i>
            <h4 style="font-size: 16px; font-weight: 700;">Görevlerle Aç</h4>
            <span style="font-weight: 800; color: var(--green);">Bedava</span>
            <span style="font-size: 11px; color: var(--text-muted);">3 görev tamamla</span>
          </div>
        </div>

        <p style="font-size: 12px; color: var(--text-muted); text-align: center; margin-top: 10px;">
          <i class="fa-solid fa-lightbulb" style="color: var(--gold);"></i> Satın aldığın scriptler kalıcı olarak sana ait olur.
        </p>
      </div>
    </div>
  </div>

  <!-- 3 Tasks Countdown Modal -->
  <div class="modal-overlay" id="tasksCountdownModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-tasks"></i> Görevleri Tamamla</h3>
        <button class="modal-close-btn" onclick="closeModal('tasksCountdownModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <p style="font-size: 13px; color: var(--text-secondary);">Her göreve tıklayıp 25 saniye bekle. 3 görev tamamlanınca script ücretsiz olarak hesabına eklenecek!</p>

        <!-- Task 1 Discord -->
        <div class="task-step">
          <div style="display: flex; align-items: center; gap: 12px;">
            <i class="fa-brands fa-discord" style="font-size: 26px; color: #5865F2;"></i>
            <div>
              <h5 style="font-size: 14px; font-weight: 700;">1. Discord Sunucusuna Katıl</h5>
              <a href="https://discord.gg/Bpn6bYFHsm" target="_blank" rel="noopener noreferrer" style="font-size: 12px; color: #5865F2; text-decoration: underline;">discord.gg/Bpn6bYFHsm</a>
            </div>
          </div>
          <div>
            <button class="btn btn-outline btn-sm" id="btnTask1" onclick="triggerTaskCountdown(1)">Başla (25s)</button>
            <span class="step-timer" id="timerTask1" style="display: none;">25s</span>
          </div>
        </div>

        <!-- Task 2 YouTube -->
        <div class="task-step">
          <div style="display: flex; align-items: center; gap: 12px;">
            <i class="fa-brands fa-youtube" style="font-size: 26px; color: #FF0000;"></i>
            <div>
              <h5 style="font-size: 14px; font-weight: 700;">2. YouTube Kanalımıza Göz At / Abone Ol</h5>
              <a href="https://youtube.com/@mm2_ultimatehub" target="_blank" rel="noopener noreferrer" style="font-size: 12px; color: #FF0000; text-decoration: underline;">@mm2_ultimatehub</a>
            </div>
          </div>
          <div>
            <button class="btn btn-outline btn-sm" id="btnTask2" onclick="triggerTaskCountdown(2)">Başla (25s)</button>
            <span class="step-timer" id="timerTask2" style="display: none;">25s</span>
          </div>
        </div>

        <!-- Task 3 TikTok -->
        <div class="task-step">
          <div style="display: flex; align-items: center; gap: 12px;">
            <i class="fa-brands fa-tiktok" style="font-size: 26px; color: #00f2fe;"></i>
            <div>
              <h5 style="font-size: 14px; font-weight: 700;">3. TikTok Sayfamızı Takip Et</h5>
              <a href="https://www.tiktok.com/@mm2_ultimatehub" target="_blank" rel="noopener noreferrer" style="font-size: 12px; color: #00f2fe; text-decoration: underline;">@mm2_ultimatehub</a>
            </div>
          </div>
          <div>
            <button class="btn btn-outline btn-sm" id="btnTask3" onclick="triggerTaskCountdown(3)">Başla (25s)</button>
            <span class="step-timer" id="timerTask3" style="display: none;">25s</span>
          </div>
        </div>

        <div style="background: rgba(255,255,255,0.03); padding: 12px; border-radius: 12px; text-align: center;">
          <span style="font-size: 13px; font-weight: 700;" id="taskCompletionProgressText">İlerleme: 0 / 3 Tamamlandı</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Script Code Modal -->
  <div class="modal-overlay" id="scriptCodeModal">
    <div class="modal-container modal-lg">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-code"></i> <span id="codeModalTitle">Script Kodu</span></h3>
        <button class="modal-close-btn" onclick="closeModal('scriptCodeModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <!-- Community Working Status & Voting -->
        <div id="modalVotingSection"></div>

                <div class="code-modal-top-row">
          <span style="font-size: 13px; color: var(--text-muted);"><i class="fa-solid fa-terminal" style="color: var(--accent-light);"></i> Lua Script Kodu:</span>
          <div class="code-btn-group">
            <button class="btn btn-primary btn-sm" onclick="copyScriptCode()" id="btnModalCopy" title="Panoya Kopyala">
              <i class="fa-solid fa-copy"></i>
              <span id="btnCopyCodeText">Kopyala</span>
            </button>
            <button class="btn btn-outline btn-sm" onclick="downloadScriptLuaFile()" title="Lua Dosyası Olarak İndir (.lua)">
              <i class="fa-solid fa-download"></i>
              <span>İndir (.lua)</span>
            </button>
            <button class="btn btn-outline btn-sm" onclick="openRawCode()" title="Yeni Sekmede Ham Kodu Aç">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
              <span>Raw</span>
            </button>
          </div>
        </div>
        <div class="code-viewer" id="scriptCodeContent">loadstring(...)()</div>
        <!-- 3-Step Execution Guidance -->
        <div class="code-execution-guide">
          <div class="exec-step-item">
            <span class="step-badge">1</span>
            <div class="step-text"><strong>Executor Aç:</strong> Delta, Wave, Solara veya Codex programını çalıştır.</div>
          </div>
          <div class="exec-step-item">
            <span class="step-badge">2</span>
            <div class="step-text"><strong>Kodu Yapıştır:</strong> "Kopyala" butonuna basıp executor editörüne yapıştır.</div>
          </div>
          <div class="exec-step-item">
            <span class="step-badge">3</span>
            <div class="step-text"><strong>Çalıştır:</strong> Oyunda "Execute / Run" butonuna tıkla ve menüyü aç!</div>
          </div>
        </div>
        <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid rgba(124, 58, 237, 0.3); padding: 12px 16px; border-radius: 14px; font-size: 12px; color: var(--text-secondary);">
          <i class="fa-solid fa-shield-halved" style="color: var(--accent-light);"></i> Bu script güvenli kaynaktan sağlanmıştır. Executor programınızda çalıştırabilirsiniz.
        </div>
      </div>
    </div>
  </div>

  <!-- Coin Store Modal -->
  <div class="modal-overlay" id="coinStoreModal">
    <div class="modal-container modal-lg">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-store" style="color: var(--gold);"></i> Coin Mağazası</h3>
        <button class="modal-close-btn" onclick="closeModal('coinStoreModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <!-- Balance Row -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(251, 191, 36, 0.1); border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 16px; padding: 12px 20px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <i class="fa-solid fa-coins" style="font-size: 24px; color: var(--gold);"></i>
            <div>
              <span style="font-size: 12px; color: var(--text-muted);">Mevcut Bakiyeniz</span>
              <h4 style="font-size: 20px; font-weight: 800; color: var(--gold);" id="storeBalanceDisplay">50 coin</h4>
            </div>
          </div>
          <button class="btn btn-outline" style="font-size: 12px;" onclick="switchAuthTab('tasks')">
            <i class="fa-solid fa-circle-plus"></i> Görevlerle Kazan
          </button>
        </div>

        <!-- Tabs -->
        <div class="tab-nav">
          <button class="tab-btn active" id="storeTabScriptsBtn" onclick="switchStoreTab('scripts')">
            <i class="fa-solid fa-scroll"></i> Premium Scriptler
          </button>
          <button class="tab-btn" id="storeTabCosmeticsBtn" onclick="switchStoreTab('cosmetics')">
            <i class="fa-solid fa-wand-magic-sparkles"></i> Kozmetikler
          </button>
          <button class="tab-btn" id="storeTabInventoryBtn" onclick="switchStoreTab('inventory')">
            <i class="fa-solid fa-box-open"></i> Koleksiyon
          </button>
        </div>

        <!-- Tab 1: Premium Scripts -->
        <div id="storeScriptsTab" class="store-tab-content">
          <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px;" id="storePremiumScriptsGrid">
            <!-- Injected by JS -->
          </div>
        </div>

        <!-- Tab 2: Cosmetics -->
        <div id="storeCosmeticsTab" class="store-tab-content" style="display: none;">
          <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px;" id="storeCosmeticsGrid">
            <!-- Injected by JS -->
          </div>
        </div>

        <!-- Tab 3: Collection / Inventory -->
        <div id="storeInventoryTab" class="store-tab-content" style="display: none;">
          <div style="display: flex; flex-direction: column; gap: 16px;" id="storeInventoryContent">
            <!-- Injected by JS -->
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- User Profile Modal -->
  <div class="modal-overlay" id="userProfileModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-id-card"></i> Kullanıcı Profili</h3>
        <button class="modal-close-btn" onclick="closeModal('userProfileModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div style="display: flex; align-items: center; gap: 18px;">
          <img src="" id="profileAvatarImg" style="width: 80px; height: 80px; border-radius: 50%; border: 3px solid var(--accent); object-fit: cover;" />
          <div>
            <h3 style="font-size: 20px; font-weight: 800;" id="profileDisplayName">Kullanıcı</h3>
            <p style="font-size: 13px; color: var(--text-muted);" id="profileEmail">email@example.com</p>
            <div id="profileAdminBadge" style="display: none; margin-top: 6px; align-items: center; gap: 5px; background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); color: var(--gold); padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 800;">
              <i class="fa-solid fa-crown"></i> <span>Yönetici (Admin)</span>
            </div>
            <span style="font-size: 11px; color: var(--accent-light);" id="profileJoinDate">Üyelik: Bugün</span>
          </div>
        </div>

        <!-- Stats cards -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 6px;">
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Scriptler</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="statUserScripts">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Oyunlar</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="statUserGames">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Coinler</span>
            <h4 style="font-size: 18px; font-weight: 800; color: var(--gold);" id="statUserCoins">50</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Açılan Script</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="statUserUnlocked">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Favoriler</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="statUserFavs">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Toplam Kazanç</span>
            <h4 style="font-size: 18px; font-weight: 800; color: var(--gold);" id="statUserTotalCoins">50</h4>
          </div>
        </div>

        <div style="display: flex; gap: 10px; margin-top: 10px;">
          <button class="btn btn-outline" style="flex: 1;" onclick="openEditProfileModal()">
            <i class="fa-solid fa-pen"></i> Profili Düzenle
          </button>
          <button class="btn btn-outline" style="border-color: #ef4444; color: #ef4444;" onclick="handleSignOut()">
            <i class="fa-solid fa-right-from-bracket"></i> Çıkış Yap
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Edit Profile Modal -->
  <div class="modal-overlay" id="editProfileModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-user-pen"></i> Profili Düzenle</h3>
        <button class="modal-close-btn" onclick="closeModal('editProfileModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div style="display: flex; align-items: center; gap: 16px;">
          <img src="" id="editAvatarPreview" style="width: 70px; height: 70px; border-radius: 50%; border: 2px solid var(--accent-light); object-fit: cover;" />
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-outline btn-sm" onclick="generateRandomEditAvatar()">
              <i class="fa-solid fa-dice"></i> Rastgele Avatar
            </button>
            <label class="btn btn-outline btn-sm" style="cursor: pointer;">
              <i class="fa-solid fa-upload"></i> Yükle
              <input type="file" id="avatarFileInput" accept="image/*" style="display: none;" onchange="handleAvatarFileSelect(event)" />
            </label>
          </div>
        </div>

        <div class="form-group">
          <label>Kullanıcı Adı</label>
          <input type="text" id="editUsernameInput" class="form-input" minlength="3" />
        </div>

        <div class="form-group">
          <label>E-posta (Değiştirilemez)</label>
          <input type="email" id="editEmailInput" class="form-input" disabled style="opacity: 0.6;" />
        </div>

        <div class="form-group">
          <label>Avatar Görsel URL (Opsiyonel)</label>
          <input type="url" id="editAvatarUrlInput" class="form-input" placeholder="https://..." oninput="previewEditAvatarUrl(this.value)" />
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 10px;">
          <button class="btn btn-outline" onclick="closeModal('editProfileModal')">İptal</button>
          <button class="btn btn-primary" onclick="saveUserProfileChanges()">Kaydet</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Add Script Modal -->
  <div class="modal-overlay" id="addScriptModal">
    <div class="modal-container modal-lg">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-file-code"></i> Script Ekle</h3>
        <button class="modal-close-btn" onclick="closeModal('addScriptModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <form onsubmit="handleNewScriptSubmit(event)" style="display: flex; flex-direction: column; gap: 14px;">
          <div class="form-group">
            <label>Script Adı *</label>
            <input type="text" id="addScriptName" class="form-input" placeholder="Örn: Blade Ball Auto Parry Hub" required />
          </div>

          <div class="form-group">
            <label>Kategori *</label>
            <select id="addScriptCategory" class="form-select" required>
              <option value="mm2">MM2 (Murder Mystery 2)</option>
              <option value="bloxfruits">Blox Fruits</option>
              <option value="petsim">Pet Simulator 99</option>
              <option value="dahood">Da Hood</option>
              <option value="bladeball">Blade Ball</option>
              <option value="brookhaven">Brookhaven</option>
              <option value="other">Diğer</option>
            </select>
          </div>

          <div class="form-group">
            <label>Açıklama *</label>
            <textarea id="addScriptDesc" class="form-textarea" placeholder="Scriptin ne yaptığını, hangi executorlarda çalıştığını açıklayın..." required></textarea>
          </div>

          <div class="form-group">
            <label>Özellikler (Virgülle ayırın)</label>
            <input type="text" id="addScriptFeatures" class="form-input" placeholder="Aimbot, ESP, Auto Farm, Speed Hack" />
          </div>

          <div class="form-group">
            <label>Script Kodu (Lua) *</label>
            <textarea id="addScriptCode" class="form-textarea" placeholder="loadstring(game:HttpGet('...'))()" required style="min-height: 120px;"></textarea>
          </div>

          <div class="form-group">
            <label>Resim URL (Opsiyonel)</label>
            <input type="url" id="addScriptImage" class="form-input" placeholder="https://..." oninput="previewAddScriptImage(this.value)" />
            <img id="addScriptImagePreview" style="max-height: 140px; border-radius: 12px; margin-top: 6px; display: none; object-fit: cover;" />
          </div>

          <div class="form-group">
            <label>🪙 Açma Fiyatı (Coin, 0-9999) *</label>
            <input type="number" id="addScriptPrice" class="form-input" min="0" max="9999" value="30" required />
            <span style="font-size: 11px; color: var(--text-muted);">Kullanıcılar bu scripti açmak için bu kadar coin harcar veya görev yapar.</span>
          </div>

          <button type="submit" class="btn btn-primary" style="margin-top: 8px;">
            <i class="fa-solid fa-rocket"></i> <span>Herkese Açık Ekle! (+25 Coin)</span>
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- Add Game Modal -->
  <div class="modal-overlay" id="addGameModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-gamepad" style="color: var(--green);"></i> Oyun Ekle</h3>
        <button class="modal-close-btn" onclick="closeModal('addGameModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <form onsubmit="handleNewGameSubmit(event)" style="display: flex; flex-direction: column; gap: 14px;">
          <div class="form-group">
            <label>Oyun Adı *</label>
            <input type="text" id="addGameName" class="form-input" placeholder="Örn: Arsenal" required />
          </div>

          <div class="form-group">
            <label>Roblox Linki *</label>
            <input type="url" id="addGameLink" class="form-input" placeholder="https://www.roblox.com/games/..." required />
          </div>

          <div class="form-group">
            <label>Oyun Resmi URL (Opsiyonel)</label>
            <input type="url" id="addGameImage" class="form-input" placeholder="https://..." oninput="previewAddGameImage(this.value)" />
            <img id="addGameImagePreview" style="max-height: 140px; border-radius: 12px; margin-top: 6px; display: none; object-fit: cover;" />
          </div>

          <div class="form-group">
            <label>Açıklama</label>
            <textarea id="addGameDesc" class="form-textarea" placeholder="Oyun hakkında kısa bir bilgi..."></textarea>
          </div>

          <button type="submit" class="btn btn-green" style="margin-top: 8px;">
            <i class="fa-solid fa-gamepad"></i> <span>Oyunu Ekle! (+20 Coin)</span>
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- Admin Panel Modal -->
  <div class="modal-overlay" id="adminModal">
    <div class="modal-container modal-lg">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-wrench" style="color: #ef4444;"></i> Admin Yönetim Paneli</h3>
        <button class="modal-close-btn" onclick="closeModal('adminModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <!-- Stats -->
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px;">
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Toplam Script</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="adminStatScripts">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Toplam Kullanıcı</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="adminStatUsers">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Toplam Oyun</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="adminStatGames">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Toplam Yorum</span>
            <h4 style="font-size: 18px; font-weight: 800;" id="adminStatComments">0</h4>
          </div>
          <div style="background: var(--bg-card); padding: 12px; border-radius: 16px; text-align: center; border: 1px solid var(--border-color);">
            <span style="font-size: 11px; color: var(--text-muted);">Toplam Rapor</span>
            <h4 style="font-size: 18px; font-weight: 800; color: #ef4444;" id="adminStatReports">0</h4>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
          <h4 style="font-size: 15px; font-weight: 700;">Script Yönetimi</h4>
          <button class="btn btn-outline btn-sm" onclick="resetAdminPremiumOverrides()">
            <i class="fa-solid fa-rotate-left"></i> Premium Sıfırla
          </button>
        </div>

        <div style="max-height: 350px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: 16px;">
          <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
            <thead>
              <tr style="border-bottom: 1px solid var(--border-color); text-align: left; background: rgba(0,0,0,0.2);">
                <th style="padding: 10px 14px;">Script</th>
                <th style="padding: 10px 14px;">Kategori</th>
                <th style="padding: 10px 14px;">Fiyat</th>
                <th style="padding: 10px 14px;">İşlemler</th>
              </tr>
            </thead>
            <tbody id="adminScriptTableBody">
              <!-- Injected by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Leaderboard Modal -->
  <div class="modal-overlay" id="leaderboardModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-trophy" style="color: var(--gold);"></i> Liderlik Tablosu</h3>
        <button class="modal-close-btn" onclick="closeModal('leaderboardModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div class="tab-nav">
          <button class="tab-btn active" onclick="switchLeaderboardTab('coins')" id="lbCoinsBtn">🪙 Coin</button>
          <button class="tab-btn" onclick="switchLeaderboardTab('scripts')" id="lbScriptsBtn">📜 Script</button>
          <button class="tab-btn" onclick="switchLeaderboardTab('ratings')" id="lbRatingsBtn">⭐ Puan</button>
          <button class="tab-btn" onclick="switchLeaderboardTab('comments')" id="lbCommentsBtn">💬 Yorum</button>
        </div>

        <div id="leaderboardList" style="display: flex; flex-direction: column; gap: 8px; max-height: 400px; overflow-y: auto;">
          <!-- Injected by JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- Report Modal -->
  <div class="modal-overlay" id="reportModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-triangle-exclamation" style="color: #ef4444;"></i> Script Raporla</h3>
        <button class="modal-close-btn" onclick="closeModal('reportModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <p style="font-size: 13px; color: var(--text-secondary);" id="reportScriptTargetName">Script Adı</p>
        <div class="form-group">
          <label>Rapor Nedeni *</label>
          <select id="reportReasonSelect" class="form-select">
            <option value="broken">Script çalışmıyor / bozuk</option>
            <option value="virus">Zararlı yazılım / şüpheli link</option>
            <option value="fake">Sahte başlık / yanıltıcı açıklama</option>
            <option value="inappropriate">Uygunsuz içerik</option>
            <option value="other">Diğer</option>
          </select>
        </div>
        <div class="form-group">
          <label>Ek Açıklama (Opsiyonel)</label>
          <textarea id="reportNotes" class="form-textarea" placeholder="Lütfen detay verin..."></textarea>
        </div>
        <div style="display: flex; justify-content: flex-end; gap: 10px;">
          <button class="btn btn-outline" onclick="closeModal('reportModal')">İptal</button>
          <button class="btn btn-primary" style="background: #ef4444;" onclick="submitScriptReport()">Raporu Gönder</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Privacy Policy Modal -->
  <div class="modal-overlay" id="privacyModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-shield-halved"></i> Gizlilik Politikası</h3>
        <button class="modal-close-btn" onclick="closeModal('privacyModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body" style="font-size: 13px; line-height: 1.6; color: var(--text-secondary);">
        <h4 style="color: var(--text-primary); margin-bottom: 4px;">1. Bilgi Toplama</h4>
        <p>ScriptHub, kullanıcı hesap doğrulaması, coin bakiyesi ve script etkileşimleri için gerekli olan asgari bilgileri (e-posta, kullanıcı adı, profil resmi) Firebase üzerinde saklar.</p>
        
        <h4 style="color: var(--text-primary); margin: 12px 0 4px 0;">2. Çerezler ve Yerel Depolama</h4>
        <p>Tercih edilen tema, dil ve oturum verileriniz tarayıcınızın LocalStorage belleğinde tutulur. Üçüncü şahıslarla paylaşılmaz.</p>
        
        <h4 style="color: var(--text-primary); margin: 12px 0 4px 0;">3. Topluluk İçerikleri</h4>
        <p>Kullanıcılar tarafından paylaşılan scriptler ve yorumlar herkese açık olarak listelenir. Rapor edilen sakıncalı içerikler admin onayına müteakip kaldırılır.</p>
      </div>
    </div>
  </div>

  <!-- Promo / Kupon Kodu Modal -->
  <div class="modal-overlay" id="promoCodeModal">
    <div class="modal-container">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-gift" style="color: var(--gold);"></i> Kupon / Promosyon Kodu</h3>
        <button class="modal-close-btn" onclick="closeModal('promoCodeModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <p style="font-size: 13px; color: var(--text-secondary);">Discord, YouTube veya TikTok topluluğumuzdan aldığınız kupon kodunu girerek anında ücretsiz Coin kazanın!</p>
        
        <div class="form-group" style="margin-top: 14px;">
          <label>Kupon Kodu</label>
          <div style="display: flex; gap: 8px;">
            <input type="text" id="promoCodeInput" class="form-input" placeholder="Örn: MM2ULTIMATE, DISCORD..." style="text-transform: uppercase; font-weight: 700; letter-spacing: 1px;" onkeyup="if(event.key==='Enter') submitPromoCode()" />
            <button class="btn btn-gold" onclick="submitPromoCode()" style="white-space: nowrap;">
              <i class="fa-solid fa-check"></i> Kullan
            </button>
          </div>
          <div id="promoResultMsg" style="display: none; font-size: 13px; font-weight: 700; margin-top: 8px;"></div>
        </div>

        <div class="promo-box">
          <span style="font-size: 12px; font-weight: 700; color: var(--gold); display: block; margin-bottom: 6px;">
            <i class="fa-solid fa-sparkles"></i> Popüler Aktif Kodlar (Tıkla Doldur):
          </span>
          <div style="display: flex; flex-wrap: wrap; gap: 6px;">
            <span class="promo-chip" onclick="document.getElementById('promoCodeInput').value='MM2ULTIMATE'; submitPromoCode();">MM2ULTIMATE (+100 🪙)</span>
            <span class="promo-chip" onclick="document.getElementById('promoCodeInput').value='DISCORD'; submitPromoCode();">DISCORD (+50 🪙)</span>
            <span class="promo-chip" onclick="document.getElementById('promoCodeInput').value='TIKTOK'; submitPromoCode();">TIKTOK (+50 🪙)</span>
            <span class="promo-chip" onclick="document.getElementById('promoCodeInput').value='YOUTUBE'; submitPromoCode();">YOUTUBE (+50 🪙)</span>
            <span class="promo-chip" onclick="document.getElementById('promoCodeInput').value='SCRIPTHUB2026'; submitPromoCode();">SCRIPTHUB2026 (+75 🪙)</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Mobile Bottom Navigation Bar -->
  <nav class="mobile-bottom-nav" id="mobileBottomNav">
    <button class="mobile-nav-item active" id="mobNav_home" onclick="switchMobileNav('home')">
      <i class="fa-solid fa-house"></i>
      <span>Ana Sayfa</span>
    </button>
    <button class="mobile-nav-item" id="mobNav_games" onclick="switchMobileNav('games')">
      <i class="fa-solid fa-gamepad"></i>
      <span>Oyunlar</span>
    </button>
    <button class="mobile-nav-item" id="mobNav_tasks" onclick="switchMobileNav('tasks')">
      <i class="fa-solid fa-bullseye"></i>
      <span>Görevler</span>
    </button>
    <button class="mobile-nav-item" id="mobNav_promo" onclick="switchMobileNav('promo')">
      <i class="fa-solid fa-gift" style="color: var(--gold);"></i>
      <span>Kupon</span>
    </button>
    <button class="mobile-nav-item" id="mobNav_profile" onclick="switchMobileNav('profile')">
      <i class="fa-solid fa-user"></i>
      <span>Profil</span>
    </button>
  </nav>


  <!-- Detailed Guide & Tutorial Modal -->
  <div class="modal-overlay" id="guideModal">
    <div class="modal-container modal-lg">
      <div class="modal-header">
        <h3 class="modal-title"><i class="fa-solid fa-book-open" style="color: var(--accent-light);"></i> ScriptHub Kullanım Rehberi</h3>
        <button class="modal-close-btn" onclick="closeModal('guideModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <!-- Tabs -->
        <div class="tab-nav">
          <button class="tab-btn active" id="guideTab_howtouse_btn" onclick="switchGuideTab('howtouse')">
            <i class="fa-solid fa-play"></i> Nasıl Kullanılır?
          </button>
          <button class="tab-btn" id="guideTab_executors_btn" onclick="switchGuideTab('executors')">
            <i class="fa-solid fa-microchip"></i> Executor Nedir?
          </button>
          <button class="tab-btn" id="guideTab_coins_btn" onclick="switchGuideTab('coins')">
            <i class="fa-solid fa-coins"></i> Coin Kazanma
          </button>
          <button class="tab-btn" id="guideTab_safety_btn" onclick="switchGuideTab('safety')">
            <i class="fa-solid fa-shield-halved"></i> Ban & Güvenlik
          </button>
          <button class="tab-btn" id="guideTab_faq_btn" onclick="switchGuideTab('faq')">
            <i class="fa-solid fa-circle-question"></i> SSS
          </button>
        </div>

        <!-- Tab 1: How to Use -->
        <div id="guideTab_howtouse" class="guide-tab-content">
          <div class="guide-step-card">
            <div class="guide-step-num">1</div>
            <div class="guide-step-content">
              <h4>Bir Executor Edinin</h4>
              <p>Roblox üzerinde script çalıştırmak için bir Executor programına ihtiyacınız vardır. Mobil için <b>Delta</b> veya <b>Hydrogen</b>; PC için <b>Wave</b> veya <b>Solara</b> önerilir.</p>
            </div>
          </div>
          <div class="guide-step-card">
            <div class="guide-step-num">2</div>
            <div class="guide-step-content">
              <h4>ScriptHub'dan Scriptinizi Seçin & Açın</h4>
              <p>Oynamak istediğiniz oyunu (Örn: MM2, Blox Fruits) kategorilerden seçin. Script kartındaki <b>GET</b> butonuna basarak Coin bakiyenizle veya 3 sponsor adımıyla (Discord, YouTube, TikTok) script kodunu açın.</p>
            </div>
          </div>
          <div class="guide-step-card">
            <div class="guide-step-num">3</div>
            <div class="guide-step-content">
              <h4>Kodu Kopyalayın ve Oyuna Aktarın</h4>
              <p>Açılan pencerede <code>Kopyala</code> butonuna tıklayın. Kod panonuza kaydedilir. Roblox'a girin, executor penceresine yapıştırın ve <b>Execute</b> (Çalıştır) butonuna basın. Menü oyun ekranında açılacaktır!</p>
            </div>
          </div>
          <div class="tip-box">
            <i class="fa-solid fa-lightbulb" style="color: var(--gold); font-size: 18px;"></i>
            <span><b>İpucu:</b> Script kodları <code>loadstring()</code> formatındadır ve cihazınıza hiçbir dosya indirmez; tamamen tarayıcı üzerinden hafızada çalışır.</span>
          </div>
        </div>

        <!-- Tab 2: Executors -->
        <div id="guideTab_executors" class="guide-tab-content" style="display: none;">
          <h4 style="font-size: 15px; font-weight: 700; margin-bottom: 12px;">Desteklenen Popüler Executorlar</h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-bottom: 14px;">
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-color); border-radius: 14px; padding: 14px;">
              <h5 style="color: #10b981; font-weight: 800; font-size: 14px; margin-bottom: 4px;">Delta (Mobil / Android & iOS)</h5>
              <p style="font-size: 12px; color: var(--text-secondary);">Mobil kullanıcılar için en popüler ve stabil çalışan executor. Key sistemi hızlıdır.</p>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-color); border-radius: 14px; padding: 14px;">
              <h5 style="color: #38bdf8; font-weight: 800; font-size: 14px; margin-bottom: 4px;">Wave (PC / Windows)</h5>
              <p style="font-size: 12px; color: var(--text-secondary);">Yüksek UNC desteği ile en karmaşık Murder Mystery 2 ve Blox Fruits scriptlerini dahi hatasız çalıştırır.</p>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-color); border-radius: 14px; padding: 14px;">
              <h5 style="color: #fbbf24; font-weight: 800; font-size: 14px; margin-bottom: 4px;">Solara (PC / Windows)</h5>
              <p style="font-size: 12px; color: var(--text-secondary);">Key gerektirmeyen hafif yapılı PC executor. Temel esp, aimbot ve coin farm scriptleriyle tam uyumlu.</p>
            </div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-color); border-radius: 14px; padding: 14px;">
              <h5 style="color: #c084fc; font-weight: 800; font-size: 14px; margin-bottom: 4px;">Hydrogen & Codex (Mobil)</h5>
              <p style="font-size: 12px; color: var(--text-secondary);">Android telefon ve tabletlerde yüksek FPS ile çalışan alternatif mobil motorlar.</p>
            </div>
          </div>
        </div>

        <!-- Tab 3: Coins -->
        <div id="guideTab_coins" class="guide-tab-content" style="display: none;">
          <h4 style="font-size: 15px; font-weight: 700; margin-bottom: 10px;">Ücretsiz Coin Toplama Taktikleri</h4>
          <div class="guide-step-card">
            <div class="guide-step-num"><i class="fa-solid fa-bullseye"></i></div>
            <div class="guide-step-content">
              <h4>Günlük Görevler (Günde 8 Görev)</h4>
              <p>Her gün sayfayı ziyaret et, scriptleri incele, favorilere ekle veya yorum yap. Günde 80+ Coin kazanabilirsin!</p>
            </div>
          </div>
          <div class="guide-step-card">
            <div class="guide-step-num"><i class="fa-solid fa-gift"></i></div>
            <div class="guide-step-content">
              <h4>Promosyon / Kupon Kodları</h4>
              <p>Üst bardaki <b>Kupon</b> butonuna tıkla. <code>MM2ULTIMATE</code> yazarak anında <b>+100 Coin</b>, <code>DISCORD</code> ile <b>+50 Coin</b> kazan!</p>
            </div>
          </div>
          <div class="guide-step-card">
            <div class="guide-step-num"><i class="fa-solid fa-thumbs-up"></i></div>
            <div class="guide-step-content">
              <h4>Topluluk Oylaması</h4>
              <p>Denediğin scriptlerin altındaki "Çalışıyor" veya "Patched" butonlarına oy vererek her seferinde <b>+2 Coin</b> kazan!</p>
            </div>
          </div>
        </div>

        <!-- Tab 4: Safety & Ban -->
        <div id="guideTab_safety" class="guide-tab-content" style="display: none;">
          <div class="warning-box">
            <i class="fa-solid fa-triangle-exclamation" style="color: #ef4444; font-size: 20px;"></i>
            <span><b>Önemli Güvenlik Kuralı:</b> Roblox kuralları gereği hile kullanımı hesap yaptırımı getirebilir. Değerli eşyalarınızın olduğu ana hesabınız yerine daima alternatif (yan) hesap kullanmanız önerilir.</span>
          </div>
          <div class="guide-step-card">
            <div class="guide-step-num">1</div>
            <div class="guide-step-content">
              <h4>Doğrulanmış Scriptler (No Virus / No Keylog)</h4>
              <p>ScriptHub'da listelenen tüm scriptler GitHub üzerindeki açık kaynaklı repolardan çekilir. Asla şüpheli dosya veya <code>.exe</code> indirtmeyiz.</p>
            </div>
          </div>
          <div class="guide-step-card">
            <div class="guide-step-num">2</div>
            <div class="guide-step-content">
              <h4>Hileleri Belli Etmeden Kullanın (Legit Play)</h4>
              <p>Murder Mystery 2 veya Blox Fruits oynarken otomatik vuruş (aimbot) veya ışınlanma özelliklerini diğer oyuncuları rahatsız edecek düzeyde abartmayın.</p>
            </div>
          </div>
        </div>

        <!-- Tab 5: FAQ -->
        <div id="guideTab_faq" class="guide-tab-content" style="display: none;">
          <div class="faq-item" onclick="toggleFaq('faq1')">
            <div class="faq-question">
              <span>Script bende çalışmıyor, ne yapmalıyım?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer" id="faq1">
              Roblox haftalık güncellemelerinde bazı scriptler bozulabilir. Script kartındaki "Çalışıyor / Patched" durumunu kontrol edin. Eğer patched görünüyorsa listedeki diğer alternatif scriptleri deneyin.
            </div>
          </div>

          <div class="faq-item" onclick="toggleFaq('faq2')">
            <div class="faq-question">
              <span>Executor "Attach / Inject" olmuyor, sebebi nedir?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer" id="faq2">
              Windows Defender veya antivirüs yazılımınız executor DLL dosyasını engelliyor olabilir. Defender ayarlarına girerek executor klasörünü 'Dışlananlar' (Exclusions) listesine ekleyin.
            </div>
          </div>

          <div class="faq-item" onclick="toggleFaq('faq3')">
            <div class="faq-question">
              <span>Coin bakiyem silinir mi?</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer" id="faq3">
              Hesabınıza giriş yaptığınızda coinleriniz ve açtığınız scriptler bulut üzerinde güvenle saklanır. Misafir girişte ise tarayıcı çerezlerinizde tutulur.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


  <!-- Mobile Action Drawer / Sheet Modal -->
  <div class="modal-overlay" id="mobileDrawerModal">
    <div class="modal-container mobile-drawer-sheet">
      <div class="modal-header">
        <h3 class="modal-title">
          <i class="fa-solid fa-compass" style="color: var(--accent-light);"></i>
          <span>ScriptHub Menü</span>
        </h3>
        <button class="modal-close-btn" onclick="closeModal('mobileDrawerModal')" title="Kapat">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div class="modal-body">
        <!-- User Account Card -->
        <div class="drawer-user-card" onclick="closeModal('mobileDrawerModal'); handleAuthOrProfileClick();">
          <div class="drawer-user-avatar">
            <i class="fa-solid fa-user"></i>
          </div>
          <div class="drawer-user-info">
            <h4 id="drawerUserName">Misafir Kullanıcı</h4>
            <span id="drawerUserStatus">50 Coin • Giriş yap veya profilini gör</span>
          </div>
          <button class="btn btn-outline btn-sm" id="drawerAuthActionBtn">Giriş</button>
        </div>

        <!-- Quick Actions Grid -->
        <div class="drawer-section-title">Hızlı İşlemler</div>
        <div class="drawer-grid">
          <button class="drawer-btn" onclick="closeModal('mobileDrawerModal'); openAddScriptModal();">
            <i class="fa-solid fa-code" style="color: var(--accent-light);"></i>
            <span>Script Ekle</span>
          </button>
          <button class="drawer-btn" onclick="closeModal('mobileDrawerModal'); openAddGameModal();">
            <i class="fa-solid fa-gamepad" style="color: var(--green);"></i>
            <span>Oyun Ekle</span>
          </button>
          <button class="drawer-btn" onclick="closeModal('mobileDrawerModal'); openCoinStoreModal('scripts');">
            <i class="fa-solid fa-store" style="color: #38bdf8;"></i>
            <span>Mağaza</span>
          </button>
          <button class="drawer-btn" onclick="closeModal('mobileDrawerModal'); openCoinStoreModal('inventory');">
            <i class="fa-solid fa-box-open" style="color: var(--gold);"></i>
            <span>Koleksiyon</span>
          </button>
          <button class="drawer-btn" onclick="closeModal('mobileDrawerModal'); openPromoCodeModal();">
            <i class="fa-solid fa-gift" style="color: #f43f5e;"></i>
            <span>Kupon Kodu</span>
          </button>
          <button class="drawer-btn" onclick="closeModal('mobileDrawerModal'); openLeaderboardModal();">
            <i class="fa-solid fa-trophy" style="color: var(--gold);"></i>
            <span>Liderlik</span>
          </button>
        </div>

        <!-- Preferences / Settings -->
        <div class="drawer-section-title">Ayarlar & Tercihler</div>
        <div class="drawer-settings-list">
          <div class="drawer-setting-row">
            <div class="drawer-setting-label">
              <i class="fa-solid fa-palette"></i>
              <span>Renk Teması</span>
            </div>
            <div class="theme-picker" style="display: flex;">
              <div class="theme-dot dot-dark" onclick="switchTheme('dark')" title="Dark"></div>
              <div class="theme-dot dot-light" onclick="switchTheme('light')" title="Light"></div>
              <div class="theme-dot dot-blue" onclick="switchTheme('blue')" title="Blue"></div>
              <div class="theme-dot dot-green" onclick="switchTheme('green')" title="Green"></div>
            </div>
          </div>
          <div class="drawer-setting-row">
            <div class="drawer-setting-label">
              <i class="fa-solid fa-volume-high"></i>
              <span>Ses Efektleri</span>
            </div>
            <button class="btn btn-outline btn-sm" onclick="toggleSound()" id="drawerSoundBtn">
              <span id="drawerSoundText">Açık</span>
            </button>
          </div>
          <div class="drawer-setting-row">
            <div class="drawer-setting-label">
              <i class="fa-solid fa-language"></i>
              <span>Dil (Language)</span>
            </div>
            <button class="btn btn-outline btn-sm" onclick="toggleLanguage()" id="drawerLangBtn">
              <span id="drawerLangText">Türkçe (TR)</span>
            </button>
          </div>
          <div class="drawer-setting-row">
            <div class="drawer-setting-label">
              <i class="fa-solid fa-floppy-disk"></i>
              <span>Veri Yedekleme</span>
            </div>
            <button class="btn btn-outline btn-sm" onclick="exportDataBackup()">JSON İndir</button>
          </div>
        </div>

        <!-- Social Community Links -->
        <div class="drawer-section-title">Topluluk & Sosyal Medya</div>
        <div class="drawer-socials">
          <a href="https://discord.gg/Bpn6bYFHsm" target="_blank" rel="noopener noreferrer" class="btn btn-social-discord">
            <i class="fa-brands fa-discord"></i>
            <span>Discord Sunucumuza Katıl</span>
          </a>
          <a href="https://youtube.com/@mm2_ultimatehub" target="_blank" rel="noopener noreferrer" class="btn btn-social-youtube">
            <i class="fa-brands fa-youtube"></i>
            <span>YouTube Kanalımız</span>
          </a>
          <a href="https://www.tiktok.com/@mm2_ultimatehub" target="_blank" rel="noopener noreferrer" class="btn btn-social-tiktok">
            <i class="fa-brands fa-tiktok"></i>
            <span>TikTok Sayfamız</span>
          </a>
        </div>
      </div>
    </div>
  </div>
"""

if __name__ == "__main__":
    print(f"HTML module generated, length: {len(get_html())}")
