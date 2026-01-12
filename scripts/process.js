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

const SCREEN_LAG_MAGIC_NUM = 0.1;
const TICK_INTERVAL = 30;
let scrollTarget = { x: 0, y: 0 };
let scrollPos = { x: 0, y: 0 };
function _process() {
  scrollPos = vlerp(scrollPos, scrollTarget, SCREEN_LAG_MAGIC_NUM);

  window.scroll(scrollPos.x, scrollPos.y);
}

setInterval(_process, TICK_INTERVAL);

let worldContainer = document.getElementById("world-container");
console.log(
  "Width, window: " +
    window.innerWidth +
    ", world: " +
    worldContainer.offsetWidth,
);
console.log(
  "Height, window: " +
    window.innerHeight +
    ", world: " +
    worldContainer.offsetHeight,
);

let mouseX, mouseY;
document.onmousemove = handleMouseMove;
function handleMouseMove(event) {
  event = event || window.event; // IE-ism
  mouseX = event.pageX;
  mouseY = event.pageY;

  let widthDiff = worldContainer.offsetWidth - window.innerWidth;
  let heightDiff = worldContainer.offsetHeight - window.innerHeight;

  let xPercent = mouseX / window.innerWidth;
  let yPercent = mouseY / window.innerHeight;

  scrollTarget.x = xPercent * widthDiff;
  scrollTarget.y = yPercent * heightDiff;

  console.log(scrollTarget);
}
