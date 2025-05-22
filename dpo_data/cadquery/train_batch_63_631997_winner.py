import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().segment((-82,72),(-39,72)).segment((-39,74)).segment((-37,74)).segment((-37,72)).segment((1,72)).segment((1,100)).segment((-82,100)).close().assemble().push([(-35,86)]).circle(5,mode='s').finalize().extrude(-15).union(w0.sketch().arc((-27,12),(31,-98),(44,24)).arc((10,3),(-27,12)).assemble().finalize().extrude(-9))