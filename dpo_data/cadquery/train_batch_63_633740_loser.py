import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.sketch().segment((21,42),(21,78)).segment((38,78)).segment((38,81)).arc((-28,21),(59,18)).segment((38,18)).segment((38,22)).arc((16,33),(21,59)).segment((21,68)).segment((26,68)).segment((26,42)).close().assemble().finalize().extrude(82).union(w0.workplane(offset=82/2).moveTo(42,-38).cylinder(82,58)).union(w1.sketch().push([(-67,73.5)]).rect(66,45).push([(-58,72)]).circle(2,mode='s').finalize().extrude(51))