// Scene Setup
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x050505, 0.002);

// Camera Setup
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 50;

// Renderer Setup
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.getElementById('canvas-container').appendChild(renderer.domElement);

// Particles / Neural Network Nodes
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 700;
const posArray = new Float32Array(particlesCount * 3);
const colorsArray = new Float32Array(particlesCount * 3);

const color1 = new THREE.Color(0x00ff87); // Neon green
const color2 = new THREE.Color(0x1f6feb); // Blue
const color3 = new THREE.Color(0x60efff); // Cyan

for(let i = 0; i < particlesCount * 3; i+=3) {
    // Spread particles in a wide area
    posArray[i] = (Math.random() - 0.5) * 150;
    posArray[i+1] = (Math.random() - 0.5) * 150;
    posArray[i+2] = (Math.random() - 0.5) * 150;

    // Mix colors
    const randColor = Math.random();
    let mixedColor;
    if (randColor < 0.33) mixedColor = color1;
    else if (randColor < 0.66) mixedColor = color2;
    else mixedColor = color3;

    colorsArray[i] = mixedColor.r;
    colorsArray[i+1] = mixedColor.g;
    colorsArray[i+2] = mixedColor.b;
}

particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colorsArray, 3));

// Material
const particlesMaterial = new THREE.PointsMaterial({
    size: 0.8,
    vertexColors: true,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
});

// Create Point Cloud
const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);

// Mouse Interaction Variables
let mouseX = 0;
let mouseY = 0;
let targetX = 0;
let targetY = 0;
const windowHalfX = window.innerWidth / 2;
const windowHalfY = window.innerHeight / 2;

document.addEventListener('mousemove', (event) => {
    mouseX = (event.clientX - windowHalfX);
    mouseY = (event.clientY - windowHalfY);
});

// Animation Loop
const clock = new THREE.Clock();

function animate() {
    requestAnimationFrame(animate);
    const elapsedTime = clock.getElapsedTime();

    // Rotate entire particle system slowly
    particlesMesh.rotation.y = elapsedTime * 0.05;
    particlesMesh.rotation.x = elapsedTime * 0.02;

    // Smooth mouse follow
    targetX = mouseX * 0.001;
    targetY = mouseY * 0.001;
    
    camera.rotation.y += 0.05 * (targetX - camera.rotation.y);
    camera.rotation.x += 0.05 * (targetY - camera.rotation.x);

    // Dynamic wave effect on particles
    const positions = particlesGeometry.attributes.position.array;
    for(let i = 0; i < particlesCount; i++) {
        const i3 = i * 3;
        const x = particlesGeometry.attributes.position.array[i3];
        // Move Y slightly based on sin wave
        particlesGeometry.attributes.position.array[i3+1] += Math.sin(elapsedTime + x) * 0.02;
    }
    particlesGeometry.attributes.position.needsUpdate = true;

    renderer.render(scene, camera);
}

animate();

// Handle Resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// GSAP UI Animations
gsap.from("header", { y: -50, opacity: 0, duration: 1, ease: "power3.out" });
gsap.from(".hero-content > *", { 
    y: 50, 
    opacity: 0, 
    duration: 1, 
    stagger: 0.2, 
    ease: "power3.out", 
    delay: 0.5 
});
gsap.from(".glass-panel", { 
    x: 100, 
    opacity: 0, 
    duration: 1, 
    ease: "power3.out", 
    delay: 1 
});
