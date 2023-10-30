// script.js
document.getElementById('addButton').addEventListener('click', function () {
    var contents = document.getElementById('addNewInput').value;
    window.location.href = '/get?contents=' + contents;
});