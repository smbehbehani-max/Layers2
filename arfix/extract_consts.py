import re,sys,json
def scan(h,i):
    # i at opening bracket; return end index (exclusive) of balanced literal
    st=[];j=i;n=len(h)
    while j<n:
        c=h[j]
        if c in '"\'`':
            q=c;j+=1
            while j<n and h[j]!=q:
                if h[j]=='\\': j+=1
                elif q=='`' and h[j]=='$' and h[j+1]=='{':
                    # skip template expr roughly
                    d=1;j+=2
                    while d: 
                        if h[j]=='{':d+=1
                        elif h[j]=='}':d-=1
                        j+=1
                    continue
                j+=1
        elif c in '[{(': st.append(c)
        elif c in ']})':
            st.pop()
            if not st: return j+1
        j+=1
def run(path,out):
    h=open(path,encoding='utf-8').read()
    parts=[]
    for m in re.finditer(r'(?:const|let|var) ([A-Za-z_][A-Za-z0-9_]*)=([\[{])',h):
        e=scan(h,m.end()-1)
        if e: parts.append(f'try{{globalThis[{json.dumps(m.group(1))}]=O[{json.dumps(m.group(1))}]=({h[m.end()-1:e]})}}catch(e){{console.error({json.dumps(m.group(1))},String(e).slice(0,80))}}')
    open(out,'w',encoding='utf-8').write('const O={};globalThis.P=(en,ar)=>({en,ar});'+'\n'.join(parts)+'\nmodule.exports=O;')
run(sys.argv[1],sys.argv[2])
