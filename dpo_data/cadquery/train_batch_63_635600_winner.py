import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().push([(-80,12)]).circle(19).push([(-80,11.5)]).rect(26,23,mode='s').finalize().extrude(-65).union(w0.sketch().arc((47,88),(-87,-49),(100,-10)).arc((57,35),(47,88)).assemble().finalize().extrude(-39))