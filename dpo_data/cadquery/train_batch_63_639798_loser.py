import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
w1=cq.Workplane('ZX',origin=(0,75,0))
r=w0.sketch().arc((-100,-35),(-4,-46),(-63,26)).arc((-48,-27),(-100,-35)).assemble().finalize().extrude(-113).union(w1.sketch().arc((-20,39),(-64,25),(-17,29)).arc((90,55),(-20,39)).assemble().push([(-39,27)]).circle(23,mode='s').finalize().extrude(-96))