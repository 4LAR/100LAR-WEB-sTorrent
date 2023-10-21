
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

async function get_info() {
  let response = await fetch(`/get_info`, {
    method: 'GET'
  });
  if (!response.ok) {
    clear_ul("download_list");
    append_to_ul("download_list", `
      <p>NAME</p>
      <p>SIZE</p>
      <p>STATE</p>
      <p>STATUS</p>
      <p>SPEED</p>
      <p></p>
      <img src="static/img/add.svg" class="add_ico icon">
    `);
    for (const item of response.json.data) {
      append_to_ul("download_list", `
        <img src="static/img/download.svg" class="download_ico icon">
        <p class="name">${item.name}</p>
        <p class="size">${convert_size(item.)}</p>
        <p class="state">${}</p>
        <p class="status">${}</p>
        <p class="speed_in">${}</p>
        <img src="static/img/trash.svg" class="delete_ico icon">
      `);
    }
  }
}

function delete_item(id) {

}

function download_item() {

}

function add_item() {

}
