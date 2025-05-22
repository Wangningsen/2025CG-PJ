import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('ZX',origin=(0,-39,0))
r=w0.sketch().arc((-72,-4),(-81,-32),(-70,-59)).arc((-73,-68),(-65,-64)).arc((-10,-63),(-2,-8)).segment((9,-8)).arc((-26,100),(-72,-4)).assemble().finalize().extrude(-104).union(w1.workplane(offset=129/2).moveTo(-64,31).cylinder(129,36))