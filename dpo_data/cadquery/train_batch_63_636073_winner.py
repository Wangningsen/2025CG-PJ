import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().push([(-17,34)]).circle(44).push([(-17,34.5)]).rect(28,37,mode='s').push([(-5.5,-46)]).rect(15,74).finalize().extrude(-47).union(w0.workplane(offset=11/2).moveTo(-62,-70).cylinder(11,30)).union(w1.sketch().segment((7,56),(23,56)).segment((23,47)).segment((66,47)).segment((66,21)).segment((67,21)).segment((67,16)).segment((66,16)).segment((66,-4)).segment((21,-4)).arc((98,48),(7,56)).assemble().finalize().extrude(77))