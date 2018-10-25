function inViewport(pos) {
  return (pos.top <= window.innerHeight && pos.top > 0)
    || (pos.bottom >= 0 && pos.bottom <= window.innerHeight);
}

function lazyLoad(el) {
  el.src = el.getAttribute('data-src');
  el.classList.remove('lazy');
}

function onScroll() {
  var lazyEls = document.querySelectorAll('img.lazy');
  for (var i = 0; i < laxyEls.length; i++) {
    var el = lazyEls[i];
    var pos = el.getBoundingClientRect();
    if (inViewport(pos)) {
      lazyLoad(el)
    }
  }
}

window.addEventListener('scroll', onScroll, {passive: true});
