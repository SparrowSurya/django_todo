const removeMsg = (id) => {
    const ele = document.getElementById(id);
    if (ele) {
        ele.parentNode.removeChild(ele);
    }
}
