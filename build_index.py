import json

with open('repos_neural_graph.json', encoding='utf-8') as f:
    graph_data = json.load(f)

graph_json_str = json.dumps(graph_data)

html_template = f'''<!DOCTYPE html>
<html lang="en" class="h-full overflow-hidden select-none">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Sai Siddharth | 3D Neural Repository Universe</title>
    <meta name="description" content="Full 3D Neural Network Universe of Vooka Sai Siddharth. 3D Character in the center connected via synaptic take-lines to all 83+ open-source repositories.">
    
    <!-- Open Graph & Social -->
    <meta property="og:title" content="Sai Siddharth | 3D Neural Repository Universe">
    <meta property="og:description" content="Interactive 3D neural brain connecting Sai Siddharth to 83+ open-source repositories and AI architectures.">
    <meta property="og:image" content="assets/profile.jpg">
    <meta property="og:type" content="website">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Outfit:wght@300;400;600;800;900&family=Space+Grotesk:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
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
                        }},
                        dark: {{
                            950: '#030306',
                            900: '#07070d',
                            850: '#0d0d17',
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
            background: rgba(7, 7, 13, 0.82);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6);
        }}

        .cursor-target {{
            pointer-events: none; position: fixed; width: 34px; height: 34px;
            border: 1.5px dashed rgba(6, 182, 212, 0.6); border-radius: 50%;
            transform: translate(-50%, -50%); transition: width 0.2s, height 0.2s, opacity 0.2s;
            z-index: 50; opacity: 0;
        }}
        .cursor-target.active {{ opacity: 1; width: 48px; height: 48px; border-color: #a78bfa; }}

        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: #07070d; }}
        ::-webkit-scrollbar-thumb {{ background: #7c3aed; border-radius: 999px; }}
    </style>
</head>
<body class="relative w-full h-full">

    <!-- 3D Canvas & Overlays -->
    <canvas id="canvas3d"></canvas>
    <div class="film-grain"></div>
    <div id="reticle" class="cursor-target"></div>

    <!-- Top Navigation HUD -->
    <header class="fixed top-0 left-0 right-0 z-30 px-6 py-4 flex justify-between items-center pointer-events-none">
        <div class="flex items-center space-x-3 pointer-events-auto">
            <div onclick="flyToTarget('architect')" class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-brand-600 via-brand-500 to-cyber-cyan p-[1.5px] cursor-pointer shadow-lg shadow-brand-500/25 hover:scale-105 transition-all">
                <div class="w-full h-full bg-dark-950 rounded-[14px] flex items-center justify-center font-display font-black text-white text-base">
                    VSS
                </div>
            </div>
            <div class="flex flex-col">
                <h1 class="font-display font-black text-lg tracking-wider text-white flex items-center leading-tight">
                    VOOKA SAI SIDDHARTH
                    <span class="w-2 h-2 rounded-full bg-cyber-emerald ml-2 animate-ping"></span>
                    <span class="w-2 h-2 rounded-full bg-cyber-emerald -ml-2"></span>
                </h1>
                <span class="text-[10px] font-mono tracking-widest text-brand-300/80 uppercase">
                    3D Neural Brain • 83 Repos Connected
                </span>
            </div>
        </div>

        <div class="flex items-center space-x-3 pointer-events-auto">
            <div class="hidden md:flex items-center space-x-4 glass-panel px-4 py-2 rounded-xl text-xs font-mono">
                <div class="flex items-center space-x-1.5 text-gray-300">
                    <i class="fa-solid fa-network-wired text-brand-400"></i>
                    <span>NEURAL SYNAPSES: <strong class="text-white">83 NODES</strong></span>
                </div>
                <div class="w-px h-3 bg-white/20"></div>
                <div class="flex items-center space-x-1.5 text-gray-300">
                    <i class="fa-solid fa-bolt text-cyber-cyan"></i>
                    <span>RENDER: <strong class="text-cyber-emerald">60 FPS</strong></span>
                </div>
            </div>

            <!-- Sound FX Toggle -->
            <button id="audio-toggle" class="glass-panel w-10 h-10 rounded-xl flex items-center justify-center text-gray-300 hover:text-brand-300 hover:border-brand-500/50 transition-all text-sm" title="Toggle 3D Audio FX">
                <i class="fa-solid fa-volume-high" id="audio-icon"></i>
            </button>

            <!-- Overview Button -->
            <button onclick="flyToTarget('overview')" class="glass-panel px-3.5 py-2 rounded-xl flex items-center space-x-2 text-xs font-mono text-gray-300 hover:text-white hover:border-brand-500 transition-all" title="Return to Full Overview">
                <i class="fa-solid fa-compass text-brand-400"></i>
                <span class="hidden sm:inline">Overview</span>
            </button>

            <!-- GitHub Link -->
            <a href="https://github.com/siddharth-1118" target="_blank" rel="noopener noreferrer" class="glass-panel px-3.5 py-2 rounded-xl flex items-center space-x-2 text-xs font-mono text-brand-300 hover:text-white hover:bg-brand-600/20 hover:border-brand-400 transition-all">
                <i class="fa-brands fa-github text-sm"></i>
                <span class="hidden sm:inline">GitHub</span>
            </a>
        </div>
    </header>

    <!-- Top Right: Instant 3D Node Search & Filter -->
    <div class="fixed top-20 right-6 z-30 w-72 pointer-events-auto">
        <div class="glass-panel p-2 rounded-2xl border border-white/10 shadow-2xl">
            <div class="relative">
                <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs"></i>
                <input type="text" id="repo-search" oninput="handleSearch(this.value)" placeholder="Search 83 neurons (e.g. agent, skedio)..." class="w-full bg-dark-950/80 rounded-xl pl-8 pr-3 py-1.5 text-xs font-mono text-white placeholder-gray-500 border border-white/5 focus:outline-none focus:border-brand-500 transition-all">
            </div>
            <div id="search-dropdown" class="hidden mt-2 max-h-52 overflow-y-auto space-y-1 font-mono text-xs"></div>
        </div>
    </div>

    <!-- Floating 3D Interaction Guide Pill -->
    <div class="fixed bottom-20 left-1/2 -translate-x-1/2 z-20 pointer-events-none opacity-80" id="interaction-hint">
        <div class="glass-panel px-4 py-1.5 rounded-full text-[11px] font-mono tracking-widest uppercase text-gray-300 flex items-center space-x-2 border border-white/10">
            <i class="fa-solid fa-hand-pointer text-brand-400"></i>
            <span>Drag to Orbit • Scroll to Zoom • Click any 3D Neuron or Siddharth to Inspect</span>
        </div>
    </div>

    <!-- Bottom Neural Lobe Camera Presets -->
    <nav class="fixed bottom-5 left-1/2 -translate-x-1/2 z-30 max-w-[96vw] pointer-events-auto">
        <div class="glass-panel px-3 py-2 sm:px-4 sm:py-2.5 rounded-2xl flex items-center gap-1.5 sm:gap-2 overflow-x-auto max-w-full border border-white/10 shadow-2xl">
            <button onclick="flyToTarget('architect')" id="btn-architect" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-white font-bold bg-brand-600 border border-brand-400 flex items-center space-x-1.5 whitespace-nowrap shadow-md shadow-brand-500/30 transition-all">
                <i class="fa-solid fa-user-astronaut text-xs"></i>
                <span>Siddharth (Center)</span>
            </button>
            <button onclick="flyToCluster('ai')" id="btn-ai" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all">
                <i class="fa-solid fa-brain text-brand-400 text-xs"></i>
                <span>AI & Models (20)</span>
            </button>
            <button onclick="flyToCluster('campus')" id="btn-campus" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all">
                <i class="fa-solid fa-graduation-cap text-cyber-cyan text-xs"></i>
                <span>Campus Portals (19)</span>
            </button>
            <button onclick="flyToCluster('vision')" id="btn-vision" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all">
                <i class="fa-solid fa-eye text-cyber-emerald text-xs"></i>
                <span>Vision & Gestures (7)</span>
            </button>
            <button onclick="flyToCluster('languages')" id="btn-languages" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all">
                <i class="fa-solid fa-code text-cyber-amber text-xs"></i>
                <span>Compilers & DSLs (5)</span>
            </button>
            <button onclick="flyToCluster('systems')" id="btn-systems" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all">
                <i class="fa-solid fa-comments text-cyber-pink text-xs"></i>
                <span>Chat & OS (11)</span>
            </button>
            <button onclick="flyToCluster('apps')" id="btn-apps" class="cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all">
                <i class="fa-solid fa-cubes text-cyber-blue text-xs"></i>
                <span>Web & Creative (20)</span>
            </button>
        </div>
    </nav>

    <!-- 3D Node Holographic Detail Inspector Drawer -->
    <aside id="detail-drawer" class="fixed top-0 right-0 bottom-0 w-full sm:w-[460px] z-40 bg-dark-950/95 backdrop-blur-2xl border-l border-white/10 p-6 flex flex-col justify-between transition-transform duration-500 translate-x-full shadow-2xl overflow-y-auto">
        <div>
            <div class="flex items-center justify-between pb-4 border-b border-white/10 mb-6">
                <div class="flex items-center space-x-2">
                    <span id="drawer-dot" class="w-2.5 h-2.5 rounded-full bg-cyber-cyan animate-pulse"></span>
                    <span id="drawer-tag" class="text-xs font-mono text-cyber-cyan tracking-widest uppercase font-bold">NEURAL NODE TELEMETRY</span>
                </div>
                <button onclick="closeDetailDrawer()" class="w-8 h-8 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-all">
                    <i class="fa-solid fa-xmark text-sm"></i>
                </button>
            </div>

            <!-- Visual Preview Container -->
            <div id="drawer-media-box" class="w-full rounded-2xl overflow-hidden aspect-[16/9] bg-dark-900 border border-white/10 mb-6 relative group shadow-xl flex items-center justify-center">
                <img id="drawer-img" src="assets/vss-agent-arch.svg" alt="Repository Schematic Preview" class="w-full h-full object-contain p-2">
                <span id="drawer-media-caption" class="absolute bottom-2 left-3 text-[10px] font-mono text-gray-300">SYSTEM SCHEMATIC // VSS CORE</span>
            </div>

            <!-- Title & Badges -->
            <h2 id="drawer-title" class="font-display font-black text-2xl text-white tracking-tight mb-2 break-all">
                vss-self-deciding-agent
            </h2>
            <div id="drawer-badges" class="flex flex-wrap gap-2 mb-4 font-mono text-xs">
                <span class="px-2.5 py-0.5 rounded-md bg-brand-500/20 text-brand-300 border border-brand-500/30">Python</span>
            </div>

            <!-- Description -->
            <p id="drawer-desc" class="text-gray-300 text-sm font-light leading-relaxed mb-6">
                System-One decision intelligence model built from scratch in PyTorch.
            </p>

            <!-- Metadata Box -->
            <div class="glass-panel p-4 rounded-xl border border-white/5 mb-6 space-y-2 text-xs font-mono">
                <div class="flex justify-between text-gray-400">
                    <span>Architect:</span>
                    <span class="text-white font-bold">Vooka Sai Siddharth</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>Neural Lobe:</span>
                    <span id="drawer-cluster-name" class="text-brand-300">AI & Deep Learning</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>Synapse Status:</span>
                    <span class="text-cyber-emerald font-bold">● Online &amp; Open Source</span>
                </div>
            </div>
        </div>

        <div class="pt-4 border-t border-white/10 space-y-3">
            <a id="drawer-github-link" href="#" target="_blank" rel="noopener noreferrer" class="w-full py-3.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-mono text-xs font-bold tracking-widest uppercase flex items-center justify-center space-x-2 shadow-lg shadow-brand-600/30 transition-all">
                <i class="fa-brands fa-github text-sm"></i>
                <span>Open Repository on GitHub</span>
            </a>
            <button id="drawer-clone-btn" onclick="copyDrawerCloneUrl(this)" class="w-full py-3 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 hover:text-white font-mono text-xs flex items-center justify-center space-x-2 transition-all">
                <i class="fa-regular fa-clone"></i>
                <span id="drawer-clone-text">Copy git clone command</span>
            </button>
        </div>
    </aside>

    <!-- Embedded 3D Neural Graph Data & Three.js Engine -->
    <script>
        const NEURAL_GRAPH = {graph_json_str};

        // --- Web Audio Synthesizer ---
        let audioCtx = null;
        let soundEnabled = true;

        function initAudio() {{
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }}

        function playSound(freq = 600, duration = 0.05, type = 'sine', vol = 0.04) {{
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
                icon.className = 'fa-solid fa-volume-high';
                playSound(700, 0.08);
            }} else {{
                icon.className = 'fa-solid fa-volume-xmark';
            }}
        }});

        // --- Reticle Crosshair Following Pointer ---
        const reticle = document.getElementById('reticle');
        window.addEventListener('pointermove', (e) => {{
            reticle.style.left = e.clientX + 'px';
            reticle.style.top = e.clientY + 'px';
        }});

        // --- Three.js Neural Scene Variables ---
        let scene, camera, renderer, controls;
        let characterGroup, headMesh, coreLight, daisRings = [];
        let allNeuronMeshes = [];
        let allSynapseLines = [];
        let actionPotentials = [];
        let clusterHubMeshes = [];
        let raycaster = new THREE.Raycaster();
        let mouse = new THREE.Vector2(-100, -100);
        let hoveredNeuron = null;
        let clock = new THREE.Clock();

        function initScene() {{
            const canvas = document.getElementById('canvas3d');
            renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: false }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.toneMapping = THREE.ACESFilmicToneMapping;
            renderer.toneMappingExposure = 1.15;

            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x030306);
            scene.fog = new THREE.FogExp2(0x030306, 0.012);

            camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 4, 22);

            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 55;
            controls.minDistance = 3.5;
            controls.target.set(0, 1.2, 0);

            // Lighting
            const ambient = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambient);

            const sun = new THREE.DirectionalLight(0xa78bfa, 1.5);
            sun.position.set(12, 25, 18);
            scene.add(sun);

            const rim = new THREE.DirectionalLight(0x06b6d4, 1.2);
            rim.position.set(-18, -12, -12);
            scene.add(rim);

            // Build Components
            buildBackgroundStars();
            buildCentralArchitect();
            buildNeuralNetworkWorld();

            window.addEventListener('resize', onWindowResize);
            window.addEventListener('pointermove', onPointerMove);
            window.addEventListener('click', onClick);

            animate();
        }}

        // --- Background Celestial Stars ---
        function buildBackgroundStars() {{
            const starCount = 2000;
            const starGeom = new THREE.BufferGeometry();
            const starPos = new Float32Array(starCount * 3);
            const starColors = new Float32Array(starCount * 3);

            const cViolet = new THREE.Color(0x8b5cf6);
            const cCyan = new THREE.Color(0x06b6d4);
            const cWhite = new THREE.Color(0xffffff);

            for (let i = 0; i < starCount * 3; i += 3) {{
                starPos[i] = (Math.random() - 0.5) * 260;
                starPos[i + 1] = (Math.random() - 0.5) * 260;
                starPos[i + 2] = (Math.random() - 0.5) * 260;

                const r = Math.random();
                const col = r > 0.6 ? cViolet : r > 0.3 ? cCyan : cWhite;
                starColors[i] = col.r;
                starColors[i + 1] = col.g;
                starColors[i + 2] = col.b;
            }}

            starGeom.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
            starGeom.setAttribute('color', new THREE.BufferAttribute(starColors, 3));

            const starMat = new THREE.PointsMaterial({{
                size: 1.5,
                vertexColors: true,
                transparent: true,
                opacity: 0.7,
                blending: THREE.AdditiveBlending
            }});

            scene.add(new THREE.Points(starGeom, starMat));

            const grid = new THREE.GridHelper(100, 60, 0x8b5cf6, 0x1e1b4b);
            grid.position.y = -4.5;
            grid.material.transparent = true;
            grid.material.opacity = 0.2;
            scene.add(grid);
        }}

        // --- Central 3D Character of Sai Siddharth ---
        function buildCentralArchitect() {{
            characterGroup = new THREE.Group();

            // Pedestal Dais
            const daisGeom = new THREE.CylinderGeometry(2.2, 2.6, 0.4, 32);
            const daisMat = new THREE.MeshStandardMaterial({{ color: 0x070712, roughness: 0.2, metalness: 0.9 }});
            const dais = new THREE.Mesh(daisGeom, daisMat);
            dais.position.y = -2.6;
            characterGroup.add(dais);

            for (let i = 1; i <= 3; i++) {{
                const ringGeom = new THREE.TorusGeometry(1.3 + i * 0.4, 0.02, 16, 64);
                const ringMat = new THREE.MeshBasicMaterial({{ color: i % 2 === 0 ? 0x06b6d4 : 0x8b5cf6, transparent: true, opacity: 0.85 }});
                const ring = new THREE.Mesh(ringGeom, ringMat);
                ring.rotation.x = Math.PI / 2;
                ring.position.y = -2.38 + i * 0.02;
                characterGroup.add(ring);
                daisRings.push(ring);
            }}

            // Torso & Body
            const torsoGroup = new THREE.Group();
            const darkCyberMat = new THREE.MeshStandardMaterial({{ color: 0x0d0d1a, roughness: 0.3, metalness: 0.8 }});

            const chest = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1.1, 0.7), darkCyberMat);
            chest.position.y = 0.2;
            torsoGroup.add(chest);

            // Glowing Arc Core Reactor
            const coreGeom = new THREE.OctahedronGeometry(0.24, 1);
            const coreMat = new THREE.MeshStandardMaterial({{ color: 0x06b6d4, emissive: 0x06b6d4, emissiveIntensity: 1.2, wireframe: true }});
            const chestCore = new THREE.Mesh(coreGeom, coreMat);
            chestCore.position.set(0, 0.25, 0.38);
            torsoGroup.add(chestCore);

            coreLight = new THREE.PointLight(0x8b5cf6, 2.5, 9);
            coreLight.position.set(0, 0.25, 0.5);
            torsoGroup.add(coreLight);

            // Arms in Conductor pose
            const armL = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.1, 0.9, 12), darkCyberMat);
            armL.position.set(-1.1, 0.2, 0.3);
            armL.rotation.z = -Math.PI / 4;
            armL.rotation.x = Math.PI / 5;
            torsoGroup.add(armL);

            const armR = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.1, 0.9, 12), darkCyberMat);
            armR.position.set(1.1, 0.2, 0.3);
            armR.rotation.z = Math.PI / 4;
            armR.rotation.x = Math.PI / 5;
            torsoGroup.add(armR);

            const handMat = new THREE.MeshBasicMaterial({{ color: 0x06b6d4 }});
            const handL = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 12), handMat);
            handL.position.set(-1.45, -0.15, 0.55);
            torsoGroup.add(handL);

            const handR = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 12), handMat);
            handR.position.set(1.45, -0.15, 0.55);
            torsoGroup.add(handR);

            // Head with Real Portrait Texture
            headMesh = new THREE.Group();
            headMesh.position.y = 1.35;

            new THREE.TextureLoader().load('assets/profile.jpg', (tex) => {{
                tex.generateMipmaps = true;
                const face = new THREE.Mesh(
                    new THREE.PlaneGeometry(0.85, 0.85),
                    new THREE.MeshBasicMaterial({{ map: tex, side: THREE.FrontSide }})
                );
                face.position.z = 0.41;
                headMesh.add(face);
            }});

            const headShell = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.95, 0.8), darkCyberMat);
            headMesh.add(headShell);

            const visor = new THREE.Mesh(new THREE.TorusGeometry(0.55, 0.025, 16, 32), new THREE.MeshBasicMaterial({{ color: 0x8b5cf6 }}));
            visor.position.z = 0.42;
            headMesh.add(visor);

            // Floating Nameplate
            const nameCanvas = document.createElement('canvas');
            nameCanvas.width = 512;
            nameCanvas.height = 128;
            const nctx = nameCanvas.getContext('2d');
            nctx.fillStyle = 'rgba(7, 7, 13, 0.88)';
            nctx.roundRect(10, 10, 492, 108, 20);
            nctx.fill();
            nctx.strokeStyle = '#8b5cf6';
            nctx.lineWidth = 4;
            nctx.stroke();
            nctx.fillStyle = '#ffffff';
            nctx.font = 'bold 36px sans-serif';
            nctx.textAlign = 'center';
            nctx.fillText('VOOKA SAI SIDDHARTH', 256, 56);
            nctx.fillStyle = '#06b6d4';
            nctx.font = 'bold 22px monospace';
            nctx.fillText('SRM KTR CS • VSS NEURAL CORE', 256, 92);

            const namePlate = new THREE.Mesh(
                new THREE.PlaneGeometry(2.4, 0.6),
                new THREE.MeshBasicMaterial({{ map: new THREE.CanvasTexture(nameCanvas), transparent: true, side: THREE.DoubleSide }})
            );
            namePlate.position.y = 1.0;
            headMesh.add(namePlate);

            torsoGroup.add(headMesh);
            characterGroup.add(torsoGroup);

            dais.userData = {{ isCharacter: true }};
            headShell.userData = {{ isCharacter: true }};
            allNeuronMeshes.push(dais, headShell);

            scene.add(characterGroup);
        }}

        // --- Build Entire 3D Neural Network with all 82 Nodes & Synapses ---
        function buildNeuralNetworkWorld() {{
            const handL = new THREE.Vector3(-1.45, -0.15, 0.55);
            const handR = new THREE.Vector3(1.45, -0.15, 0.55);

            const clusterHubs = {{}};

            Object.entries(NEURAL_GRAPH.clusters).forEach(([catKey, cfg]) => {{
                const hubCenter = new THREE.Vector3(...cfg.center);

                const hubGeom = new THREE.IcosahedronGeometry(0.8, 1);
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
                    new THREE.TorusGeometry(1.2, 0.02, 16, 48),
                    new THREE.MeshBasicMaterial({{ color: cfg.color, transparent: true, opacity: 0.7 }})
                );
                hubMesh.add(ring);

                const hubCanvas = document.createElement('canvas');
                hubCanvas.width = 512;
                hubCanvas.height = 128;
                const hctx = hubCanvas.getContext('2d');
                hctx.fillStyle = 'rgba(7, 7, 13, 0.9)';
                hctx.roundRect(10, 10, 492, 108, 18);
                hctx.fill();
                hctx.strokeStyle = cfg.hex;
                hctx.lineWidth = 4;
                hctx.stroke();
                hctx.fillStyle = '#ffffff';
                hctx.font = 'bold 32px sans-serif';
                hctx.textAlign = 'center';
                hctx.fillText(cfg.name.toUpperCase(), 256, 58);
                hctx.fillStyle = cfg.hex;
                hctx.font = 'bold 22px monospace';
                hctx.fillText('NEURAL CLUSTER HUB', 256, 92);

                const hubLabel = new THREE.Mesh(
                    new THREE.PlaneGeometry(2.6, 0.65),
                    new THREE.MeshBasicMaterial({{ map: new THREE.CanvasTexture(hubCanvas), transparent: true, side: THREE.DoubleSide }})
                );
                hubLabel.position.y = 1.3;
                hubMesh.add(hubLabel);

                hubMesh.userData = {{ isHub: true, clusterKey: catKey, clusterName: cfg.name, labelMesh: hubLabel }};
                allNeuronMeshes.push(hubMesh);
                clusterHubMeshes.push(hubMesh);
                scene.add(hubMesh);

                clusterHubs[catKey] = {{ hubMesh, center: hubCenter, color: cfg.color, nodes: [] }};

                const origin = (hubCenter.x < 0) ? handL : handR;
                const mid = new THREE.Vector3((origin.x + hubCenter.x) * 0.5, (origin.y + hubCenter.y) * 0.5 + 1.2, (origin.z + hubCenter.z) * 0.5);
                const curve = new THREE.QuadraticBezierCurve3(origin, mid, hubCenter);
                const lineGeom = new THREE.BufferGeometry().setFromPoints(curve.getPoints(40));
                const lineMat = new THREE.LineBasicMaterial({{ color: cfg.color, transparent: true, opacity: 0.75, linewidth: 2 }});
                const mainLine = new THREE.Line(lineGeom, lineMat);
                scene.add(mainLine);

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
                const somaSize = isFlagship ? 0.45 : 0.28;

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

                const shellGeom = new THREE.OctahedronGeometry(somaSize * 1.4, 0);
                const shellMat = new THREE.MeshBasicMaterial({{
                    color: clusterColor,
                    wireframe: true,
                    transparent: true,
                    opacity: 0.4
                }});
                const shell = new THREE.Mesh(shellGeom, shellMat);
                neuronGroup.add(shell);

                const labelCanvas = document.createElement('canvas');
                labelCanvas.width = 384;
                labelCanvas.height = 112;
                const lctx = labelCanvas.getContext('2d');
                lctx.fillStyle = 'rgba(7, 7, 13, 0.82)';
                lctx.roundRect(6, 6, 372, 100, 14);
                lctx.fill();
                lctx.strokeStyle = clusterCfg.hex;
                lctx.lineWidth = 3;
                lctx.stroke();

                lctx.fillStyle = '#ffffff';
                lctx.font = 'bold 24px monospace';
                lctx.textAlign = 'center';
                const displayName = repo.name.length > 20 ? repo.name.slice(0, 18) + '..' : repo.name;
                lctx.fillText(displayName, 192, 46);

                lctx.fillStyle = clusterCfg.hex;
                lctx.font = 'bold 18px monospace';
                lctx.fillText(repo.language.toUpperCase(), 192, 82);

                const labelTex = new THREE.CanvasTexture(labelCanvas);
                const labelMesh = new THREE.Mesh(
                    new THREE.PlaneGeometry(isFlagship ? 2.2 : 1.7, isFlagship ? 0.65 : 0.5),
                    new THREE.MeshBasicMaterial({{ map: labelTex, transparent: true, side: THREE.DoubleSide }})
                );
                labelMesh.position.y = somaSize + 0.5;
                neuronGroup.add(labelMesh);

                soma.userData = {{
                    isNeuron: true,
                    repo: repo,
                    clusterCfg: clusterCfg,
                    parentGroup: neuronGroup,
                    shellMesh: shell,
                    labelMesh: labelMesh,
                    defaultScale: 1.0,
                    synapses: []
                }};

                labelMesh.userData = soma.userData;

                allNeuronMeshes.push(soma, labelMesh);
                scene.add(neuronGroup);

                clusterHubs[repo.cluster].nodes.push({{ soma, pos: nodePos }});

                const hubPos = clusterHubs[repo.cluster].center;
                const synGeom = new THREE.BufferGeometry().setFromPoints([hubPos, nodePos]);
                const synMat = new THREE.LineBasicMaterial({{
                    color: clusterColor,
                    transparent: true,
                    opacity: isFlagship ? 0.7 : 0.32,
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

            Object.values(clusterHubs).forEach(hub => {{
                const nodes = hub.nodes;
                for (let i = 0; i < nodes.length; i++) {{
                    for (let j = i + 1; j < nodes.length; j++) {{
                        const dist = nodes[i].pos.distanceTo(nodes[j].pos);
                        if (dist < 3.2) {{
                            const interGeom = new THREE.BufferGeometry().setFromPoints([nodes[i].pos, nodes[j].pos]);
                            const interMat = new THREE.LineBasicMaterial({{
                                color: hub.color,
                                transparent: true,
                                opacity: 0.2,
                                linewidth: 1
                            }});
                            const interLine = new THREE.Line(interGeom, interMat);
                            scene.add(interLine);
                            allSynapseLines.push(interLine);
                            nodes[i].soma.userData.synapses.push(interLine);
                            nodes[j].soma.userData.synapses.push(interLine);
                        }}
                    }}
                }}
            }});
        }}

        // --- Pointer Move Raycasting & Hover Feedback ---
        function onPointerMove(e) {{
            mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

            if (headMesh) {{
                headMesh.rotation.y = mouse.x * 0.45;
                headMesh.rotation.x = -mouse.y * 0.3;
            }}

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(allNeuronMeshes, false);

            if (intersects.length > 0) {{
                const obj = intersects[0].object;
                if (hoveredNeuron !== obj) {{
                    if (hoveredNeuron && hoveredNeuron.userData && hoveredNeuron.userData.isNeuron) {{
                        hoveredNeuron.userData.parentGroup.scale.set(1, 1, 1);
                        hoveredNeuron.userData.synapses.forEach(l => l.material.opacity = 0.3);
                    }}

                    hoveredNeuron = obj;
                    reticle.classList.add('active');
                    playSound(650, 0.03, 'triangle', 0.03);

                    if (obj.userData && obj.userData.isNeuron) {{
                        obj.userData.parentGroup.scale.set(1.2, 1.2, 1.2);
                        obj.userData.synapses.forEach(l => l.material.opacity = 0.9);
                    }}
                }}
            }} else {{
                if (hoveredNeuron) {{
                    if (hoveredNeuron.userData && hoveredNeuron.userData.isNeuron) {{
                        hoveredNeuron.userData.parentGroup.scale.set(1, 1, 1);
                        hoveredNeuron.userData.synapses.forEach(l => l.material.opacity = 0.3);
                    }}
                    hoveredNeuron = null;
                    reticle.classList.remove('active');
                }}
            }}
        }}

        // --- Click Raycasting to Inspect 3D Neuron ---
        function onClick(e) {{
            if (e.target.closest('header, nav, aside, #repo-search, .glass-panel')) return;

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(allNeuronMeshes, false);

            if (intersects.length > 0) {{
                const obj = intersects[0].object;
                playSound(880, 0.1, 'sine', 0.05);

                if (obj.userData && obj.userData.isNeuron) {{
                    openNeuronDrawer(obj.userData.repo, obj.userData.clusterCfg);
                    flyCameraTo(obj.userData.parentGroup.position.clone().add(new THREE.Vector3(0, 0, 3.8)), obj.userData.parentGroup.position);
                }} else if (obj.userData && obj.userData.isHub) {{
                    flyToCluster(obj.userData.clusterKey);
                }} else if (obj.userData && obj.userData.isCharacter) {{
                    flyToTarget('architect');
                }}
            }}
        }}

        // --- Camera Navigation Presets ---
        function flyToTarget(key) {{
            playSound(600, 0.08);

            document.querySelectorAll('.cam-btn').forEach(b => {{
                b.className = 'cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all';
            }});
            const btn = document.getElementById(`btn-${{key}}`);
            if (btn) {{
                btn.className = 'cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-white font-bold bg-brand-600 border border-brand-400 flex items-center space-x-1.5 whitespace-nowrap shadow-md shadow-brand-500/30 transition-all';
            }}

            if (key === 'architect') {{
                closeDetailDrawer();
                flyCameraTo(new THREE.Vector3(0, 1.4, 4.2), new THREE.Vector3(0, 1.2, 0));
            }} else if (key === 'overview') {{
                closeDetailDrawer();
                flyCameraTo(new THREE.Vector3(0, 4, 22), new THREE.Vector3(0, 1.2, 0));
            }}
        }}

        function flyToCluster(clusterKey) {{
            playSound(650, 0.08);

            document.querySelectorAll('.cam-btn').forEach(b => {{
                b.className = 'cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-gray-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 flex items-center space-x-1.5 whitespace-nowrap transition-all';
            }});
            const btn = document.getElementById(`btn-${{clusterKey}}`);
            if (btn) {{
                btn.className = 'cam-btn px-3 py-1.5 rounded-xl text-xs font-mono uppercase tracking-wider text-white font-bold bg-brand-600 border border-brand-400 flex items-center space-x-1.5 whitespace-nowrap shadow-md shadow-brand-500/30 transition-all';
            }}

            const cfg = NEURAL_GRAPH.clusters[clusterKey];
            if (cfg) {{
                const targetPos = new THREE.Vector3(...cfg.center);
                flyCameraTo(targetPos.clone().add(new THREE.Vector3(0, 1, 9)), targetPos);
            }}
        }}

        function flyCameraTo(targetPos, lookAtPos) {{
            new TWEEN.Tween(camera.position)
                .to({{ x: targetPos.x, y: targetPos.y, z: targetPos.z }}, 1200)
                .easing(TWEEN.Easing.Cubic.Out)
                .start();

            new TWEEN.Tween(controls.target)
                .to({{ x: lookAtPos.x, y: lookAtPos.y, z: lookAtPos.z }}, 1200)
                .easing(TWEEN.Easing.Cubic.Out)
                .start();
        }}

        // --- Holographic Detail Drawer ---
        function openNeuronDrawer(repo, clusterCfg) {{
            document.getElementById('drawer-dot').style.backgroundColor = clusterCfg.hex;
            document.getElementById('drawer-tag').innerText = `SYNAPSE // ${{clusterCfg.name.toUpperCase()}}`;
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
                <span class="px-2.5 py-0.5 rounded-md bg-white/5 text-gray-300 border border-white/10">Active Synapse</span>
            `;

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
            setTimeout(() => {{
                document.getElementById('drawer-clone-text').innerText = 'Copy git clone command';
            }}, 2000);
        }}

        // --- Live Search across 82 Neurons ---
        function handleSearch(val) {{
            const dropdown = document.getElementById('search-dropdown');
            if (!val.trim()) {{
                dropdown.classList.add('hidden');
                return;
            }}

            const query = val.toLowerCase();
            const matches = [];

            allNeuronMeshes.forEach(mesh => {{
                if (mesh.userData && mesh.userData.isNeuron) {{
                    const repo = mesh.userData.repo;
                    if (repo.name.toLowerCase().includes(query) || repo.description.toLowerCase().includes(query)) {{
                        matches.push({{
                            name: repo.name,
                            lang: repo.language,
                            cluster: mesh.userData.clusterCfg.name,
                            action: () => {{
                                openNeuronDrawer(repo, mesh.userData.clusterCfg);
                                flyCameraTo(mesh.userData.parentGroup.position.clone().add(new THREE.Vector3(0, 0, 3.8)), mesh.userData.parentGroup.position);
                            }}
                        }});
                    }}
                }}
            }});

            if (matches.length > 0) {{
                dropdown.innerHTML = matches.slice(0, 8).map((m, idx) => `
                    <div onclick="executeSearchMatch(${{idx}})" class="p-2 rounded-lg bg-dark-900/90 hover:bg-brand-600/30 border border-white/5 cursor-pointer flex justify-between items-center text-gray-200 hover:text-white">
                        <span>${{m.name}}</span>
                        <span class="text-[10px] text-brand-400 uppercase">${{m.lang}}</span>
                    </div>
                `).join('');
                dropdown.classList.remove('hidden');
                window.currentSearchMatches = matches;
            }} else {{
                dropdown.innerHTML = '<div class="p-2 text-gray-500 text-center">No neuron matches</div>';
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

        function onWindowResize() {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }}

        // --- 60fps Animation Loop ---
        function animate() {{
            requestAnimationFrame(animate);
            TWEEN.update();

            const time = clock.getElapsedTime();
            controls.update();

            if (characterGroup) {{
                characterGroup.position.y = Math.sin(time * 1.5) * 0.12;
            }}

            daisRings.forEach((r, idx) => {{
                r.rotation.z += (idx % 2 === 0 ? 0.008 : -0.008);
            }});

            if (coreLight) {{
                coreLight.intensity = 2.0 + Math.sin(time * 3) * 0.8;
            }}

            clusterHubMeshes.forEach(hub => {{
                hub.rotation.y += 0.01;
                hub.rotation.x += 0.005;
                if (hub.userData.labelMesh) {{
                    hub.userData.labelMesh.quaternion.copy(camera.quaternion);
                }}
            }});

            allNeuronMeshes.forEach(mesh => {{
                if (mesh.userData && mesh.userData.isNeuron) {{
                    if (mesh.userData.labelMesh) {{
                        mesh.userData.labelMesh.quaternion.copy(camera.quaternion);
                    }}
                    if (mesh.userData.shellMesh) {{
                        mesh.userData.shellMesh.rotation.x += 0.01;
                        mesh.userData.shellMesh.rotation.y += 0.015;
                    }}
                }}
            }});

            actionPotentials.forEach(ap => {{
                const t = (time * ap.speed) % 1.0;
                const pos = ap.curve.getPointAt(t);
                ap.photon.position.copy(pos);
            }});

            renderer.render(scene, camera);
        }}

        window.addEventListener('DOMContentLoaded', initScene);
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Successfully written updated index.html with all 82 repos neural network!')
