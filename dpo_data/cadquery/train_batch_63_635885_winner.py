import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
w1=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.sketch().segment((87,16),(99,15)).segment((100,82)).segment((87,82)).close().assemble().finalize().extrude(22).union(w1.sketch().segment((-100,-12),(-87,-12)).arc((-22,-82),(47,-15)).segment((47,-9)).segment((47,-5)).arc((45,3),(43,10)).segment((43,75)).segment((-40,75)).segment((-40,50)).arc((-71,29),(-87,-5)).segment((-100,-5)).close().assemble().push([(-44,-55)]).circle(9,mode='s').finalize().extrude(98))