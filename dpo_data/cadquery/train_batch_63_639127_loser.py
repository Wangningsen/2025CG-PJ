import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-78,0))
r=w0.sketch().push([(-12,22)]).circle(73).circle(62,mode='s').finalize().extrude(85).union(w0.sketch().arc((19,43),(-4,-98),(42,37)).segment((42,43)).close().assemble().finalize().extrude(156))