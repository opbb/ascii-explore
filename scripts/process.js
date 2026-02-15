// Linearly interpolates between a and b over time t
function lerp(a, b, t) {
  return a + (b - a) * t;
}

// Lerp between 2d vectors
function vlerp(vecA, vecB, t) {
  return {
    x: lerp(vecA.x, vecB.x, t),
    y: lerp(vecA.y, vecB.y, t),
  };
}

const SCREEN_LAG_MAGIC_NUM = 0.005;
//const TICK_INTERVAL = 30;
let scrollTarget = { x: 0, y: 0 };
let scrollPos = { x: 0, y: 0 };
let lastFrameTimestamp = performance.now();
function updateScreenPos(timestamp) {
  timeElapsed = timestamp - lastFrameTimestamp;
  lastFrameTimestamp = timestamp;

  scrollPos = vlerp(
    scrollPos,
    scrollTarget,
    SCREEN_LAG_MAGIC_NUM * timeElapsed, // Multiply by time elapsed to normalize movement across framerates
  );

  window.scroll(scrollPos.x, scrollPos.y);

  requestAnimationFrame(updateScreenPos);
}

requestAnimationFrame(updateScreenPos);

let worldContainer = document.getElementById("world-container");

let mouseX, mouseY;
document.onmousemove = handleMouseMove;

// TODO: These need to be updated when the window is resized
let widthDiff = worldContainer.offsetWidth - window.innerWidth;
let heightDiff = worldContainer.offsetHeight - window.innerHeight;
let deadZoneX = 10; // horizontal dead zone in pixels
let deadZoneY = 10; // vertical dead zone in pixels
function handleMouseMove(event) {
  mouseX = event.clientX;
  mouseY = event.clientY;

  let xPercent = mouseX / window.innerWidth;
  let yPercent = mouseY / window.innerHeight;

  scrollTarget.x = Math.min(
    widthDiff - deadZoneX,
    Math.max(deadZoneX, xPercent * widthDiff),
  );
  scrollTarget.y = Math.min(
    heightDiff - deadZoneY,
    Math.max(deadZoneY, yPercent * heightDiff),
  );
}
