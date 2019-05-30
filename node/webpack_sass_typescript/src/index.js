import './index.css';
import './index.scss';
import img from './index.jpg';

function component() {
  const el = document.createElement('div');
  el.innerHTML = 'hello world';
  const e = new Image();
  e.src = img;
  el.appendChild(e);
  const bt = document.createElement('button');
  bt.innerText = 'hello';
  bt.onclick = () => { bt.innerText = `${bt.innerHTML} clicked`; };
  el.appendChild(bt);
  return el;
}

document.body.appendChild(component());
