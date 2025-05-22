import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
r=w0.sketch().arc((7,27),(8,25),(9,24)).arc((94,12),(62,82)).arc((36,83),(16,65)).arc((11,47),(9,28)).arc((8,28),(7,27)).assemble().finalize().extrude(-73).union(w0.sketch().segment((-100,-37),(-95,-37)).arc((-25,-66),(-93,-33)).segment((-100,-33)).close().assemble().push([(-64,-79)]).circle(2,mode='s').finalize().extrude(50))