const addTaskBtn = document.getElementById("addTask-btn");
const listContainer = document.getElementById("list-container");

addTaskBtn.addEventListener("click", createInput);

const today = document.getElementById("today");
let count = today.innerText;

function createInput() {
  const li = document.createElement("li");

  li.setAttribute("class", "new");

  const input = document.createElement("input");

  input.setAttribute("type", "text");
  input.setAttribute("placeholder", "할일을 입력해주세요.");

  input.setAttribute("id", "task-input");

  const button = document.createElement("button");

  button.setAttribute("type", "button");
  button.innerText = "+";

  button.addEventListener("click", addTask);

  li.appendChild(input);
  li.appendChild(button);

  listContainer.appendChild(li);
}

function addTask() {
  const input = document.getElementById("task-input");
  const task = input.value;

  const li = document.createElement("li");
  li.innerText = task;

  if (task === "") {
    alert("할 일을 적어주세요.");
  } else {
    listContainer.appendChild(li);
    listContainer.removeChild(input.parentElement);
    saveData();
  }
}

function checkTodoNum() {
  listContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("new")) {
      return;
    }
    if (e.target.tagName === "LI") {
      if (e.target.classList.contains("checked")) {
        e.target.classList.remove("checked");
        count--;
      } else {
        e.target.classList.add("checked");
        count++;
      }
      today.innerText = count;
      saveData();
    }
  });
}
checkTodoNum();

let todoNum = localStorage.getItem("todoNum");

function saveData() {
  localStorage.setItem("data", listContainer.innerHTML);
  localStorage.setItem("todoNum", today.innerText);
}

function showTask() {
  listContainer.innerHTML = localStorage.getItem("data");
  today.innerText = localStorage.getItem("todoNum") || 0;
  count = today.innerText;

  const newlist = document.querySelectorAll(".new");
  newlist.forEach((e) => e.remove());
}

showTask();

const TODO_LIST_DATA = [
  {
    category: "동아리",
    todolist: [
      "후회없는 여름방학 보내기",
      "좋은 인연 많이 만들기",
      "헤맨만큼 내 땅이다! 마음껏 헤매기",
      "자식같은 프로젝트 해보기",
    ],
  },
  {
    category: "학교",
    todolist: ["등교하기", "하교하기"],
  },
];

const main = document.getElementsByTagName("main")[0];

TODO_LIST_DATA.forEach((block) => {
  const h2 = document.createElement("h2");
  h2.innerText = block.category;
  main.appendChild(h2);

  const ul = document.createElement("ul");

  block.todolist.forEach((item) => {
    const li = document.createElement("li");
    li.innerText = item;
    ul.appendChild(li);
  });
  main.appendChild(ul);
});
