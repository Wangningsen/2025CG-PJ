import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().push([(29.5,5)]).rect(89,96).push([(30,-11)]).circle(12,mode='s').finalize().extrude(-56).union(w0.sketch().arc((22,2),(35,0),(47,-6)).segment((47,2)).segment((38,2)).segment((38,33)).segment((22,33)).close().assemble().finalize().extrude(100)).union(w1.workplane(offset=-65/2).moveTo(-74,-28).box(52,92,65))