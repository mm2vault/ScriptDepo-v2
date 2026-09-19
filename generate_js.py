#!/usr/bin/env python3

def get_js():
    return """
// ==================== CONFIG & CONSTANTS ====================
const ADMIN_EMAILS = ['mm2ultimatehub@gmail.com', 'admin@scripthub.com'];
const ADMIN_UID = 'WAtZhXqj2KUEib0RaRXMTOAgYpc2';

function isUserAdmin(user = currentUser) {
  if (!user) return false;
  if (user.uid && user.uid === ADMIN_UID) return true;
  if (user.email && ADMIN_EMAILS.some(e => e.toLowerCase() === (user.email || '').toLowerCase())) return true;
  return false;
}
const MM2_IMAGE = 'https://i.postimg.cc/rFhbs0Xg/images.jpg';

// Official Social Community Accounts
const SOCIAL_LINKS = {
  discord: 'https://discord.gg/Bpn6bYFHsm',
  youtube: 'https://youtube.com/@mm2_ultimatehub',
  tiktok: 'https://www.tiktok.com/@mm2_ultimatehub'
};

// Available Promo Codes
const PROMO_CODES = {
  'MM2ULTIMATE': { coins: 100, desc: 'MM2 Ultimate Özel Kodu' },
  'DISCORD': { coins: 50, desc: 'Discord Topluluk Bonusu' },
  'TIKTOK': { coins: 50, desc: 'TikTok Takipçi Bonusu' },
  'YOUTUBE': { coins: 50, desc: 'YouTube Abone Hediyesi' },
  'SCRIPTHUB2026': { coins: 75, desc: 'Yeni Sezon Kuponu' }
};

// ==================== WEB AUDIO SFX SYNTHESIZER ====================
let audioCtx = null;
let soundEnabled = localStorage.getItem('scriptHubSound') !== 'false';

function initAudioContext() {
  if (!audioCtx && (window.AudioContext || window.webkitAudioContext)) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function toggleSound() {
  soundEnabled = !soundEnabled;
  localStorage.setItem('scriptHubSound', soundEnabled ? 'true' : 'false');
  updateSoundIcon();
  if (soundEnabled) {
    playCoinSound();
    showToast("Ses efektleri açıldı!", "fa-volume-high", "green");
  } else {
    showToast("Sesler kapatıldı.", "fa-volume-xmark");
  }
}

function updateSoundIcon() {
  const icon = document.getElementById('soundToggleIcon');
  if (icon) {
    icon.className = soundEnabled ? "fa-solid fa-volume-high" : "fa-solid fa-volume-xmark";
    icon.style.color = soundEnabled ? "var(--accent-light)" : "var(--text-muted)";
  }
}

function playCoinSound() {
  if (!soundEnabled) return;
  try {
    initAudioContext();
    if (!audioCtx) return;
    if (audioCtx.state === 'suspended') audioCtx.resume();

    const osc1 = audioCtx.createOscillator();
    const osc2 = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc1.type = 'sine';
    osc2.type = 'triangle';

    const now = audioCtx.currentTime;
    osc1.frequency.setValueAtTime(987.77, now); // B5
    osc1.frequency.setValueAtTime(1318.51, now + 0.08); // E6

    osc2.frequency.setValueAtTime(493.88, now);
    osc2.frequency.setValueAtTime(659.25, now + 0.08);

    gain.gain.setValueAtTime(0.18, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);

    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(audioCtx.destination);

    osc1.start(now);
    osc2.start(now);
    osc1.stop(now + 0.3);
    osc2.stop(now + 0.3);
  } catch (e) {}
}

function playSuccessSound() {
  if (!soundEnabled) return;
  try {
    initAudioContext();
    if (!audioCtx) return;
    if (audioCtx.state === 'suspended') audioCtx.resume();

    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    notes.forEach((freq, idx) => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      const startTime = audioCtx.currentTime + idx * 0.07;
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, startTime);
      gain.gain.setValueAtTime(0.15, startTime);
      gain.gain.exponentialRampToValueAtTime(0.001, startTime + 0.2);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(startTime);
      osc.stop(startTime + 0.2);
    });
  } catch (e) {}
}

function playCopySound() {
  if (!soundEnabled) return;
  try {
    initAudioContext();
    if (!audioCtx) return;
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const now = audioCtx.currentTime;
    // Pleasant ascending harmonic chime (A5 880Hz -> E6 1320Hz)
    [ { freq: 880, time: 0 }, { freq: 1320, time: 0.07 } ].forEach(tone => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(tone.freq, now + tone.time);
      gain.gain.setValueAtTime(0.12, now + tone.time);
      gain.gain.exponentialRampToValueAtTime(0.001, now + tone.time + 0.22);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(now + tone.time);
      osc.stop(now + tone.time + 0.22);
    });
  } catch (e) {}
}

function playClickSound() {
  if (!soundEnabled) return;
  try {
    initAudioContext();
    if (!audioCtx) return;
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const now = audioCtx.currentTime;
    osc.type = 'sine';
    osc.frequency.setValueAtTime(450, now);
    osc.frequency.exponentialRampToValueAtTime(120, now + 0.04);
    gain.gain.setValueAtTime(0.07, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.04);
  } catch (e) {}
}

function playErrorSound() {
  if (!soundEnabled) return;
  try {
    initAudioContext();
    if (!audioCtx) return;
    if (audioCtx.state === 'suspended') audioCtx.resume();

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const now = audioCtx.currentTime;
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(220, now);
    osc.frequency.setValueAtTime(140, now + 0.1);
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.25);
  } catch (e) {}
}

const CATEGORY_IMAGES = {
  mm2: 'https://i.postimg.cc/rFhbs0Xg/images.jpg',
  bloxfruits: 'https://i.postimg.cc/jScztNGG/no-Filter.jpg',
  petsim: 'https://i.postimg.cc/28fvW2mz/PS99Icon.webp',
  dahood: 'https://i.postimg.cc/s28GgJwX/no-Filter.webp',
  bladeball: 'https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp',
  brookhaven: 'https://i.postimg.cc/yYdKLz7P/no-Filter-(2).webp',
  rivals: 'https://i.postimg.cc/jScztNGG/no-Filter.jpg',
  fisch: 'https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png',
  doors: 'https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png',
  arsenal: 'https://i.postimg.cc/rFhbs0Xg/images.jpg',
  kinglegacy: 'https://i.postimg.cc/jScztNGG/no-Filter.jpg',
  bedwars: 'https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp',
  slapbattles: 'https://i.postimg.cc/s28GgJwX/no-Filter.webp',
  other: 'https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png'
};

const DEFAULT_SCRIPT_IMAGE = 'https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png';


// ==================== RBLXSCRIPTS EXECUTORS DATABASE ====================
const EXECUTORS_DATA = [
  {
    id: "solara",
    name: "Solara Executor",
    type: "PC (Windows 10/11)",
    platforms: ["windows"],
    badge: "Keyless / Hızlı",
    status: "Undetected & Çalışıyor",
    isWorking: true,
    unc: "68% UNC",
    level: "Level 3",
    version: "v3.1.5",
    downloadUrl: "https://solaraexecutor.org/",
    shortDesc: "Windows 10 ve 11 için tamamen Keyless (anahtarsız), anında çalışan ve hafif executor.",
    steps: [
      "1. Solara zip dosyasını resmi adresinden indirin.",
      "2. Windows Defender dışlamalarına Solara klasörünü ekleyin.",
      "3. Roblox oyununu açıp Solara.exe uygulamasını çalıştırın.",
      "4. ScriptHub'dan kopyaladığınız scripti yapıştırıp 'Inject' ve 'Execute' butonuna basın."
    ],
    features: ["Keyless (Key İstemez)", "Hızlı Enjeksiyon", "Hafif & CPU Dostu", "Otomatik Güncelleme", "MM2 & Blox Fruits Uyumlu"],
    icon: "fa-solid fa-bolt",
    iconColor: "#38bdf8"
  },
  {
    id: "delta",
    name: "Delta Executor",
    type: "Android & PC (Emulator)",
    platforms: ["android", "windows"],
    badge: "En Popüler Mobil",
    status: "%100 Çalışıyor",
    isWorking: true,
    unc: "99% UNC",
    level: "Level 8",
    version: "v2.648",
    downloadUrl: "https://delta-executor.com/",
    shortDesc: "Android telefonlar ve emülatörler için en stabil, yüksek UNC skorlu ve popüler executor.",
    steps: [
      "1. Delta APK dosyasını Android cihazınıza indirin.",
      "2. İndirilen APK dosyasını kurun ve Roblox'a giriş yapın.",
      "3. Delta simgesine tıklayıp key adımını tamamlayın.",
      "4. ScriptHub script kodunu ekleyip 'Execute' butonuna basın."
    ],
    features: ["Android APK & Emülatör", "Oyun İçi Floating UI", "%99 UNC Skoru", "Düşük Gecikme", "Tüm Hub Scriptleri Uyumlu"],
    icon: "fa-solid fa-mobile-screen-button",
    iconColor: "#10b981"
  },
  {
    id: "wave",
    name: "Wave Executor",
    type: "PC (Windows 10/11)",
    platforms: ["windows"],
    badge: "Yüksek Performans",
    status: "Undetected",
    isWorking: true,
    unc: "99% UNC",
    level: "Level 8",
    version: "v1.4.2",
    downloadUrl: "https://getwave.gg/",
    shortDesc: "PC kullanıcıları için gelişmiş LuaU derleyicisi, decompiler ve yüksek UNC skorlu profesyonel araç.",
    steps: [
      "1. Wave resmi sitesinden kurulum dosyasını indirin.",
      "2. Kurulumu yapın ve Roblox oyununa bağlanın.",
      "3. ScriptHub'dan aldığınız script kodunu yapıştırıp çalıştırın."
    ],
    features: ["LuaU Desteği", "Gelişmiş Decompiler", "Ultra Yüksek UNC", "Şık Arayüz", "Dahili Script Kütüphanesi"],
    icon: "fa-solid fa-water",
    iconColor: "#6366f1"
  },
  {
    id: "hydrogen",
    name: "Hydrogen Executor",
    type: "Android & macOS",
    platforms: ["android", "apple"],
    badge: "Mac & Mobil",
    status: "Çalışıyor",
    isWorking: true,
    unc: "96% UNC",
    level: "Level 8",
    version: "v2.1.2",
    downloadUrl: "https://hydrogen.sh/",
    shortDesc: "macOS ve Android kullanıcıları için özel optimize edilmiş, akıcı arayüze sahip executor.",
    steps: [
      "1. macOS veya Android cihazınıza uygun paketi indirin.",
      "2. Uygulamayı kurup başlatın.",
      "3. Roblox'a inject edip dilediğiniz scripti çalıştırın."
    ],
    features: ["macOS Native Destek", "Akıcı Floating Panel", "Güçlü API", "Gelişmiş Hata Ayıklama"],
    icon: "fa-solid fa-atom",
    iconColor: "#a855f7"
  },
  {
    id: "codex",
    name: "Codex Executor",
    type: "Android, iOS & PC",
    platforms: ["android", "apple", "windows"],
    badge: "Çoklu Platform",
    status: "Çalışıyor",
    isWorking: true,
    unc: "96% UNC",
    level: "Level 8",
    version: "v2.645",
    downloadUrl: "https://codex.lol/",
    shortDesc: "iOS (Scarlet/TrollStore), Android ve PC desteğiyle her cihazda çalışan modern executor.",
    steps: [
      "1. Cihazınıza uygun olan yükleyiciyi indirin.",
      "2. Codex ile Roblox'u açın.",
      "3. Kod panelinden scriptinizi yapıştırıp 'Execute' butonuna basın."
    ],
    features: ["iOS (IPA) ve Android", "Otomatik Key Sistemi", "Yüksek FPS / 120 FPS", "Hızlı Script Yükleme"],
    icon: "fa-solid fa-code",
    iconColor: "#ec4899"
  },
  {
    id: "vegax",
    name: "Vega X Executor",
    type: "Android & PC",
    platforms: ["android", "windows"],
    badge: "Keyless / Kolay",
    status: "Çalışıyor",
    isWorking: true,
    unc: "92% UNC",
    level: "Level 7",
    version: "v2.2.0",
    downloadUrl: "https://vegax.gg/",
    shortDesc: "Düşük sistem gereksinimi, keyless mod seçeneği ve basit kullanımıyla popüler executor.",
    steps: [
      "1. Vega X APK dosyasını indirin.",
      "2. Kurulumu yapıp oyuna katılın.",
      "3. ScriptHub scriptini yapıştırıp çalıştırın."
    ],
    features: ["Keyless Seçeneği", "Hafif RAM Kullanımı", "Hızlı Yükleme", "Kullanıcı Dostu"],
    icon: "fa-solid fa-v",
    iconColor: "#f59e0b"
  }
];

const INITIAL_PREMIUM_SCRIPTS = [
  // --- BLOX FRUITS ---
  {
    id: "bf_hoho",
    name: "Hoho Hub Blox Fruits",
    category: "bloxfruits",
    desc: "En kapsamlı Blox Fruits scripti. Auto Farm Level, Sea Events (Kitsune / Leviathan), Fruit Sniper ve Race V4.",
    features: ["Auto Farm Level", "Kitsune Event", "Fruit Sniper", "Race V4", "Fast Attack"],
    executors: ["Delta", "Wave", "Solara", "Codex", "Hydrogen"],
    workingVotes: 342,
    patchedVotes: 4,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/acsu123/HOHO_HUB/main/Loading_NEW.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/jScztNGG/no-Filter.jpg",
    downloads: 18450,
    views: 46200,
    status: "active",
    version: "v4.5.1",
    userId: "system",
    userName: "HohoTeam",
    rating: 4.9,
    ratingCount: 388,
    comments: []
  },
  {
    id: "bf_redz",
    name: "Redz Hub Blox Fruits (Update 24+)",
    category: "bloxfruits",
    desc: "Mobil ve PC için süper akıcı. Otomatik sandık toplama, görev kasma, deniz yaratıkları ve kılıç ustalıkları.",
    features: ["Auto Farm Chest", "Sea 1/2/3 Farm", "Mastery Farm", "Auto Boss"],
    executors: ["Delta", "Solara", "Wave", "Hydrogen", "Codex"],
    workingVotes: 290,
    patchedVotes: 3,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/realredz/BloxFruits/main/Source.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/jScztNGG/no-Filter.jpg",
    downloads: 14200,
    views: 38900,
    status: "active",
    version: "v3.8.0",
    userId: "system",
    userName: "RedzDev",
    rating: 4.9,
    ratingCount: 295,
    comments: []
  },
  {
    id: "bf_wazure",
    name: "W-Azure Hub Blox Fruits",
    category: "bloxfruits",
    desc: "Mirage Island bulucu, Gear farm, Auto Raid ve gelişmiş ESP araçları içeren üst düzey hub.",
    features: ["Mirage Finder", "Auto Raid", "Fruit Finder ESP", "Kill Aura"],
    executors: ["Delta", "Wave", "Hydrogen", "Codex"],
    workingVotes: 215,
    patchedVotes: 5,
    code: "loadstring(game:HttpGet('https://api.luarmor.net/files/v3/loaders/3b2169cf53bc6104dabe8e19562e5cc2.lua'))()",
    isPremium: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/jScztNGG/no-Filter.jpg",
    downloads: 9800,
    views: 28400,
    status: "active",
    version: "v2.9.0",
    userId: "system",
    userName: "Azure Studio",
    rating: 4.8,
    ratingCount: 190,
    comments: []
  },

  // --- MURDER MYSTERY 2 (MM2) ---
  {
    id: "mm2_eclipse",
    name: "Eclipse Hub MM2",
    category: "mm2",
    desc: "MM2 için en popüler ve keyless hub. Otomatik coin toplama, Murderer/Sheriff ESP, Silent Aim ve X-Ray.",
    features: ["Auto Coin Farm", "Sheriff & Murderer ESP", "Silent Aim", "God Mode"],
    executors: ["Solara", "Delta", "Wave", "Codex", "Hydrogen", "Vega X"],
    workingVotes: 410,
    patchedVotes: 3,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/Ethanoj1/EclipseHub/master/Script'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/rFhbs0Xg/images.jpg",
    downloads: 22100,
    views: 58000,
    status: "active",
    version: "v5.2.0",
    userId: "system",
    userName: "EclipseTeam",
    rating: 5.0,
    ratingCount: 460,
    comments: []
  },
  {
    id: "mm2_snapsanix",
    name: "SnapSanix HUB MM2",
    category: "mm2",
    desc: "Silahı anında alma (Grab Gun), katili otomatik vurma, görünmezlik ve uçma menüsü.",
    features: ["Grab Gun Teleport", "Auto Shoot Murderer", "Invisibility", "Speed Hack"],
    executors: ["Solara", "Delta", "Wave", "Hydrogen"],
    workingVotes: 185,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/Roman34296589/SnapSanixHUB/refs/heads/main/SnapSanixHUB.lua'))()",
    isPremium: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/rFhbs0Xg/images.jpg",
    downloads: 8700,
    views: 24100,
    status: "active",
    version: "v3.1.0",
    userId: "system",
    userName: "SnapSanix",
    rating: 4.8,
    ratingCount: 162,
    comments: []
  },
  {
    id: "mm2_vynixius",
    name: "Vynixius MM2 Pro",
    category: "mm2",
    desc: "Bıçak/Silah efektleri, lobiyi temizleme (Kill All) ve otomatik kazanma paneli.",
    features: ["Kill All (Murderer)", "Custom Weapon Skins", "Anti-Fling", "ESP Boxes"],
    executors: ["Delta", "Wave", "Solara", "Codex"],
    workingVotes: 145,
    patchedVotes: 4,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/RegularVynixu/Vynixius/main/Loader.lua'))()",
    isPremium: true,
    coinPrice: 50,
    image: "https://i.postimg.cc/rFhbs0Xg/images.jpg",
    downloads: 6400,
    views: 19500,
    status: "active",
    version: "v2.0.4",
    userId: "system",
    userName: "Vynixu",
    rating: 4.7,
    ratingCount: 118,
    comments: []
  },

  // --- BLADE BALL ---
  {
    id: "bb_redz",
    name: "Redz Hub Blade Ball (Auto Parry)",
    category: "bladeball",
    desc: "%100 hatasız Auto Parry, Spam Deflect, Curve Ball desteği ve sonsuz savunma kalkanı.",
    features: ["Auto Parry 100%", "Spam Deflect", "Visual Curve", "Auto Clash"],
    executors: ["Delta", "Solara", "Wave", "Codex", "Hydrogen"],
    workingVotes: 310,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/realredz/BladeBall/main/Source.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp",
    downloads: 16800,
    views: 43200,
    status: "active",
    version: "v4.1.0",
    userId: "system",
    userName: "RedzDev",
    rating: 4.9,
    ratingCount: 320,
    comments: []
  },
  {
    id: "bb_nova",
    name: "Nova Hub Blade Ball",
    category: "bladeball",
    desc: "Top yön tahmini, otomatik zıplama savuşturması ve rakip hedef kilidi.",
    features: ["Ball Prediction", "Jump Parry", "Target Lock", "Speed Boost"],
    executors: ["Delta", "Wave", "Solara"],
    workingVotes: 160,
    patchedVotes: 3,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/Synergy-System/NovaHub/main/BladeBall.lua'))()",
    isPremium: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp",
    downloads: 7200,
    views: 21000,
    status: "active",
    version: "v2.4.0",
    userId: "system",
    userName: "NovaDev",
    rating: 4.8,
    ratingCount: 145,
    comments: []
  },

  // --- DA HOOD ---
  {
    id: "dh_swagmode",
    name: "Swagmode Da Hood GUI",
    category: "dahood",
    desc: "Da Hood için efsanevi script. Silent Aim, Auto Lock, Macro Speed, Godmode ve Para farmı.",
    features: ["Silent Aim Lock", "Macro Speed", "Godmode (Unhit)", "Auto Stomp", "Cash Farm"],
    executors: ["Solara", "Delta", "Wave", "Hydrogen", "Codex"],
    workingVotes: 280,
    patchedVotes: 4,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/Lerma101/Swagmode-Da-Hood/main/Main.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/s28GgJwX/no-Filter.webp",
    downloads: 13900,
    views: 37500,
    status: "active",
    version: "v6.0.0",
    userId: "system",
    userName: "SwagMode",
    rating: 4.9,
    ratingCount: 260,
    comments: []
  },
  {
    id: "dh_rayx",
    name: "RayX Da Hood Pro",
    category: "dahood",
    desc: "Otomatik silah satın alma, ışınlanma, anti-slow ve süper zıplama.",
    features: ["Auto Buy Weapons", "Teleports", "Anti-Slow", "Fly Hack"],
    executors: ["Solara", "Delta", "Wave"],
    workingVotes: 130,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/RayX-Development/RayX/main/DaHood.lua'))()",
    isPremium: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/s28GgJwX/no-Filter.webp",
    downloads: 5800,
    views: 16400,
    status: "active",
    version: "v3.2.0",
    userId: "system",
    userName: "RayX Team",
    rating: 4.7,
    ratingCount: 98,
    comments: []
  },

  // --- PET SIMULATOR 99 ---
  {
    id: "ps99_zap",
    name: "ZapHub Pet Simulator 99",
    category: "petsim",
    desc: "Elmas toplama (Auto Farm Diamonds), Huge Pet avcısı, otomatik yumurta açma ve bölge geçişi.",
    features: ["Auto Farm Diamonds", "Huge Pet Hunter", "Auto Hatch Eggs", "Zone Unlocker"],
    executors: ["Delta", "Wave", "Solara", "Codex", "Hydrogen"],
    workingVotes: 240,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/ZapHub-Roblox/ZapHub/main/PS99.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/28fvW2mz/PS99Icon.webp",
    downloads: 11200,
    views: 31000,
    status: "active",
    version: "v2.8.0",
    userId: "system",
    userName: "ZapHub",
    rating: 4.9,
    ratingCount: 215,
    comments: []
  },

  // --- RIVALS ---
  {
    id: "rivals_eclipse",
    name: "Eclipse Rivals Silent Aim & ESP",
    category: "rivals",
    desc: "Rivals için 100% isabetli Silent Aim, FOV çemberi, duvar arkası ESP kutuları ve sınırsız mermi.",
    features: ["Silent Aim", "ESP Box / Tracers", "Infinite Ammo", "No Recoil"],
    executors: ["Solara", "Delta", "Wave", "Codex"],
    workingVotes: 195,
    patchedVotes: 3,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/EclipseRivals/Rivals/main/Loader.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/jScztNGG/no-Filter.jpg",
    downloads: 9400,
    views: 26800,
    status: "active",
    version: "v1.9.0",
    userId: "system",
    userName: "EclipseTeam",
    rating: 4.9,
    ratingCount: 180,
    comments: []
  },

  // --- BROOKHAVEN RP ---
  {
    id: "bh_icehub",
    name: "IceHub Brookhaven (All Passes)",
    category: "brookhaven",
    desc: "Tüm gamepass'leri ücretsiz açar, gökkuşağı araba, ev eşyaları, admin komutları ve uçma.",
    features: ["Unlock All Gamepasses", "Rainbow Vehicles", "Admin GUI", "Fly / Noclip"],
    executors: ["Delta", "Solara", "Wave", "Hydrogen", "Codex", "Vega X"],
    workingVotes: 260,
    patchedVotes: 3,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/IceM4n/IceHub/main/Brookhaven.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/yYdKLz7P/no-Filter-(2).webp",
    downloads: 12500,
    views: 34000,
    status: "active",
    version: "v4.0.0",
    userId: "system",
    userName: "IceMan",
    rating: 4.8,
    ratingCount: 240,
    comments: []
  },

  // --- FISCH ---
  {
    id: "fisch_speedhub",
    name: "Speed Hub Fisch (Auto Fish & Radar)",
    category: "fisch",
    desc: "Anında balık yakalama (Instant Catch), balık radarı, otomatik satma ve adalara ışınlanma.",
    features: ["Instant Catch", "Fish Radar", "Auto Sell Fish", "Island Teleport"],
    executors: ["Delta", "Wave", "Solara", "Codex", "Hydrogen"],
    workingVotes: 210,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/SpeedHubX/Fisch/main/Loader.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png",
    downloads: 10400,
    views: 29800,
    status: "active",
    version: "v2.1.0",
    userId: "system",
    userName: "SpeedHub",
    rating: 4.9,
    ratingCount: 195,
    comments: []
  },

  // --- DOORS ---
  {
    id: "doors_omghub",
    name: "OmgHub Doors (Floor 1 & 2)",
    category: "doors",
    desc: "Canavar bildirimleri (Rush, Ambush, Screech ESP), otomatik kapı açma, anahtar bulucu ve aydınlatma.",
    features: ["Entity Notifier / ESP", "Key & Item ESP", "Auto Open Doors", "Fullbright"],
    executors: ["Delta", "Solara", "Wave", "Hydrogen"],
    workingVotes: 175,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/OmgScripts/Doors/main/OmgHub.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png",
    downloads: 8200,
    views: 22400,
    status: "active",
    version: "v3.0.0",
    userId: "system",
    userName: "OmgDev",
    rating: 4.8,
    ratingCount: 150,
    comments: []
  },

  // --- ARSENAL ---
  {
    id: "arsenal_quotas",
    name: "Quotas Hub Arsenal",
    category: "arsenal",
    desc: "Silent Aim, Kill All, Duvar Arkası Vuruş (Wallbang), Sekmeme ve Sınırsız Mermi.",
    features: ["Silent Aim", "Wallbang", "Kill All Lobby", "Infinite Ammo", "Gun Mods"],
    executors: ["Solara", "Delta", "Wave", "Codex"],
    workingVotes: 180,
    patchedVotes: 3,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/QuotasHub/Arsenal/main/Loader.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/rFhbs0Xg/images.jpg",
    downloads: 8900,
    views: 25100,
    status: "active",
    version: "v2.5.0",
    userId: "system",
    userName: "QuotasTeam",
    rating: 4.8,
    ratingCount: 165,
    comments: []
  },

  // --- KING LEGACY ---
  {
    id: "kl_zenith",
    name: "Zenith Hub King Legacy",
    category: "kinglegacy",
    desc: "Deniz canavarı kasma, otomatik stat yükseltme, meyve arayıcı ve hızlı görev tamamlama.",
    features: ["Auto Farm Level", "Sea Monster Farm", "Auto Stats", "Fruit Sniper"],
    executors: ["Delta", "Solara", "Wave", "Codex"],
    workingVotes: 140,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/ZenithHub/KingLegacy/main/Loader.lua'))()",
    isPremium: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/jScztNGG/no-Filter.jpg",
    downloads: 6700,
    views: 18200,
    status: "active",
    version: "v1.8.0",
    userId: "system",
    userName: "ZenithTeam",
    rating: 4.7,
    ratingCount: 120,
    comments: []
  },

  // --- BEDWARS ---
  {
    id: "bedwars_vape",
    name: "Vape V4 BedWars Client",
    category: "bedwars",
    desc: "KillAura, Fly, Speed, Scaffold (otomatik yol yapma) ve sandık hilesi içeren üst düzey client.",
    features: ["KillAura", "Fly / Speed", "Scaffold", "Auto Win"],
    executors: ["Delta", "Solara", "Wave"],
    workingVotes: 165,
    patchedVotes: 4,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/7GrandDadPGN/VapeV4ForRoblox/main/New经.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp",
    downloads: 8100,
    views: 23600,
    status: "active",
    version: "v4.2.0",
    userId: "system",
    userName: "VapeClient",
    rating: 4.8,
    ratingCount: 148,
    comments: []
  },

  // --- SLAP BATTLES ---
  {
    id: "sb_slapmaster",
    name: "Slap Battles Master GUI",
    category: "slapbattles",
    desc: "Otomatik tokat atma (Auto Slap), tüm eldiven kilitlerini açma simülatörü ve Godmode.",
    features: ["Auto Slap All", "Glove Unlocker", "Godmode", "Anti-Void"],
    executors: ["Delta", "Solara", "Wave", "Codex"],
    workingVotes: 135,
    patchedVotes: 2,
    code: "loadstring(game:HttpGet('https://raw.githubusercontent.com/SlapMaster/SlapBattles/main/Script.lua'))()",
    isPremium: true,
    isKeyless: true,
    coinPrice: 0,
    image: "https://i.postimg.cc/s28GgJwX/no-Filter.webp",
    downloads: 6200,
    views: 17800,
    status: "active",
    version: "v2.0.0",
    userId: "system",
    userName: "SlapTeam",
    rating: 4.7,
    ratingCount: 110,
    comments: []
  }
];

const INITIAL_GAMES = [
  {id:"bloxfruits",name:"Blox Fruits",link:"https://www.roblox.com/games/2753915549",image:"https://i.postimg.cc/jScztNGG/no-Filter.jpg",desc:"Kılıç ustası ol, meyve güçlerini uyandır, denizlerde canavarları avla.",userName:"Gamer Robot",scriptCount:18},
  {id:"mm2",name:"Murder Mystery 2",link:"https://www.roblox.com/games/142823291",image:"https://i.postimg.cc/rFhbs0Xg/images.jpg",desc:"Gizem, katil, masum ve şerif rolleri. Otomatik coin toplama ve ESP.",userName:"Nikilis",scriptCount:14},
  {id:"bladeball",name:"Blade Ball",link:"https://www.roblox.com/games/13772394625",image:"https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp",desc:"Hızlanan topu savuştur, otomatik parry ve kılıç yetenekleriyle rakipleri alt et.",userName:"Wiggity",scriptCount:12},
  {id:"dahood",name:"Da Hood",link:"https://www.roblox.com/games/2788229376",image:"https://i.postimg.cc/s28GgJwX/no-Filter.webp",desc:"Şehirde çeteler, silahlı çatışmalar, otomatik aimlock ve para toplama.",userName:"Da Hood Ent.",scriptCount:10},
  {id:"petsim",name:"Pet Simulator 99",link:"https://www.roblox.com/games/13566893764",image:"https://i.postimg.cc/28fvW2mz/PS99Icon.webp",desc:"Devasa evcil hayvanları topla, yumurtaları otomatik aç ve elmas kazan.",userName:"BIG Games",scriptCount:9},
  {id:"rivals",name:"Rivals",link:"https://www.roblox.com/games/17625359962",image:"https://i.postimg.cc/jScztNGG/no-Filter.jpg",desc:"Hızlı tempolu 1v1 ve 2v2 FPS nişancı aksiyonu. Silent aim ve ESP.",userName:"Nosniy Games",scriptCount:8},
  {id:"brookhaven",name:"Brookhaven RP",link:"https://www.roblox.com/games/4924922222",image:"https://i.postimg.cc/yYdKLz7P/no-Filter-(2).webp",desc:"Özgür rol yapma dünyası, evler, arabalar ve tüm gamepass kilitlerini açma.",userName:"Wolfpaq",scriptCount:7},
  {id:"fisch",name:"Fisch",link:"https://www.roblox.com/games/16732694052",image:"https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png",desc:"Derin deniz balıkçılığı, efsanevi balıklar, otomatik olta çekme ve ada teleport.",userName:"Wooz Studios",scriptCount:6},
  {id:"doors",name:"Doors (Floor 1 & 2)",link:"https://www.roblox.com/games/6516141723",image:"https://i.postimg.cc/d12QcRfB/Gemini-Generated-Image-q6hh2jq6hh2jq6hh.png",desc:"Korku ve bulmaca oteli. Canavar bildirimleri, anahtar ESP ve otomatik kapı.",userName:"LSPLASH",scriptCount:6},
  {id:"arsenal",name:"Arsenal",link:"https://www.roblox.com/games/286090443",image:"https://i.postimg.cc/rFhbs0Xg/images.jpg",desc:"Silah yarışları ve pvp arena aksiyonu. Silent aim, wallbang ve kill all.",userName:"ROLVe Community",scriptCount:5},
  {id:"kinglegacy",name:"King Legacy",link:"https://www.roblox.com/games/4520749081",image:"https://i.postimg.cc/jScztNGG/no-Filter.jpg",desc:"Anime dünyasında seviye kasma, deniz canavarları ve meyve güçleri.",userName:"Venture Lagoons",scriptCount:5},
  {id:"bedwars",name:"BedWars",link:"https://www.roblox.com/games/6872265039",image:"https://i.postimg.cc/gkDwZpNw/no-Filter-(1).webp",desc:"Yatakları koru, killaura ve otomatik blok yerleştirme ile zafere ulaş.",userName:"Easy.gg",scriptCount:4},
  {id:"slapbattles",name:"Slap Battles",link:"https://www.roblox.com/games/6403373529",image:"https://i.postimg.cc/s28GgJwX/no-Filter.webp",desc:"Özel güçlere sahip eldivenlerle rakipleri uçur. Otomatik tokat ve godmode.",userName:"Tencell",scriptCount:4}
];

const COSMETICS_LIST = [
  {id:"c_gold_frame",name:"Altın Çerçeve",nameEn:"Gold Frame",price:150,type:"frame",desc:"Profil avatarınızın etrafında ışıltılı altın halka.",class:"avatar-frame-gold"},
  {id:"c_rainbow_frame",name:"Premium Çerçeve",nameEn:"Premium Frame",price:200,type:"frame",desc:"Neon mor ve camgöbeği gradient çerçeve.",class:"avatar-frame-rainbow"},
  {id:"c_purple_name",name:"Mor İsim",nameEn:"Purple Name",price:100,type:"name",desc:"Kullanıcı adınız parlayan neon mor görünür.",class:"name-purple"},
  {id:"c_gold_name",name:"Altın İsim",nameEn:"Gold Name",price:200,type:"name",desc:"Kullanıcı adınız altın sarısı stil alır.",class:"name-gold"}
];

const I18N = {
  tr: {
    appTitle: "ScriptHub",
    appSubtitle: "90+ Script & Oyunlar",
    searchPlaceholder: "Script, oyun veya özellik ara...",
    signIn: "Giriş Yap",
    profile: "Profilim",
    addScript: "Script Ekle",
    addGame: "Oyun Ekle",
    dailyTasksTitle: "Günlük Görevler",
    claimAll: "Tümünü Topla",
    sortLabel: "Sırala:",
    typeLabel: "Tip:",
    ratingLabel: "Puan:",
    backup: "Yedekle",
    leaderboard: "Liderlik",
    allScripts: "Tüm Scriptler",
    allGames: "Roblox Oyunları",
    noResults: "Sonuç bulunamadı",
    noResultsDesc: "Aramanıza veya seçtiğiniz filtrelere uygun içerik bulunamadı.",
    openScript: "Scripti Aç",
    get: "GET",
    unlocked: "Açık",
    owner: "Sahibim",
    community: "Topluluk",
    premium: "Premium",
    copy: "Kopyala",
    copied: "Kopyalandı!",
    report: "Raporla"
  },
  en: {
    appTitle: "ScriptHub",
    appSubtitle: "90+ Scripts & Games",
    searchPlaceholder: "Search scripts, games, features...",
    signIn: "Sign In",
    profile: "Profile",
    addScript: "Add Script",
    addGame: "Add Game",
    dailyTasksTitle: "Daily Tasks",
    claimAll: "Claim All",
    sortLabel: "Sort:",
    typeLabel: "Type:",
    ratingLabel: "Rating:",
    backup: "Backup",
    leaderboard: "Leaderboard",
    allScripts: "All Scripts",
    allGames: "Roblox Games",
    noResults: "No results found",
    noResultsDesc: "No content matching your search or filters was found.",
    openScript: "Unlock Script",
    get: "GET",
    unlocked: "Unlocked",
    owner: "Owner",
    community: "Community",
    premium: "Premium",
    copy: "Copy",
    copied: "Copied!",
    report: "Report"
  }
};

// ==================== STATE MANAGEMENT ====================
let currentUser = null;
let userProfile = {
  coins: 50,
  totalCoinsEarned: 50,
  purchasedScripts: [],
  inventory: [],
  activeCosmetics: [],
  dailyTasks: {},
  dailyTaskStats: { viewedScripts: 0, commentsCount: 0, favsCount: 0, addedScripts: 0, addedGames: 0, likesCount: 0, visitedCategories: [] },
  favorites: [],
  displayName: "Misafir Oyuncu",
  email: "",
  photoURL: "https://api.dicebear.com/7.x/bottts/svg?seed=RobloxPro",
  createdAt: new Date().toISOString()
};

let scriptsData = [];
let gamesData = [];
let reportsData = [];
let appNotifications = [];
let currentLang = localStorage.getItem('scriptHubLang') || 'tr';
let currentTheme = localStorage.getItem('scriptHubTheme') || 'dark';
let activeCategory = 'all';
let activeQuickFilter = 'all';
let searchQuery = '';
let searchDebounceTimeout = null;
let currentPage = 1;
const ITEMS_PER_PAGE = 20;
let selectedScriptForUnlock = null;
let taskCountdownInterval = null;
let currentTaskStep = 0;
let taskStepsDone = [false, false, false];

// Firebase References
let db = null;
let auth = null;
let supabaseClient = null;

// ==================== INIT FIREBASE ====================
function initFirebase() {
  const firebaseConfig = {
    apiKey: "AIzaSyBtPMr5FMRm6uNLSM3prXwqsyE0KihlWvY",
    authDomain: "scripthub-77a51.firebaseapp.com",
    projectId: "scripthub-77a51",
    storageBucket: "scripthub-77a51.firebasestorage.app",
    messagingSenderId: "104478963564",
    appId: "1:104478963564:web:da8ad1c2820cf781016549",
    measurementId: "G-RK45YY0RKC"
  };

  try {
    if (typeof firebase !== 'undefined' && !firebase.apps.length) firebase.initializeApp(firebaseConfig);
    if (typeof firebase !== 'undefined') {
      db = firebase.firestore();
      try { db.enablePersistence({ synchronizeTabs: true }).catch(() => {}); } catch (e) {}
    }
  } catch (err) {
    console.warn("Firebase data services notice:", err);
  }
}

function initSupabase() {
  try {
    if (!window.supabase || supabaseClient) return;
    supabaseClient = window.supabase.createClient(
      'https://jjwqdvjtcorzpvxlfnog.supabase.co',
      'sb_publishable_J4NQfjyOIj_sMUA53iSnVA_inPdNLZ7',
      { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } }
    );
  } catch (err) {
    console.warn("Supabase initialize notice:", err);
  }
}

async function ensureSupabaseProfile(user, isNewUser = false) {
  if (!supabaseClient || !user) return;
  currentUser = {
    uid: user.id,
    email: user.email || '',
    displayName: user.user_metadata?.display_name || user.user_metadata?.full_name || (user.email || '').split('@')[0],
    photoURL: user.user_metadata?.avatar_url || user.user_metadata?.picture || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(user.id)}`
  };

  const { data, error } = await supabaseClient.from('profiles').select('*').eq('id', user.id).maybeSingle();
  if (error) {
    console.log("Supabase profile load notice:", error.message);
    updateUIUserInfo();
    return;
  }

  if (data) {
    userProfile = {
      ...userProfile,
      ...data.app_data,
      displayName: data.display_name || currentUser.displayName,
      email: data.email || currentUser.email,
      photoURL: data.app_data?.photoURL || currentUser.photoURL
    };
  } else {
    userProfile = {
      ...userProfile,
      coins: 50,
      totalCoinsEarned: 50,
      displayName: currentUser.displayName,
      email: currentUser.email,
      photoURL: currentUser.photoURL,
      usedPromoCodes: [],
      favorites: [],
      activeCosmetics: [],
      purchasedScripts: [],
      inventory: []
    };
    await saveUserProfile();
  }

  updateUIUserInfo();
  renderDailyTasks();
  checkHeroCollapsedState();
  renderMainGrid();
}

// ==================== LOAD LOCAL / REMOTE STATE ====================
function loadSavedData() {
  // Load local user profile backup if exists
  const savedProfile = localStorage.getItem('scriptHubUserProfile');
  if (savedProfile) {
    try {
      const parsed = JSON.parse(savedProfile);
      userProfile = { ...userProfile, ...parsed };
    } catch (e) {}
  }

  // Load scripts from cache or defaults
  const savedScripts = localStorage.getItem('scriptHubCustomScripts');
  let customScripts = [];
  if (savedScripts) {
    try {
      customScripts = JSON.parse(savedScripts);
    } catch (e) {}
  }

  // Merge premium overrides if admin modified
  const adminOverrides = localStorage.getItem('scriptHubAdminPremiumOverrides');
  let premiumPool = [...INITIAL_PREMIUM_SCRIPTS];
  if (adminOverrides) {
    try {
      premiumPool = JSON.parse(adminOverrides);
    } catch (e) {}
  }

  scriptsData = [...premiumPool, ...customScripts];

  // Games
  const savedGames = localStorage.getItem('scriptHubCustomGames');
  let customGames = [];
  if (savedGames) {
    try {
      customGames = JSON.parse(savedGames);
    } catch (e) {}
  }
  gamesData = [...INITIAL_GAMES, ...customGames];

  // Notifications
  const savedNotifs = localStorage.getItem('scriptHubNotifications');
  if (savedNotifs) {
    try {
      appNotifications = JSON.parse(savedNotifs);
    } catch (e) {
      appNotifications = [];
    }
  } else {
    appNotifications = [
      { id: "n1", type: "welcome", title: "Hoş Geldiniz!", text: "ScriptHub'a hoş geldiniz! 50 hediye coin hesabınıza tanımlandı.", time: new Date().toLocaleTimeString() }
    ];
  }

  // Check Daily Tasks date reset
  checkDailyTasksDateReset();
}

function checkDailyTasksDateReset() {
  const todayStr = new Date().toISOString().slice(0, 10);
  const lastTaskDate = localStorage.getItem('scriptHubLastTaskDate');
  if (lastTaskDate !== todayStr) {
    userProfile.dailyTasks = {
      task1: false, task2: false, task3: false, task4: false,
      task5: false, task6: false, task7: false, task8: false
    };
    userProfile.dailyTaskStats = {
      viewedScripts: 0, commentsCount: 0, favsCount: 0,
      addedScripts: 0, addedGames: 0, likesCount: 0, visitedCategories: []
    };
    localStorage.setItem('scriptHubLastTaskDate', todayStr);
    saveUserProfile();
  }
}

function saveUserProfile() {
  localStorage.setItem('scriptHubUserProfile', JSON.stringify(userProfile));
  updateUIUserInfo();

  if (currentUser && supabaseClient) {
    supabaseClient.from('profiles').upsert({
      id: currentUser.uid,
      email: userProfile.email || currentUser.email || '',
      display_name: userProfile.displayName || '',
      app_data: {
        coins: userProfile.coins || 0,
        totalCoinsEarned: userProfile.totalCoinsEarned || 0,
        purchasedScripts: userProfile.purchasedScripts || [],
        inventory: userProfile.inventory || [],
        dailyTasks: userProfile.dailyTasks || {},
        dailyTaskStats: userProfile.dailyTaskStats || {},
        usedPromoCodes: userProfile.usedPromoCodes || [],
        favorites: userProfile.favorites || [],
        activeCosmetics: userProfile.activeCosmetics || [],
        photoURL: userProfile.photoURL || ''
      },
      updated_at: new Date().toISOString()
    }, { onConflict: 'id' }).then(({ error }) => {
      if (error) console.log("Supabase profile sync notice:", error.message);
    });
  }
}

function syncFromFirestore() {
  if (!db) return;

  // Listen to scripts collection
  try {
    db.collection('scripts').limit(50).onSnapshot(snapshot => {
      const remoteScripts = [];
      snapshot.forEach(doc => {
        remoteScripts.push({ id: doc.id, ...doc.data() });
      });
      if (remoteScripts.length > 0) {
        // combine with initial premium scripts
        const nonDuplicateRemote = remoteScripts.filter(rs => !INITIAL_PREMIUM_SCRIPTS.some(p => p.id === rs.id));
        scriptsData = [...INITIAL_PREMIUM_SCRIPTS, ...nonDuplicateRemote];
        renderMainGrid();
      }
    }, err => {
      console.log("Firestore scripts snapshot notice:", err.message);
    });
  } catch (e) {}

  // Listen to games collection
  try {
    db.collection('games').limit(30).onSnapshot(snapshot => {
      const remoteGames = [];
      snapshot.forEach(doc => {
        remoteGames.push({ id: doc.id, ...doc.data() });
      });
      if (remoteGames.length > 0) {
        const nonDuplicateGames = remoteGames.filter(rg => !INITIAL_GAMES.some(g => g.id === rg.id));
        gamesData = [...INITIAL_GAMES, ...nonDuplicateGames];
        if (activeCategory === 'games') renderMainGrid();
      }
    }, err => {});
  } catch (e) {}
}

// ==================== COIN & NOTIFICATION SYSTEM ====================
function addCoins(amount, reason) {
  userProfile.coins += amount;
  userProfile.totalCoinsEarned = (userProfile.totalCoinsEarned || 0) + amount;
  saveUserProfile();
  playCoinSound();

  // Animation pulse
  const badge = document.getElementById('headerCoinBadge');
  if (badge) {
    badge.classList.remove('coin-pulse');
    void badge.offsetWidth;
    badge.classList.add('coin-pulse');
  }

  showToast(`+${amount} Coin! (${reason})`, "fa-coins", "gold");
  addNotification("coin", `Coin Kazanıldı: +${amount}`, reason);
}

function deductCoins(amount, reason) {
  if (userProfile.coins < amount) return false;
  userProfile.coins -= amount;
  saveUserProfile();
  showToast(`-${amount} Coin (${reason})`, "fa-coins", "red");
  return true;
}

function addNotification(type, title, text) {
  const notif = {
    id: "n_" + Date.now(),
    type: type,
    title: title,
    text: text,
    time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  };
  appNotifications.unshift(notif);
  if (appNotifications.length > 50) appNotifications.pop();
  localStorage.setItem('scriptHubNotifications', JSON.stringify(appNotifications));

  renderNotifications();
  const dot = document.getElementById('notifBadgeDot');
  if (dot) dot.classList.add('show');
}

function renderNotifications() {
  const list = document.getElementById('notifList');
  if (!list) return;

  if (appNotifications.length === 0) {
    list.innerHTML = `<div class="notif-empty"><i class="fa-solid fa-bell-slash" style="font-size: 24px; margin-bottom: 8px;"></i><p>Henüz bildirim yok.</p></div>`;
    return;
  }

  let html = '';
  appNotifications.forEach(n => {
    let icon = 'fa-bell';
    if (n.type === 'coin') icon = 'fa-coins';
    else if (n.type === 'task') icon = 'fa-bullseye';
    else if (n.type === 'script') icon = 'fa-file-code';
    else if (n.type === 'comment') icon = 'fa-comment';
    else if (n.type === 'welcome') icon = 'fa-sparkles';

    html += `
      <div class="notif-item">
        <i class="fa-solid ${icon}"></i>
        <div style="flex: 1;">
          <div style="display: flex; justify-content: space-between;">
            <strong style="font-size: 12px; color: var(--text-primary);">${n.title}</strong>
            <span style="font-size: 10px; color: var(--text-muted);">${n.time}</span>
          </div>
          <p style="font-size: 11px; color: var(--text-secondary); margin-top: 2px;">${n.text}</p>
        </div>
      </div>
    `;
  });
  list.innerHTML = html;
}

function toggleNotifDropdown() {
  const dropdown = document.getElementById('notifDropdown');
  const dot = document.getElementById('notifBadgeDot');
  if (dropdown) {
    dropdown.classList.toggle('active');
    if (dropdown.classList.contains('active') && dot) {
      dot.classList.remove('show');
    }
  }
}

function clearAllNotifications() {
  appNotifications = [];
  localStorage.removeItem('scriptHubNotifications');
  renderNotifications();
  const dot = document.getElementById('notifBadgeDot');
  if (dot) dot.classList.remove('show');
}

// ==================== TOAST FEEDBACK ====================
function showToast(message, icon = "fa-circle-info", color = "accent") {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  
  let iconColor = 'var(--accent-light)';
  if (color === 'gold') iconColor = 'var(--gold)';
  if (color === 'green') iconColor = 'var(--green)';
  if (color === 'red') iconColor = 'var(--red)';

  toast.innerHTML = `<i class="fa-solid ${icon}" style="color: ${iconColor}; font-size: 16px;"></i><span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(50px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ==================== THEME & LANGUAGE ====================
function switchTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('scriptHubTheme', theme);

  document.querySelectorAll('.theme-dot').forEach(dot => dot.classList.remove('active'));
  const targetDot = document.querySelector(`.dot-${theme}`);
  if (targetDot) targetDot.classList.add('active');
}

function toggleLanguage() {
  currentLang = currentLang === 'tr' ? 'en' : 'tr';
  localStorage.setItem('scriptHubLang', currentLang);
  applyTranslations();
  renderCategories();
  renderDailyTasks();
  checkHeroCollapsedState();
  renderMainGrid();
}

function applyTranslations() {
  const dict = I18N[currentLang];
  const langLabel = document.getElementById('langLabel');
  if (langLabel) langLabel.textContent = currentLang.toUpperCase();

  const title = document.getElementById('appTitle');
  if (title) title.textContent = dict.appTitle;

  const subtitle = document.getElementById('appSubtitle');
  if (subtitle) subtitle.textContent = dict.appSubtitle;

  const search = document.getElementById('searchInput');
  if (search) search.placeholder = dict.searchPlaceholder;

  const authBtnText = document.getElementById('authProfileBtnText');
  if (authBtnText && !currentUser) authBtnText.textContent = dict.signIn;

  const btnAddScript = document.getElementById('btnAddScript');
  if (btnAddScript) btnAddScript.querySelector('span').textContent = dict.addScript;

  const btnAddGame = document.getElementById('btnAddGame');
  if (btnAddGame) btnAddGame.querySelector('span').textContent = dict.addGame;

  const dailyTasksTitle = document.getElementById('dailyTasksTitle');
  if (dailyTasksTitle) dailyTasksTitle.querySelector('span').textContent = dict.dailyTasksTitle;

  const btnClaimAllTasks = document.getElementById('btnClaimAllTasks');
  if (btnClaimAllTasks) btnClaimAllTasks.querySelector('span').textContent = dict.claimAll;

  const sortLabelText = document.getElementById('sortLabelText');
  if (sortLabelText) sortLabelText.textContent = dict.sortLabel;

  const typeLabelText = document.getElementById('typeLabelText');
  if (typeLabelText) typeLabelText.textContent = dict.typeLabel;

  const ratingLabelText = document.getElementById('ratingLabelText');
  if (ratingLabelText) ratingLabelText.textContent = dict.ratingLabel;

  const btnBackupText = document.getElementById('btnBackupText');
  if (btnBackupText) btnBackupText.textContent = dict.backup;

  const btnLeaderboardText = document.getElementById('btnLeaderboardText');
  if (btnLeaderboardText) btnLeaderboardText.textContent = dict.leaderboard;

  const emptyTitle = document.getElementById('emptyTitle');
  if (emptyTitle) emptyTitle.textContent = dict.noResults;

  const emptyDesc = document.getElementById('emptyDesc');
  if (emptyDesc) emptyDesc.textContent = dict.noResultsDesc;
}

// ==================== DAILY TASKS SYSTEM ====================
const DAILY_TASKS_CONFIG = [
  { id: "task1", nameTr: "Günlük Giriş", nameEn: "Daily Login", descTr: "Giriş yapınca otomatik kazan", descEn: "Automatic on login", reward: 10, icon: "fa-door-open" },
  { id: "task2", nameTr: "3 Script Görüntüle", nameEn: "View 3 Scripts", descTr: "Detayları veya kodu aç", descEn: "Open details or code", reward: 15, icon: "fa-eye", target: 3, statKey: "viewedScripts" },
  { id: "task3", nameTr: "2 Yorum Yap", nameEn: "Post 2 Comments", descTr: "Scriptlere yorum bırak", descEn: "Leave comments on scripts", reward: 15, icon: "fa-comments", target: 2, statKey: "commentsCount" },
  { id: "task4", nameTr: "2 Favori Ekle", nameEn: "Add 2 Favorites", descTr: "Beğendiğin scriptleri kaydet", descEn: "Save scripts you like", reward: 10, icon: "fa-heart", target: 2, statKey: "favsCount" },
  { id: "task5", nameTr: "Script Ekle", nameEn: "Submit Script", descTr: "Topluluğa yeni script paylaş", descEn: "Share new script to community", reward: 25, icon: "fa-code", target: 1, statKey: "addedScripts" },
  { id: "task6", nameTr: "Oyun Ekle", nameEn: "Add Game", descTr: "Roblox oyun linki ekle", descEn: "Add Roblox game link", reward: 20, icon: "fa-gamepad", target: 1, statKey: "addedGames" },
  { id: "task7", nameTr: "3 Script Beğen", nameEn: "Like 3 Scripts", descTr: "Puan ver veya beğen", descEn: "Rate or like scripts", reward: 10, icon: "fa-thumbs-up", target: 3, statKey: "likesCount" },
  { id: "task8", nameTr: "3 Kategori Gez", nameEn: "Browse 3 Categories", descTr: "Farklı kategorilere göz at", descEn: "Browse different categories", reward: 15, icon: "fa-compass", target: 3, isCategoryCheck: true }
];

function checkTaskCompletion(taskId) {
  if (!userProfile.dailyTasks) userProfile.dailyTasks = {};
  if (userProfile.dailyTasks[taskId]) return; // already claimed

  const cfg = DAILY_TASKS_CONFIG.find(t => t.id === taskId);
  if (!cfg) return;

  let isComplete = false;
  if (taskId === "task1") {
    isComplete = true;
  } else if (cfg.isCategoryCheck) {
    const visited = userProfile.dailyTaskStats?.visitedCategories || [];
    if (visited.length >= 3) isComplete = true;
  } else {
    const currentVal = (userProfile.dailyTaskStats && userProfile.dailyTaskStats[cfg.statKey]) || 0;
    if (currentVal >= cfg.target) isComplete = true;
  }

  if (isComplete) {
    userProfile.dailyTasks[taskId] = true;
    addCoins(cfg.reward, `${cfg.nameTr} Görevi`);
    addNotification("task", "Görev Tamamlandı!", `${cfg.nameTr} tamamlandı ve +${cfg.reward} coin kazanıldı.`);
    renderDailyTasks();
  checkHeroCollapsedState();
  }
}

function recordTaskProgress(type, extraVal = 1) {
  if (!userProfile.dailyTaskStats) {
    userProfile.dailyTaskStats = { viewedScripts: 0, commentsCount: 0, favsCount: 0, addedScripts: 0, addedGames: 0, likesCount: 0, visitedCategories: [] };
  }

  if (type === 'view') {
    userProfile.dailyTaskStats.viewedScripts = (userProfile.dailyTaskStats.viewedScripts || 0) + 1;
    // Script viewing gives +1 coin max 10 times a day
    if (userProfile.dailyTaskStats.viewedScripts <= 10) {
      addCoins(1, "Script Görüntüleme");
    }
    checkTaskCompletion('task2');
  } else if (type === 'comment') {
    userProfile.dailyTaskStats.commentsCount = (userProfile.dailyTaskStats.commentsCount || 0) + 1;
    addCoins(5, "Yorum Yapma");
    checkTaskCompletion('task3');
  } else if (type === 'favorite') {
    userProfile.dailyTaskStats.favsCount = (userProfile.dailyTaskStats.favsCount || 0) + 1;
    addCoins(3, "Favori Ekleme");
    checkTaskCompletion('task4');
  } else if (type === 'script') {
    userProfile.dailyTaskStats.addedScripts = (userProfile.dailyTaskStats.addedScripts || 0) + 1;
    checkTaskCompletion('task5');
  } else if (type === 'game') {
    userProfile.dailyTaskStats.addedGames = (userProfile.dailyTaskStats.addedGames || 0) + 1;
    checkTaskCompletion('task6');
  } else if (type === 'like') {
    userProfile.dailyTaskStats.likesCount = (userProfile.dailyTaskStats.likesCount || 0) + 1;
    addCoins(2, "Puanlama / Beğeni");
    checkTaskCompletion('task7');
  } else if (type === 'category') {
    if (!userProfile.dailyTaskStats.visitedCategories) userProfile.dailyTaskStats.visitedCategories = [];
    if (!userProfile.dailyTaskStats.visitedCategories.includes(extraVal)) {
      userProfile.dailyTaskStats.visitedCategories.push(extraVal);
      checkTaskCompletion('task8');
    }
  }

  saveUserProfile();
}

function renderDailyTasks() {
  const banner = document.getElementById('dailyTasksSection');
  if (!banner) return;

  // Show only if logged in or demo active
  // Daily tasks visible for both logged-in and guest accounts
  banner.classList.add('visible');
  banner.classList.add('visible');

  // Ensure task1 (daily login) is rewarded
  if (!userProfile.dailyTasks?.task1) {
    userProfile.dailyTasks.task1 = true;
    addCoins(10, "Günlük Giriş Bonusu");
    saveUserProfile();
  }

  const grid = document.getElementById('tasksGrid');
  if (!grid) return;

  let completedCount = 0;
  let totalRewardPending = 0;
  let html = '';

  DAILY_TASKS_CONFIG.forEach(task => {
    const isDone = userProfile.dailyTasks && userProfile.dailyTasks[task.id];
    if (isDone) completedCount++;

    let progressText = '';
    if (!isDone) {
      if (task.id === 'task1') progressText = 'Hazır';
      else if (task.isCategoryCheck) {
        const count = userProfile.dailyTaskStats?.visitedCategories?.length || 0;
        progressText = `(${count}/3)`;
      } else {
        const currentVal = (userProfile.dailyTaskStats && userProfile.dailyTaskStats[task.statKey]) || 0;
        progressText = `(${Math.min(currentVal, task.target)}/${task.target})`;
      }
    }

    html += `
      <div class="task-card">
        <div class="task-left">
          <div class="task-icon">
            <i class="fa-solid ${task.icon}"></i>
          </div>
          <div class="task-details">
            <h4>${currentLang === 'tr' ? task.nameTr : task.nameEn} ${progressText}</h4>
            <p>${currentLang === 'tr' ? task.descTr : task.descEn}</p>
            <div class="task-reward">
              <i class="fa-solid fa-coins"></i> +${task.reward} coin
            </div>
          </div>
        </div>
        <div>
          ${isDone 
            ? `<button class="btn btn-outline task-btn" style="border-color: var(--green); color: var(--green);" disabled><i class="fa-solid fa-check"></i> Alındı</button>`
            : `<button class="btn btn-gold task-btn" onclick="manualCheckTask('${task.id}')">Tamamla</button>`
          }
        </div>
      </div>
    `;
  });

  grid.innerHTML = html;

  const counterDisplay = document.getElementById('tasksCounterDisplay');
  if (counterDisplay) {
    counterDisplay.innerHTML = `<i class="fa-solid fa-coins"></i> +${completedCount * 15} coin (${completedCount}/8)`;
  }
}

function manualCheckTask(taskId) {
  checkTaskCompletion(taskId);
  if (!userProfile.dailyTasks[taskId]) {
    showToast("Bu görevin gereksinimlerini tamamlamanız gerekiyor.", "fa-circle-info");
  }
}

function claimAllCompletedTasks() {
  DAILY_TASKS_CONFIG.forEach(t => checkTaskCompletion(t.id));
  showToast("Tamamlanan tüm görevler güncellendi!", "fa-circle-check", "green");
}

// ==================== CATEGORIES CAROUSEL ====================
const CATEGORIES_DEF = [
  { id: 'all', nameTr: 'Hepsi', nameEn: 'All', icon: 'fa-solid fa-star' },
  { id: 'mm2', nameTr: 'MM2', nameEn: 'MM2', img: CATEGORY_IMAGES.mm2 },
  { id: 'bloxfruits', nameTr: 'Blox Fruits', nameEn: 'Blox Fruits', img: CATEGORY_IMAGES.bloxfruits },
  { id: 'petsim', nameTr: 'Pet Sim 99', nameEn: 'Pet Sim 99', img: CATEGORY_IMAGES.petsim },
  { id: 'dahood', nameTr: 'Da Hood', nameEn: 'Da Hood', img: CATEGORY_IMAGES.dahood },
  { id: 'bladeball', nameTr: 'Blade Ball', nameEn: 'Blade Ball', img: CATEGORY_IMAGES.bladeball },
  { id: 'brookhaven', nameTr: 'Brookhaven', nameEn: 'Brookhaven', img: CATEGORY_IMAGES.brookhaven },
  { id: 'other', nameTr: 'Diğer', nameEn: 'Other', img: CATEGORY_IMAGES.other },
  { id: 'community', nameTr: 'Topluluk', nameEn: 'Community', icon: 'fa-solid fa-users' },
  { id: 'favorites', nameTr: 'Favorilerim', nameEn: 'Favorites', icon: 'fa-solid fa-heart' },
  { id: 'games', nameTr: 'Oyunlar', nameEn: 'Games', icon: 'fa-solid fa-gamepad', isGames: true }
];

function renderCategories() {
  const container = document.getElementById('categoriesList');
  if (!container) return;

  let html = '';
  CATEGORIES_DEF.forEach(cat => {
    const isActive = activeCategory === cat.id ? 'active' : '';
    const isGameClass = cat.isGames ? 'games-pill' : '';
    const name = currentLang === 'tr' ? cat.nameTr : cat.nameEn;
    const gameCountBadge = cat.isGames ? ` (${gamesData.length})` : '';

    let visual = '';
    if (cat.img) {
      visual = `<img src="${cat.img}" alt="${name}" onerror="this.src='${DEFAULT_SCRIPT_IMAGE}'" />`;
    } else if (cat.icon) {
      visual = `<i class="${cat.icon}"></i>`;
    }

    html += `
      <div class="category-pill ${isActive} ${isGameClass}" onclick="selectCategory('${cat.id}')">
        ${visual}
        <span>${name}${gameCountBadge}</span>
      </div>
    `;
  });

  container.innerHTML = html;
}

function selectCategory(catId) {
  activeCategory = catId;
  currentPage = 1;
  recordTaskProgress('category', catId);
  
  // Sync top nav active classes
  document.querySelectorAll('.rblx-nav-btn').forEach(b => b.classList.remove('active'));
  const targetNavBtn = document.getElementById('rblxNav_' + catId);
  if (targetNavBtn) targetNavBtn.classList.add('active');

  renderCategories();
  renderMainGrid();
}

// ==================== SEARCH & FILTERS ====================
function handleSearchDebounce(e) {
  clearTimeout(searchDebounceTimeout);
  searchDebounceTimeout = setTimeout(() => {
    searchQuery = (e.target.value || '').trim().toLowerCase();
    currentPage = 1;
    renderMainGrid();
  }, 300);
}


// ==================== QUICK FILTER CHIPS ====================
function selectQuickFilter(filterKey) {
  activeQuickFilter = filterKey;
  currentPage = 1;
  document.querySelectorAll('.quick-filter-chip').forEach(chip => {
    chip.classList.toggle('active', chip.getAttribute('data-filter') === filterKey);
  });
  playClickSound();
  renderMainGrid();
}

function clearSearchInput() {
  const input = document.getElementById('searchInput');
  const clearBtn = document.getElementById('searchClearBtn');
  if (input) {
    input.value = '';
    searchQuery = '';
    if (clearBtn) clearBtn.style.display = 'none';
    currentPage = 1;
    renderMainGrid();
    input.focus();
  }
}

function resetFilters() {
  activeCategory = 'all';
  searchQuery = '';
  currentPage = 1;
  const search = document.getElementById('searchInput');
  if (search) search.value = '';
  const sort = document.getElementById('sortSelect');
  if (sort) sort.value = 'default';
  const type = document.getElementById('typeSelect');
  if (type) type.value = 'all';
  const rating = document.getElementById('ratingSelect');
  if (rating) rating.value = 'all';

  renderCategories();
  renderMainGrid();
}

function applyFilters() {
  currentPage = 1;
  renderMainGrid();
}

// ==================== RENDER MAIN GRID ====================
function getFilteredScripts() {
  let list = [...scriptsData];

  // Category filter
  if (activeCategory === 'favorites') {
    const favs = userProfile.favorites || [];
    list = list.filter(s => favs.includes(s.id));
  } else if (activeCategory === 'community') {
    list = list.filter(s => !s.isPremium);
  } else if (activeCategory !== 'all' && activeCategory !== 'games') {
    list = list.filter(s => (s.category || '').toLowerCase() === activeCategory.toLowerCase());
  }

  // Quick Filter Chips Bar
  if (activeQuickFilter === 'popular') {
    list.sort((a, b) => (b.views || 0) - (a.views || 0));
  } else if (activeQuickFilter === 'keyless') {
    list = list.filter(s => s.isKeyless || !s.keyRequired || !((s.desc || '') + (s.name || '')).toLowerCase().includes('keyli'));
  } else if (activeQuickFilter === 'mobile') {
    list = list.filter(s => (s.executors || []).some(e => ['delta', 'fluxus', 'codex', 'arceus', 'hydrogen'].includes(e.toLowerCase())));
  } else if (activeQuickFilter === 'pc') {
    list = list.filter(s => (s.executors || []).some(e => ['solara', 'wave', 'xeno', 'celery'].includes(e.toLowerCase())));
  } else if (activeQuickFilter === 'working') {
    list = list.filter(s => {
      const w = s.workingVotes || 40;
      const p = s.patchedVotes || 2;
      return (w / (w + p)) >= 0.8;
    });
  } else if (activeQuickFilter === 'new') {
    list.sort((a, b) => (b.id || '').localeCompare(a.id || ''));
  } else if (activeQuickFilter === 'favs') {
    const favs = userProfile.favorites || [];
    list = list.filter(s => favs.includes(s.id));
  }

  // Search filter (name, description, features, executors, category, author)
  if (searchQuery) {
    list = list.filter(s => {
      const name = (s.name || '').toLowerCase();
      const desc = (s.desc || '').toLowerCase();
      const feats = (s.features || []).join(' ').toLowerCase();
      const execs = (s.executors || []).join(' ').toLowerCase();
      const cat = (s.category || '').toLowerCase();
      const user = (s.userName || '').toLowerCase();
      return name.includes(searchQuery) || desc.includes(searchQuery) || feats.includes(searchQuery) || execs.includes(searchQuery) || cat.includes(searchQuery) || user.includes(searchQuery);
    });
  }

  // Type filter
  const typeVal = document.getElementById('typeSelect')?.value || 'all';
  if (typeVal === 'premium') {
    list = list.filter(s => s.isPremium);
  } else if (typeVal === 'community') {
    list = list.filter(s => !s.isPremium);
  }

  // Rating filter
  const ratingVal = document.getElementById('ratingSelect')?.value || 'all';
  if (ratingVal === '4') {
    list = list.filter(s => (s.rating || 0) >= 4);
  } else if (ratingVal === '3') {
    list = list.filter(s => (s.rating || 0) >= 3);
  }

  // Executor filter
  const execVal = document.getElementById('executorSelect')?.value || 'all';
  if (execVal !== 'all') {
    list = list.filter(s => (s.executors || ["Delta", "Wave", "Solara"]).some(e => e.toLowerCase() === execVal.toLowerCase()));
  }

  // Sort
  const sortVal = document.getElementById('sortSelect')?.value || 'default';
  if (sortVal === 'az') {
    list.sort((a, b) => (a.name || '').localeCompare(b.name || ''));
  } else if (sortVal === 'za') {
    list.sort((a, b) => (b.name || '').localeCompare(a.name || ''));
  } else if (sortVal === 'popular') {
    list.sort((a, b) => (b.views || 0) - (a.views || 0));
  } else if (sortVal === 'new') {
    list.sort((a, b) => (b.createdAt || 0) - (a.createdAt || 0));
  }

  return list;
}

function getFilteredGames() {
  let list = [...gamesData];
  if (searchQuery) {
    list = list.filter(g => {
      const name = (g.name || '').toLowerCase();
      const desc = (g.desc || '').toLowerCase();
      return name.includes(searchQuery) || desc.includes(searchQuery);
    });
  }
  return list;
}

function renderMainGrid() {
  const container = document.getElementById('mainGridContainer');
  const emptyState = document.getElementById('emptyState');
  const paginationWrapper = document.getElementById('paginationWrapper');
  const sectionTitle = document.getElementById('currentSectionTitle');
  const itemsCountDisplay = document.getElementById('itemsCountDisplay');

  if (!container) return;

  // Executors Hub Mode (RBLXScripts Style)
  if (activeCategory === 'executors') {
    if (sectionTitle) sectionTitle.innerHTML = '<i class="fa-solid fa-microchip" style="color: var(--accent-light); margin-right: 8px;"></i> Roblox Executorlar & İndirme Merkezi';
    if (itemsCountDisplay) itemsCountDisplay.textContent = `${EXECUTORS_DATA.length} ${currentLang === 'tr' ? 'çalışan executor listelendi' : 'executors available'}`;
    emptyState.style.display = 'none';
    paginationWrapper.style.display = 'none';
    
    let html = '';
    EXECUTORS_DATA.forEach(ex => {
      const platformIcons = ex.platforms.map(p => {
        if (p === 'windows') return '<span class="platform-badge" title="Windows PC"><i class="fa-brands fa-windows"></i> Windows</span>';
        if (p === 'android') return '<span class="platform-badge" title="Android APK"><i class="fa-brands fa-android"></i> Android</span>';
        if (p === 'apple') return '<span class="platform-badge" title="iOS / macOS"><i class="fa-brands fa-apple"></i> Apple (iOS/Mac)</span>';
        return '';
      }).join(' ');

      const featurePills = ex.features.map(f => `<span class="feature-tag"><i class="fa-solid fa-check" style="color: #10b981; margin-right: 4px;"></i>${f}</span>`).join('');

      html += `
        <div class="executor-card" id="execCard_${ex.id}">
          <div class="executor-card-header">
            <div class="executor-card-title-wrap">
              <div class="executor-icon-box" style="color: ${ex.iconColor};">
                <i class="${ex.icon}"></i>
              </div>
              <div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <h3 style="font-size: 17px; font-weight: 800;">${ex.name}</h3>
                  <span class="badge-status-dot-pill">
                    <span class="status-pulse-dot" style="background: #10b981;"></span>
                    <span>${ex.status}</span>
                  </span>
                </div>
                <span style="font-size: 12px; color: var(--text-muted);">${ex.type} • ${ex.version}</span>
              </div>
            </div>
            <span class="executor-unc-badge">${ex.unc}</span>
          </div>

          <p style="font-size: 13px; color: var(--text-secondary); margin: 10px 0; line-height: 1.45;">${ex.shortDesc}</p>

          <div class="executor-platforms-row" style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px;">
            ${platformIcons}
            <span class="platform-badge" style="background: rgba(124, 58, 237, 0.15); color: var(--accent-light);"><i class="fa-solid fa-shield"></i> ${ex.level}</span>
          </div>

          <div class="executor-features-grid" style="display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 14px;">
            ${featurePills}
          </div>

          <div class="executor-card-actions" style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: auto;">
            <a href="${ex.downloadUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="display: flex; align-items: center; justify-content: center; gap: 6px; text-decoration: none;">
              <i class="fa-solid fa-download"></i>
              <span>Resmi İndir</span>
            </a>
            <button class="btn btn-outline btn-sm" onclick="openExecutorGuideModal('${ex.id}')" style="display: flex; align-items: center; justify-content: center; gap: 6px;">
              <i class="fa-solid fa-circle-info"></i>
              <span>Nasıl Kurulur?</span>
            </button>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
    return;
  }

  // Games Mode
  if (activeCategory === 'games') {
    if (sectionTitle) sectionTitle.textContent = currentLang === 'tr' ? "Roblox Oyunları" : "Roblox Games";
    const games = getFilteredGames();
    if (itemsCountDisplay) itemsCountDisplay.textContent = `${games.length} ${currentLang === 'tr' ? 'oyun bulundu' : 'games found'}`;
    if (games.length === 0) {
      container.innerHTML = '';
      emptyState.style.display = 'block';
      paginationWrapper.style.display = 'none';
      return;
    }
    emptyState.style.display = 'none';
    paginationWrapper.style.display = 'none';

    let html = '';
    games.forEach(g => {
      html += `
        <div class="game-card">
          <img src="${g.image || DEFAULT_SCRIPT_IMAGE}" class="game-card-img" alt="${g.name}" loading="lazy" decoding="async" onerror="this.onerror=null;this.src='${DEFAULT_SCRIPT_IMAGE}'" />
          <div class="game-card-body">
            <h4 style="font-size: 17px; font-weight: 700;">${g.name}</h4>
            <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.4;">${g.desc || 'Açıklama belirtilmedi.'}</p>
            <span style="font-size: 12px; color: var(--text-muted);"><i class="fa-solid fa-user"></i> ${g.userName || 'Roblox'}</span>
          </div>
          <div class="game-card-footer">
            <a href="${g.link}" target="_blank" rel="noopener noreferrer" class="btn btn-green" style="width: 100%;">
              <i class="fa-solid fa-play"></i> <span>Roblox'ta Oyna</span>
            </a>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;
    return;
  }

  // Scripts Mode
  if (sectionTitle) {
    if (activeCategory === 'all') sectionTitle.textContent = currentLang === 'tr' ? "Tüm Scriptler" : "All Scripts";
    else if (activeCategory === 'favorites') sectionTitle.textContent = currentLang === 'tr' ? "Favorilerim" : "My Favorites";
    else if (activeCategory === 'community') sectionTitle.textContent = currentLang === 'tr' ? "Topluluk Scriptleri" : "Community Scripts";
    else sectionTitle.textContent = `${activeCategory.toUpperCase()} Scriptleri`;
  }

  const allFiltered = getFilteredScripts();
  if (itemsCountDisplay) {
    itemsCountDisplay.textContent = `${allFiltered.length} ${currentLang === 'tr' ? 'script bulundu' : 'scripts found'}`;
  }

  if (allFiltered.length === 0) {
    container.innerHTML = '';
    emptyState.style.display = 'block';
    paginationWrapper.style.display = 'none';
    return;
  }

  emptyState.style.display = 'none';

  // Pagination
  const totalPages = Math.ceil(allFiltered.length / ITEMS_PER_PAGE);
  if (currentPage > totalPages) currentPage = 1;
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const currentSlice = allFiltered.slice(startIndex, startIndex + ITEMS_PER_PAGE);

  if (totalPages > 1) {
    paginationWrapper.style.display = 'flex';
    document.getElementById('pageIndicator').textContent = `${currentPage} / ${totalPages}`;
    document.getElementById('prevPageBtn').disabled = currentPage === 1;
    document.getElementById('nextPageBtn').disabled = currentPage === totalPages;
  } else {
    paginationWrapper.style.display = 'none';
  }

  let html = '';
  currentSlice.forEach(s => {
    const isFav = (userProfile.favorites || []).includes(s.id);
    const isOwner = currentUser && s.userId === currentUser.uid;
    const isUnlocked = isOwner || (userProfile.purchasedScripts || []).includes(s.id) || (s.coinPrice || 0) === 0;
    const catImage = s.image || CATEGORY_IMAGES[s.category] || DEFAULT_SCRIPT_IMAGE;
    const ratingScore = (s.rating || 4.5).toFixed(1);
    const viewsCount = s.views || 120;
    const commentsCount = (s.comments || []).length;

    // Working votes calculation
    const workingVotes = s.workingVotes || 42;
    const patchedVotes = s.patchedVotes || 2;
    const totalVotes = workingVotes + patchedVotes;
    const workPercent = Math.round((workingVotes / totalVotes) * 100);
    const isWorking = workPercent >= 70;

    // Features
    let featsHtml = '';
    (s.features || ["Aimbot", "ESP", "Auto Farm"]).slice(0, 3).forEach(f => {
      featsHtml += `<span class="feature-tag"><i class="fa-solid fa-check" style="color: var(--accent-light); font-size: 9px;"></i> ${f}</span>`;
    });

    // Executors
    let execsHtml = '';
    (s.executors || ["Delta", "Wave", "Solara", "Codex"]).slice(0, 4).forEach(ex => {
      execsHtml += `<span class="badge-executor">${ex}</span>`;
    });

    // Action buttons (RBLXScripts 1-Click Fast Copy & Inspect)
    actionsHtml = `
      <div class="card-action-btns">
        <button class="btn btn-primary btn-copy-loadstring" onclick="copyScriptCode('${s.id}', event)" title="1-Tıkla Loadstring Kopyala">
          <i class="fa-solid fa-copy"></i>
          <span>Kodu Kopyala</span>
        </button>
        <button class="btn btn-outline btn-view-code" onclick="openScriptCodeModal(scriptsData.find(i=>i.id==='${s.id}'))" title="Kodu İncele & İndir">
          <i class="fa-solid fa-code"></i>
          <span>İncele</span>
        </button>
      </div>
    `;
    // Owner or admin action buttons
    let adminOrOwnerActions = '';
    if (isOwner || (isUserAdmin(currentUser))) {
      adminOrOwnerActions = `
        <button class="btn btn-outline btn-icon btn-sm" title="Sil" onclick="deleteScript('${s.id}')" style="color: #ef4444; width: 28px; height: 28px; font-size: 11px;">
          <i class="fa-solid fa-trash"></i>
        </button>
      `;
    }

    // Report button
    let reportBtn = '';
    if (!s.isPremium) {
      reportBtn = `
        <button class="btn btn-outline btn-icon btn-sm" title="Raporla" onclick="openReportModal('${s.id}')" style="width: 28px; height: 28px; font-size: 11px; color: var(--text-muted);">
          <i class="fa-solid fa-flag"></i>
        </button>
      `;
    }

    // Comments drawer
    let commentsListHtml = '';
    if (s.isPremium) {
      commentsListHtml = `<div class="comment-notice"><i class="fa-solid fa-shield-halved" style="color: var(--gold);"></i> Premium doğrulanmış resmi script.</div>`;
    } else {
      const recentComments = (s.comments || []).slice(-3);
      if (recentComments.length > 0) {
        recentComments.forEach(c => {
          commentsListHtml += `
            <div class="comment-single">
              <span class="comment-author">${c.user}:</span>
              <span class="comment-body">${c.text}</span>
            </div>
          `;
        });
      } else {
        commentsListHtml = `<div class="comment-empty">Henüz yorum yok. İlk yorumu sen yap!</div>`;
      }
      commentsListHtml += `
        <div class="comment-form">
          <input type="text" class="comment-input" placeholder="Yorum yaz..." id="commentInput_${s.id}" onkeydown="if(event.key==='Enter') submitComment('${s.id}')" />
          <button class="btn btn-primary comment-submit-btn" onclick="submitComment('${s.id}')">Gönder</button>
        </div>
      `;
    }

    html += `
      <div class="script-card" id="scriptCard_${s.id}">
        <!-- Top Image Banner -->
        <div class="script-card-img-wrap" onclick="isUnlocked ? openScriptCodeModal(scriptsData.find(i=>i.id==='${s.id}')) : handleGetScript('${s.id}')">
          <img src="${catImage}" class="script-card-img" alt="${s.name}" loading="lazy" decoding="async" onerror="this.onerror=null;this.src='${DEFAULT_SCRIPT_IMAGE}'" />
          <div class="script-card-img-overlay"></div>

          <!-- Badges Top Left -->
          <div class="card-badge-top-left">
            <span class="status-pill ${isWorking ? 'status-working' : 'status-patched'}" title="${workingVotes} Çalışıyor, ${patchedVotes} Patched oyu">
              <span class="status-pulse-dot" style="background: ${isWorking ? '#10b981' : '#ef4444'};"></span>
              <span>%${workPercent} Çalışıyor</span>
            </span>
            ${s.isPremium ? `
              <span class="badge-premium-star" title="Doğrulanmış Premium Script">
                <i class="fa-solid fa-star"></i> <span>Premium</span>
              </span>
            ` : ''}
          </div>

          <!-- Badges Top Right -->
          <div class="card-badge-top-right">
            <span class="badge-keyless" title="Key gerektirmez, hemen çalışır">
              <i class="fa-solid fa-bolt"></i> <span>Keyless</span>
            </span>
            <button class="btn-fav ${isFav ? 'active' : ''}" onclick="toggleFavorite('${s.id}', event)" title="Favorilere Ekle">
              <i class="fa-solid fa-heart"></i>
            </button>
          </div>

          <!-- Badges Bottom Left -->
          <div class="card-badge-bottom-left">
            <span class="card-game-pill">
              <i class="fa-solid fa-gamepad"></i> ${(s.category || 'mm2').toUpperCase()}
            </span>
            ${s.version ? `<span class="card-version-pill">${s.version}</span>` : ''}
          </div>

          <!-- Badges Bottom Right -->
          <div class="card-badge-bottom-right">
            ${(s.coinPrice || 0) === 0 ? `
              <span class="card-price-pill card-price-free"><i class="fa-solid fa-bolt"></i> Ücretsiz</span>
            ` : isUnlocked ? `
              <span class="card-price-pill card-price-free"><i class="fa-solid fa-circle-check"></i> Açık</span>
            ` : `
              <span class="card-price-pill"><i class="fa-solid fa-coins"></i> ${s.coinPrice} Coin</span>
            `}
          </div>
        </div>

        <!-- Body Content -->
        <div class="script-card-body">
          <div class="card-title-row">
            <h4 class="card-title" title="${s.name}" onclick="isUnlocked ? openScriptCodeModal(scriptsData.find(i=>i.id==='${s.id}')) : handleGetScript('${s.id}')">${s.name}</h4>
          </div>
          
          <p class="card-desc">${s.desc || 'Bu script için henüz detaylı bir açıklama eklenmedi.'}</p>

          <!-- Feature Badges -->
          <div class="card-features">${featsHtml}</div>

          <!-- Supported Executors -->
          <div class="executor-tags">
            <span style="font-size: 10px; color: var(--text-muted); font-weight: 700;">Uyum:</span>
            ${execsHtml}
          </div>

          <!-- Working Status Mini Bar -->
          <div class="card-vote-bar">
            <div class="vote-bar-track" title="%${workPercent} Çalışıyor">
              <div class="vote-bar-fill" style="width: ${workPercent}%;"></div>
            </div>
            <div class="vote-btns-group">
              <button class="vote-btn-mini vote-up" onclick="voteScriptStatus('${s.id}', true)" title="Çalışıyor Oyu Ver (+2 Coin)">
                <i class="fa-solid fa-thumbs-up"></i> <span>${workingVotes}</span>
              </button>
              <button class="vote-btn-mini vote-down" onclick="voteScriptStatus('${s.id}', false)" title="Patched Bildir (+2 Coin)">
                <i class="fa-solid fa-thumbs-down"></i> <span>${patchedVotes}</span>
              </button>
            </div>
          </div>

          <!-- Meta Row -->
          <div class="card-meta-row">
            <div class="owner-info">
              <div class="owner-avatar-badge">${(s.userName || 'D').charAt(0).toUpperCase()}</div>
              <span class="owner-name">${s.userName || 'Topluluk'}</span>
              ${s.isPremium ? '<i class="fa-solid fa-circle-check" style="color: var(--accent-light); font-size: 11px;" title="Doğrulanmış Geliştirici"></i>' : ''}
            </div>
            <div class="card-stats-right">
              <span class="rating-badge" onclick="rateScriptPrompt('${s.id}')" title="Puan Ver (+2 Coin)">
                <i class="fa-solid fa-star" style="color: var(--gold);"></i> ${ratingScore}
              </span>
              <span class="views-badge" title="Görüntülenme">
                <i class="fa-solid fa-eye"></i> ${viewsCount > 1000 ? (viewsCount/1000).toFixed(1)+'k' : viewsCount}
              </span>
            </div>
          </div>

          <!-- Comments Drawer -->
          <div class="card-comments-box" id="commentsBox_${s.id}">
            <div class="comments-box-header">
              <span style="font-size: 12px; font-weight: 700; color: var(--text-muted);">Yorumlar (${commentsCount})</span>
            </div>
            ${commentsListHtml}
          </div>
        </div>

        <!-- Footer -->
        <div class="script-card-footer">
          ${actionsHtml}
          
          <div class="card-footer-sub">
            ${!s.isPremium ? `
              <button class="btn-toggle-comments" onclick="toggleCardComments('${s.id}', event)">
                <i class="fa-solid fa-comments"></i>
                <span>Yorumlar (${commentsCount})</span>
                <i class="fa-solid fa-chevron-down chevron-icon" id="commentChevron_${s.id}"></i>
              </button>
            ` : `
              <span style="font-size: 11px; color: var(--gold); display: flex; align-items: center; gap: 4px;">
                <i class="fa-solid fa-shield-check"></i> Doğrulanmış Script
              </span>
            `}
            <div style="display: flex; align-items: center; gap: 4px;">
              ${reportBtn}
              ${adminOrOwnerActions}
            </div>
          </div>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}

function changePage(delta) {
  currentPage += delta;
  renderMainGrid();
  window.scrollTo({ top: 400, behavior: 'smooth' });
}

// ==================== INTERACTION HANDLERS ====================
function toggleFavorite(scriptId, event) {
  if (event) event.stopPropagation();
  if (!userProfile.favorites) userProfile.favorites = [];

  const index = userProfile.favorites.indexOf(scriptId);
  if (index > -1) {
    userProfile.favorites.splice(index, 1);
    showToast("Favorilerden çıkarıldı", "fa-heart-crack");
  } else {
    userProfile.favorites.push(scriptId);
    showToast("Favorilere eklendi! (+3 Coin)", "fa-heart", "gold");
    recordTaskProgress('favorite');
  }

  saveUserProfile();
  renderMainGrid();
}

function rateScriptPrompt(scriptId) {
  const rating = prompt("Bu script için puanınız (1 - 5 arası):", "5");
  if (!rating) return;
  const num = parseInt(rating, 10);
  if (isNaN(num) || num < 1 || num > 5) {
    showToast("Geçersiz puan! 1 ile 5 arasında bir sayı girin.", "fa-circle-xmark", "red");
    return;
  }

  const s = scriptsData.find(item => item.id === scriptId);
  if (s) {
    const currentCount = s.ratingCount || 10;
    const currentRating = s.rating || 4.5;
    s.rating = ((currentRating * currentCount) + num) / (currentCount + 1);
    s.ratingCount = currentCount + 1;
    showToast(`Puan verildi: ${num} Yıldız! (+2 Coin)`, "fa-star", "gold");
    recordTaskProgress('like');
    renderMainGrid();
  }
}

function submitComment(scriptId) {
  const input = document.getElementById(`commentInput_${scriptId}`);
  if (!input) return;
  const text = (input.value || '').trim();
  if (!text) return;

  const s = scriptsData.find(item => item.id === scriptId);
  if (!s) return;

  if (s.isPremium) {
    showToast("Premium scriptlere yorum yapılamaz.", "fa-lock", "red");
    return;
  }

  if (!s.comments) s.comments = [];
  const authorName = currentUser ? userProfile.displayName : "Misafir";

  s.comments.push({
    id: "c_" + Date.now(),
    user: authorName,
    text: text,
    time: new Date().toLocaleTimeString()
  });

  input.value = '';
  showToast("Yorum gönderildi! (+5 Coin)", "fa-comment", "gold");
  recordTaskProgress('comment');
  renderMainGrid();
}

// ==================== UNLOCK & GET SCRIPT FLOW ====================
function handleGetScript(scriptId) {
  const s = scriptsData.find(item => item.id === scriptId);
  if (!s) return;

  selectedScriptForUnlock = s;
  recordTaskProgress('view');

  const isOwner = currentUser && s.userId === currentUser.uid;
  const isAdmin = isUserAdmin(currentUser);
  const isPurchased = (userProfile.purchasedScripts || []).includes(s.id);
  const isFree = (s.coinPrice || 0) === 0;

  // Direct open if condition met
  if (isOwner || isAdmin || isPurchased || isFree) {
    openScriptCodeModal(s);
    return;
  }

  // Show 2-option unlock modal
  document.getElementById('unlockScriptName').textContent = s.name;
  document.getElementById('unlockCoinPriceLabel').textContent = `${s.coinPrice || 30} coin`;
  openModal('unlockChoiceModal');
}

function confirmCoinUnlock() {
  if (!selectedScriptForUnlock) return;
  const price = selectedScriptForUnlock.coinPrice || 30;

  if (userProfile.coins < price) {
    showToast(`Yetersiz bakiye! Bu script için ${price} coin gerekiyor.`, "fa-triangle-exclamation", "red");
    return;
  }

  if (deductCoins(price, selectedScriptForUnlock.name)) {
    if (!userProfile.purchasedScripts) userProfile.purchasedScripts = [];
    userProfile.purchasedScripts.push(selectedScriptForUnlock.id);
    saveUserProfile();

    closeModal('unlockChoiceModal');
    openScriptCodeModal(selectedScriptForUnlock);
    renderMainGrid();
    showToast("Script kalıcı olarak açıldı!", "fa-lock-open", "green");
  }
}

function startTasksUnlock() {
  closeModal('unlockChoiceModal');
  taskStepsDone = [false, false, false];
  updateTaskProgressDisplay();
  openModal('tasksCountdownModal');
}

function triggerTaskCountdown(stepNum) {
  const btn = document.getElementById(`btnTask${stepNum}`);
  const timer = document.getElementById(`timerTask${stepNum}`);
  if (!btn || !timer) return;

  btn.style.display = 'none';
  timer.style.display = 'inline-block';

  let seconds = 25;
  timer.textContent = `${seconds}s`;

  // Open verified social media links
  let targetUrl = SOCIAL_LINKS.discord;
  if (stepNum === 2) targetUrl = SOCIAL_LINKS.youtube;
  if (stepNum === 3) targetUrl = SOCIAL_LINKS.tiktok;

  try {
    window.open(targetUrl, '_blank');
  } catch (e) {}

  const interval = setInterval(() => {
    seconds--;
    timer.textContent = `${seconds}s`;
    if (seconds <= 0) {
      clearInterval(interval);
      timer.innerHTML = `<i class="fa-solid fa-check" style="color: var(--green);"></i>`;
      taskStepsDone[stepNum - 1] = true;
      updateTaskProgressDisplay();
    }
  }, 1000);
}

function updateTaskProgressDisplay() {
  const completed = taskStepsDone.filter(Boolean).length;
  const progressText = document.getElementById('taskCompletionProgressText');
  if (progressText) {
    progressText.textContent = `İlerleme: ${completed} / 3 Tamamlandı`;
  }

  if (completed === 3 && selectedScriptForUnlock) {
    if (!userProfile.purchasedScripts) userProfile.purchasedScripts = [];
    userProfile.purchasedScripts.push(selectedScriptForUnlock.id);
    saveUserProfile();

    setTimeout(() => {
      closeModal('tasksCountdownModal');
      openScriptCodeModal(selectedScriptForUnlock);
      renderMainGrid();
      showToast("Tebrikler! Görevler tamamlandı, script açıldı.", "fa-gift", "green");
    }, 800);
  }
}

// ==================== LUA SYNTAX HIGHLIGHTER ====================
function highlightLuaCode(rawCode) {
  if (!rawCode) return "-- Kod bulunamadı.";

  const lines = (rawCode || '').split(String.fromCharCode(10)).map(function(l) { return l.replace(String.fromCharCode(13), ''); });
  let result = '';

  const kwList = [
    'and', 'break', 'do', 'else', 'elseif', 'end', 'false', 'for', 'function',
    'if', 'in', 'local', 'nil', 'not', 'or', 'repeat', 'return', 'then',
    'true', 'until', 'while', 'game', 'workspace', 'script', 'loadstring',
    'HttpGet', 'GetService', 'spawn', 'wait', 'print', 'warn', 'error'
  ];
  const kwRegex = new RegExp('(\\\\b)(' + kwList.join('|') + ')(\\\\b)', 'g');
  const strRegex = /('[^']*'|"[^"]*")/g;
  const numRegex = new RegExp('(\\\\b)(\\\\d+)(\\\\b)', 'g');

  lines.forEach((line, index) => {
    let safe = line
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    if (safe.includes('--')) {
      const parts = safe.split('--');
      const codePart = parts[0];
      const commentPart = parts.slice(1).join('--');

      const coloredCode = codePart
        .replace(strRegex, '<span class="lua-string">$1</span>')
        .replace(kwRegex, '$1<span class="lua-kw">$2</span>$3')
        .replace(numRegex, '$1<span class="lua-num">$2</span>$3');

      safe = coloredCode + '<span class="lua-comment">--' + commentPart + '</span>';
    } else {
      safe = safe
        .replace(strRegex, '<span class="lua-string">$1</span>')
        .replace(kwRegex, '$1<span class="lua-kw">$2</span>$3')
        .replace(numRegex, '$1<span class="lua-num">$2</span>$3');
    }

    result += `<div class="code-line"><span class="line-num">${index + 1}</span><span class="line-content">${safe || ' '}</span></div>`;
  });

  return result;
}

function updateCodeModalVoting(script) {
  const container = document.getElementById('modalVotingSection');
  if (!container || !script) return;
  const w = script.workingVotes || 40;
  const p = script.patchedVotes || 2;
  const total = w + p;
  const pct = Math.round((w / total) * 100);
  const userVote = (userProfile.votedScripts || {})[script.id];

  container.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 12px; border: 1px solid var(--border-color); margin-bottom: 12px;">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span class="status-pill ${pct >= 70 ? 'status-working' : 'status-patched'}">
          <i class="fa-solid ${pct >= 70 ? 'fa-circle-check' : 'fa-triangle-exclamation'}"></i> %${pct} Çalışıyor (${total} Topluluk Oyu)
        </span>
      </div>
      <div style="display: flex; gap: 6px;">
        <button class="btn btn-sm ${userVote === 'working' ? 'btn-green' : 'btn-outline'}" onclick="voteScriptStatus('${script.id}', true)" ${userVote ? 'disabled' : ''}>
          <i class="fa-solid fa-thumbs-up"></i> Çalışıyor
        </button>
        <button class="btn btn-sm ${userVote === 'patched' ? 'btn-red' : 'btn-outline'}" onclick="voteScriptStatus('${script.id}', false)" ${userVote ? 'disabled' : ''}>
          <i class="fa-solid fa-thumbs-down"></i> Patched
        </button>
      </div>
    </div>
  `;
}


function voteScriptStatus(scriptId, isWorking) {
  if (!currentUser) {
    showToast("Oy kullanmak ve +2 Coin kazanmak için lütfen giriş yapın!", "fa-right-to-bracket", "blue");
    openAuthModal();
    return;
  }

  if (!userProfile.votedScripts) {
    userProfile.votedScripts = {};
  }

  if (userProfile.votedScripts[scriptId]) {
    showToast("Bu script için zaten oy kullandınız!", "fa-circle-exclamation", "amber");
    return;
  }

  const s = scriptsData.find(item => item.id === scriptId);
  if (!s) return;

  if (isWorking) {
    s.workingVotes = (s.workingVotes || 40) + 1;
    userProfile.votedScripts[scriptId] = "working";
  } else {
    s.patchedVotes = (s.patchedVotes || 2) + 1;
    userProfile.votedScripts[scriptId] = "patched";
  }

  const total = (s.workingVotes || 0) + (s.patchedVotes || 0);
  if (total > 0) {
    s.statusPercent = Math.round(((s.workingVotes || 0) / total) * 100);
    s.isPatched = (s.workingVotes || 0) < (s.patchedVotes || 0) && total >= 3;
  }

  // Coin reward
  userProfile.coins = (userProfile.coins || 0) + 2;
  saveUserProfile();
  updateUIUserInfo();
  if (typeof playSuccessSound === "function") playSuccessSound();

  // Firestore sync if available
  if (db) {
    try {
      db.collection("scripts").doc(scriptId).update({
        workingVotes: s.workingVotes,
        patchedVotes: s.patchedVotes,
        statusPercent: s.statusPercent,
        isPatched: s.isPatched
      }).catch(() => {});
    } catch (e) {}
  }

  // Refresh UI
  renderMainGrid();

  if (selectedScriptForUnlock && selectedScriptForUnlock.id === scriptId) {
    updateCodeModalVoting(s);
  }

  showToast(
    isWorking 
      ? "Oyunuz kaydedildi! (+2 Coin kazandınız)" 
      : "Patched bildirimi kaydedildi! (+2 Coin kazandınız)",
    isWorking ? "fa-thumbs-up" : "fa-thumbs-down",
    isWorking ? "green" : "red"
  );
}

function openScriptCodeModal(scriptObj) {
  selectedScriptForUnlock = scriptObj;
  document.getElementById('codeModalTitle').textContent = scriptObj.name;
  document.getElementById('scriptCodeContent').innerHTML = highlightLuaCode(scriptObj.code || "");
  updateCodeModalVoting(scriptObj);
  openModal('scriptCodeModal');
}

function copyScriptCode(scriptIdOrObj, e) {
  if (e && e.stopPropagation) e.stopPropagation();
  let s = null;
  if (typeof scriptIdOrObj === 'string') {
    s = scriptsData.find(item => item.id === scriptIdOrObj);
  } else if (scriptIdOrObj && scriptIdOrObj.code) {
    s = scriptIdOrObj;
  } else if (selectedScriptForUnlock) {
    s = selectedScriptForUnlock;
  }

  if (!s) {
    showToast("Script bulunamadı!", "fa-circle-xmark", "red");
    return;
  }

  const rawCode = s.code || `loadstring(game:HttpGet("${s.rawUrl || 'https://raw.githubusercontent.com/...'}"))()`;
  
  navigator.clipboard.writeText(rawCode).then(() => {
    playCopySound();
    s.copies = (s.copies || 0) + 1;
    recordTaskProgress('copy', s.id);
    
    // Animate target button if triggered from a card
    if (e && e.currentTarget) {
      const btn = e.currentTarget;
      const oldHtml = btn.innerHTML;
      btn.innerHTML = `<i class="fa-solid fa-check"></i> <span>Kopyalandı!</span>`;
      btn.classList.add('btn-copied-success');
      setTimeout(() => {
        btn.innerHTML = oldHtml;
        btn.classList.remove('btn-copied-success');
      }, 2000);
    }
    
    // Modal copy button sync
    const btnText = document.getElementById('btnCopyCodeText');
    if (btnText) {
      const orig = btnText.textContent;
      btnText.textContent = 'Kopyalandı! ✓';
      setTimeout(() => { btnText.textContent = orig; }, 2200);
    }

    showToast(`${s.name} loadstring panoya kopyalandı!`, "fa-copy", "green");
  }).catch(() => {
    showToast("Kopyalama izni verilmedi, lütfen kodu manuel kopyalayın.", "fa-circle-xmark", "red");
  });
}

function copyCurrentScriptCode() {
  copyScriptCode(selectedScriptForUnlock);
}

function downloadScriptLuaFile() {
  if (!selectedScriptForUnlock) return;
  const s = selectedScriptForUnlock;
  const filename = (s.name || 'script').replace(/[^a-zA-Z0-9_-]/g, '_') + '.lua';
  const blob = new Blob([s.code || ''], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  playSuccessSound();
  showToast(`${filename} başarıyla indirildi!`, "fa-download", "green");
}

function openRawCode() {
  if (!selectedScriptForUnlock) return;
  const raw = selectedScriptForUnlock.code || "";
  const rawBlob = new Blob([raw], { type: 'text/plain;charset=utf-8' });
  const rawUrl = URL.createObjectURL(rawBlob);
  window.open(rawUrl, '_blank');
}

function quickCopyScript(scriptId, event) {
  if (event) event.stopPropagation();
  const s = scriptsData.find(item => item.id === scriptId);
  if (!s) return;

  const isOwner = currentUser && s.userId === currentUser.uid;
  const isAdmin = isUserAdmin(currentUser);
  const isPurchased = (userProfile.purchasedScripts || []).includes(s.id);
  const isFree = (s.coinPrice || 0) === 0;

  if (!isOwner && !isAdmin && !isPurchased && !isFree) {
    handleGetScript(scriptId);
    return;
  }

  const raw = s.code || '';
  navigator.clipboard.writeText(raw).then(() => {
    playCopySound();
    recordTaskProgress('view');
    showToast(`"${s.name}" scripti panoya kopyalandı!`, "fa-copy", "green");

    if (event && event.currentTarget) {
      const btn = event.currentTarget;
      const originalHtml = btn.innerHTML;
      btn.innerHTML = '<i class="fa-solid fa-check" style="color: #10b981;"></i> <span style="color: #10b981; font-weight: 800;">Kopyalandı!</span>';
      setTimeout(() => {
        btn.innerHTML = originalHtml;
      }, 2200);
    }
  }).catch(() => {
    openScriptCodeModal(s);
  });
}

function toggleCardComments(scriptId, event) {
  if (event) event.stopPropagation();
  const box = document.getElementById(`commentsBox_${scriptId}`);
  const chevron = document.getElementById(`commentChevron_${scriptId}`);
  if (!box) return;

  const isExpanded = box.classList.contains('expanded');
  if (isExpanded) {
    box.classList.remove('expanded');
    if (chevron) chevron.style.transform = 'rotate(0deg)';
  } else {
    box.classList.add('expanded');
    if (chevron) chevron.style.transform = 'rotate(180deg)';
  }
}


// ==================== PROMO CODES SYSTEM ====================
function openPromoCodeModal() {
  const input = document.getElementById('promoCodeInput');
  if (input) input.value = '';
  const msg = document.getElementById('promoResultMsg');
  if (msg) msg.style.display = 'none';
  openModal('promoCodeModal');
}

function submitPromoCode() {
  const input = document.getElementById('promoCodeInput');
  const code = (input.value || '').trim().toUpperCase();
  const msgEl = document.getElementById('promoResultMsg');

  if (!code) {
    showToast("Lütfen bir promosyon kodu girin.", "fa-circle-xmark", "red");
    playErrorSound();
    return;
  }

  if (!userProfile.usedPromoCodes) userProfile.usedPromoCodes = [];
  if (userProfile.usedPromoCodes.includes(code)) {
    msgEl.style.display = 'block';
    msgEl.style.color = '#ef4444';
    msgEl.textContent = 'Bu kupon kodunu daha önce kullandınız!';
    playErrorSound();
    return;
  }

  const promo = PROMO_CODES[code];
  if (!promo) {
    msgEl.style.display = 'block';
    msgEl.style.color = '#ef4444';
    msgEl.textContent = 'Geçersiz veya süresi dolmuş kod.';
    playErrorSound();
    return;
  }

  userProfile.usedPromoCodes.push(code);
  addCoins(promo.coins, `Kupon: ${code}`);
  playSuccessSound();

  msgEl.style.display = 'block';
  msgEl.style.color = 'var(--green)';
  msgEl.textContent = `Tebrikler! ${promo.desc} uygulandı: +${promo.coins} Coin!`;
  input.value = '';

  setTimeout(() => {
    closeModal('promoCodeModal');
  }, 1800);
}

// ==================== MOBILE NAVIGATION ====================
function switchMobileNav(tab) {
  document.querySelectorAll('.mobile-nav-item').forEach(el => el.classList.remove('active'));
  const activeEl = document.getElementById(`mobNav_${tab}`);
  if (activeEl) activeEl.classList.add('active');

  if (tab === 'home') {
    selectCategory('all');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else if (tab === 'games') {
    selectCategory('games');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else if (tab === 'tasks') {
    const banner = document.getElementById('dailyTasksSection');
    if (banner) {
      banner.classList.add('visible');
      banner.scrollIntoView({ behavior: 'smooth' });
    }
  } else if (tab === 'promo') {
    openPromoCodeModal();
  } else if (tab === 'profile') {
    handleAuthOrProfileClick();
  }
}

// ==================== STORE & COSMETICS ====================
function openCoinStoreModal(tab = 'scripts') {
  document.getElementById('storeBalanceDisplay').textContent = `${userProfile.coins} coin`;
  switchStoreTab(tab);
  openModal('coinStoreModal');
}

function switchStoreTab(tab) {
  ['scripts', 'cosmetics', 'inventory'].forEach(t => {
    const btn = document.getElementById(`storeTab${t.charAt(0).toUpperCase() + t.slice(1)}Btn`);
    const content = document.getElementById(`store${t.charAt(0).toUpperCase() + t.slice(1)}Tab`);
    if (btn) btn.classList.toggle('active', t === tab);
    if (content) content.style.display = t === tab ? 'block' : 'none';
  });

  if (tab === 'scripts') renderStorePremiumScripts();
  if (tab === 'cosmetics') renderStoreCosmetics();
  if (tab === 'inventory') renderStoreInventory();
}

function renderStorePremiumScripts() {
  const grid = document.getElementById('storePremiumScriptsGrid');
  if (!grid) return;

  let html = '';
  INITIAL_PREMIUM_SCRIPTS.forEach(p => {
    const isBought = (userProfile.purchasedScripts || []).includes(p.id);
    html += `
      <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 18px; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
        <h5 style="font-size: 15px; font-weight: 700;">${p.name}</h5>
        <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.3;">${p.desc}</p>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
          <span style="font-weight: 800; color: var(--gold); font-size: 14px;"><i class="fa-solid fa-coins"></i> ${p.coinPrice}</span>
          ${isBought 
            ? `<button class="btn btn-outline btn-sm" onclick="closeModal('coinStoreModal'); openScriptCodeModal(scriptsData.find(x => x.id === '${p.id}'))">Kullan</button>`
            : `<button class="btn btn-primary btn-sm" onclick="buyStoreItem('script', '${p.id}', ${p.coinPrice})">Satın Al</button>`
          }
        </div>
      </div>
    `;
  });
  grid.innerHTML = html;
}

function renderStoreCosmetics() {
  const grid = document.getElementById('storeCosmeticsGrid');
  if (!grid) return;

  let html = '';
  COSMETICS_LIST.forEach(c => {
    const isOwned = (userProfile.inventory || []).includes(c.id);
    const isActive = (userProfile.activeCosmetics || []).includes(c.id);

    let actionBtn = '';
    if (isOwned) {
      actionBtn = `
        <button class="btn btn-outline btn-sm" onclick="toggleCosmeticActive('${c.id}')" style="border-color: ${isActive ? 'var(--green)' : 'var(--border-color)'}; color: ${isActive ? 'var(--green)' : 'var(--text-primary)'};">
          ${isActive ? '<i class="fa-solid fa-check"></i> Aktif' : 'Aktifleştir'}
        </button>
      `;
    } else {
      actionBtn = `
        <button class="btn btn-primary btn-sm" onclick="buyStoreItem('cosmetic', '${c.id}', ${c.price})">
          Satın Al
        </button>
      `;
    }

    html += `
      <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 18px; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
        <div>
          <h5 style="font-size: 15px; font-weight: 700;" class="${c.type === 'name' ? c.class : ''}">${c.name}</h5>
          <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.3; margin-top: 4px;">${c.desc}</p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
          <span style="font-weight: 800; color: var(--gold); font-size: 14px;"><i class="fa-solid fa-coins"></i> ${c.price}</span>
          ${actionBtn}
        </div>
      </div>
    `;
  });
  grid.innerHTML = html;
}

function renderStoreInventory() {
  const container = document.getElementById('storeInventoryContent');
  if (!container) return;

  const purchased = (userProfile.purchasedScripts || []).map(id => scriptsData.find(s => s.id === id)).filter(Boolean);
  const ownedCosmetics = (userProfile.inventory || []).map(id => COSMETICS_LIST.find(c => c.id === id)).filter(Boolean);

  let html = `
    <div>
      <h4 style="font-size: 16px; font-weight: 700; margin-bottom: 10px;"><i class="fa-solid fa-scroll"></i> Sahip Olduğun Scriptler (${purchased.length})</h4>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px;">
  `;

  if (purchased.length === 0) {
    html += `<p style="font-size: 13px; color: var(--text-muted);">Henüz bir script satın almadınız.</p>`;
  } else {
    purchased.forEach(p => {
      html += `
        <div style="background: var(--bg-card); padding: 12px; border-radius: 14px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 13px; font-weight: 700;">${p.name}</span>
          <button class="btn btn-outline btn-sm" onclick="closeModal('coinStoreModal'); openScriptCodeModal(scriptsData.find(x => x.id === '${p.id}'))">Kullan</button>
        </div>
      `;
    });
  }

  html += `
      </div>
    </div>
    <div style="margin-top: 14px;">
      <h4 style="font-size: 16px; font-weight: 700; margin-bottom: 10px;"><i class="fa-solid fa-wand-magic-sparkles"></i> Sahip Olduğun Kozmetikler (${ownedCosmetics.length})</h4>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px;">
  `;

  if (ownedCosmetics.length === 0) {
    html += `<p style="font-size: 13px; color: var(--text-muted);">Henüz bir kozmetik eşya açmadınız.</p>`;
  } else {
    ownedCosmetics.forEach(c => {
      const isActive = (userProfile.activeCosmetics || []).includes(c.id);
      html += `
        <div style="background: var(--bg-card); padding: 12px; border-radius: 14px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 13px; font-weight: 700;">${c.name}</span>
          <button class="btn btn-outline btn-sm" onclick="toggleCosmeticActive('${c.id}')" style="border-color: ${isActive ? 'var(--green)' : 'var(--border-color)'}; color: ${isActive ? 'var(--green)' : 'var(--text-primary)'};">
            ${isActive ? 'Devre Dışı' : 'Aktifleştir'}
          </button>
        </div>
      `;
    });
  }

  html += `
      </div>
    </div>
  `;

  container.innerHTML = html;
}

function buyStoreItem(type, itemId, price) {
  if (userProfile.coins < price) {
    showToast("Yetersiz bakiye! Görevleri tamamlayarak coin kazanabilirsiniz.", "fa-triangle-exclamation", "red");
    return;
  }

  if (type === 'script') {
    if (deductCoins(price, "Premium Script")) {
      if (!userProfile.purchasedScripts) userProfile.purchasedScripts = [];
      userProfile.purchasedScripts.push(itemId);
      saveUserProfile();
      showToast("Script koleksiyonunuza eklendi!", "fa-circle-check", "green");
      renderStorePremiumScripts();
      renderMainGrid();
    }
  } else if (type === 'cosmetic') {
    if (deductCoins(price, "Kozmetik")) {
      if (!userProfile.inventory) userProfile.inventory = [];
      userProfile.inventory.push(itemId);
      saveUserProfile();
      showToast("Kozmetik eşya açıldı!", "fa-sparkles", "green");
      renderStoreCosmetics();
      updateUIUserInfo();
    }
  }
}

function toggleCosmeticActive(cosmeticId) {
  if (!userProfile.activeCosmetics) userProfile.activeCosmetics = [];
  const index = userProfile.activeCosmetics.indexOf(cosmeticId);
  if (index > -1) {
    userProfile.activeCosmetics.splice(index, 1);
    showToast("Kozmetik devre dışı bırakıldı.", "fa-circle-minus");
  } else {
    userProfile.activeCosmetics.push(cosmeticId);
    showToast("Kozmetik aktifleştirildi!", "fa-wand-magic-sparkles", "green");
  }
  saveUserProfile();
  renderStoreCosmetics();
  renderStoreInventory();
  updateUIUserInfo();
}

// ==================== AUTHENTICATION ====================
function handleAuthOrProfileClick() {
  if (currentUser) {
    openUserProfileModal();
  } else {
    openModal('authModal');
  }
}

function switchAuthTab(tab) {
  const isSignIn = tab === 'signin';
  document.getElementById('tabSignInBtn').classList.toggle('active', isSignIn);
  document.getElementById('tabSignUpBtn').classList.toggle('active', !isSignIn);
  document.getElementById('signInFormWrap').style.display = isSignIn ? 'block' : 'none';
  document.getElementById('signUpFormWrap').style.display = !isSignIn ? 'block' : 'none';
}

function calculatePasswordStrength(pwd) {
  let score = 0;
  if (!pwd) score = 0;
  else {
    if (pwd.length >= 6) score += 25;
    if (pwd.length >= 10) score += 25;
    if (/[A-Z]/.test(pwd)) score += 25;
    if (/[0-9]/.test(pwd)) score += 25;
  }

  const bars = [document.getElementById('pwdBar1'), document.getElementById('pwdBar2'), document.getElementById('pwdBar3'), document.getElementById('pwdBar4')];
  bars.forEach(b => { b.className = 'meter-bar'; });

  if (score >= 25) bars[0].className = 'meter-bar ' + (score < 50 ? 'active-red' : score < 75 ? 'active-yellow' : 'active-green');
  if (score >= 50) bars[1].className = 'meter-bar ' + (score < 75 ? 'active-yellow' : 'active-green');
  if (score >= 75) bars[2].className = 'meter-bar active-green';
  if (score >= 100) bars[3].className = 'meter-bar active-green';
}

function generateRandomSignUpAvatar() {
  const seed = "Hero_" + Math.floor(Math.random() * 99999);
  const url = `https://api.dicebear.com/7.x/bottts/svg?seed=${seed}`;
  document.getElementById('signUpAvatarPreview').src = url;
}

async function handleSignInSubmit(e) {
  e.preventDefault();
  const email = document.getElementById('signInEmail').value.trim();
  const password = document.getElementById('signInPassword').value;
  const errBox = document.getElementById('signInError');
  errBox.style.display = 'none';

  if (!supabaseClient) {
    errBox.textContent = "Giriş sistemi hazır değil. Sayfayı yenileyin.";
    errBox.style.display = 'block';
    return;
  }

  const { error } = await supabaseClient.auth.signInWithPassword({ email, password });
  if (error) {
    errBox.textContent = error.message || "Giriş başarısız oldu.";
    errBox.style.display = 'block';
    return;
  }
  closeModal('authModal');
  showToast("Başarıyla giriş yapıldı!", "fa-right-to-bracket", "green");
}

async function handleSignUpSubmit(e) {
  e.preventDefault();
  const username = document.getElementById('signUpUsername').value.trim();
  const email = document.getElementById('signUpEmail').value.trim();
  const password = document.getElementById('signUpPassword').value;
  const avatarUrl = document.getElementById('signUpAvatarPreview').src;
  const errBox = document.getElementById('signUpError');
  errBox.style.display = 'none';

  if (!supabaseClient) {
    errBox.textContent = "Kayıt sistemi hazır değil. Sayfayı yenileyin.";
    errBox.style.display = 'block';
    return;
  }

  const { data, error } = await supabaseClient.auth.signUp({
    email,
    password,
    options: { data: { display_name: username, avatar_url: avatarUrl } }
  });

  if (error) {
    errBox.textContent = error.message || "Kayıt işlemi başarısız.";
    errBox.style.display = 'block';
    return;
  }

  if (data.user && data.session) {
    await ensureSupabaseProfile(data.user, true);
    closeModal('authModal');
    showToast("Kayıt tamamlandı! +50 Hoşgeldin Coin!", "fa-sparkles", "gold");
  } else {
    closeModal('authModal');
    showToast("Kayıt oluşturuldu. E-posta doğrulaması gerekiyorsa gelen kutunu kontrol et.", "fa-envelope", "green");
  }
}

async function handleGoogleAuth() {
  if (!supabaseClient) {
    showToast("Supabase giriş sistemi hazır değil.", "fa-triangle-exclamation", "red");
    return;
  }
  const { error } = await supabaseClient.auth.signInWithOAuth({
    provider: 'google',
    options: { redirectTo: window.location.origin + window.location.pathname }
  });
  if (error) showToast("Google girişi başarısız: " + error.message, "fa-triangle-exclamation", "red");
}



async function handleDiscordAuth() {
  if (!supabaseClient) {
    showToast("Supabase giriş sistemi hazır değil.", "fa-triangle-exclamation", "red");
    return;
  }
  const { error } = await supabaseClient.auth.signInWithOAuth({
    provider: 'discord',
    options: { redirectTo: window.location.origin + window.location.pathname }
  });
  if (error) showToast("Discord girişi başarısız: " + error.message, "fa-triangle-exclamation", "red");
}

function handleGuestDemoLogin() {
  simulateLocalLogin("DemoPro", "demo@scripthub.roblox");
}

function simulateLocalLogin(name, email, photo) {
  currentUser = {
    uid: "usr_" + Date.now(),
    displayName: name,
    email: email,
    photoURL: photo || `https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(name)}`
  };
  userProfile.displayName = currentUser.displayName;
  userProfile.email = currentUser.email;
  userProfile.photoURL = currentUser.photoURL;

  closeModal('authModal');
  showToast(`Hoş geldin, ${name}!`, "fa-user-check", "green");
  saveUserProfile();
  updateUIUserInfo();
  renderDailyTasks();
  checkHeroCollapsedState();
  renderMainGrid();
}

async function handleSignOut() {
  if (supabaseClient) await supabaseClient.auth.signOut();
  currentUser = null;
  closeModal('userProfileModal');
  showToast("Çıkış yapıldı.", "fa-right-from-bracket");
  updateUIUserInfo();
  renderDailyTasks();
  checkHeroCollapsedState();
  renderMainGrid();
}

function updateUIUserInfo() {
  const authBtnText = document.getElementById('authProfileBtnText');
  const coinDisplay = document.getElementById('headerCoinCount');
  const adminBtn = document.getElementById('adminBtn');

  if (coinDisplay) coinDisplay.textContent = userProfile.coins || 0;

  if (currentUser) {
    if (authBtnText) {
      let activeClass = '';
      if ((userProfile.activeCosmetics || []).includes('c_purple_name')) activeClass = 'name-purple';
      if ((userProfile.activeCosmetics || []).includes('c_gold_name')) activeClass = 'name-gold';

      authBtnText.className = activeClass;
      authBtnText.textContent = userProfile.displayName || "Profil";
    }

    // Admin button visibility check
    const drawerAdminBtn = document.getElementById('drawerAdminBtn');
    if (drawerAdminBtn) drawerAdminBtn.style.display = isUserAdmin(currentUser) ? 'flex' : 'none';
    if (adminBtn) {
      if (isUserAdmin(currentUser)) {
        adminBtn.style.display = 'inline-flex';
      } else {
        adminBtn.style.display = 'none';
      }
    }
  } else {
    if (authBtnText) {
      authBtnText.className = '';
      authBtnText.textContent = I18N[currentLang].signIn;
    }
    if (adminBtn) adminBtn.style.display = 'none';
  }
}

// ==================== USER PROFILE MODAL ====================
function openUserProfileModal() {
  document.getElementById('profileAvatarImg').src = userProfile.photoURL || `https://api.dicebear.com/7.x/bottts/svg?seed=Roblox`;
  document.getElementById('profileDisplayName').textContent = userProfile.displayName;
  document.getElementById('profileEmail').textContent = userProfile.email || "Giriş yapılmamış";
  const profileAdminBadge = document.getElementById('profileAdminBadge');
  if (profileAdminBadge) {
    profileAdminBadge.style.display = isUserAdmin(currentUser) ? 'inline-flex' : 'none';
  }

  // Check cosmetics on profile avatar
  const avatarImg = document.getElementById('profileAvatarImg');
  avatarImg.className = '';
  if ((userProfile.activeCosmetics || []).includes('c_gold_frame')) avatarImg.classList.add('avatar-frame-gold');
  if ((userProfile.activeCosmetics || []).includes('c_rainbow_frame')) avatarImg.classList.add('avatar-frame-rainbow');

  const myScriptsCount = scriptsData.filter(s => currentUser && s.userId === currentUser.uid).length;
  const myGamesCount = gamesData.filter(g => currentUser && g.userId === currentUser.uid).length;
  const myUnlockedCount = (userProfile.purchasedScripts || []).length;
  const myFavsCount = (userProfile.favorites || []).length;

  document.getElementById('statUserScripts').textContent = myScriptsCount;
  document.getElementById('statUserGames').textContent = myGamesCount;
  document.getElementById('statUserCoins').textContent = userProfile.coins;
  document.getElementById('statUserUnlocked').textContent = myUnlockedCount;
  document.getElementById('statUserFavs').textContent = myFavsCount;
  document.getElementById('statUserTotalCoins').textContent = userProfile.totalCoinsEarned || userProfile.coins;

  openModal('userProfileModal');
}

function openEditProfileModal() {
  closeModal('userProfileModal');
  document.getElementById('editAvatarPreview').src = userProfile.photoURL;
  document.getElementById('editUsernameInput').value = userProfile.displayName;
  document.getElementById('editEmailInput').value = userProfile.email || "Misafir Oturumu";
  document.getElementById('editAvatarUrlInput').value = userProfile.photoURL.startsWith('http') ? userProfile.photoURL : '';
  openModal('editProfileModal');
}

function generateRandomEditAvatar() {
  const seed = "Hero_" + Math.floor(Math.random() * 99999);
  const url = `https://api.dicebear.com/7.x/bottts/svg?seed=${seed}`;
  document.getElementById('editAvatarPreview').src = url;
}

function handleAvatarFileSelect(e) {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function(evt) {
    document.getElementById('editAvatarPreview').src = evt.target.result;
  };
  reader.readAsDataURL(file);
}

function previewEditAvatarUrl(url) {
  if (url && url.startsWith('http')) {
    document.getElementById('editAvatarPreview').src = url;
  }
}

function saveUserProfileChanges() {
  const newName = document.getElementById('editUsernameInput').value.trim();
  const newAvatar = document.getElementById('editAvatarPreview').src;

  if (newName.length < 3) {
    showToast("Kullanıcı adı en az 3 karakter olmalıdır.", "fa-circle-xmark", "red");
    return;
  }

  userProfile.displayName = newName;
  userProfile.photoURL = newAvatar;
  saveUserProfile();

  closeModal('editProfileModal');
  openUserProfileModal();
  showToast("Profil bilgileri güncellendi!", "fa-user-check", "green");
}

// ==================== ADD SCRIPT & GAME ====================
function openAddScriptModal() {
  if (!currentUser) {
    showToast("Script eklemek için lütfen giriş yapın.", "fa-lock");
    openModal('authModal');
    return;
  }
  openModal('addScriptModal');
}

function previewAddScriptImage(url) {
  const preview = document.getElementById('addScriptImagePreview');
  if (url && url.startsWith('http')) {
    preview.src = url;
    preview.style.display = 'block';
  } else {
    preview.style.display = 'none';
  }
}

function handleNewScriptSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('addScriptName').value.trim();
  const category = document.getElementById('addScriptCategory').value;
  const desc = document.getElementById('addScriptDesc').value.trim();
  const featuresRaw = document.getElementById('addScriptFeatures').value;
  const code = document.getElementById('addScriptCode').value.trim();
  const image = document.getElementById('addScriptImage').value.trim() || CATEGORY_IMAGES[category] || DEFAULT_SCRIPT_IMAGE;
  const price = parseInt(document.getElementById('addScriptPrice').value, 10) || 30;

  const features = featuresRaw ? featuresRaw.split(',').map(s => s.trim()).filter(Boolean) : ["Aimbot", "ESP"];

  const newScript = {
    id: "sc_" + Date.now(),
    name: name,
    category: category,
    desc: desc,
    features: features,
    code: code,
    image: image,
    coinPrice: price,
    userId: currentUser ? currentUser.uid : "anon",
    userName: currentUser ? userProfile.displayName : "Topluluk",
    userEmail: currentUser ? currentUser.email : "",
    isCommunity: true,
    isPremium: false,
    commentCount: 0,
    downloads: 0,
    views: 1,
    rating: 5.0,
    ratingCount: 1,
    status: "active",
    version: "v1.0.0",
    createdAt: Date.now(),
    comments: []
  };

  scriptsData.unshift(newScript);

  // Local storage save for custom scripts
  const customScripts = scriptsData.filter(s => !INITIAL_PREMIUM_SCRIPTS.some(p => p.id === s.id));
  localStorage.setItem('scriptHubCustomScripts', JSON.stringify(customScripts));

  // Firestore sync if connected
  if (db) {
    try {
      db.collection('scripts').doc(newScript.id).set({
        ...newScript,
        createdAt: firebase.firestore.FieldValue.serverTimestamp()
      }).catch(err => console.log("Firestore script add error:", err));
    } catch (err) {}
  }

  addCoins(25, "Script Ekleme");
  recordTaskProgress('script');
  closeModal('addScriptModal');
  renderMainGrid();
  showToast("Script başarıyla eklendi! (+25 Coin)", "fa-rocket", "green");
}

function openAddGameModal() {
  if (!currentUser) {
    showToast("Oyun eklemek için lütfen giriş yapın.", "fa-lock");
    openModal('authModal');
    return;
  }
  openModal('addGameModal');
}

function previewAddGameImage(url) {
  const preview = document.getElementById('addGameImagePreview');
  if (url && url.startsWith('http')) {
    preview.src = url;
    preview.style.display = 'block';
  } else {
    preview.style.display = 'none';
  }
}

function handleNewGameSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('addGameName').value.trim();
  const link = document.getElementById('addGameLink').value.trim();
  const image = document.getElementById('addGameImage').value.trim() || DEFAULT_SCRIPT_IMAGE;
  const desc = document.getElementById('addGameDesc').value.trim();

  const newGame = {
    id: "gm_" + Date.now(),
    name: name,
    link: link,
    image: image,
    desc: desc,
    userId: currentUser ? currentUser.uid : "anon",
    userName: currentUser ? userProfile.displayName : "Topluluk",
    createdAt: Date.now()
  };

  gamesData.push(newGame);

  const customGames = gamesData.filter(g => !INITIAL_GAMES.some(ig => ig.id === g.id));
  localStorage.setItem('scriptHubCustomGames', JSON.stringify(customGames));

  if (db) {
    try {
      db.collection('games').doc(newGame.id).set({
        ...newGame,
        createdAt: firebase.firestore.FieldValue.serverTimestamp()
      }).catch(err => {});
    } catch (e) {}
  }

  addCoins(20, "Oyun Ekleme");
  recordTaskProgress('game');
  closeModal('addGameModal');
  renderCategories();
  if (activeCategory === 'games') renderMainGrid();
  showToast("Oyun başarıyla eklendi! (+20 Coin)", "fa-gamepad", "green");
}

function deleteScript(scriptId) {
  const s = scriptsData.find(item => item.id === scriptId);
  const isOwner = currentUser && s && s.userId === currentUser.uid;
  const isAdmin = isUserAdmin(currentUser);
  if (!isOwner && !isAdmin) {
    showToast("Bu scripti silme yetkiniz yok!", "fa-ban", "red");
    return;
  }
  if (!confirm("Bu scripti silmek istediğinizden emin misiniz?")) return;

  scriptsData = scriptsData.filter(s => s.id !== scriptId);
  const customScripts = scriptsData.filter(s => !INITIAL_PREMIUM_SCRIPTS.some(p => p.id === s.id));
  localStorage.setItem('scriptHubCustomScripts', JSON.stringify(customScripts));

  if (db) {
    try {
      db.collection('scripts').doc(scriptId).delete().catch(() => {});
    } catch (e) {}
  }

  renderMainGrid();
  showToast("Script silindi.", "fa-trash", "red");
}

// ==================== ADMIN PANEL ====================
function openAdminModal() {
  if (!isUserAdmin(currentUser)) {
    showToast("Yetkisiz erişim! Bu panele yalnızca yöneticiler erişebilir.", "fa-shield-halved", "red");
    return;
  }
  document.getElementById('adminStatScripts').textContent = scriptsData.length;
  document.getElementById('adminStatUsers').textContent = "128";
  document.getElementById('adminStatGames').textContent = gamesData.length;
  document.getElementById('adminStatComments').textContent = scriptsData.reduce((acc, cur) => acc + (cur.comments || []).length, 0);
  document.getElementById('adminStatReports').textContent = reportsData.length;

  const tbody = document.getElementById('adminScriptTableBody');
  if (tbody) {
    let html = '';
    scriptsData.forEach(s => {
      html += `
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 10px 14px; font-weight: 700;">${s.name}</td>
          <td style="padding: 10px 14px; color: var(--accent-light);">${s.category}</td>
          <td style="padding: 10px 14px; color: var(--gold);">${s.coinPrice} coin</td>
          <td style="padding: 10px 14px;">
            <button class="btn btn-outline btn-sm" onclick="adminEditScriptPrompt('${s.id}')"><i class="fa-solid fa-pen"></i></button>
            <button class="btn btn-outline btn-sm" onclick="deleteScript('${s.id}'); openAdminModal();" style="color: #ef4444;"><i class="fa-solid fa-trash"></i></button>
          </td>
        </tr>
      `;
    });
    tbody.innerHTML = html;
  }

  openModal('adminModal');
}

function adminEditScriptPrompt(scriptId) {
  const s = scriptsData.find(x => x.id === scriptId);
  if (!s) return;

  const newName = prompt("Yeni Script Adı:", s.name);
  if (!newName) return;
  const newPrice = prompt("Yeni Coin Fiyatı:", s.coinPrice);
  if (newPrice === null) return;

  s.name = newName;
  s.coinPrice = parseInt(newPrice, 10) || 0;

  // Save admin override
  localStorage.setItem('scriptHubAdminPremiumOverrides', JSON.stringify(scriptsData.filter(x => x.isPremium)));
  openAdminModal();
  renderMainGrid();
  showToast("Script güncellendi!", "fa-check", "green");
}

function resetAdminPremiumOverrides() {
  localStorage.removeItem('scriptHubAdminPremiumOverrides');
  scriptsData = [...INITIAL_PREMIUM_SCRIPTS, ...scriptsData.filter(s => !s.isPremium)];
  openAdminModal();
  renderMainGrid();
  showToast("Premium scriptler varsayılana sıfırlandı.", "fa-rotate-left");
}

// ==================== LEADERBOARD ====================
function openLeaderboardModal() {
  switchLeaderboardTab('coins');
  openModal('leaderboardModal');
}

function switchLeaderboardTab(tab) {
  ['coins', 'scripts', 'ratings', 'comments'].forEach(t => {
    const btn = document.getElementById(`lb${t.charAt(0).toUpperCase() + t.slice(1)}Btn`);
    if (btn) btn.classList.toggle('active', t === tab);
  });

  const list = document.getElementById('leaderboardList');
  if (!list) return;

  // Mocked sample leaderboard players
  let players = [
    { name: "BloxKing", coins: 1450, scripts: 14, rating: 4.9, comments: 45 },
    { name: "ShadowLurker", coins: 1200, scripts: 11, rating: 4.8, comments: 38 },
    { name: "NeonByte", coins: 980, scripts: 8, rating: 4.7, comments: 29 },
    { name: "PhantomMM2", coins: 850, scripts: 6, rating: 4.9, comments: 24 },
    { name: "VoidMaster", coins: 740, scripts: 5, rating: 4.6, comments: 19 },
    { name: userProfile.displayName, coins: userProfile.coins, scripts: 2, rating: 5.0, comments: 8, isMe: true }
  ];

  if (tab === 'coins') players.sort((a, b) => b.coins - a.coins);
  if (tab === 'scripts') players.sort((a, b) => b.scripts - a.scripts);
  if (tab === 'ratings') players.sort((a, b) => b.rating - a.rating);
  if (tab === 'comments') players.sort((a, b) => b.comments - a.comments);

  let html = '';
  players.slice(0, 20).forEach((p, idx) => {
    let rankBadgeColor = 'var(--text-muted)';
    if (idx === 0) rankBadgeColor = '#fbbf24'; // gold
    if (idx === 1) rankBadgeColor = '#94a3b8'; // silver
    if (idx === 2) rankBadgeColor = '#d97706'; // bronze

    let scoreLabel = '';
    if (tab === 'coins') scoreLabel = `${p.coins} coin`;
    if (tab === 'scripts') scoreLabel = `${p.scripts} script`;
    if (tab === 'ratings') scoreLabel = `⭐ ${p.rating}`;
    if (tab === 'comments') scoreLabel = `${p.comments} yorum`;

    html += `
      <div style="background: ${p.isMe ? 'rgba(124, 58, 237, 0.15)' : 'var(--bg-card)'}; border: 1px solid ${p.isMe ? 'var(--accent-light)' : 'var(--border-color)'}; border-radius: 14px; padding: 10px 16px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <span style="font-weight: 800; font-size: 15px; color: ${rankBadgeColor}; width: 24px;">#${idx + 1}</span>
          <img src="https://api.dicebear.com/7.x/bottts/svg?seed=${encodeURIComponent(p.name)}" style="width: 28px; height: 28px; border-radius: 50%;" />
          <span style="font-weight: 700; font-size: 14px;">${p.name} ${p.isMe ? '<span style="font-size: 10px; background: var(--accent); padding: 2px 6px; border-radius: 6px; color: #fff;">Sen</span>' : ''}</span>
        </div>
        <span style="font-weight: 800; color: var(--gold); font-size: 14px;">${scoreLabel}</span>
      </div>
    `;
  });

  list.innerHTML = html;
}

// ==================== REPORT SYSTEM ====================
let activeReportingScriptId = null;

function openReportModal(scriptId) {
  const s = scriptsData.find(x => x.id === scriptId);
  if (!s) return;
  activeReportingScriptId = scriptId;
  document.getElementById('reportScriptTargetName').textContent = `Script: ${s.name}`;
  openModal('reportModal');
}

function submitScriptReport() {
  const reason = document.getElementById('reportReasonSelect').value;
  const notes = document.getElementById('reportNotes').value;
  const s = scriptsData.find(x => x.id === activeReportingScriptId);

  const reportObj = {
    id: "rep_" + Date.now(),
    scriptId: activeReportingScriptId,
    scriptName: s ? s.name : "Bilinmeyen",
    userId: currentUser ? currentUser.uid : "anon",
    userName: currentUser ? userProfile.displayName : "Misafir",
    reason: reason,
    notes: notes,
    status: "pending",
    createdAt: Date.now()
  };

  reportsData.push(reportObj);

  if (db) {
    try {
      db.collection('reports').add({
        ...reportObj,
        createdAt: firebase.firestore.FieldValue.serverTimestamp()
      }).catch(() => {});
    } catch (e) {}
  }

  closeModal('reportModal');
  showToast("Raporunuz iletildi. İnceleme sonrası gereği yapılacaktır.", "fa-shield-halved", "green");
}

// ==================== CHAT WIDGET ====================
let isChatOpen = false;

function toggleChatWidget() {
  isChatOpen = !isChatOpen;
  const modal = document.getElementById('chatIframeModal');
  const fab = document.getElementById('chatFabBtn');
  const icon = document.getElementById('chatFabIcon');

  if (modal && fab && icon) {
    if (isChatOpen) {
      modal.classList.add('show');
      fab.classList.add('open');
      icon.className = 'fa-solid fa-xmark';
    } else {
      modal.classList.remove('show');
      fab.classList.remove('open');
      icon.className = 'fa-solid fa-comment-dots';
    }
  }
}

// ==================== BACKUP & EXPORT ====================
function exportDataBackup() {
  const backupData = {
    version: "1.0",
    exportDate: new Date().toISOString(),
    scripts: scriptsData,
    games: gamesData,
    userStats: {
      coins: userProfile.coins,
      purchasedScriptsCount: (userProfile.purchasedScripts || []).length
    }
  };

  const blob = new Blob([JSON.stringify(backupData, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `scripthub_backup_${new Date().toISOString().slice(0, 10)}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  showToast("Veriler JSON formatında indirildi!", "fa-download", "green");
}

// ==================== PRIVACY & COOKIES ====================
function openPrivacyModal() {
  openModal('privacyModal');
}

function acceptCookieConsent() {
  localStorage.setItem('scriptHubCookieConsent', 'accepted');
  const banner = document.getElementById('cookieBanner');
  if (banner) banner.classList.remove('show');
}

function checkCookieConsent() {
  if (!localStorage.getItem('scriptHubCookieConsent')) {
    const banner = document.getElementById('cookieBanner');
    if (banner) banner.classList.add('show');
  }
}

// ==================== MODAL HELPERS ====================
function openModal(id) {
  const m = document.getElementById(id);
  if (m) m.classList.add('active');
}

function closeModal(id) {
  const m = document.getElementById(id);
  if (m) m.classList.remove('active');
}

// Close modal on background click
window.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-overlay')) {
    e.target.classList.remove('active');
  }
});

// Scroll to top listener
window.addEventListener('scroll', () => {
  const btn = document.getElementById('scrollTopBtn');
  if (btn) {
    if (window.scrollY > 300) btn.classList.add('show');
    else btn.classList.remove('show');
  }
});

// ==================== SERVICE WORKER REGISTRATION ====================
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(() => {});
  });
}

// ==================== BOOTSTRAP APP ====================
window.addEventListener('DOMContentLoaded', () => {
  switchTheme(currentTheme);
  initFirebase();
  initSupabase();
  loadSavedData();
  applyTranslations();
  renderCategories();
  renderDailyTasks();
  checkHeroCollapsedState();
  renderMainGrid();
  renderNotifications();
  updateUIUserInfo();
  checkCookieConsent();

  // Supabase Auth is the source of truth for login + account progress.
  if (supabaseClient) {
    supabaseClient.auth.onAuthStateChange(async (event, session) => {
      if (session && session.user) {
        await ensureSupabaseProfile(session.user);
      } else if (event === 'SIGNED_OUT') {
        currentUser = null;
        updateUIUserInfo();
        renderDailyTasks();
        checkHeroCollapsedState();
        renderMainGrid();
      }
    });

  // Restore persisted Supabase session after reloads and mobile/desktop mode changes.
  if (supabaseClient) {
    supabaseClient.auth.getSession().then(({ data }) => {
      if (data && data.session && data.session.user) ensureSupabaseProfile(data.session.user);
    }).catch(() => {});
  }

  syncFromFirestore();
});


// ==================== GUIDE & HERO INTERACTION ====================
function openGuideModal(initialTab) {
  switchGuideTab(initialTab || 'howtouse');
  openModal('guideModal');
}

function switchGuideTab(tab) {
  const tabs = ['howtouse', 'executors', 'coins', 'safety', 'faq'];
  tabs.forEach(t => {
    const btn = document.getElementById(`guideTab_${t}_btn`);
    const content = document.getElementById(`guideTab_${t}`);
    if (btn) btn.classList.toggle('active', t === tab);
    if (content) content.style.display = t === tab ? 'block' : 'none';
  });
}

function toggleFaq(faqId) {
  const el = document.getElementById(faqId);
  if (!el) return;
  const parent = el.parentElement;
  if (parent) parent.classList.toggle('active');
}

function toggleHeroIntro() {
  const content = document.getElementById('heroMainContent');
  const icon = document.getElementById('heroToggleIcon');
  const text = document.getElementById('heroToggleText');
  if (!content) return;

  const isHidden = content.style.display === 'none';
  if (isHidden) {
    content.style.display = 'block';
    if (icon) icon.className = 'fa-solid fa-chevron-up';
    if (text) text.textContent = 'Gizle';
    localStorage.setItem('scriptHubHeroCollapsed', 'false');
  } else {
    content.style.display = 'none';
    if (icon) icon.className = 'fa-solid fa-chevron-down';
    if (text) text.textContent = 'Rehberi Göster';
    localStorage.setItem('scriptHubHeroCollapsed', 'true');
  }
}

function checkHeroCollapsedState() {
  if (localStorage.getItem('scriptHubHeroCollapsed') === 'true') {
    const content = document.getElementById('heroMainContent');
    const icon = document.getElementById('heroToggleIcon');
    const text = document.getElementById('heroToggleText');
    if (content) content.style.display = 'none';
    if (icon) icon.className = 'fa-solid fa-chevron-down';
    if (text) text.textContent = 'Rehberi Göster';
  }
}

// Expose all interactive functions to window for onclick bindings
window.switchTheme = switchTheme;
window.toggleLanguage = toggleLanguage;
window.resetFilters = resetFilters;
window.handleSearchDebounce = handleSearchDebounce;
window.selectCategory = selectCategory;
window.applyFilters = applyFilters;
window.changePage = changePage;
window.toggleFavorite = toggleFavorite;
window.rateScriptPrompt = rateScriptPrompt;
window.submitComment = submitComment;
window.handleGetScript = handleGetScript;
window.confirmCoinUnlock = confirmCoinUnlock;
window.startTasksUnlock = startTasksUnlock;
window.triggerTaskCountdown = triggerTaskCountdown;
window.copyCurrentScriptCode = copyCurrentScriptCode;
window.openCoinStoreModal = openCoinStoreModal;
window.switchStoreTab = switchStoreTab;
window.buyStoreItem = buyStoreItem;
window.toggleCosmeticActive = toggleCosmeticActive;
window.handleAuthOrProfileClick = handleAuthOrProfileClick;
window.switchAuthTab = switchAuthTab;
window.calculatePasswordStrength = calculatePasswordStrength;
window.generateRandomSignUpAvatar = generateRandomSignUpAvatar;
window.handleSignInSubmit = handleSignInSubmit;
window.handleSignUpSubmit = handleSignUpSubmit;
window.handleGoogleAuth = handleGoogleAuth;
window.handleDiscordAuth = handleDiscordAuth;
window.handleGuestDemoLogin = handleGuestDemoLogin;
window.handleSignOut = handleSignOut;
window.openUserProfileModal = openUserProfileModal;
window.openEditProfileModal = openEditProfileModal;
window.generateRandomEditAvatar = generateRandomEditAvatar;
window.handleAvatarFileSelect = handleAvatarFileSelect;
window.previewEditAvatarUrl = previewEditAvatarUrl;
window.saveUserProfileChanges = saveUserProfileChanges;
window.openAddScriptModal = openAddScriptModal;
window.previewAddScriptImage = previewAddScriptImage;
window.handleNewScriptSubmit = handleNewScriptSubmit;
window.openAddGameModal = openAddGameModal;
window.previewAddGameImage = previewAddGameImage;
window.handleNewGameSubmit = handleNewGameSubmit;
window.deleteScript = deleteScript;
window.openAdminModal = openAdminModal;
window.adminEditScriptPrompt = adminEditScriptPrompt;
window.resetAdminPremiumOverrides = resetAdminPremiumOverrides;
window.openLeaderboardModal = openLeaderboardModal;
window.switchLeaderboardTab = switchLeaderboardTab;
window.openReportModal = openReportModal;
window.submitScriptReport = submitScriptReport;
window.toggleChatWidget = toggleChatWidget;
window.exportDataBackup = exportDataBackup;
window.openPrivacyModal = openPrivacyModal;
window.acceptCookieConsent = acceptCookieConsent;
window.openModal = openModal;
window.closeModal = closeModal;
window.toggleNotifDropdown = toggleNotifDropdown;
window.clearAllNotifications = clearAllNotifications;
window.manualCheckTask = manualCheckTask;
window.claimAllCompletedTasks = claimAllCompletedTasks;
window.toggleSound = toggleSound;
window.isSoundEnabled = () => soundEnabled;
window.openPromoCodeModal = openPromoCodeModal;
window.submitPromoCode = submitPromoCode;
window.voteScriptStatus = voteScriptStatus;
window.switchMobileNav = switchMobileNav;
window.openGuideModal = openGuideModal;
window.switchGuideTab = switchGuideTab;
window.toggleFaq = toggleFaq;
window.toggleHeroIntro = toggleHeroIntro;

// ==================== MOBILE DRAWER CONTROLLER ====================
function toggleMobileDrawer() {
  const modal = document.getElementById('mobileDrawerModal');
  if (!modal) return;
  if (modal.classList.contains('active')) {
    closeModal('mobileDrawerModal');
  } else {
    // Sync Drawer User Status
    const userNameEl = document.getElementById('drawerUserName');
    const userStatusEl = document.getElementById('drawerUserStatus');
    const authActionBtn = document.getElementById('drawerAuthActionBtn');
    const soundTextEl = document.getElementById('drawerSoundText');
    const langTextEl = document.getElementById('drawerLangText');

    if (userNameEl && userStatusEl && authActionBtn) {
      if (currentUser) {
        userNameEl.textContent = currentUser.displayName || currentUser.email || 'Oyuncu';
        userStatusEl.textContent = `${userProfile.coins || 0} Coin • Giriş yapıldı`;
        authActionBtn.textContent = 'Profil';
      } else {
        userNameEl.textContent = 'Misafir Kullanıcı';
        userStatusEl.textContent = `${userProfile.coins || 0} Coin • Giriş yap veya kaydol`;
        authActionBtn.textContent = 'Giriş Yap';
      }
    }
    if (soundTextEl) {
      soundTextEl.textContent = soundEnabled ? 'Açık' : 'Kapalı';
    }
    if (langTextEl) {
      langTextEl.textContent = currentLang === 'tr' ? 'Türkçe (TR)' : currentLang === 'az' ? 'Azərbaycanca (AZ)' : 'English (EN)';
    }
    // Sync active theme dots in drawer
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    document.querySelectorAll('#mobileDrawerModal .theme-dot').forEach(dot => {
      dot.classList.remove('active');
      if (dot.classList.contains(`dot-${currentTheme}`)) dot.classList.add('active');
    });

    openModal('mobileDrawerModal');
  }
}


// ==================== GLOBAL SHORTCUTS ====================
window.addEventListener('keydown', (e) => {
  // ESC closes open modals and dropdowns
  if (e.key === 'Escape') {
    document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
    const notifDropdown = document.getElementById('notifDropdown');
    if (notifDropdown && notifDropdown.classList.contains('active')) {
      notifDropdown.classList.remove('active');
    }
  }
  // '/' focuses search bar
  if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
    e.preventDefault();
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
      searchInput.focus();
      searchInput.select();
    }
  }
});





function openExecutorGuideModal(execId) {
  const ex = EXECUTORS_DATA.find(e => e.id === execId);
  if (!ex) return;
  
  const title = document.getElementById('executorGuideTitle');
  const body = document.getElementById('executorGuideBody');
  const dlBtn = document.getElementById('executorGuideDownloadBtn');

  if (title) title.innerHTML = `<i class="${ex.icon}" style="color: ${ex.iconColor}; margin-right: 8px;"></i> ${ex.name} Kurulum Rehberi`;
  if (body) {
    const stepsHtml = (ex.steps || []).map(step => `<div class="exec-step-item" style="padding: 10px 14px; background: var(--bg-card); border-radius: 10px; margin-bottom: 8px; font-size: 13px; line-height: 1.4;">${step}</div>`).join('');
    body.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 1px solid var(--border-color);">
        <div>
          <span style="font-size: 12px; color: var(--text-muted);">${ex.type}</span>
          <h4 style="font-size: 16px; font-weight: 700; color: #10b981;"><i class="fa-solid fa-circle-check"></i> ${ex.status}</h4>
        </div>
        <span class="executor-unc-badge" style="font-size: 14px; padding: 6px 12px;">${ex.unc}</span>
      </div>
      <h5 style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">Adım Adım Çalıştırma Talimatı:</h5>
      ${stepsHtml}
    `;
  }
  if (dlBtn) {
    dlBtn.href = ex.downloadUrl;
  }
  openModal('executorGuideModal');
}
"""

if __name__ == "__main__":
    pass
