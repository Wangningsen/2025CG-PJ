import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().push([(17,-48)]).circle(41).circle(26,mode='s').finalize().extrude(9).union(w0.workplane(offset=30/2).moveTo(-93,-73).cylinder(30,7)).union(w1.sketch().arc((41,72),(95,40),(44,77)).segment((49,77)).segment((49,72)).close().assemble().finalize().extrude(25))