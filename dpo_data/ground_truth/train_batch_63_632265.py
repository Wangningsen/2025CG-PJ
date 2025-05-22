import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-28))
w1=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().push([(0,4)]).rect(160,16).rect(10,14,mode='s').finalize().extrude(116).union(w0.sketch().push([(0,4)]).rect(194,6).reset().face(w0.sketch().arc((-23,-35),(0,-41),(23,-35)).close().assemble()).finalize().extrude(125)).union(w1.sketch().segment((-97,-82),(-29,-82)).segment((-29,-100)).segment((8,-100)).segment((8,-82)).segment((76,-82)).segment((76,82)).segment((8,82)).segment((8,100)).segment((-29,100)).segment((-29,82)).segment((-97,82)).close().assemble().finalize().extrude(-52))