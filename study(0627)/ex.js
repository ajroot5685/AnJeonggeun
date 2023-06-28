const second = 1000;
const minute = second * 60;
const hour = minute * 60;
const day = hour * 24;

// 값을 바꿀 element 가져오기
const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");

function fillZero(num) {
  // 숫자를 2자리수로 설정, 비어있는 자리수는 0으로 채움
  return String(num).padStart(2, "0");
}

// 종강까지 남은 시간 계산
function getCountDown() {
  const now = new Date();
  const nowTime = now.getTime();
  console.log(nowTime);

  const endDay = "08/22/2023";
  const endDayTime = new Date(endDay).getTime();
  console.log(endDayTime);

  const cal = endDayTime - nowTime;
  console.log(cal);

  const cal_day = Math.floor(cal / day);
  const cal_hour = Math.floor((cal % day) / hour);
  const cal_minute = Math.floor((cal % hour) / minute);
  const cal_second = Math.floor((cal % minute) / second);

  daysEl.innerText = fillZero(cal_day);
  hoursEl.innerText = fillZero(cal_hour);
  minutesEl.innerText = fillZero(cal_minute);
  secondsEl.innerText = fillZero(cal_second);
}

setInterval(getCountDown, 1);
