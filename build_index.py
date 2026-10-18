import json

# Load neural graph data for all 82 repositories
with open('repos_neural_graph.json', encoding='utf-8') as f:
    graph_data = json.load(f)

graph_json_str = json.dumps(graph_data)

# Master projects data
flagship_projects = [
    {
        "id": "vss-agent",
        "title": "VSS Self-Deciding Agent",
        "category": "AI / Autonomous Systems",
        "badge": "Flagship AI Core",
        "color": "#8b5cf6",
        "image": "assets/vss-agent-arch.svg",
        "description": "System-One decision intelligence framework engineered from scratch in PyTorch. Implements a 1-pass parallel decision engine for autonomous goal resolution, eliminating multi-turn deliberation latency.",
        "highlights": [
            "1-Pass Parallel Decision Neural Engine in PyTorch",
            "Sub-15ms inference latency on edge hardware",
            "Autonomous multi-step tool invocation without LLM prompt overhead",
            "Embedded state-memory cache with dynamic pruning"
        ],
        "tags": ["PyTorch", "Python", "Autonomous Agents", "Decision Systems", "Neural Networks"],
        "github": "https://github.com/siddharth-1118/vss-self-deciding-agent",
        "pos": [22, 6, -6]
    },
    {
        "id": "academia-nexus",
        "title": "Academia Nexus (SRM Portal)",
        "category": "Campus Data Infrastructure",
        "badge": "1,200+ Active Users",
        "color": "#06b6d4",
        "image": "assets/academia-nexus.svg",
        "description": "Enterprise-grade academic intelligence portal for SRM Institute of Science & Technology. Delivers real-time attendance margin calculations, automated GPA projection, and timetable synchronization.",
        "highlights": [
            "Active daily utility for 1,200+ SRM undergraduate students",
            "Dynamic Attendance Safety Guard with predictive alerts",
            "Secure encrypted session credential proxying",
            "Instant marks breakdown and SGPA/CGPA predictive planner"
        ],
        "tags": ["TypeScript", "React", "Node.js", "SRM Academia API", "Tailwind CSS"],
        "github": "https://github.com/siddharth-1118/academia-nexus",
        "pos": [26, 4, 0]
    },
    {
        "id": "classivo-skedio",
        "title": "Classivo3 / Skedio",
        "category": "Academic Scheduling & Automation",
        "badge": "Campus Favorite",
        "color": "#10b981",
        "image": "assets/classivo-skedio.svg",
        "description": "Automated schedule resolver and dynamic timetable manager built for high-tempo academic environments. Integrates real-time class status tracking, cancellation alerts, and dynamic attendance guards.",
        "highlights": [
            "Automated slot clash resolution algorithms",
            "Real-time class status tracking with live notifications",
            "Attendance margin calculators with 75% regulatory compliance",
            "Seamless offline-first local storage sync"
        ],
        "tags": ["JavaScript", "React", "State Machines", "Academic Automation"],
        "github": "https://github.com/siddharth-1118/classivo3",
        "pos": [24, 1, 6]
    },
    {
        "id": "signal-os",
        "title": "SIGNAL AI OS & Terminal",
        "category": "Operating System / Multi-Agent",
        "badge": "Priority Dispatcher",
        "color": "#ec4899",
        "image": "assets/signal-os.svg",
        "description": "Multi-agent command interface and event stream dispatcher. Features priority process scheduling, real-time socket communication, and an interactive cyberpunk terminal for high-bandwidth system monitoring.",
        "highlights": [
            "Asynchronous priority event queue and stream dispatcher",
            "Bi-directional WebSockets with sub-10ms packet ping",
            "Integrated command-line interpreter with telemetry log",
            "Custom audio reactive signal visualizer"
        ],
        "tags": ["TypeScript", "WebSockets", "Node.js", "Systems Architecture"],
        "github": "https://github.com/siddharth-1118/signal-chat",
        "pos": [19, 0, 7]
    },
    {
        "id": "vision-suite",
        "title": "Hand-Gesture Vision Suite",
        "category": "Computer Vision & Biometrics",
        "badge": "21-Point Skeletal Rig",
        "color": "#f59e0b",
        "image": "assets/vision-suite.svg",
        "description": "Real-time contactless human-computer interaction system powered by OpenCV and MediaPipe. Tracks 21 3D hand landmarks at 60 FPS for spatial air-drawing, virtual cursor steering, and biometric gesture triggers.",
        "highlights": [
            "Sub-millimeter 21-point 3D skeletal landmark tracking",
            "Virtual Air Canvas with stroke physics and color mixing",
            "Low-latency OpenCV video pipeline with zero GPU lag",
            "Custom gesture dictionary for operating system shortcuts"
        ],
        "tags": ["Python", "OpenCV", "MediaPipe", "Computer Vision", "NumPy"],
        "github": "https://github.com/siddharth-1118/hand-gesture",
        "pos": [18, 5, -8]
    },
    {
        "id": "creatorlang",
        "title": "Creatorlang & VSS-Lang",
        "category": "Compilers & Programming Languages",
        "badge": "Custom AST & Compiler",
        "color": "#a855f7",
        "image": "assets/creatorlang.svg",
        "description": "Custom programming language architecture designed and implemented from the lexer up. Features an intuitive syntax tree, recursive descent parser, and custom stack-based bytecode evaluation engine.",
        "highlights": [
            "Complete compiler toolchain: Lexer, Parser, AST, Evaluator",
            "Concise, human-centric syntax for rapid prototyping",
            "Robust runtime error reporting with exact line/column indicators",
            "Custom bytecode virtual machine with register memory"
        ],
        "tags": ["Compilers", "AST", "Language Design", "Python", "C++"],
        "github": "https://github.com/siddharth-1118/creatorlang",
        "pos": [25, -2, -2]
    }
]
flagship_json_str = json.dumps(flagship_projects)

# Timeline milestones data
timeline_milestones = [
    {
        "year": "2024 - Present",
        "title": "B.Tech in Computer Science & Engineering",
        "institution": "SRM Institute of Science and Technology, Kattankulathur",
        "badge": "Active Degree",
        "color": "#06b6d4",
        "description": "Rigorous coursework in Data Structures & Algorithms, Operating Systems, Computer Networks, and Machine Learning. Building high-impact open-source systems and campus utilities.",
        "pos": [10, -14, -12]
    },
    {
        "year": "2024",
        "title": "VSS Self-Deciding Agent Architecture",
        "institution": "Autonomous AI Research",
        "badge": "AI Core",
        "color": "#8b5cf6",
        "description": "Engineered a PyTorch-based System-One parallel decision framework that enables autonomous multi-step reasoning and sub-15ms edge inference.",
        "pos": [12, -14, -8]
    },
    {
        "year": "2024",
        "title": "Creatorlang & Language Design",
        "institution": "Compiler Engineering",
        "badge": "Compiler Core",
        "color": "#a855f7",
        "description": "Authored Creatorlang and VSS-Lang from scratch: lexer, recursive descent parser, Abstract Syntax Tree generator, and custom evaluation runtime.",
        "pos": [14, -14, -4]
    },
    {
        "year": "2024",
        "title": "Academia Nexus & Classivo Deployment",
        "institution": "Production Campus Impact",
        "badge": "1,200+ Students",
        "color": "#10b981",
        "description": "Launched academic portals solving real timetable and attendance tracking problems for over 1,200 active university students at SRM KTR.",
        "pos": [16, -14, 0]
    },
    {
        "year": "2024",
        "title": "Vision & Biometric Gesture Suite",
        "institution": "Computer Vision Lab",
        "badge": "60 FPS Rig",
        "color": "#f59e0b",
        "description": "Developed real-time 21-point skeletal hand landmark tracking and contactless human-computer interfaces using OpenCV and MediaPipe.",
        "pos": [18, -14, 4]
    }
]
timeline_json_str = json.dumps(timeline_milestones)

# About competencies
competencies = [
    {
        "name": "Software Engineering",
        "desc": "High-throughput systems, data structures, modular architectures, and clean code principles.",
        "color": "#06b6d4",
        "offset": [-4.0, 2.5, 0]
    },
    {
        "name": "AI & Deep Learning",
        "desc": "PyTorch model architecture, System-One 1-pass decision intelligence, and autonomous agents.",
        "color": "#8b5cf6",
        "offset": [0, 4.2, -3.0]
    },
    {
        "name": "Full-Stack Engineering",
        "desc": "Modern responsive web applications, real-time WebSockets, React/Next.js, Node.js, and APIs.",
        "color": "#10b981",
        "offset": [4.0, 2.5, 0]
    },
    {
        "name": "Compiler & Language Design",
        "desc": "Lexers, recursive descent parsers, Abstract Syntax Trees (AST), and bytecode virtual machines.",
        "color": "#f59e0b",
        "offset": [2.5, -2.5, 2.5]
    },
    {
        "name": "Product Building & Impact",
        "desc": "Real-world utility tools serving 1,200+ university peers with live updates and reliable uptime.",
        "color": "#ec4899",
        "offset": [-2.5, -2.5, -2.5]
    }
]
competencies_json_str = json.dumps(competencies)

# Skills clusters
skills_data = {
    "languages": {
        "title": "Programming Languages",
        "color": "#f59e0b",
        "center": [-18, 18, -14],
        "items": ["Python", "Java", "C", "C++", "JavaScript", "TypeScript", "Go", "Rust", "SQL", "HTML5/CSS3"]
    },
    "ai_data": {
        "title": "AI & Deep Learning",
        "color": "#8b5cf6",
        "center": [-10, 20, -12],
        "items": ["PyTorch", "TensorFlow", "Scikit-Learn", "OpenCV", "MediaPipe", "Neural Networks", "NLP", "LLM Agents"]
    },
    "fullstack": {
        "title": "Web & Full-Stack",
        "color": "#06b6d4",
        "center": [-10, 14, -8],
        "items": ["React", "Next.js", "Node.js", "Express", "Tailwind CSS", "WebSockets", "REST APIs", "Vite"]
    },
    "systems": {
        "title": "Systems & Tooling",
        "color": "#10b981",
        "center": [-18, 12, -10],
        "items": ["Linux", "Git", "GitHub Actions", "Docker", "Compilers / AST", "MongoDB", "PostgreSQL", "Three.js"]
    }
}
skills_json_str = json.dumps(skills_data)

# Achievements data
achievements = [
    {
        "title": "83+ Open Source Repositories",
        "subtitle": "Global Neural Constellation",
        "desc": "Spanning AI frameworks, campus platforms, computer vision suites, programming languages, and full-stack systems.",
        "metric": "83 Repos",
        "icon": "fa-network-wired",
        "color": "#8b5cf6",
        "pos": [-6, 18, 12]
    },
    {
        "title": "Creator of Custom Languages",
        "subtitle": "Compiler Engineering",
        "desc": "Architected Creatorlang and VSS-Lang with custom lexing, AST recursive descent parsing, and evaluation runtime.",
        "metric": "2 Compilers",
        "icon": "fa-code",
        "color": "#f59e0b",
        "pos": [-2, 19, 12]
    },
    {
        "title": "1,200+ Active University Users",
        "subtitle": "Campus Academic Infrastructure",
        "desc": "Academia Nexus and Classivo adopted by peers at SRM Institute of Science & Technology for daily attendance tracking.",
        "metric": "1,200+ Students",
        "icon": "fa-users-gear",
        "color": "#06b6d4",
        "pos": [2, 19, 12]
    },
    {
        "title": "Autonomous AI Decision Engine",
        "subtitle": "System-One PyTorch Core",
        "desc": "Pioneered single-pass parallel neural decision models eliminating conventional multi-turn prompt latency.",
        "metric": "< 15ms Latency",
        "icon": "fa-bolt",
        "color": "#10b981",
        "pos": [6, 18, 12]
    }
]
achievements_json_str = json.dumps(achievements)

# Generate HTML
html_content = f'''<!DOCTYPE html>
<html lang="en" class="h-full overflow-hidden select-none">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Vooka Sai Siddharth | 3D Interactive Developer Universe</title>
    <meta name="description" content="Immersive 3D Developer Portfolio of Vooka Sai Siddharth. Software Developer, AI/ML Engineer, and Creator of Custom Programming Languages. Featuring a persistent 3D universe connecting all 83 open-source repositories.">
    <meta name="author" content="Vooka Sai Siddharth">
    
    <!-- Open Graph & Social -->
    <meta property="og:title" content="Vooka Sai Siddharth | 3D Developer Universe">
    <meta property="og:description" content="Cinematic 3D WebGL universe connecting Sai Siddharth to 83+ repositories, AI architectures, and compiler systems.">
    <meta property="og:image" content="assets/profile.jpg">
    <meta property="og:type" content="website">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Space Grotesk', 'sans-serif'],
                        display: ['Outfit', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }},
                    colors: {{
                        brand: {{
                            300: '#c4b5fd',
                            400: '#a78bfa',
                            500: '#8b5cf6',
                            600: '#7c3aed',
                            900: '#2e1065',
                        }},
                        cyber: {{
                            cyan: '#06b6d4',
                            blue: '#3b82f6',
                            emerald: '#10b981',
                            pink: '#ec4899',
                            amber: '#f59e0b',
                            purple: '#a855f7',
                        }},
                        dark: {{
                            950: '#030306',
                            900: '#07070d',
                            850: '#0d0d17',
                            800: '#151522',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <!-- Three.js, Controls & TWEEN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tween.js/18.6.4/tween.umd.js"></script>

    <style>
        * {{ box-sizing: border-box; user-select: none; -webkit-user-select: none; }}
        body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background-color: #030306; color: #e2e8f0; font-family: 'Space Grotesk', sans-serif; }}
        #canvas3d {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: block; z-index: 1; cursor: grab; }}
        #canvas3d:active {{ cursor: grabbing; }}

        .film-grain {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 2; opacity: 0.035;
            background-image: url('data:image/svg+xml,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)"/%3E%3C/svg%3E');
        }}

        .glass-panel {{
            background: rgba(7, 7, 13, 0.85);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.7);
        }}

        .glass-panel-glow {{
            background: rgba(13, 13, 23, 0.9);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(139, 92, 246, 0.25);
            box-shadow: 0 0 30px rgba(139, 92, 246, 0.15), 0 12px 48px rgba(0, 0, 0, 0.8);
        }}

        .cursor-target {{
            pointer-events: none; position: fixed; width: 34px; height: 34px;
            border: 1.5px dashed rgba(6, 182, 212, 0.6); border-radius: 50%;
            transform: translate(-50%, -50%); transition: width 0.2s, height 0.2s, opacity 0.2s;
            z-index: 50; opacity: 0;
        }}
        .cursor-target.active {{ opacity: 1; width: 52px; height: 52px; border-color: #a78bfa; }}

        /* Custom scrollbar */
        ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
        ::-webkit-scrollbar-track {{ background: #07070d; }}
        ::-webkit-scrollbar-thumb {{ background: #7c3aed; border-radius: 999px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #9333ea; }}

        .glow-cyan {{ text-shadow: 0 0 15px rgba(6, 182, 212, 0.6); }}
        .glow-purple {{ text-shadow: 0 0 15px rgba(139, 92, 246, 0.6); }}

        @keyframes pulseSlow {{
            0%, 100% {{ opacity: 0.9; transform: scale(1); }}
            50% {{ opacity: 0.6; transform: scale(0.98); }}
        }}
        .animate-pulse-slow {{ animation: pulseSlow 4s ease-in-out infinite; }}
    </style>
</head>
<body class="relative w-full h-full">

    <!-- 3D Canvas, Noise Overlay & Pointer Reticle -->
    <canvas id="canvas3d"></canvas>
    <div class="film-grain"></div>
    <div id="reticle" class="cursor-target"></div>

    <!-- Master Header Navigation HUD -->
    <header class="fixed top-0 left-0 right-0 z-30 px-4 sm:px-6 py-3 flex justify-between items-center pointer-events-none">
        <!-- Brand & Architect ID -->
        <div class="flex items-center space-x-3 pointer-events-auto">
            <button onclick="warpToZone('hero')" class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-brand-600 via-brand-500 to-cyber-cyan p-[1.5px] cursor-pointer shadow-lg shadow-brand-500/25 hover:scale-105 active:scale-95 transition-all">
                <div class="w-full h-full bg-dark-950 rounded-[14px] flex items-center justify-center font-display font-black text-white text-base">
                    VSS
                </div>
            </button>
            <div class="flex flex-col">
                <button onclick="warpToZone('hero')" class="text-left font-display font-black text-base sm:text-lg tracking-wider text-white flex items-center leading-tight hover:text-brand-300 transition-colors">
                    VOOKA SAI SIDDHARTH
                    <span class="w-2 h-2 rounded-full bg-cyber-emerald ml-2 animate-ping"></span>
                    <span class="w-2 h-2 rounded-full bg-cyber-emerald -ml-2"></span>
                </button>
                <div class="flex items-center space-x-2 text-[10px] font-mono tracking-widest text-brand-300/80 uppercase">
                    <span>SRM KTR CS</span>
                    <span>•</span>
                    <span class="text-cyber-cyan">3D DIGITAL UNIVERSE</span>
                </div>
            </div>
        </div>

        <!-- Master Zone Navigation Pills (Desktop & Tablet) -->
        <nav class="hidden lg:flex items-center space-x-1 glass-panel px-3 py-1.5 rounded-2xl pointer-events-auto border border-white/10 shadow-2xl">
            <button onclick="warpToZone('hero')" id="pill-hero" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-white font-bold bg-brand-600 shadow-md shadow-brand-500/30 flex items-center space-x-1.5">
                <i class="fa-solid fa-house-chimney text-xs"></i>
                <span>Hero</span>
            </button>
            <button onclick="warpToZone('about')" id="pill-about" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-user-astronaut text-xs"></i>
                <span>About</span>
            </button>
            <button onclick="warpToZone('skills')" id="pill-skills" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-microchip text-xs"></i>
                <span>Skills</span>
            </button>
            <button onclick="warpToZone('projects')" id="pill-projects" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-layer-group text-xs"></i>
                <span>Projects</span>
            </button>
            <button onclick="warpToZone('timeline')" id="pill-timeline" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-timeline text-xs"></i>
                <span>Timeline</span>
            </button>
            <button onclick="warpToZone('achievements')" id="pill-achievements" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-trophy text-xs"></i>
                <span>Distinctions</span>
            </button>
            <button onclick="warpToZone('constellation')" id="pill-constellation" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-network-wired text-cyber-cyan text-xs"></i>
                <span>83 Repos</span>
            </button>
            <button onclick="warpToZone('contact')" id="pill-contact" class="nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5">
                <i class="fa-solid fa-satellite-dish text-xs"></i>
                <span>Contact</span>
            </button>
        </nav>

        <!-- Right Quick Controls -->
        <div class="flex items-center space-x-2 sm:space-x-3 pointer-events-auto">
            <!-- Audio Synthesizer FX Toggle -->
            <button id="audio-toggle" class="glass-panel w-9 h-9 sm:w-10 sm:h-10 rounded-xl flex items-center justify-center text-gray-300 hover:text-brand-300 hover:border-brand-500/50 transition-all text-sm" title="Toggle 3D Audio FX (Press M)">
                <i class="fa-solid fa-volume-high text-xs sm:text-sm" id="audio-icon"></i>
            </button>

            <!-- Full Overview Button -->
            <button onclick="warpToZone('overview')" class="glass-panel px-3 py-2 rounded-xl flex items-center space-x-1.5 text-xs font-mono text-gray-300 hover:text-white hover:border-brand-500 transition-all" title="Full Space Overview (Press Space)">
                <i class="fa-solid fa-compress text-brand-400 text-xs"></i>
                <span class="hidden md:inline">Space View</span>
            </button>

            <!-- GitHub Profile -->
            <a href="https://github.com/siddharth-1118" target="_blank" rel="noopener noreferrer" class="glass-panel px-3 py-2 rounded-xl flex items-center space-x-1.5 text-xs font-mono text-brand-300 hover:text-white hover:bg-brand-600/20 hover:border-brand-400 transition-all">
                <i class="fa-brands fa-github text-sm"></i>
                <span class="hidden sm:inline">GitHub</span>
            </a>
        </div>
    </header>

    <!-- Top Right: Instant 83-Neuron Search -->
    <div class="fixed top-16 right-4 sm:right-6 z-30 w-64 sm:w-72 pointer-events-auto">
        <div class="glass-panel p-2 rounded-2xl border border-white/10 shadow-2xl">
            <div class="relative">
                <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs"></i>
                <input type="text" id="repo-search" oninput="handleSearch(this.value)" placeholder="Search 83 repos (e.g. agent, skedio)..." class="w-full bg-dark-950/80 rounded-xl pl-8 pr-3 py-1.5 text-xs font-mono text-white placeholder-gray-500 border border-white/5 focus:outline-none focus:border-brand-500 transition-all">
            </div>
            <div id="search-dropdown" class="hidden mt-2 max-h-56 overflow-y-auto space-y-1 font-mono text-xs"></div>
        </div>
    </div>

    <!-- Hero Overlay (Visible when in Hero zone) -->
    <div id="hero-overlay" class="fixed inset-0 z-20 pointer-events-none flex flex-col justify-end lg:justify-center items-start px-6 sm:px-12 md:px-16 pb-24 lg:pb-0 max-w-3xl transition-opacity duration-700 opacity-100">
        <div class="pointer-events-auto space-y-4">
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-brand-500/10 border border-brand-500/30 text-brand-300 font-mono text-xs">
                <span class="w-2 h-2 rounded-full bg-brand-400 animate-pulse"></span>
                <span>CYBERNETIC ARCHITECT // DIGITAL UNIVERSE</span>
            </div>
            
            <h1 class="font-display font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-none">
                SIDDHARTH
            </h1>
            
            <div class="text-base sm:text-xl font-mono text-brand-300 font-medium">
                Software Developer <span class="text-cyber-cyan">|</span> AI/ML Engineer <span class="text-cyber-emerald">|</span> Builder
            </div>
            
            <p class="text-gray-300 text-sm sm:text-base font-light max-w-xl leading-relaxed">
                Building intelligent systems, developer tools, and products that solve real problems.
                Undergraduate in Computer Science &amp; Engineering at SRM Institute of Science and Technology.
            </p>

            <!-- Hero Action Buttons -->
            <div class="flex flex-wrap gap-3 pt-2">
                <button onclick="warpToZone('about')" class="px-5 py-3 rounded-xl bg-gradient-to-r from-brand-600 to-cyber-cyan text-white font-mono text-xs font-bold tracking-wider uppercase shadow-lg shadow-brand-500/25 hover:opacity-90 active:scale-95 transition-all flex items-center space-x-2">
                    <span>Explore My Universe</span>
                    <i class="fa-solid fa-arrow-right text-xs"></i>
                </button>
                <button onclick="warpToZone('projects')" class="px-5 py-3 rounded-xl glass-panel text-white font-mono text-xs font-bold tracking-wider uppercase border border-white/10 hover:border-brand-400 active:scale-95 transition-all flex items-center space-x-2">
                    <i class="fa-solid fa-layer-group text-brand-400 text-xs"></i>
                    <span>View Projects</span>
                </button>
                <a href="https://github.com/siddharth-1118" target="_blank" rel="noopener noreferrer" class="px-4 py-3 rounded-xl glass-panel text-gray-300 hover:text-white font-mono text-xs border border-white/10 hover:border-white/20 transition-all flex items-center space-x-1.5" title="GitHub Profile">
                    <i class="fa-brands fa-github text-sm"></i>
                </a>
                <button onclick="warpToZone('contact')" class="px-4 py-3 rounded-xl glass-panel text-gray-300 hover:text-white font-mono text-xs border border-white/10 hover:border-white/20 transition-all flex items-center space-x-1.5" title="Send Direct Transmission">
                    <i class="fa-solid fa-envelope text-sm"></i>
                </button>
            </div>

            <!-- Fast Stat Badges -->
            <div class="flex flex-wrap gap-2 pt-3 font-mono text-[11px] text-gray-400">
                <span class="px-2.5 py-1 rounded-lg bg-dark-900/90 border border-white/5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-graduation-cap text-cyber-cyan"></i>
                    <span>SRM KTR (2nd Year)</span>
                </span>
                <span class="px-2.5 py-1 rounded-lg bg-dark-900/90 border border-white/5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-brain text-brand-400"></i>
                    <span>PyTorch &amp; Agents</span>
                </span>
                <span class="px-2.5 py-1 rounded-lg bg-dark-900/90 border border-white/5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-code text-cyber-amber"></i>
                    <span>Creatorlang AST</span>
                </span>
                <span class="px-2.5 py-1 rounded-lg bg-dark-900/90 border border-white/5 flex items-center space-x-1.5">
                    <i class="fa-solid fa-network-wired text-cyber-emerald"></i>
                    <span>83 Repos Connected</span>
                </span>
            </div>
        </div>
    </div>

    <!-- Bottom Left 3D Radar HUD Minimap -->
    <div class="fixed bottom-5 left-4 sm:left-6 z-30 pointer-events-auto hidden sm:block">
        <div class="glass-panel p-2.5 rounded-2xl border border-white/10 shadow-2xl flex flex-col items-center">
            <div class="flex items-center justify-between w-full pb-1 text-[10px] font-mono text-gray-400">
                <span class="flex items-center space-x-1">
                    <i class="fa-solid fa-crosshairs text-cyber-cyan"></i>
                    <span>SPATIAL RADAR</span>
                </span>
                <span id="current-zone-tag" class="text-brand-300 font-bold uppercase">HERO ZONE</span>
            </div>
            <canvas id="radar-canvas" width="130" height="130" class="rounded-xl bg-dark-950/90 border border-white/5 cursor-crosshair"></canvas>
            <div class="text-[9px] font-mono text-gray-500 pt-1 text-center">Click radar point to warp</div>
        </div>
    </div>

    <!-- Floating 3D Interaction Guide Pill -->
    <div class="fixed bottom-20 left-1/2 -translate-x-1/2 z-20 pointer-events-none opacity-80" id="interaction-hint">
        <div class="glass-panel px-4 py-1.5 rounded-full text-[11px] font-mono tracking-widest uppercase text-gray-300 flex items-center space-x-2 border border-white/10 shadow-lg">
            <i class="fa-solid fa-hand-pointer text-brand-400"></i>
            <span>Drag to Orbit • Scroll to Zoom • Click any 3D Object or Zone to Warp</span>
        </div>
    </div>

    <!-- Bottom Mobile/Tablet Zone Selector Bar -->
    <nav class="fixed bottom-4 left-1/2 -translate-x-1/2 z-30 max-w-[96vw] pointer-events-auto lg:hidden">
        <div class="glass-panel px-2.5 py-2 rounded-2xl flex items-center gap-1 overflow-x-auto max-w-full border border-white/10 shadow-2xl">
            <button onclick="warpToZone('hero')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-white bg-brand-600 flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-house-chimney text-xs"></i>
                <span>Hero</span>
            </button>
            <button onclick="warpToZone('about')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-user-astronaut text-xs"></i>
                <span>About</span>
            </button>
            <button onclick="warpToZone('skills')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-microchip text-xs"></i>
                <span>Skills</span>
            </button>
            <button onclick="warpToZone('projects')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-layer-group text-xs"></i>
                <span>Projects</span>
            </button>
            <button onclick="warpToZone('timeline')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-timeline text-xs"></i>
                <span>Timeline</span>
            </button>
            <button onclick="warpToZone('constellation')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-network-wired text-cyber-cyan text-xs"></i>
                <span>83 Repos</span>
            </button>
            <button onclick="warpToZone('contact')" class="m-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap">
                <i class="fa-solid fa-satellite-dish text-xs"></i>
                <span>Contact</span>
            </button>
        </div>
    </nav>

    <!-- Holographic Detail Inspector Drawer (Right Side) -->
    <aside id="detail-drawer" class="fixed top-0 right-0 bottom-0 w-full sm:w-[480px] z-40 bg-dark-950/95 backdrop-blur-2xl border-l border-white/10 p-6 flex flex-col justify-between transition-transform duration-500 translate-x-full shadow-2xl overflow-y-auto">
        <div>
            <!-- Drawer Header -->
            <div class="flex items-center justify-between pb-4 border-b border-white/10 mb-6">
                <div class="flex items-center space-x-2">
                    <span id="drawer-dot" class="w-2.5 h-2.5 rounded-full bg-cyber-cyan animate-pulse"></span>
                    <span id="drawer-tag" class="text-xs font-mono text-cyber-cyan tracking-widest uppercase font-bold">TELEMETRY INSPECTOR</span>
                </div>
                <button onclick="closeDetailDrawer()" class="w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-all" title="Close (Press Esc)">
                    <i class="fa-solid fa-xmark text-sm"></i>
                </button>
            </div>

            <!-- Media Preview Container -->
            <div id="drawer-media-box" class="w-full rounded-2xl overflow-hidden aspect-[16/9] bg-dark-900 border border-white/10 mb-6 relative group shadow-xl flex items-center justify-center">
                <img id="drawer-img" src="assets/vss-agent-arch.svg" alt="Project Architecture Preview" class="w-full h-full object-contain p-2">
                <span id="drawer-media-caption" class="absolute bottom-2 left-3 text-[10px] font-mono text-gray-300">ARCHITECTURE SCHEMATIC // VSS CORE</span>
            </div>

            <!-- Title & Badges -->
            <h2 id="drawer-title" class="font-display font-black text-2xl text-white tracking-tight mb-2 break-all">
                VSS Self-Deciding Agent
            </h2>
            <div id="drawer-badges" class="flex flex-wrap gap-2 mb-4 font-mono text-xs">
                <span class="px-2.5 py-0.5 rounded-md bg-brand-500/20 text-brand-300 border border-brand-500/30">PyTorch</span>
                <span class="px-2.5 py-0.5 rounded-md bg-white/5 text-gray-300 border border-white/10">Flagship Core</span>
            </div>

            <!-- Description -->
            <p id="drawer-desc" class="text-gray-300 text-sm font-light leading-relaxed mb-6">
                System-One decision intelligence framework engineered from scratch in PyTorch.
            </p>

            <!-- Highlights Checklist -->
            <div id="drawer-highlights-container" class="mb-6 space-y-2">
                <div class="text-xs font-mono tracking-wider uppercase text-gray-400 font-bold">Key Architectural Specs:</div>
                <div id="drawer-highlights" class="space-y-1.5 text-xs text-gray-300 font-light"></div>
            </div>

            <!-- Metadata Box -->
            <div class="glass-panel p-4 rounded-xl border border-white/5 mb-6 space-y-2 text-xs font-mono">
                <div class="flex justify-between text-gray-400">
                    <span>Architect:</span>
                    <span class="text-white font-bold">Vooka Sai Siddharth</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>Institution:</span>
                    <span class="text-brand-300">SRM Institute of Science &amp; Tech</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>Category:</span>
                    <span id="drawer-cluster-name" class="text-cyber-cyan font-bold">AI &amp; Autonomous Systems</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>Repository Status:</span>
                    <span class="text-cyber-emerald font-bold">● Active &amp; Open Source</span>
                </div>
            </div>
        </div>

        <!-- Action Buttons -->
        <div class="pt-4 border-t border-white/10 space-y-3">
            <a id="drawer-github-link" href="#" target="_blank" rel="noopener noreferrer" class="w-full py-3.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-mono text-xs font-bold tracking-widest uppercase flex items-center justify-center space-x-2 shadow-lg shadow-brand-600/30 transition-all">
                <i class="fa-brands fa-github text-sm"></i>
                <span id="drawer-primary-btn-text">Open Repository on GitHub</span>
            </a>
            <button id="drawer-clone-btn" onclick="copyDrawerCloneUrl(this)" class="w-full py-3 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 hover:text-white font-mono text-xs flex items-center justify-center space-x-2 transition-all">
                <i class="fa-regular fa-clone"></i>
                <span id="drawer-clone-text">Copy git clone command</span>
            </button>
        </div>
    </aside>

    <!-- Contact Transmission Modal (Centered when active) -->
    <div id="contact-modal" class="fixed inset-0 z-40 bg-dark-950/80 backdrop-blur-md flex items-center justify-center p-4 transition-all duration-300 opacity-0 pointer-events-none">
        <div class="glass-panel-glow w-full max-w-lg rounded-3xl p-6 sm:p-8 relative border border-brand-500/40">
            <button onclick="closeContactModal()" class="absolute top-6 right-6 w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-all">
                <i class="fa-solid fa-xmark"></i>
            </button>

            <div class="flex items-center space-x-2 mb-2">
                <span class="w-2.5 h-2.5 rounded-full bg-cyber-emerald animate-ping"></span>
                <span class="text-xs font-mono text-cyber-emerald tracking-widest uppercase font-bold">COMMUNICATION GATEWAY</span>
            </div>

            <h3 class="font-display font-black text-2xl sm:text-3xl text-white tracking-tight mb-2">
                Initiate Direct Transmission
            </h3>
            <p class="text-gray-400 text-xs sm:text-sm font-light mb-6">
                Send an encrypted telemetry dispatch directly to Vooka Sai Siddharth.
            </p>

            <form onsubmit="handleContactSubmit(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-mono text-gray-300 uppercase mb-1">Your Name</label>
                    <input type="text" id="contact-name" required placeholder="Dr. Alan Turing" class="w-full bg-dark-950/80 rounded-xl px-4 py-2.5 text-xs font-mono text-white placeholder-gray-600 border border-white/10 focus:outline-none focus:border-brand-500 transition-all">
                </div>
                <div>
                    <label class="block text-xs font-mono text-gray-300 uppercase mb-1">Your Email</label>
                    <input type="email" id="contact-email" required placeholder="alan@bletchley.edu" class="w-full bg-dark-950/80 rounded-xl px-4 py-2.5 text-xs font-mono text-white placeholder-gray-600 border border-white/10 focus:outline-none focus:border-brand-500 transition-all">
                </div>
                <div>
                    <label class="block text-xs font-mono text-gray-300 uppercase mb-1">Transmission Subject</label>
                    <input type="text" id="contact-subject" required placeholder="AI Architecture Collaboration / Opportunity" class="w-full bg-dark-950/80 rounded-xl px-4 py-2.5 text-xs font-mono text-white placeholder-gray-600 border border-white/10 focus:outline-none focus:border-brand-500 transition-all">
                </div>
                <div>
                    <label class="block text-xs font-mono text-gray-300 uppercase mb-1">Message Payload</label>
                    <textarea id="contact-message" required rows="3" placeholder="Greetings Siddharth, I reviewed your VSS Agent architecture..." class="w-full bg-dark-950/80 rounded-xl px-4 py-2 text-xs font-mono text-white placeholder-gray-600 border border-white/10 focus:outline-none focus:border-brand-500 transition-all"></textarea>
                </div>

                <div class="flex items-center space-x-3 pt-2">
                    <button type="submit" id="contact-submit-btn" class="flex-1 py-3 rounded-xl bg-gradient-to-r from-brand-600 to-cyber-cyan text-white font-mono text-xs font-bold tracking-widest uppercase flex items-center justify-center space-x-2 shadow-lg shadow-brand-500/30 hover:opacity-95 transition-all">
                        <i class="fa-solid fa-paper-plane text-xs"></i>
                        <span>Transmit Signal</span>
                    </button>
                    <button type="button" onclick="copyEmailDirectly()" class="px-4 py-3 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-brand-300 hover:text-white font-mono text-xs flex items-center space-x-1.5 transition-all" title="Copy Email to Clipboard">
                        <i class="fa-regular fa-copy"></i>
                        <span id="copy-email-label">Copy Email</span>
                    </button>
                </div>
            </form>

            <div id="contact-feedback" class="hidden mt-4 p-3 rounded-xl text-xs font-mono text-center"></div>
        </div>
    </div>

    <!-- Toast Notification Overlay -->
    <div id="toast-box" class="fixed top-20 left-1/2 -translate-x-1/2 z-50 pointer-events-none transition-all duration-300 opacity-0 translate-y-2">
        <div class="glass-panel px-5 py-2.5 rounded-full border border-cyber-cyan/50 text-white font-mono text-xs flex items-center space-x-2 shadow-2xl">
            <i class="fa-solid fa-circle-check text-cyber-cyan"></i>
            <span id="toast-message">Notification message</span>
        </div>
    </div>

    <!-- Three.js Universe Data & 3D Interactive Engine -->
    <script>
        // --- Static JSON Payloads from Python Generation ---
        const NEURAL_GRAPH = {graph_json_str};
        const FLAGSHIP_PROJECTS = {flagship_json_str};
        const TIMELINE_DATA = {timeline_json_str};
        const COMPETENCIES = {competencies_json_str};
        const SKILLS_DATA = {skills_json_str};
        const ACHIEVEMENTS_DATA = {achievements_json_str};

        // --- Camera Zones Coordinates & Targets ---
        const SPATIAL_ZONES = {{
            hero: {{
                name: 'Hero Gateway',
                pos: new THREE.Vector3(0, 2.5, 14),
                target: new THREE.Vector3(0, 1.2, 0),
                fov: 50
            }},
            about: {{
                name: '3D Identity Core',
                pos: new THREE.Vector3(-22, 3.5, 9),
                target: new THREE.Vector3(-22, 2.0, 0),
                fov: 48
            }},
            skills: {{
                name: 'Spatial Skill Clusters',
                pos: new THREE.Vector3(-14, 18, 0),
                target: new THREE.Vector3(-14, 16, -11),
                fov: 52
            }},
            projects: {{
                name: 'Exhibition Pavilions',
                pos: new THREE.Vector3(22, 5.0, 13),
                target: new THREE.Vector3(22, 2.8, 0),
                fov: 50
            }},
            timeline: {{
                name: 'Spatial Timeline Highway',
                pos: new THREE.Vector3(14, -12, 5),
                target: new THREE.Vector3(14, -14, -4),
                fov: 50
            }},
            achievements: {{
                name: 'Distinctions Pedestals',
                pos: new THREE.Vector3(0, 19, 21),
                target: new THREE.Vector3(0, 18.5, 12),
                fov: 48
            }},
            constellation: {{
                name: '83-Neuron Repository Brain',
                pos: new THREE.Vector3(0, 8, 28),
                target: new THREE.Vector3(0, 1.5, 0),
                fov: 55
            }},
            contact: {{
                name: 'Communication Gateway',
                pos: new THREE.Vector3(0, -20.5, 18),
                target: new THREE.Vector3(0, -22, 10),
                fov: 48
            }},
            overview: {{
                name: 'Infinite Universe Overview',
                pos: new THREE.Vector3(0, 22, 45),
                target: new THREE.Vector3(0, 0, 0),
                fov: 60
            }}
        }};

        let activeZoneKey = 'hero';

        // --- Web Audio Synthesizer ---
        let audioCtx = null;
        let soundEnabled = true;

        function initAudio() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
        }}

        function playSound(freq = 600, duration = 0.05, type = 'sine', vol = 0.035) {{
            if (!soundEnabled) return;
            try {{
                initAudio();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(vol, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            }} catch(e) {{}}
        }}

        document.getElementById('audio-toggle').addEventListener('click', () => {{
            soundEnabled = !soundEnabled;
            const icon = document.getElementById('audio-icon');
            if (soundEnabled) {{
                icon.className = 'fa-solid fa-volume-high text-xs sm:text-sm';
                playSound(720, 0.08);
                showToast('Audio FX Synthesizer Active');
            }} else {{
                icon.className = 'fa-solid fa-volume-xmark text-xs sm:text-sm';
                showToast('Audio FX Muted');
            }}
        }});

        function showToast(msg) {{
            const box = document.getElementById('toast-box');
            document.getElementById('toast-message').innerText = msg;
            box.classList.remove('opacity-0', 'translate-y-2');
            setTimeout(() => {{
                box.classList.add('opacity-0', 'translate-y-2');
            }}, 2400);
        }}

        // --- Crosshair Reticle Follower ---
        const reticle = document.getElementById('reticle');
        window.addEventListener('pointermove', (e) => {{
            reticle.style.left = e.clientX + 'px';
            reticle.style.top = e.clientY + 'px';
        }});

        // --- Three.js Scene Variables ---
        let scene, camera, renderer, controls;
        let characterGroup, headMesh, coreLight, daisRings = [];
        let allInteractiveMeshes = [];
        let allSynapseLines = [];
        let actionPotentials = [];
        let clusterHubMeshes = [];
        let raycaster = new THREE.Raycaster();
        let mouse = new THREE.Vector2(-100, -100);
        let hoveredMesh = null;
        let clock = new THREE.Clock();

        // Architectural Groups
        let aboutZoneGroup, skillsZoneGroup, projectsZoneGroup, timelineZoneGroup, achievementsZoneGroup, contactZoneGroup;

        function initUniverse() {{
            const canvas = document.getElementById('canvas3d');
            
            // WebGL Support Check
            try {{
                renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: false, powerPreference: 'high-performance' }});
            }} catch(e) {{
                showWebGLFallback();
                return;
            }}

            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.toneMapping = THREE.ACESFilmicToneMapping;
            renderer.toneMappingExposure = 1.15;

            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x030306);
            scene.fog = new THREE.FogExp2(0x030306, 0.011);

            camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.copy(SPATIAL_ZONES.hero.pos);

            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 65;
            controls.minDistance = 3.0;
            controls.target.copy(SPATIAL_ZONES.hero.target);

            // Lighting Setup
            const ambient = new THREE.AmbientLight(0xffffff, 0.65);
            scene.add(ambient);

            const sunLight = new THREE.DirectionalLight(0xa78bfa, 1.4);
            sunLight.position.set(16, 30, 20);
            scene.add(sunLight);

            const rimLight = new THREE.DirectionalLight(0x06b6d4, 1.1);
            rimLight.position.set(-20, -15, -15);
            scene.add(rimLight);

            // Build Spatial Zones & Components
            buildAtmosphereAndGrid();
            buildCentralHeroAvatar();
            buildAboutIdentityZone();
            buildSkillsArchitectureZone();
            buildProjectsExhibitionZone();
            buildTimelineZone();
            buildAchievementsZone();
            buildContactGatewayZone();
            build83RepoNeuralNetwork();

            // Event Listeners
            window.addEventListener('resize', onWindowResize);
            window.addEventListener('pointermove', onPointerMove);
            window.addEventListener('click', onClick);
            window.addEventListener('keydown', onKeyDown);

            initRadarMinimap();
            animate();
        }}

        // --- Fallback if WebGL crashes or is not supported ---
        function showWebGLFallback() {{
            const fallbackDiv = document.createElement('div');
            fallbackDiv.className = 'fixed inset-0 z-50 bg-dark-950 p-8 flex flex-col items-center justify-center text-center text-white font-mono';
            fallbackDiv.innerHTML = `
                <div class="glass-panel p-8 rounded-3xl max-w-xl border border-brand-500/40 space-y-4">
                    <h2 class="text-2xl font-bold font-display text-cyber-cyan">WebGL Acceleration Unavailable</h2>
                    <p class="text-gray-300 text-sm">Your browser does not have WebGL enabled. You can still explore Sai Siddharth's portfolio and 83+ open-source repositories directly on GitHub.</p>
                    <div class="pt-4 flex justify-center space-x-4">
                        <a href="https://github.com/siddharth-1118" class="px-6 py-3 rounded-xl bg-brand-600 text-white font-bold text-xs uppercase">Visit GitHub Profile</a>
                        <a href="mailto:siddharthvooka@gmail.com" class="px-6 py-3 rounded-xl bg-white/10 text-white font-bold text-xs uppercase">Send Email</a>
                    </div>
                </div>
            `;
            document.body.appendChild(fallbackDiv);
        }}

        // --- Celestial Stars, Atmospheric Nebula & Horizon Grid ---
        function buildAtmosphereAndGrid() {{
            const count = 2800;
            const geom = new THREE.BufferGeometry();
            const pos = new Float32Array(count * 3);
            const colors = new Float32Array(count * 3);

            const cViolet = new THREE.Color(0x8b5cf6);
            const cCyan = new THREE.Color(0x06b6d4);
            const cWhite = new THREE.Color(0xffffff);

            for (let i = 0; i < count * 3; i += 3) {{
                pos[i] = (Math.random() - 0.5) * 320;
                pos[i + 1] = (Math.random() - 0.5) * 320;
                pos[i + 2] = (Math.random() - 0.5) * 320;

                const r = Math.random();
                const col = r > 0.6 ? cViolet : r > 0.3 ? cCyan : cWhite;
                colors[i] = col.r;
                colors[i + 1] = col.g;
                colors[i + 2] = col.b;
            }}

            geom.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            geom.setAttribute('color', new THREE.BufferAttribute(colors, 3));

            const mat = new THREE.PointsMaterial({{
                size: 1.6,
                vertexColors: true,
                transparent: true,
                opacity: 0.75,
                blending: THREE.AdditiveBlending
            }});

            scene.add(new THREE.Points(geom, mat));

            // Ground Cyberspace Grid
            const grid = new THREE.GridHelper(140, 70, 0x8b5cf6, 0x1e1b4b);
            grid.position.y = -5.0;
            grid.material.transparent = true;
            grid.material.opacity = 0.22;
            scene.add(grid);
        }}

        // --- Helper: Create 3D Canvas Label Mesh ---
        function make3DTextPlate(title, subtitle, borderColorHex = '#8b5cf6', w = 384, h = 112, scaleW = 2.2, scaleH = 0.65) {{
            const c = document.createElement('canvas');
            c.width = w;
            c.height = h;
            const ctx = c.getContext('2d');
            ctx.fillStyle = 'rgba(7, 7, 13, 0.88)';
            ctx.roundRect(8, 8, w - 16, h - 16, 16);
            ctx.fill();
            ctx.strokeStyle = borderColorHex;
            ctx.lineWidth = 3.5;
            ctx.stroke();

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 24px monospace';
            ctx.textAlign = 'center';
            ctx.fillText(title, w / 2, h * 0.45);

            ctx.fillStyle = borderColorHex;
            ctx.font = 'bold 16px monospace';
            ctx.fillText(subtitle, w / 2, h * 0.78);

            const tex = new THREE.CanvasTexture(c);
            const m = new THREE.Mesh(
                new THREE.PlaneGeometry(scaleW, scaleH),
                new THREE.MeshBasicMaterial({{ map: tex, transparent: true, side: THREE.DoubleSide }})
            );
            return m;
        }}

        // --- ZONE 1: Central Hero Character of Sai Siddharth ---
        function buildCentralHeroAvatar() {{
            characterGroup = new THREE.Group();
            characterGroup.position.set(0, 0, 0);

            // Dais Base
            const daisGeom = new THREE.CylinderGeometry(2.4, 2.8, 0.45, 32);
            const daisMat = new THREE.MeshStandardMaterial({{ color: 0x070712, roughness: 0.2, metalness: 0.9 }});
            const dais = new THREE.Mesh(daisGeom, daisMat);
            dais.position.y = -2.6;
            characterGroup.add(dais);

            for (let i = 1; i <= 3; i++) {{
                const ringGeom = new THREE.TorusGeometry(1.4 + i * 0.45, 0.025, 16, 64);
                const ringMat = new THREE.MeshBasicMaterial({{ color: i % 2 === 0 ? 0x06b6d4 : 0x8b5cf6, transparent: true, opacity: 0.85 }});
                const ring = new THREE.Mesh(ringGeom, ringMat);
                ring.rotation.x = Math.PI / 2;
                ring.position.y = -2.35 + i * 0.02;
                characterGroup.add(ring);
                daisRings.push(ring);
            }}

            // Cybernetic Torso
            const darkCyberMat = new THREE.MeshStandardMaterial({{ color: 0x0d0d1a, roughness: 0.3, metalness: 0.85 }});
            const chest = new THREE.Mesh(new THREE.BoxGeometry(1.25, 1.15, 0.75), darkCyberMat);
            chest.position.y = 0.2;
            characterGroup.add(chest);

            // Glowing Arc Core Reactor
            const coreGeom = new THREE.OctahedronGeometry(0.26, 1);
            const coreMat = new THREE.MeshStandardMaterial({{ color: 0x06b6d4, emissive: 0x06b6d4, emissiveIntensity: 1.3, wireframe: true }});
            const chestCore = new THREE.Mesh(coreGeom, coreMat);
            chestCore.position.set(0, 0.25, 0.41);
            characterGroup.add(chestCore);

            coreLight = new THREE.PointLight(0x8b5cf6, 2.5, 9);
            coreLight.position.set(0, 0.25, 0.55);
            characterGroup.add(coreLight);

            // Arms in Conductor Pose
            const armL = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.1, 0.95, 12), darkCyberMat);
            armL.position.set(-1.15, 0.2, 0.35);
            armL.rotation.z = -Math.PI / 4;
            armL.rotation.x = Math.PI / 5;
            characterGroup.add(armL);

            const armR = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.1, 0.95, 12), darkCyberMat);
            armR.position.set(1.15, 0.2, 0.35);
            armR.rotation.z = Math.PI / 4;
            armR.rotation.x = Math.PI / 5;
            characterGroup.add(armR);

            const handMat = new THREE.MeshBasicMaterial({{ color: 0x06b6d4 }});
            const handL = new THREE.Mesh(new THREE.SphereGeometry(0.13, 12, 12), handMat);
            handL.position.set(-1.5, -0.15, 0.6);
            characterGroup.add(handL);

            const handR = new THREE.Mesh(new THREE.SphereGeometry(0.13, 12, 12), handMat);
            handR.position.set(1.5, -0.15, 0.6);
            characterGroup.add(handR);

            // Head with Real Portrait Photo Texture
            headMesh = new THREE.Group();
            headMesh.position.y = 1.38;

            new THREE.TextureLoader().load('assets/profile.jpg', (tex) => {{
                tex.generateMipmaps = true;
                const face = new THREE.Mesh(
                    new THREE.PlaneGeometry(0.88, 0.88),
                    new THREE.MeshBasicMaterial({{ map: tex, side: THREE.FrontSide }})
                );
                face.position.z = 0.42;
                headMesh.add(face);
            }});

            const headShell = new THREE.Mesh(new THREE.BoxGeometry(0.92, 0.96, 0.82), darkCyberMat);
            headMesh.add(headShell);

            const visor = new THREE.Mesh(new THREE.TorusGeometry(0.56, 0.025, 16, 32), new THREE.MeshBasicMaterial({{ color: 0x8b5cf6 }}));
            visor.position.z = 0.43;
            headMesh.add(visor);

            // Floating Nameplate
            const namePlate = make3DTextPlate('VOOKA SAI SIDDHARTH', 'SRM KTR CS • AI/ML & COMPILERS', '#8b5cf6', 512, 128, 2.6, 0.65);
            namePlate.position.y = 1.1;
            headMesh.add(namePlate);

            characterGroup.add(headMesh);

            dais.userData = {{ isCharacter: true, label: 'Sai Siddharth' }};
            headShell.userData = {{ isCharacter: true, label: 'Sai Siddharth' }};
            allInteractiveMeshes.push(dais, headShell);

            scene.add(characterGroup);
        }}

        // --- ZONE 2: About 3D Digital Identity Structure ---
        function buildAboutIdentityZone() {{
            aboutZoneGroup = new THREE.Group();
            aboutZoneGroup.position.set(-22, 2.0, 0);

            // Central Identity Core Crystal
            const coreGeom = new THREE.IcosahedronGeometry(1.3, 1);
            const coreMat = new THREE.MeshStandardMaterial({{
                color: 0x8b5cf6,
                emissive: 0x7c3aed,
                emissiveIntensity: 0.8,
                roughness: 0.2,
                metalness: 0.85,
                wireframe: true
            }});
            const identityCore = new THREE.Mesh(coreGeom, coreMat);
            aboutZoneGroup.add(identityCore);

            const innerSphere = new THREE.Mesh(new THREE.SphereGeometry(0.65, 16, 16), new THREE.MeshBasicMaterial({{ color: 0x06b6d4 }}));
            aboutZoneGroup.add(innerSphere);

            // Main Zone Billboard
            const label = make3DTextPlate('3D IDENTITY CORE', 'BIOGRAPHY & CORE COMPETENCIES', '#06b6d4', 420, 112, 2.8, 0.75);
            label.position.y = 2.4;
            aboutZoneGroup.add(label);

            identityCore.userData = {{
                isZoneWarp: true,
                zoneKey: 'about',
                title: 'Vooka Sai Siddharth — Digital Identity',
                desc: 'Undergraduate student at SRM Institute of Science and Technology. Deep passion for autonomous AI agents, custom compilers, and engineering real products used by thousands of students.',
                image: 'assets/profile.jpg',
                tags: ['SRM University', 'Full-Stack Developer', 'AI/ML Enthusiast', 'Compiler Engineer'],
                highlights: [
                    '2nd Year B.Tech Computer Science and Engineering @ SRM KTR',
                    'Creator of Creatorlang programming language and VSS-Lang compiler',
                    'Engineered VSS Self-Deciding Agent with sub-15ms decision latency in PyTorch',
                    'Shipped campus platforms serving 1,200+ undergraduate peers'
                ]
            }};
            allInteractiveMeshes.push(identityCore);

            // 5 Orbital Competency Nodes
            COMPETENCIES.forEach((comp, idx) => {{
                const nodePos = new THREE.Vector3(...comp.offset);
                const nodeGroup = new THREE.Group();
                nodeGroup.position.copy(nodePos);

                const nodeGeom = new THREE.OctahedronGeometry(0.45, 0);
                const nodeMat = new THREE.MeshStandardMaterial({{
                    color: comp.color,
                    emissive: comp.color,
                    emissiveIntensity: 0.7,
                    roughness: 0.2,
                    metalness: 0.8
                }});
                const nodeMesh = new THREE.Mesh(nodeGeom, nodeMat);
                nodeGroup.add(nodeMesh);

                const nodeLabel = make3DTextPlate(comp.name.toUpperCase(), 'COMPETENCY NODE', comp.color, 360, 96, 2.0, 0.53);
                nodeLabel.position.y = 0.75;
                nodeGroup.add(nodeLabel);

                nodeMesh.userData = {{
                    isCompetency: true,
                    comp: comp,
                    labelMesh: nodeLabel,
                    parentGroup: nodeGroup
                }};

                allInteractiveMeshes.push(nodeMesh, nodeLabel);
                aboutZoneGroup.add(nodeGroup);

                // Laser Conduit connecting to Central Core
                const conduitGeom = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), nodePos]);
                const conduitMat = new THREE.LineBasicMaterial({{ color: comp.color, transparent: true, opacity: 0.5, linewidth: 2 }});
                const conduit = new THREE.Line(conduitGeom, conduitMat);
                aboutZoneGroup.add(conduit);
            }});

            scene.add(aboutZoneGroup);
        }}

        // --- ZONE 3: Skills 3D Spatial Architecture ---
        function buildSkillsArchitectureZone() {{
            skillsZoneGroup = new THREE.Group();

            Object.entries(SKILLS_DATA).forEach(([key, cl]) => {{
                const center = new THREE.Vector3(...cl.center);
                const clGroup = new THREE.Group();
                clGroup.position.copy(center);

                // Pylon Structure
                const pylonGeom = new THREE.CylinderGeometry(0.5, 0.8, 1.8, 8);
                const pylonMat = new THREE.MeshStandardMaterial({{
                    color: cl.color,
                    emissive: cl.color,
                    emissiveIntensity: 0.5,
                    wireframe: true
                }});
                const pylon = new THREE.Mesh(pylonGeom, pylonMat);
                clGroup.add(pylon);

                const ring = new THREE.Mesh(
                    new THREE.TorusGeometry(1.6, 0.03, 16, 48),
                    new THREE.MeshBasicMaterial({{ color: cl.color, transparent: true, opacity: 0.75 }})
                );
                ring.rotation.x = Math.PI / 2;
                clGroup.add(ring);

                const clLabel = make3DTextPlate(cl.title.toUpperCase(), 'TECH CLUSTER', cl.color, 420, 112, 2.6, 0.7);
                clLabel.position.y = 1.6;
                clGroup.add(clLabel);

                pylon.userData = {{
                    isSkillCluster: true,
                    clusterKey: key,
                    clusterData: cl
                }};
                allInteractiveMeshes.push(pylon);

                // Satellite Skill Spheres
                cl.items.forEach((skillName, sIdx) => {{
                    const angle = (sIdx / cl.items.length) * Math.PI * 2;
                    const radius = 2.4 + (sIdx % 2) * 0.5;
                    const sx = Math.cos(angle) * radius;
                    const sz = Math.sin(angle) * radius;
                    const sy = Math.sin(angle * 2) * 0.4;

                    const sGeom = new THREE.SphereGeometry(0.22, 12, 12);
                    const sMat = new THREE.MeshStandardMaterial({{
                        color: cl.color,
                        emissive: cl.color,
                        emissiveIntensity: 0.4,
                        roughness: 0.3
                    }});
                    const sMesh = new THREE.Mesh(sGeom, sMat);
                    sMesh.position.set(sx, sy, sz);
                    clGroup.add(sMesh);

                    const sLabel = make3DTextPlate(skillName, 'VERIFIED SKILL', cl.color, 256, 80, 1.3, 0.4);
                    sLabel.position.set(sx, sy + 0.42, sz);
                    clGroup.add(sLabel);

                    sMesh.userData = {{
                        isSkillNode: true,
                        skillName: skillName,
                        clusterTitle: cl.title,
                        color: cl.color,
                        parentGroup: clGroup
                    }};
                    allInteractiveMeshes.push(sMesh, sLabel);

                    // Connecting thin wire
                    const wireGeom = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(sx, sy, sz)]);
                    const wireMat = new THREE.LineBasicMaterial({{ color: cl.color, transparent: true, opacity: 0.25 }});
                    clGroup.add(new THREE.Line(wireGeom, wireMat));
                }});

                skillsZoneGroup.add(clGroup);
            }});

            scene.add(skillsZoneGroup);
        }}

        // --- ZONE 4: Flagship Projects Exhibition Pavilions ---
        function buildProjectsExhibitionZone() {{
            projectsZoneGroup = new THREE.Group();

            FLAGSHIP_PROJECTS.forEach((proj, idx) => {{
                const pGroup = new THREE.Group();
                pGroup.position.set(...proj.pos);

                // Architectural Pavilion Base & Pillar
                const baseGeom = new THREE.CylinderGeometry(1.2, 1.5, 0.35, 16);
                const baseMat = new THREE.MeshStandardMaterial({{ color: 0x090915, roughness: 0.3, metalness: 0.8 }});
                const baseMesh = new THREE.Mesh(baseGeom, baseMat);
                baseMesh.position.y = -1.2;
                pGroup.add(baseMesh);

                // Rotating Crystalline Project Monolith
                const coreGeom = new THREE.BoxGeometry(1.1, 1.6, 0.8);
                const coreMat = new THREE.MeshStandardMaterial({{
                    color: proj.color,
                    emissive: proj.color,
                    emissiveIntensity: 0.8,
                    roughness: 0.2,
                    metalness: 0.85,
                    wireframe: true
                }});
                const coreMesh = new THREE.Mesh(coreGeom, coreMat);
                pGroup.add(coreMesh);

                // Inner Hologram Diamond
                const innerD = new THREE.Mesh(
                    new THREE.OctahedronGeometry(0.45, 0),
                    new THREE.MeshBasicMaterial({{ color: 0xffffff }})
                );
                pGroup.add(innerD);

                // Floating Orbital Rings
                const ring = new THREE.Mesh(
                    new THREE.TorusGeometry(1.3, 0.025, 16, 48),
                    new THREE.MeshBasicMaterial({{ color: proj.color, transparent: true, opacity: 0.8 }})
                );
                ring.rotation.x = Math.PI / 2.5;
                pGroup.add(ring);

                // 3D Billboard Label
                const label = make3DTextPlate(proj.title.toUpperCase(), proj.badge.toUpperCase(), proj.color, 460, 116, 2.9, 0.72);
                label.position.y = 1.6;
                pGroup.add(label);

                coreMesh.userData = {{
                    isFlagshipProject: true,
                    project: proj,
                    parentGroup: pGroup,
                    coreMesh: coreMesh,
                    labelMesh: label
                }};
                baseMesh.userData = coreMesh.userData;

                allInteractiveMeshes.push(coreMesh, label, baseMesh);
                projectsZoneGroup.add(pGroup);
            }});

            scene.add(projectsZoneGroup);
        }}

        // --- ZONE 5: 3D Spatial Timeline Highway ---
        function buildTimelineZone() {{
            timelineZoneGroup = new THREE.Group();

            // 3D Spline Guide
            const splinePoints = TIMELINE_DATA.map(t => new THREE.Vector3(...t.pos));
            const curve = new THREE.CatmullRomCurve3(splinePoints);
            const tubeGeom = new THREE.TubeGeometry(curve, 40, 0.08, 8, false);
            const tubeMat = new THREE.MeshBasicMaterial({{ color: 0x8b5cf6, transparent: true, opacity: 0.6 }});
            timelineZoneGroup.add(new THREE.Mesh(tubeGeom, tubeMat));

            TIMELINE_DATA.forEach((t, idx) => {{
                const mGroup = new THREE.Group();
                mGroup.position.set(...t.pos);

                // Milestone Crystal Pylon
                const pylonGeom = new THREE.CylinderGeometry(0.2, 0.35, 1.4, 6);
                const pylonMat = new THREE.MeshStandardMaterial({{
                    color: t.color,
                    emissive: t.color,
                    emissiveIntensity: 0.7,
                    roughness: 0.2,
                    metalness: 0.85
                }});
                const pylon = new THREE.Mesh(pylonGeom, pylonMat);
                mGroup.add(pylon);

                const beacon = new THREE.Mesh(
                    new THREE.SphereGeometry(0.18, 12, 12),
                    new THREE.MeshBasicMaterial({{ color: 0xffffff }})
                );
                beacon.position.y = 0.85;
                mGroup.add(beacon);

                const label = make3DTextPlate(t.year, t.title.toUpperCase(), t.color, 384, 112, 2.3, 0.67);
                label.position.y = 1.4;
                mGroup.add(label);

                pylon.userData = {{
                    isTimelineMilestone: true,
                    milestone: t,
                    parentGroup: mGroup,
                    labelMesh: label
                }};
                allInteractiveMeshes.push(pylon, label);
                timelineZoneGroup.add(mGroup);
            }});

            scene.add(timelineZoneGroup);
        }}

        // --- ZONE 6: Distinctions & Achievements Pedestals ---
        function buildAchievementsZone() {{
            achievementsZoneGroup = new THREE.Group();

            ACHIEVEMENTS_DATA.forEach((ach, idx) => {{
                const achGroup = new THREE.Group();
                achGroup.position.set(...ach.pos);

                // Pedestal
                const pedGeom = new THREE.BoxGeometry(1.6, 0.25, 1.2);
                const pedMat = new THREE.MeshStandardMaterial({{ color: 0x090915, roughness: 0.3, metalness: 0.8 }});
                const pedestal = new THREE.Mesh(pedGeom, pedMat);
                pedestal.position.y = -0.8;
                achGroup.add(pedestal);

                // Trophy Crystal
                const trophyGeom = new THREE.DodecahedronGeometry(0.65, 0);
                const trophyMat = new THREE.MeshStandardMaterial({{
                    color: ach.color,
                    emissive: ach.color,
                    emissiveIntensity: 0.8,
                    roughness: 0.15,
                    metalness: 0.9,
                    wireframe: true
                }});
                const trophy = new THREE.Mesh(trophyGeom, trophyMat);
                achGroup.add(trophy);

                const innerOrb = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 16), new THREE.MeshBasicMaterial({{ color: 0xffffff }}));
                achGroup.add(innerOrb);

                const label = make3DTextPlate(ach.metric, ach.title.toUpperCase(), ach.color, 420, 112, 2.6, 0.7);
                label.position.y = 1.35;
                achGroup.add(label);

                trophy.userData = {{
                    isAchievement: true,
                    achievement: ach,
                    parentGroup: achGroup,
                    labelMesh: label
                }};
                allInteractiveMeshes.push(trophy, label);
                achievementsZoneGroup.add(achGroup);
            }});

            scene.add(achievementsZoneGroup);
        }}

        // --- ZONE 7: Communication Gateway (Contact) ---
        function buildContactGatewayZone() {{
            contactZoneGroup = new THREE.Group();
            contactZoneGroup.position.set(0, -22, 10);

            // Laser Gateway Portal Frame
            const frameL = new THREE.Mesh(new THREE.BoxGeometry(0.35, 4.2, 0.35), new THREE.MeshStandardMaterial({{ color: 0x06b6d4, emissive: 0x06b6d4, emissiveIntensity: 0.8 }}));
            frameL.position.set(-2.2, 0, 0);
            contactZoneGroup.add(frameL);

            const frameR = new THREE.Mesh(new THREE.BoxGeometry(0.35, 4.2, 0.35), new THREE.MeshStandardMaterial({{ color: 0x06b6d4, emissive: 0x06b6d4, emissiveIntensity: 0.8 }}));
            frameR.position.set(2.2, 0, 0);
            contactZoneGroup.add(frameR);

            const frameTop = new THREE.Mesh(new THREE.BoxGeometry(4.75, 0.35, 0.35), new THREE.MeshStandardMaterial({{ color: 0x8b5cf6, emissive: 0x8b5cf6, emissiveIntensity: 0.8 }}));
            frameTop.position.set(0, 2.1, 0);
            contactZoneGroup.add(frameTop);

            // Holographic Laser Curtain
            const curtainGeom = new THREE.PlaneGeometry(4.0, 3.8);
            const curtainMat = new THREE.MeshBasicMaterial({{
                color: 0x06b6d4,
                transparent: true,
                opacity: 0.18,
                side: THREE.DoubleSide
            }});
            const curtain = new THREE.Mesh(curtainGeom, curtainMat);
            contactZoneGroup.add(curtain);

            // Center Telemetry Terminal Core
            const coreGeom = new THREE.IcosahedronGeometry(0.65, 1);
            const coreMat = new THREE.MeshStandardMaterial({{
                color: 0x10b981,
                emissive: 0x10b981,
                emissiveIntensity: 0.9,
                wireframe: true
            }});
            const terminalCore = new THREE.Mesh(coreGeom, coreMat);
            contactZoneGroup.add(terminalCore);

            const label = make3DTextPlate('COMMUNICATION GATEWAY', 'CLICK TO TRANSMIT DISPATCH', '#10b981', 460, 116, 2.8, 0.7);
            label.position.y = 2.8;
            contactZoneGroup.add(label);

            terminalCore.userData = {{
                isContactGateway: true
            }};
            curtain.userData = terminalCore.userData;
            allInteractiveMeshes.push(terminalCore, curtain, label);

            scene.add(contactZoneGroup);
        }}

        // --- ZONE 8: Entire 83-Neuron Repository Constellation ---
        function build83RepoNeuralNetwork() {{
            const handL = new THREE.Vector3(-1.5, -0.15, 0.6);
            const handR = new THREE.Vector3(1.5, -0.15, 0.6);

            const clusterHubs = {{}};

            Object.entries(NEURAL_GRAPH.clusters).forEach(([catKey, cfg]) => {{
                const hubCenter = new THREE.Vector3(...cfg.center);

                const hubGeom = new THREE.IcosahedronGeometry(0.85, 1);
                const hubMat = new THREE.MeshStandardMaterial({{
                    color: cfg.color,
                    emissive: cfg.color,
                    emissiveIntensity: 0.6,
                    wireframe: true,
                    roughness: 0.2
                }});
                const hubMesh = new THREE.Mesh(hubGeom, hubMat);
                hubMesh.position.copy(hubCenter);

                const inner = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), new THREE.MeshBasicMaterial({{ color: 0xffffff }}));
                hubMesh.add(inner);

                const ring = new THREE.Mesh(
                    new THREE.TorusGeometry(1.25, 0.02, 16, 48),
                    new THREE.MeshBasicMaterial({{ color: cfg.color, transparent: true, opacity: 0.7 }})
                );
                hubMesh.add(ring);

                const hubLabel = make3DTextPlate(cfg.name.toUpperCase(), '83-REPO BRAIN CLUSTER', cfg.hex, 440, 112, 2.6, 0.65);
                hubLabel.position.y = 1.35;
                hubMesh.add(hubLabel);

                hubMesh.userData = {{ isHub: true, clusterKey: catKey, clusterName: cfg.name, labelMesh: hubLabel }};
                allInteractiveMeshes.push(hubMesh);
                clusterHubMeshes.push(hubMesh);
                scene.add(hubMesh);

                clusterHubs[catKey] = {{ hubMesh, center: hubCenter, color: cfg.color, nodes: [] }};

                // Beam connecting to Siddharth's cybernetic hand
                const origin = (hubCenter.x < 0) ? handL : handR;
                const mid = new THREE.Vector3((origin.x + hubCenter.x) * 0.5, (origin.y + hubCenter.y) * 0.5 + 1.2, (origin.z + hubCenter.z) * 0.5);
                const curve = new THREE.QuadraticBezierCurve3(origin, mid, hubCenter);
                const lineGeom = new THREE.BufferGeometry().setFromPoints(curve.getPoints(40));
                const lineMat = new THREE.LineBasicMaterial({{ color: cfg.color, transparent: true, opacity: 0.75, linewidth: 2 }});
                scene.add(new THREE.Line(lineGeom, lineMat));

                const photon = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 12), new THREE.MeshBasicMaterial({{ color: 0xffffff }}));
                scene.add(photon);
                actionPotentials.push({{ curve, photon, speed: 0.35 }});
            }});

            NEURAL_GRAPH.nodes.forEach((repo, idx) => {{
                const nodePos = new THREE.Vector3(...repo.pos);
                const clusterCfg = NEURAL_GRAPH.clusters[repo.cluster];
                const clusterColor = clusterCfg.color;

                const neuronGroup = new THREE.Group();
                neuronGroup.position.copy(nodePos);

                const isFlagship = (repo.name === 'vss-self-deciding-agent' || repo.name === 'academia-nexus' || repo.name === 'creatorlang' || repo.name === 'hand-gesture' || repo.name === 'classivo3');
                const somaSize = isFlagship ? 0.44 : 0.28;

                const somaGeom = new THREE.SphereGeometry(somaSize, 16, 16);
                const somaMat = new THREE.MeshStandardMaterial({{
                    color: clusterColor,
                    emissive: clusterColor,
                    emissiveIntensity: isFlagship ? 0.9 : 0.5,
                    roughness: 0.2,
                    metalness: 0.8
                }});
                const soma = new THREE.Mesh(somaGeom, somaMat);
                neuronGroup.add(soma);

                const shellGeom = new THREE.OctahedronGeometry(somaSize * 1.35, 0);
                const shellMat = new THREE.MeshBasicMaterial({{ color: clusterColor, wireframe: true, transparent: true, opacity: 0.4 }});
                const shell = new THREE.Mesh(shellGeom, shellMat);
                neuronGroup.add(shell);

                const displayName = repo.name.length > 20 ? repo.name.slice(0, 18) + '..' : repo.name;
                const labelMesh = make3DTextPlate(displayName, repo.language.toUpperCase(), clusterCfg.hex, 360, 96, isFlagship ? 2.1 : 1.6, isFlagship ? 0.58 : 0.44);
                labelMesh.position.y = somaSize + 0.5;
                neuronGroup.add(labelMesh);

                soma.userData = {{
                    isNeuron: true,
                    repo: repo,
                    clusterCfg: clusterCfg,
                    parentGroup: neuronGroup,
                    shellMesh: shell,
                    labelMesh: labelMesh,
                    synapses: []
                }};
                labelMesh.userData = soma.userData;

                allInteractiveMeshes.push(soma, labelMesh);
                scene.add(neuronGroup);

                clusterHubs[repo.cluster].nodes.push({{ soma, pos: nodePos }});

                // Laser Synapse to Hub
                const hubPos = clusterHubs[repo.cluster].center;
                const synGeom = new THREE.BufferGeometry().setFromPoints([hubPos, nodePos]);
                const synMat = new THREE.LineBasicMaterial({{
                    color: clusterColor,
                    transparent: true,
                    opacity: isFlagship ? 0.7 : 0.3,
                    linewidth: isFlagship ? 2 : 1
                }});
                const synLine = new THREE.Line(synGeom, synMat);
                scene.add(synLine);
                allSynapseLines.push(synLine);
                soma.userData.synapses.push(synLine);

                if (idx % 2 === 0) {{
                    const synCurve = new THREE.LineCurve3(hubPos, nodePos);
                    const synPhoton = new THREE.Mesh(new THREE.SphereGeometry(0.06, 8, 8), new THREE.MeshBasicMaterial({{ color: 0xffffff }}));
                    scene.add(synPhoton);
                    actionPotentials.push({{ curve: synCurve, photon: synPhoton, speed: 0.15 + (idx % 4) * 0.05 }});
                }}
            }});
        }}

        // --- Warp Camera to Specified Spatial Zone ---
        function warpToZone(zoneKey) {{
            const z = SPATIAL_ZONES[zoneKey];
            if (!z) return;

            activeZoneKey = zoneKey;
            playSound(680, 0.09, 'sine', 0.04);

            // Update Header Navigation Pill Styles
            document.querySelectorAll('.nav-pill').forEach(p => {{
                p.className = 'nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-gray-400 hover:text-white hover:bg-white/5 flex items-center space-x-1.5';
            }});
            const activePill = document.getElementById(`pill-${{zoneKey}}`);
            if (activePill) {{
                activePill.className = 'nav-pill px-3 py-1.5 rounded-xl text-xs font-mono tracking-wide transition-all text-white font-bold bg-brand-600 shadow-md shadow-brand-500/30 flex items-center space-x-1.5';
            }}

            // Update Mobile Nav
            document.querySelectorAll('.m-nav-btn').forEach(btn => {{
                btn.className = 'm-nav-btn px-2.5 py-1.5 rounded-xl text-[11px] font-mono text-gray-400 hover:text-white flex items-center space-x-1 whitespace-nowrap';
            }});

            // Toggle Hero Overlay visibility
            const heroOverlay = document.getElementById('hero-overlay');
            if (zoneKey === 'hero') {{
                heroOverlay.classList.remove('opacity-0', 'pointer-events-none');
                heroOverlay.classList.add('opacity-100');
            }} else {{
                heroOverlay.classList.remove('opacity-100');
                heroOverlay.classList.add('opacity-0', 'pointer-events-none');
            }}

            // Update Radar HUD Tag
            const radarTag = document.getElementById('current-zone-tag');
            if (radarTag) radarTag.innerText = z.name.toUpperCase();

            // Smooth Camera Glide via TWEEN
            new TWEEN.Tween(camera.position)
                .to({{ x: z.pos.x, y: z.pos.y, z: z.pos.z }}, 1400)
                .easing(TWEEN.Easing.Cubic.InOut)
                .start();

            new TWEEN.Tween(controls.target)
                .to({{ x: z.target.x, y: z.target.y, z: z.target.z }}, 1400)
                .easing(TWEEN.Easing.Cubic.InOut)
                .start();

            // If contact zone, open contact modal after glide
            if (zoneKey === 'contact') {{
                setTimeout(openContactModal, 700);
            }} else {{
                closeContactModal();
            }}
        }}

        // --- Pointer Move Raycasting & Hover Feedback ---
        function onPointerMove(e) {{
            mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

            if (headMesh && activeZoneKey === 'hero') {{
                headMesh.rotation.y = mouse.x * 0.45;
                headMesh.rotation.x = -mouse.y * 0.3;
            }}

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(allInteractiveMeshes, false);

            if (intersects.length > 0) {{
                const obj = intersects[0].object;
                if (hoveredMesh !== obj) {{
                    resetHoveredMesh();
                    hoveredMesh = obj;
                    reticle.classList.add('active');
                    playSound(650, 0.03, 'triangle', 0.025);

                    if (obj.userData) {{
                        if (obj.userData.isNeuron) {{
                            obj.userData.parentGroup.scale.set(1.2, 1.2, 1.2);
                            obj.userData.synapses.forEach(l => l.material.opacity = 0.9);
                        }} else if (obj.userData.isFlagshipProject) {{
                            obj.userData.parentGroup.scale.set(1.15, 1.15, 1.15);
                        }} else if (obj.userData.isCompetency) {{
                            obj.userData.parentGroup.scale.set(1.25, 1.25, 1.25);
                        }}
                    }}
                }}
            }} else {{
                if (hoveredMesh) {{
                    resetHoveredMesh();
                    hoveredMesh = null;
                    reticle.classList.remove('active');
                }}
            }}
        }}

        function resetHoveredMesh() {{
            if (!hoveredMesh || !hoveredMesh.userData) return;
            if (hoveredMesh.userData.isNeuron) {{
                hoveredMesh.userData.parentGroup.scale.set(1, 1, 1);
                hoveredMesh.userData.synapses.forEach(l => l.material.opacity = 0.3);
            }} else if (hoveredMesh.userData.isFlagshipProject) {{
                hoveredMesh.userData.parentGroup.scale.set(1, 1, 1);
            }} else if (hoveredMesh.userData.isCompetency) {{
                hoveredMesh.userData.parentGroup.scale.set(1, 1, 1);
            }}
        }}

        // --- Click Raycasting to Inspect 3D Objects ---
        function onClick(e) {{
            if (e.target.closest('header, nav, aside, #contact-modal, #repo-search, .glass-panel')) return;

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(allInteractiveMeshes, false);

            if (intersects.length > 0) {{
                const obj = intersects[0].object;
                playSound(880, 0.1, 'sine', 0.04);

                if (obj.userData.isNeuron) {{
                    openNeuronDrawer(obj.userData.repo, obj.userData.clusterCfg);
                    smoothFlyCamera(obj.userData.parentGroup.position.clone().add(new THREE.Vector3(0, 0, 3.8)), obj.userData.parentGroup.position);
                }} else if (obj.userData.isFlagshipProject) {{
                    openProjectDrawer(obj.userData.project);
                    smoothFlyCamera(obj.userData.parentGroup.position.clone().add(new THREE.Vector3(0, 0, 5.0)), obj.userData.parentGroup.position);
                }} else if (obj.userData.isCompetency) {{
                    openCompetencyDrawer(obj.userData.comp);
                }} else if (obj.userData.isTimelineMilestone) {{
                    openTimelineDrawer(obj.userData.milestone);
                }} else if (obj.userData.isAchievement) {{
                    openAchievementDrawer(obj.userData.achievement);
                }} else if (obj.userData.isContactGateway) {{
                    openContactModal();
                }} else if (obj.userData.isCharacter) {{
                    warpToZone('hero');
                }} else if (obj.userData.isZoneWarp) {{
                    warpToZone(obj.userData.zoneKey);
                }}
            }}
        }}

        function smoothFlyCamera(targetPos, lookAtPos) {{
            new TWEEN.Tween(camera.position)
                .to({{ x: targetPos.x, y: targetPos.y, z: targetPos.z }}, 1100)
                .easing(TWEEN.Easing.Cubic.Out)
                .start();

            new TWEEN.Tween(controls.target)
                .to({{ x: lookAtPos.x, y: lookAtPos.y, z: lookAtPos.z }}, 1100)
                .easing(TWEEN.Easing.Cubic.Out)
                .start();
        }}

        // --- Keyboard Shortcuts ---
        function onKeyDown(e) {{
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

            const key = e.key.toLowerCase();
            if (key === '1' || key === 'h') warpToZone('hero');
            else if (key === '2') warpToZone('about');
            else if (key === '3') warpToZone('skills');
            else if (key === '4') warpToZone('projects');
            else if (key === '5') warpToZone('timeline');
            else if (key === '6') warpToZone('achievements');
            else if (key === '7') warpToZone('constellation');
            else if (key === '8') warpToZone('contact');
            else if (key === ' ') {{ e.preventDefault(); warpToZone('overview'); }}
            else if (key === 'm') document.getElementById('audio-toggle').click();
            else if (key === 'escape') {{ closeDetailDrawer(); closeContactModal(); }}
        }}

        // --- Holographic Detail Drawer Logic ---
        function openProjectDrawer(proj) {{
            document.getElementById('drawer-dot').style.backgroundColor = proj.color;
            document.getElementById('drawer-tag').innerText = `EXHIBITION // ${{proj.category.toUpperCase()}}`;
            document.getElementById('drawer-tag').style.color = proj.color;
            document.getElementById('drawer-title').innerText = proj.title;
            document.getElementById('drawer-desc').innerText = proj.description;
            document.getElementById('drawer-cluster-name').innerText = proj.category;
            document.getElementById('drawer-github-link').href = proj.github;
            document.getElementById('drawer-clone-btn').setAttribute('data-clone', `${{proj.github}}.git`);
            document.getElementById('drawer-clone-text').innerText = 'Copy git clone command';
            document.getElementById('drawer-img').src = proj.image;

            const badgeBox = document.getElementById('drawer-badges');
            badgeBox.innerHTML = proj.tags.map(t => `
                <span class="px-2.5 py-0.5 rounded-md bg-brand-500/20 text-brand-300 border border-brand-500/30 font-mono text-xs">${{t}}</span>
            `).join('');

            const highlightsBox = document.getElementById('drawer-highlights');
            highlightsBox.innerHTML = proj.highlights.map(h => `
                <div class="flex items-start space-x-2">
                    <i class="fa-solid fa-check text-cyber-emerald mt-0.5 text-xs"></i>
                    <span>${{h}}</span>
                </div>
            `).join('');
            document.getElementById('drawer-highlights-container').classList.remove('hidden');

            document.getElementById('detail-drawer').classList.remove('translate-x-full');
        }}

        function openNeuronDrawer(repo, clusterCfg) {{
            document.getElementById('drawer-dot').style.backgroundColor = clusterCfg.hex;
            document.getElementById('drawer-tag').innerText = `NEURAL SYNAPSE // ${{clusterCfg.name.toUpperCase()}}`;
            document.getElementById('drawer-tag').style.color = clusterCfg.hex;
            document.getElementById('drawer-title').innerText = repo.name;
            document.getElementById('drawer-desc').innerText = repo.description;
            document.getElementById('drawer-cluster-name').innerText = clusterCfg.name;
            document.getElementById('drawer-github-link').href = repo.url;
            document.getElementById('drawer-clone-btn').setAttribute('data-clone', `${{repo.url}}.git`);
            document.getElementById('drawer-clone-text').innerText = 'Copy git clone command';

            let previewImg = 'assets/vss-agent-arch.svg';
            if (repo.name.includes('academia') || repo.name.includes('classivo') || repo.name.includes('skedio')) {{
                previewImg = 'assets/academia-nexus.svg';
            }} else if (repo.name.includes('signal') || repo.name.includes('chat') || repo.name.includes('office')) {{
                previewImg = 'assets/signal-os.svg';
            }} else if (repo.name.includes('gesture') || repo.name.includes('vision') || repo.name.includes('face') || repo.name.includes('draw')) {{
                previewImg = 'assets/vision-suite.svg';
            }} else if (repo.name.includes('creatorlang') || repo.name.includes('lang') || repo.name.includes('devlang')) {{
                previewImg = 'assets/creatorlang.svg';
            }}
            document.getElementById('drawer-img').src = previewImg;

            const badgeBox = document.getElementById('drawer-badges');
            badgeBox.innerHTML = `
                <span class="px-2.5 py-0.5 rounded-md bg-brand-500/20 text-brand-300 border border-brand-500/30">${{repo.language}}</span>
                <span class="px-2.5 py-0.5 rounded-md bg-white/5 text-gray-300 border border-white/10">Connected Neuron</span>
            `;

            document.getElementById('drawer-highlights-container').classList.add('hidden');
            document.getElementById('detail-drawer').classList.remove('translate-x-full');
        }}

        function openCompetencyDrawer(comp) {{
            document.getElementById('drawer-dot').style.backgroundColor = comp.color;
            document.getElementById('drawer-tag').innerText = `COMPETENCY NODE`;
            document.getElementById('drawer-tag').style.color = comp.color;
            document.getElementById('drawer-title').innerText = comp.name;
            document.getElementById('drawer-desc').innerText = comp.desc;
            document.getElementById('drawer-cluster-name').innerText = 'Core Competency';
            document.getElementById('drawer-github-link').href = 'https://github.com/siddharth-1118';
            document.getElementById('drawer-img').src = 'assets/profile.jpg';
            document.getElementById('drawer-highlights-container').classList.add('hidden');
            document.getElementById('detail-drawer').classList.remove('translate-x-full');
        }}

        function openTimelineDrawer(m) {{
            document.getElementById('drawer-dot').style.backgroundColor = m.color;
            document.getElementById('drawer-tag').innerText = `TIMELINE MILESTONE // ${{m.year}}`;
            document.getElementById('drawer-tag').style.color = m.color;
            document.getElementById('drawer-title').innerText = m.title;
            document.getElementById('drawer-desc').innerText = m.description;
            document.getElementById('drawer-cluster-name').innerText = m.institution;
            document.getElementById('drawer-github-link').href = 'https://github.com/siddharth-1118';
            document.getElementById('drawer-img').src = 'assets/profile.jpg';
            document.getElementById('drawer-highlights-container').classList.add('hidden');
            document.getElementById('detail-drawer').classList.remove('translate-x-full');
        }}

        function openAchievementDrawer(ach) {{
            document.getElementById('drawer-dot').style.backgroundColor = ach.color;
            document.getElementById('drawer-tag').innerText = `DISTINCTION // ${{ach.metric}}`;
            document.getElementById('drawer-tag').style.color = ach.color;
            document.getElementById('drawer-title').innerText = ach.title;
            document.getElementById('drawer-desc').innerText = ach.desc;
            document.getElementById('drawer-cluster-name').innerText = ach.subtitle;
            document.getElementById('drawer-github-link').href = 'https://github.com/siddharth-1118';
            document.getElementById('drawer-img').src = 'assets/profile.jpg';
            document.getElementById('drawer-highlights-container').classList.add('hidden');
            document.getElementById('detail-drawer').classList.remove('translate-x-full');
        }}

        function closeDetailDrawer() {{
            playSound(500, 0.05);
            document.getElementById('detail-drawer').classList.add('translate-x-full');
        }}

        function copyDrawerCloneUrl(btn) {{
            playSound(800, 0.08);
            const cloneUrl = btn.getAttribute('data-clone') || 'https://github.com/siddharth-1118/siddharth-1118.git';
            navigator.clipboard.writeText(`git clone ${{cloneUrl}}`);
            document.getElementById('drawer-clone-text').innerText = 'Copied to clipboard!';
            showToast('Git Clone Command Copied!');
            setTimeout(() => {{
                document.getElementById('drawer-clone-text').innerText = 'Copy git clone command';
            }}, 2000);
        }}

        // --- Contact Modal Handlers ---
        function openContactModal() {{
            playSound(750, 0.08);
            const m = document.getElementById('contact-modal');
            m.classList.remove('opacity-0', 'pointer-events-none');
            m.classList.add('opacity-100');
        }}

        function closeContactModal() {{
            const m = document.getElementById('contact-modal');
            m.classList.remove('opacity-100');
            m.classList.add('opacity-0', 'pointer-events-none');
        }}

        function handleContactSubmit(e) {{
            e.preventDefault();
            const name = document.getElementById('contact-name').value;
            const email = document.getElementById('contact-email').value;
            const subject = document.getElementById('contact-subject').value;
            const msg = document.getElementById('contact-message').value;

            playSound(900, 0.15);
            const fb = document.getElementById('contact-feedback');
            fb.className = 'mt-4 p-3 rounded-xl text-xs font-mono text-center bg-cyber-emerald/10 border border-cyber-emerald/30 text-cyber-emerald';
            fb.innerText = 'Transmission encoded. Triggering direct mail client dispatch...';
            fb.classList.remove('hidden');

            setTimeout(() => {{
                const bodyContent = msg + '\\n\\nSender: ' + name + ' (' + email + ')';
                window.location.href = 'mailto:siddharthvooka@gmail.com?subject=' + encodeURIComponent(subject + ' [via 3D Portfolio: ' + name + ']') + '&body=' + encodeURIComponent(bodyContent);
            }}, 600);
        }}

        function copyEmailDirectly() {{
            playSound(800, 0.08);
            navigator.clipboard.writeText('siddharthvooka@gmail.com');
            const lbl = document.getElementById('copy-email-label');
            lbl.innerText = 'Copied!';
            showToast('Email copied: siddharthvooka@gmail.com');
            setTimeout(() => {{ lbl.innerText = 'Copy Email'; }}, 2000);
        }}

        // --- Live Search Across 83 Repositories ---
        function handleSearch(val) {{
            const dropdown = document.getElementById('search-dropdown');
            if (!val.trim()) {{
                dropdown.classList.add('hidden');
                return;
            }}

            const query = val.toLowerCase();
            const matches = [];

            allInteractiveMeshes.forEach(mesh => {{
                if (mesh.userData && mesh.userData.isNeuron) {{
                    const repo = mesh.userData.repo;
                    if (repo.name.toLowerCase().includes(query) || repo.description.toLowerCase().includes(query)) {{
                        matches.push({{
                            name: repo.name,
                            lang: repo.language,
                            action: () => {{
                                openNeuronDrawer(repo, mesh.userData.clusterCfg);
                                smoothFlyCamera(mesh.userData.parentGroup.position.clone().add(new THREE.Vector3(0, 0, 3.8)), mesh.userData.parentGroup.position);
                            }}
                        }});
                    }}
                }}
            }});

            if (matches.length > 0) {{
                dropdown.innerHTML = matches.slice(0, 8).map((m, idx) => `
                    <div onclick="executeSearchMatch(${{idx}})" class="p-2 rounded-lg bg-dark-900/90 hover:bg-brand-600/30 border border-white/5 cursor-pointer flex justify-between items-center text-gray-200 hover:text-white">
                        <span class="truncate pr-2">${{m.name}}</span>
                        <span class="text-[10px] text-brand-400 uppercase font-mono">${{m.lang}}</span>
                    </div>
                `).join('');
                dropdown.classList.remove('hidden');
                window.currentSearchMatches = matches;
            }} else {{
                dropdown.innerHTML = '<div class="p-2 text-gray-500 text-center font-mono">No repository matches found</div>';
                dropdown.classList.remove('hidden');
            }}
        }}

        function executeSearchMatch(idx) {{
            if (window.currentSearchMatches && window.currentSearchMatches[idx]) {{
                window.currentSearchMatches[idx].action();
                document.getElementById('search-dropdown').classList.add('hidden');
                document.getElementById('repo-search').value = '';
            }}
        }}

        // --- 2D Radar Minimap HUD ---
        function initRadarMinimap() {{
            const canvas = document.getElementById('radar-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            canvas.addEventListener('click', (e) => {{
                const rect = canvas.getBoundingClientRect();
                const x = e.clientX - rect.left - 65;
                const y = e.clientY - rect.top - 65;

                // Find closest zone
                let closestKey = 'hero';
                let closestDist = 999999;
                Object.entries(SPATIAL_ZONES).forEach(([k, z]) => {{
                    const zx = z.pos.x * 2.2;
                    const zy = z.pos.z * 2.2;
                    const d = Math.hypot(zx - x, zy - y);
                    if (d < closestDist) {{
                        closestDist = d;
                        closestKey = k;
                    }}
                }});
                warpToZone(closestKey);
            }});
        }}

        function drawRadar() {{
            const canvas = document.getElementById('radar-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;

            ctx.clearRect(0, 0, w, h);

            // Radar rings
            ctx.strokeStyle = 'rgba(139, 92, 246, 0.2)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.arc(w / 2, h / 2, 24, 0, Math.PI * 2);
            ctx.arc(w / 2, h / 2, 48, 0, Math.PI * 2);
            ctx.stroke();

            // Crosshairs
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
            ctx.beginPath();
            ctx.moveTo(w / 2, 0); ctx.lineTo(w / 2, h);
            ctx.moveTo(0, h / 2); ctx.lineTo(w, h / 2);
            ctx.stroke();

            // Draw Zone Points
            Object.entries(SPATIAL_ZONES).forEach(([key, z]) => {{
                const px = w / 2 + z.pos.x * 1.5;
                const py = h / 2 + z.pos.z * 1.5;
                ctx.fillStyle = (key === activeZoneKey) ? '#06b6d4' : '#8b5cf6';
                ctx.beginPath();
                ctx.arc(px, py, (key === activeZoneKey) ? 4.5 : 2.5, 0, Math.PI * 2);
                ctx.fill();
            }});

            // Draw Camera Position & Heading
            const camX = w / 2 + camera.position.x * 1.5;
            const camY = h / 2 + camera.position.z * 1.5;
            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(camX, camY, 3, 0, Math.PI * 2);
            ctx.fill();
        }}

        function onWindowResize() {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }}

        // --- Master 60 FPS Animation Loop ---
        function animate() {{
            requestAnimationFrame(animate);
            TWEEN.update();

            const time = clock.getElapsedTime();
            controls.update();

            // Subtle Avatar breathing & core pulse
            if (characterGroup) {{
                characterGroup.position.y = Math.sin(time * 1.6) * 0.12;
            }}

            daisRings.forEach((r, idx) => {{
                r.rotation.z += (idx % 2 === 0 ? 0.008 : -0.008);
            }});

            if (coreLight) {{
                coreLight.intensity = 2.0 + Math.sin(time * 3) * 0.8;
            }}

            // Rotate Crystalline Zones & Pavilions
            if (aboutZoneGroup) aboutZoneGroup.rotation.y = Math.sin(time * 0.3) * 0.08;
            if (projectsZoneGroup) {{
                projectsZoneGroup.children.forEach((p, idx) => {{
                    const core = p.children[1];
                    if (core) core.rotation.y += 0.012;
                }});
            }}
            if (achievementsZoneGroup) {{
                achievementsZoneGroup.children.forEach(a => {{
                    const trophy = a.children[1];
                    if (trophy) {{
                        trophy.rotation.y += 0.015;
                        trophy.rotation.x += 0.008;
                    }}
                }});
            }}

            // Billboards auto-orient towards camera
            allInteractiveMeshes.forEach(mesh => {{
                if (mesh.userData && mesh.userData.labelMesh) {{
                    mesh.userData.labelMesh.quaternion.copy(camera.quaternion);
                }}
            }});

            clusterHubMeshes.forEach(hub => {{
                hub.rotation.y += 0.01;
                hub.rotation.x += 0.005;
                if (hub.userData.labelMesh) hub.userData.labelMesh.quaternion.copy(camera.quaternion);
            }});

            // Action potential photons traveling along laser synapses
            actionPotentials.forEach(ap => {{
                const t = (time * ap.speed) % 1.0;
                const p = ap.curve.getPointAt(t);
                ap.photon.position.copy(p);
            }});

            drawRadar();
            renderer.render(scene, camera);
        }}

        window.addEventListener('DOMContentLoaded', initUniverse);
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated master 3D index.html ({len(html_content)} bytes)!")
