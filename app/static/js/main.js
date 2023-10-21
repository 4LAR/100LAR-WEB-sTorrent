
// добавить элемент в список (ul)
function append_to_ul(id, content) {
  var ul = document.getElementById(id);

  var li = document.createElement("li");

  li.innerHTML = content;

  ul.appendChild(li);
}

// очистить список (ul)
function clear_ul(id) {
  document.getElementById(id).innerHTML = '';
}

// вычисление логарифма
function getBaseLog(x, y) {
  return Math.log(y) / Math.log(x);
}

var size_name = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];

// конвертирование байтов в [size_name]
function convert_size(size_bytes, name_bool=false) {
  if (size_bytes == 0)
    if (name_bool)
      return [0, 'B', 0]
    else
      return '0 B';

  i = Math.floor(getBaseLog(1024, size_bytes)); // индекс названия
  p = Math.pow(1024, i);
  s = Math.round((size_bytes / p) * 100) / 100; // размер

  if (name_bool)
    return [s, size_name[i], i]
  else
    return s + ' ' + size_name[i]
}

////////////////////////////////////////////////////////////////////////////////

var state_str = [
    'queued',
    'checking',
    'downloading metadata',
    'downloading',
    'finished',
    'seeding',
    'allocating',
    'checking fastresume'
]

var state_color = [
  '#FFF',
  '#FFF',
  '#FFF',
  '#0000FF',
  '#0000FF',
  '#FFF',
  '#FFF',
  '#FFF'
]

function get_info() {
  fetch(`/get_info`, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
    }
  })
  .then(response => response.json())
  .then(data => {
    clear_ul("download_list");
    append_to_ul("download_list", `
      <p>NAME</p>
      <p>SIZE</p>
      <p>STATE</p>
      <p>STATUS</p>
      <p>SPEED</p>
      <label for="fileElem" class="delete_ico">
        <img src="static/img/add.svg" class="add_ico icon">
      </label>
    `);
    let i = 0;
    for (const item of data.data) {
      append_to_ul("download_list", `
        <div class="status_ico" style="background-color: ${state_color[item.state]};"></div>
        <p class="name">${item.name}</p>
        <p class="size">${convert_size(item.total_size)}</p>
        <p class="state">${item.progress} %</p>
        <p class="status">${state_str[item.state]}</p>
        <p class="speed_in">${(item.download)? (convert_size(item.download) + "/s"): ""}</p>
        <img src="static/img/trash.svg" class="delete_ico icon" onclick="delete_item(${i})">
      `);
      i++;
    }
  })
}

setInterval(() => get_info(), 1000);

function delete_item(id) {
  fetch(`/remove_torrent?id=${id}`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
    }
  })
  .then(response => response.json())
  .then(data => {
    clear_ul("download_list");
  })
}

function download_item() {

}

function add_item(file) {
  form = new FormData();
  var xhr = new XMLHttpRequest();
  form.append("file", file[0]);
  xhr.open('post', `/add_torrent`, true);
  xhr.upload.onload = function() {
    clear_ul("download_list");
  }
  xhr.send(form);
}
