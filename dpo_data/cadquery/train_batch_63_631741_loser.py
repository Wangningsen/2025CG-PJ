import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().circle(100).push([(-83,-43)]).circle(5,mode='s').push([(80,14)]).circle(10,mode='s').finalize().extrude(-28)