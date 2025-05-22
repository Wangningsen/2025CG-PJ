import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
r=w0.sketch().push([(-47.5,-20.5)]).rect(101,87).push([(-17,8)]).circle(15,mode='s').finalize().extrude(-99).union(w0.sketch().segment((52,-21),(59,-52)).segment((98,-43)).segment((89,-4)).arc((38,60),(52,-21)).assemble().finalize().extrude(101))