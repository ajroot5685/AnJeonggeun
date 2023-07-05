let time = 0;
let timerId;
const stopwatch = document.getElementById("time");
let sec, msec;

function printTime() {
  time++;
  stopwatch.innerText = getTimeFormatString();
}

function startClock() {
  printTime();
  stopInterval();
  timerId = setTimeout(startClock, 10);
}

function stopInterval() {
  if (timerId != null) {
    clearTimeout(timerId);
  }
}

function stopClock() {
  if (timerId != null) {
    clearTimeout(timerId);
    recordClock();
  }
}

function resetClock() {
  stopInterval();
  stopwatch.innerText = "00:00";
  const content = document.querySelector("#content");
  content.innerHTML = "";
  time = 0;

  const all = document.querySelector("#selectall");
  if (!all.classList.contains("invisible")) {
    all.classList.add("invisible");
  }
}

function getTimeFormatString() {
  sec = parseInt(time / 100);
  msec = time % 100;

  return String(sec).padStart(2, "0") + ":" + String(msec).padStart(2, "0");
}

function recordClock() {
  const content = document.querySelector("#content");
  content.innerHTML += createRecord(stopwatch.innerText);
}

function createRecord(record) {
  return `
    <div class="list invisible">
            <div class="checkbox select" onclick="select(this)">
              <div class="check"></div>
            </div>
            <span>${record}</span>
            <div class="space"></div>
          </div>
    `;
}

function selectAll() {
  const all = document.querySelector("#selectall");
  const allcheck = document.querySelectorAll(".list");
  //   console.log(all.classList);
  if (all.classList.contains("invisible")) {
    all.classList.remove("invisible");
    allcheck.forEach((list) => list.classList.remove("invisible"));
  } else {
    all.classList.add("invisible");
    allcheck.forEach((list) => list.classList.add("invisible"));
  }
}

function select(event) {
  const clickedDiv = event.parentNode;
  clickedDiv.classList.toggle("invisible");
}

function dlist() {
  const select = document.querySelectorAll(".list:not(.invisible)");
  select.forEach((div) => {
    div.remove();
  });
}
