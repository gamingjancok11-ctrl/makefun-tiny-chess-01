import json,os,urllib.request as u
E=os.environ['MAKEFUN_ENV_URL']
V=(0,100,320,330,500,900,0)
N8=(-33,-31,-18,-14,14,18,31,33);K8=(-17,-16,-15,-1,1,15,16,17);B4=(-17,-15,15,17);R4=(-16,-1,1,16)
D=(0,0,N8,B4,R4,K8,K8);M=100000;TT={};Nd=[0];LIM=30000;R={0:2,7:1,112:8,119:4};L=dict(zip('pnbrqk',range(1,7)))
S=[chr(97+(i&7))+str((i>>4)+1) for i in range(128)]
class X(Exception):pass
def P(p,b):
 with u.urlopen(u.Request(E+p,data=json.dumps(b).encode())) as x:return json.load(x)
def sf(n):return (int(n[1])-1)*16+ord(n[0])-97
def uc(m):return S[m&127]+S[(m>>7)&127]+('nbrq'[(m>>14)-2] if m>>14 else '')
def pf(f):
 b=[0]*128;p=f.split();s=''.join(c*int(c) if c.isdigit() else c for c in p[0] if c!='/')
 for i,ch in enumerate(s):
  if ch.isalpha():b[(7-i//8)*16+i%8]=L[ch.lower()]*((ch<'a')*2-1)
 return b,(p[1]=='w')*2-1,sum(1<<'KQkq'.index(ch)for ch in p[2]if ch in'KQkq'),(sf(p[3]) if p[3]!='-' else -1)
def ak(b,s,t):
 for ds,v,sl in(((-15*t,-17*t),1,0),(N8,2,0),(K8,6,0),(B4,3,1),(R4,4,1)):
  for d in ds:
   o=s+d
   while not o&136:
    p=b[o]
    if p:
     if p==v*t or(sl and p==5*t):return 1
     break
    if not sl:break
    o+=d
 return 0
def gn(b,t,c,e,qo=0):
 m=[];Y=lambda o:m.extend(s|o<<7|q<<14 for q in(5,4,3,2))
 for s,p in enumerate(b):
  if not p or p*t<0:continue
  a=abs(p)
  if a==1:
   d=16*t;st=(7-5*t)//2;r7=(s>>4)==(7+5*t)//2
   for o,k in((s+d,0),(s+d-1,1),(s+d+1,1),(s+2*d,2)):
    if not o&136 and((b[o]*t<0 or o==e) if k==1 else not b[o] and(k!=2 or(s>>4)==st and not b[s+d])):
     if r7:Y(o)
     elif k==1 or not qo:m.append(s|o<<7)
  else:
   sl=2<a<6
   for d in D[a]:
    o=s+d
    while not o&136:
     if b[o]*t>0:break
     if not qo or b[o]:m.append(s|o<<7)
     if b[o] or not sl:break
     o+=d
 if not qo:
  k=4 if t>0 else 116
  if b[k]==6*t and not ak(b,k,-t):
   for o in(2,-2):
    h=k+o//2
    if c&(1<<((o<0)+2*(t<0))) and not b[h] and not b[k+o] and(o>0 or not b[k-3])and not ak(b,h,-t) and not ak(b,k+o,-t):m.append(k|(k+o)<<7)
 return m
def mk(b,m,t,c,e):
 f=m&127;o=(m>>7)&127;q=m>>14;n=b[:];p=n[f];n[f]=0;A=abs(p);j=abs(o-f)
 if A==1 and o==e and(f&7)!=(o&7):n[o-16*t]=0
 n[o]=q*t if q else p
 if A==6:
  c&=3+9*(t>0)
  if j==2:r=f+3-7*(o<f);n[(f+o)//2]=n[r];n[r]=0
 c&=~R.get(f,0);c&=~R.get(o,0)
 return n,-t,c,((f+o)//2 if A==1 and j==32 else -1)
def C(f,r):return min(f,7-f)+min(r,7-r)
def ZK(k,n):
 r,f=k
 if n>3000:return (18,24,10,0)[min(f,7-f)] if r==0 else max(-40,-12*r)
 return 8*C(f,r)-20
def ev(b,t):
 s=0;n=0;g=[0,0];K=[[0,0],[0,0]]
 for q,p in enumerate(b):
  if not p:continue
  a=abs(p);w=p>0;r=q>>4;f=q&7
  if not w:r=7-r
  if a==6:K[w]=r,f
  else:
   v=V[a]
   if a==1:v+=r*(r+1)+6*(2<f<5)
   else:v+=(6,4,0,2)[a-2]*C(f,r)+(-18,-6,0,-4)[a-2]+12*(a==4)*(r==6);g[w]+=a==3
   s+=v*(w*2-1)
   if a>1:n+=V[a]
 s+=ZK(K[1],n)-ZK(K[0],n)
 if g[1]>1:s+=28
 if g[0]>1:s-=28
 return s*t
def od(ms,b,tm):
 def s(m):
  v=b[(m>>7)&127];q=m>>14
  return ((m==tm)<<20)+10*V[abs(v)]+9000*(q>0)+V[q]
 ms.sort(key=s,reverse=True)
def sr(b,t,c,e,d,a,be,pl):
 Nd[0]+=1
 if Nd[0]>LIM:raise X
 k=(tuple(b),t,c,e);ck=ak(b,b.index(6*t),-t)
 if d<=0:
  st=ev(b,t) if not ck else -M
  if st>=be:return be
  if st>a:a=st
  if pl>64:return a
 tm=TT.get(k,0) if d>0 else 0
 ms=gn(b,t,c,e,0 if d>0 or ck else 1);od(ms,b,tm);bs=-M;bm=0;lg=0
 for m in ms:
  n=mk(b,m,t,c,e)
  if ak(n[0],n[0].index(6*t),-t):continue
  lg+=1;s=-sr(*n,d-1,-be,-a,pl+1)
  if s>bs:bs=s;bm=m
  if s>a:a=s
  if a>=be:break
 if not lg:return -M+pl if ck else 0 if d>0 else a
 if d>0:
  if len(TT)>200000:TT.clear()
  TT[k]=bm
 return bs if d>0 else a
def th(fen,legal):
 b,t,c,e=pf(fen)
 ms=[sf(u[:2])|sf(u[2:4])<<7|L.get(u[4:],0)<<14 for u in legal]
 if len(ms)==1:return ms[0]
 bm=ms[0]
 for d in range(1,33):
  Nd[0]=0
  try:
   a=-M-1;bb=bm;od(ms,b,bb)
   for m in ms:
    s=-sr(*mk(b,m,t,c,e),d-1,-M-1,-a,1)
    if s>a:a=s;bb=m
   bm=bb
   if a>=M-1000:break
  except X:break
 return bm
g={}
while 1:
 g=P('/move',{'game':g['game'],'move':uc(th(g['fen'],g['legal_moves']))}) if g.get('status')=='your_move' else P('/game',{})
 if g['status']=='done':break
