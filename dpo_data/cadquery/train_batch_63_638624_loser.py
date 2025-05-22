import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
w1=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().segment((-94,-65),(-80,-65)).segment((-82,-98)).segment((-35,-100)).segment((-33,-65)).segment((-18,-65)).segment((-18,-43)).segment((-32,-43)).segment((-31,-10)).segment((-78,-8)).segment((-79,-43)).segment((-94,-43)).close().assemble().finalize().extrude(-63).union(w0.sketch().segment((12,7),(55,-11)).segment((94,82)).segment((52,100)).close().assemble().finalize().extrude(24)).union(w1.workplane(offset=-31/2).moveTo(-50,-65).cylinder(31,11))