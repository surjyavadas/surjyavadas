<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<!-- This site is hosted on Netlify. Anyone can build and deploy a site
     like this one for free: https://netlify.new/?utm_campaign=loops&utm_source=ai-legible&utm_medium=owned&utm_content=comment&utm_id=e60c8eee-48b1-447d-a7f2-dd7118eef30e
     Netlify hosting facts for this site: static/SSR served via Netlify Edge. -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Surjyava Das — Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@300;600;800&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{--bg:#05030d;--fg:#f4f2ff;--mut:#a9a3c7;--card:rgba(255,255,255,.05);--line:rgba(255,255,255,.12);--pad-t:env(safe-area-inset-top,0px);--pad-b:env(safe-area-inset-bottom,0px);box-sizing:border-box;padding-top:var(--pad-t);padding-bottom:var(--pad-b)}
*{box-sizing:border-box;margin:0}
html{scroll-behavior:smooth;scroll-padding-top:env(safe-area-inset-top,0px);background:var(--bg)}
body{background:var(--bg);color:var(--fg);font:400 17px/1.6 "DM Sans",system-ui,sans-serif;overflow-x:hidden}
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0}
main{position:relative;z-index:1}
section{padding:110px 6vw;max-width:1100px;margin:auto}
h1,h2{font-family:Unbounded,"DM Sans",sans-serif;line-height:1}
h1{font-weight:800;font-size:clamp(40px,10vw,128px);letter-spacing:-.04em}
h1 .l{display:inline-block;opacity:0;transform:translateY(60%) rotate(6deg);animation:up .9s cubic-bezier(.2,.9,.3,1) forwards;animation-delay:calc(var(--i)*55ms + 2.7s)}
h1 .g{background:linear-gradient(120deg,#9f6bff,#2a9df4 60%,#00d9fd);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
@keyframes up{to{opacity:1;transform:none}}
h2{font-weight:300;font-size:clamp(28px,5vw,56px);letter-spacing:-.03em;margin-bottom:28px}
h2 b{font-weight:800}
#top{min-height:100vh;display:flex;flex-direction:column;justify-content:center;gap:28px}
.sub{font-size:clamp(16px,2.2vw,22px);color:var(--mut);max-width:30em}
.row{display:flex;flex-wrap:wrap;gap:16px}
.scroll{position:absolute;bottom:28px;left:6vw;display:flex;align-items:center;gap:12px;color:var(--mut);font-size:14px}
.scroll i{width:1px;height:46px;background:linear-gradient(var(--fg),transparent);animation:dr 1.8s ease-in-out infinite;transform-origin:top}
@keyframes dr{0%{transform:scaleY(0)}60%{transform:scaleY(1)}100%{transform:scaleY(1);opacity:0}}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:26px;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.card h3{font:600 18px Unbounded,sans-serif;margin-bottom:8px}
.card p{color:var(--mut);font-size:15px}
.about{max-width:38em;font-size:clamp(18px,2.4vw,24px);margin-bottom:34px}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
.chips span{border:1px solid var(--line);border-radius:99px;padding:6px 16px;font-size:15px;background:var(--card)}
.rv{opacity:0;transform:translateY(26px);transition:opacity .8s,transform .8s}.rv.on{opacity:1;transform:none}
/* slide-fill button */
.btn{position:relative;overflow:hidden;display:inline-flex;align-items:center;justify-content:center;padding:18px 40px;border-radius:99px;border:2px solid transparent;background:#D9DADB;color:#000;font:500 19px "DM Sans",sans-serif;text-decoration:none;cursor:pointer;-webkit-tap-highlight-color:transparent;transition:color .45s cubic-bezier(.25,1,.5,1)}
.btn .w{position:absolute;inset:0;background:#0E87CC;pointer-events:none;transform:translateY(calc(100% + 20px));transition:transform .45s cubic-bezier(.25,1,.5,1)}
.btn .w div{position:absolute;top:-15px;left:0;right:0;height:16px}
.btn .w svg{position:absolute;top:0;left:0;width:200%;height:100%}
.btn .w svg:first-child{opacity:.45;animation:wv 7s linear infinite}.btn .w svg+svg{animation:wv 5s linear infinite reverse}
@keyframes wv{to{transform:translateX(-50%)}}
.btn span{position:relative;z-index:2}
.btn:hover,.btn:focus-visible{color:#fff;outline:none}.btn:hover .w,.btn:focus-visible .w{transform:none}
/* cables */
#cab{position:relative;overflow:hidden;background:#000;margin-top:40px;-webkit-mask-image:linear-gradient(transparent,#000 22%);mask-image:linear-gradient(transparent,#000 22%)}
#cab canvas{position:absolute;inset:0;width:100%;height:100%}
#cab section{position:relative;min-height:84vh;display:flex;flex-direction:column;justify-content:center;gap:22px;padding-top:160px}
#cab .big{font:300 clamp(24px,4.4vw,46px)/1.15 Unbounded,sans-serif;letter-spacing:-.03em}
footer{position:relative;text-align:center;color:var(--mut);font-size:14px;padding:0 0 30px;margin-top:-50px}
/* loader */
#ld{position:fixed;inset:0;z-index:100;background:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;transition:opacity .8s}
#ld p{font:300 14px Unbounded,sans-serif;letter-spacing:.3em;color:var(--mut)}
#ld.off{opacity:0;pointer-events:none}
.cl{position:fixed;pointer-events:none;z-index:99;background:#fff}
@media(prefers-reduced-motion:reduce){h1 .l{animation-duration:.01s;animation-delay:0s}.btn .w svg{animation:none}}
</style>
</head>
<body>
<div id="ld"><canvas id="orb" style="width:240px;height:240px"></canvas><p>LOADING</p></div>
<canvas id="bg"></canvas>
<main>
<section id="top">
  <p class="sub">Hi, I'm</p>
  <h1 id="nm" aria-label="Surjyava Das"></h1>
  <p class="sub">Second-year Computer Science &amp; Engineering student who likes turning ideas into working software.</p>
  <div class="row">
    <a class="btn" href="https://github.com/surjyavadas" target="_blank" rel="noopener"><span>View GitHub</span></a>
    <a class="btn" href="#contact"><span>Get in touch</span></a>
  </div>
  <div class="scroll"><i></i>Scroll down</div>
</section>

<section id="about">
  <h2 class="rv">Building, <b>learning</b>, shipping.</h2>
  <p class="about rv">I'm a CSE student in my second year. I learn by making things, and I keep my code public on GitHub so my progress is easy to follow.</p>
  <div class="grid">
    <div class="card rv"><h3>Studying</h3><p>B.Tech in Computer Science &amp; Engineering, 2nd year.</p></div>
    <div class="card rv"><h3>Focus</h3><p>Writing clean code and building small projects end to end.</p></div>
    <div class="card rv"><h3>Open to</h3><p>Collaborations, internships and learning from other developers.</p></div>
  </div>
</section>

<section id="skills">
  <h2 class="rv">Tools I <b>use</b></h2>
  <div class="chips rv"><span>C</span><span>C++</span><span>Python</span><span>JavaScript</span><span>HTML &amp; CSS</span><span>Git &amp; GitHub</span><span>Data structures</span></div>
</section>

<section id="work">
  <h2 class="rv">My <b>work</b></h2>
  <p class="about rv">Every project I build lives on GitHub. Browse the repositories to see what I'm working on.</p>
  <a class="btn" href="https://github.com/surjyavadas" target="_blank" rel="noopener"><span>Open repositories</span></a>
</section>

<div id="cab">
  <canvas></canvas>
  <section id="contact">
    <h2 class="big">Let's build something together.</h2>
    <p class="sub">The fastest way to reach me is email.</p>
    <div class="row">
      <a class="btn" href="mailto:surjyavadas.pro@gmail.com"><span>Email me</span></a>
      <a class="btn" href="https://www.linkedin.com/in/surjyava-das" target="_blank" rel="noopener"><span>LinkedIn</span></a>
      <a class="btn" href="https://github.com/surjyavadas" target="_blank" rel="noopener"><span>GitHub</span></a>
    </div>
    <p class="sub">surjyavadas.pro@gmail.com</p>
  </section>
</div>
<footer>© 2026 Surjyava Das</footer>
</main>

<script>
(function(){
const TAU=Math.PI*2,$=s=>document.querySelector(s);
const hx=h=>[1,3,5].map(i=>parseInt(h.substr(i,2),16)/255);

/* name with per-letter reveal */
const nm=$('#nm');let k=0;
[['Surjyava',''],['Das','g']].forEach((w,j)=>{const d=document.createElement('span');d.style.display='block';
[...w[0]].forEach(c=>{const s=document.createElement('span');s.className='l '+w[1];s.style.setProperty('--i',k++);s.textContent=c;d.appendChild(s)});nm.appendChild(d)});

/* slide-fill button waves */
function wave(p,a,inv){let n=Math.round(400/p),q=p/4,A=inv?a:-a,d='M 0 15';for(let i=0;i<n;i++){const x=i*p;d+=` C ${x+q} ${15+A}, ${x+p-q} ${15-A}, ${x+p} 15`}return d+' V 40 H 0 Z'}
const B=wave(200,9,1),F=wave(100,10);
document.querySelectorAll('.btn').forEach(b=>{const w=document.createElement('div');w.className='w';
w.innerHTML=`<div><svg viewBox="0 0 400 30" preserveAspectRatio="none"><path d="${B}" fill="#0E87CC"/></svg><svg viewBox="0 0 400 30" preserveAspectRatio="none"><path d="${F}" fill="#0E87CC"/></svg></div>`;b.prepend(w)});

/* WebGL helper */
function GL(c,frag,o){const g=c.getContext('webgl',o);if(!g)return null;
const mk=(t,s)=>{const x=g.createShader(t);g.shaderSource(x,s);g.compileShader(x);return x};
const p=g.createProgram();g.attachShader(p,mk(g.VERTEX_SHADER,'attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}'));
g.attachShader(p,mk(g.FRAGMENT_SHADER,frag));g.linkProgram(p);g.useProgram(p);
g.bindBuffer(g.ARRAY_BUFFER,g.createBuffer());g.bufferData(g.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),g.STATIC_DRAW);
const l=g.getAttribLocation(p,'a');g.enableVertexAttribArray(l);g.vertexAttribPointer(l,2,g.FLOAT,false,0,0);
return{g,u:n=>g.getUniformLocation(p,n)}}
function fit(c,g,s){const w=Math.round(c.clientWidth*s),h=Math.round(c.clientHeight*s);if(!w||!h)return 0;if(c.width!==w||c.height!==h){c.width=w;c.height=h}g.viewport(0,0,w,h);return 1}

/* Cosmic BG */
const COSMIC=`precision highp float;uniform float t0;uniform vec2 R;
mat2 rot(float a){float s=sin(a),c=cos(a);return mat2(c,-s,s,c);}
float hash(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<7;i++){v+=a*noise(p);p*=rot(.5);p*=2.1;a*=.5;}return v;}
void main(){
vec3 uc=vec3(${hx('#6823C3')}),um=vec3(${hx('#007BFF')}),ua=vec3(${hx('#9900FF')}),uo=vec3(${hx('#F9F9F9')});
vec2 p=(gl_FragCoord.xy-.5*R)/min(R.x,R.y);float t=t0*.1;
p*=rot(t0*.75*.05);float dist=length(p);
float an=fbm(p*3.+t*.5)*.3;float dd=dist+an*smoothstep(.5,0.,dist);
vec2 nb=p*5.;
vec2 q=vec2(fbm(nb+vec2(cos(t),sin(t))),fbm(nb+1.2));
vec2 r=vec2(fbm(nb+4.*q+t),fbm(nb+4.*q+2.8));
float f=fbm(nb+4.*r);
float cm=smoothstep(.8,0.,dd)*(.5+.5*smoothstep(.1,.9,f));
float cg=exp(-3.*dd);
vec3 cc=uc*(cm*2.+cg*1.5);
float ring=smoothstep(.05,.35,dist)*smoothstep(.9,.3,dist);
float fil=pow(f,1.2);
vec3 cx=mix(um,ua,smoothstep(.2,.6,f));cx=mix(cx,uo,smoothstep(.4,.9,f));
vec3 co=cx*ring*fil*2.;
float dust=smoothstep(.3,.9,fbm(nb*1.5+r));dust=mix(1.,dust,smoothstep(0.,.3,dist));
vec3 fc=(cc+co)*dust*.96;fc+=um*cm*ring*.8;
float lum=max(fc.r,max(fc.g,fc.b));gl_FragColor=vec4(fc,clamp(lum,0.,1.));}`;
const bg=$('#bg'),C=GL(bg,COSMIC,{alpha:true,depth:false,antialias:false,premultipliedAlpha:true});
const RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
if(C){const g=C.g;g.enable(g.BLEND);g.blendFunc(g.ONE,g.ONE);const uT=C.u('t0'),uR=C.u('R');
(function lp(n){if(fit(bg,g,.5)){g.clearColor(0,0,0,0);g.clear(g.COLOR_BUFFER_BIT);g.uniform1f(uT,RM?6:n/1000*3);g.uniform2f(uR,bg.width,bg.height);g.drawArrays(g.TRIANGLES,0,3)}requestAnimationFrame(lp)})(0)}

/* Light Cables */
const CAB=`precision highp float;uniform vec2 uRes,uMouse;uniform float uTime,uHover;
float sat(float x){return clamp(x,0.,1.);}
float h21(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+34.56);return fract(p.x*p.y);}
float vn(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h21(i),h21(i+vec2(1,0)),f.x),mix(h21(i+vec2(0,1)),h21(i+vec2(1,1)),f.x),f.y);}
float fbm3(vec2 p){float s=0.,a=.5;for(int i=0;i<3;i++){s+=a*vn(p);p=p*2.07+vec2(4.1,2.3);a*=.5;}return s;}
void main(){
vec3 uAccent=vec3(${hx('#FF7500')}),uHigh=vec3(${hx('#FFD900')});
float uBend=0.,uSpread=.89,uWS=0.,uWE=3.,uThick=2.2,uFlow=3.,uPulses=1.,uGrab=1.,uCount=48.;
float ar=uRes.x/max(uRes.y,1.);vec2 uv=gl_FragCoord.xy/uRes;vec2 p=(uv-.5)*vec2(ar,1.);float t=uTime;
vec2 pA=p-vec2(-.13*ar,-.21)*.5;
vec3 col=vec3(0.);
float extent=1.;float along=-pA.y;float across=pA.x;
float s01=sat((along+extent*.5)/max(extent,.001));
vec2 pr=(uMouse-.5)*vec2(ar,1.);float pAl=-pr.y,pAc=pr.x;
float kAlong=-.18,kAcross=.10;vec3 acc=vec3(0.);float surge=0.;
for(int i=0;i<48;i++){
float fi=float(i)/47.;float o=fi-.5;float rnd=h21(vec2(fi*7.31,2.));
float kA=kAlong+o*.10+(rnd-.5)*.03;float bi=uBend*(.88+.24*rnd);
float sp=uSpread*mix(uWS,uWE,s01)*(.090+.34*sat((along-kAlong)*.85+.25));
float ba=sqrt((along-kA)*(along-kA)+.0035);
float yy=kAcross+o*sp-bi*ba+.008*sin(along*3.+fi*19.);
float gx=exp(-pow((along-pAl)/max(uGrab*.30,.02),2.));
yy=mix(yy,pAc+o*sp*.55,gx*.60*uHover);
float dd=(across-yy)/(uThick*.0038);
float core=1./(1.+dd*dd*9.);float sh=1./(1.+dd*dd*.6);
float ph=s01*uPulses-t*uFlow*.55-rnd*.22;float f=fract(ph);
float pulse=exp(-pow((f-.55)/.15,2.));float w=(.22+1.6*pulse)*(.55+.45*rnd);
acc+=(uHigh*core*1.45+uAccent*sh*.20)*w;surge+=core*gx;}
float feed=smoothstep(0.,.09,s01)*smoothstep(1.02,.30,s01);
col+=acc*feed*.20;col+=uHigh*surge*.05*uHover;
col+=(h21(gl_FragCoord.xy+fract(uTime)*71.)-.5)*.012;
gl_FragColor=vec4(max(col,0.),1.);}`;
const cs=$('#cab'),cv=cs.querySelector('canvas'),L=GL(cv,CAB,{alpha:false,depth:false,antialias:false});
if(L){const g=L.g,uT=L.u('uTime'),uR=L.u('uRes'),uM=L.u('uMouse'),uH=L.u('uHover');
const m={x:.5,y:.5,tx:.5,ty:.5,on:0,to:0};let vis=false,clk=0,last=performance.now();
new IntersectionObserver(e=>vis=e[0].isIntersecting).observe(cs);
cs.addEventListener('pointermove',e=>{const r=cs.getBoundingClientRect();m.tx=Math.min(1,Math.max(0,(e.clientX-r.left)/r.width));m.ty=Math.min(1,Math.max(0,(e.clientY-r.top)/r.height));m.to=1});
cs.addEventListener('pointerleave',()=>m.to=0);
(function lp(n){requestAnimationFrame(lp);const dt=Math.min(.05,(n-last)/1000);last=n;if(!vis)return;
if(!RM)clk=(clk+dt*.68)%3600;const k=1-Math.exp(-6*dt);m.on+=(m.to-m.on)*k;m.x+=((m.to?m.tx:.5)-m.x)*k;m.y+=((m.to?m.ty:.5)-m.y)*k;
if(!fit(cv,g,Math.min(devicePixelRatio||1,1.5)))return;
g.uniform2f(uR,cv.width,cv.height);g.uniform1f(uT,clk+scrollY*.002);g.uniform2f(uM,m.x,1-m.y);g.uniform1f(uH,m.on*1.14);g.drawArrays(g.TRIANGLES,0,3)})(0)}

/* Particle Tether loader */
const oc=$('#orb'),x=oc.getContext('2d'),S=240,dp=Math.min(2,devicePixelRatio||1);oc.width=oc.height=S*dp;x.scale(dp,dp);
const N=450,P=[];for(let i=0;i<N;i++){const y=1-i/(N-1)*2;P.push([Math.acos(y),2.399963*i])}
const sp=(p,y,pi)=>{const a=Math.cos(y),b=Math.sin(y),rx=p[0]*a-p[2]*b;let rz=p[0]*b+p[2]*a;const c=Math.cos(pi),s=Math.sin(pi),ry=p[1]*c-rz*s;rz=p[1]*s+rz*c;return[rx,ry,rz]};
let oraf;(function orb(n){const t=(n/1000/4.8)%1,kk=.5-.5*Math.cos(TAU*t),o=[];
for(const q of P){const th=q[0]+(Math.PI/2-q[0])*kk,sr=Math.sin(th);o.push(sp(sp([Math.cos(q[1])*sr,Math.cos(th),Math.sin(q[1])*sr],TAU*t,.4),TAU*t,0))}
o.sort((a,b)=>a[2]-b[2]);x.clearRect(0,0,S,S);x.fillStyle='#00D9FD';
for(const q of o){const s=3.5/(3.5-q[2]),f=Math.min(1,Math.max(0,(q[2]+1.1)/2.2));
x.globalAlpha=(.07+.93*Math.pow(f,1.55))*.9;x.beginPath();x.arc(S/2+q[0]*S*.3*s,S/2+q[1]*S*.3*s,Math.max(.6,1.77*(.4+1.6*f)*s*(.8+.5*kk)),0,TAU);x.fill()}
oraf=requestAnimationFrame(orb)})(0);
setTimeout(()=>{$('#ld').classList.add('off');setTimeout(()=>{cancelAnimationFrame(oraf);$('#ld').remove()},900)},2400);

/* Click effect: sniper */
document.addEventListener('click',e=>{if(RM)return;const X=e.clientX,Y=e.clientY,D=300;
const mk=(w,h,tr0,tr1,dl)=>{const el=document.createElement('i');el.className='cl';el.style.cssText=`left:${X}px;top:${Y}px;width:${w}px;height:${h}px`;document.body.appendChild(el);
el.animate([{transform:tr0,opacity:1},{transform:tr1,opacity:1,offset:.6},{transform:tr1+' scale(0)',opacity:0}],{duration:D,easing:'cubic-bezier(.2,.7,.3,1)'}).onfinish=()=>el.remove()};
[0,90,180,270].forEach(a=>mk(18,2,`translate(-50%,-50%) rotate(${a}deg) translateX(14px)`,`translate(-50%,-50%) rotate(${a}deg) translateX(32px)`));
[30,60,120,150,210,240,300,330].forEach(a=>{const r=a*Math.PI/180;mk(3,3,'translate(-50%,-50%)',`translate(calc(-50% + ${Math.cos(r)*36}px),calc(-50% + ${Math.sin(r)*36}px))`)})});

/* reveal on scroll */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.15});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
})();
</script>
</body>
</html>
