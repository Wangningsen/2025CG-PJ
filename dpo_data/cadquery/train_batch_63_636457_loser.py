import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.workplane(offset=-32/2).moveTo(84,-27).cylinder(32,16).union(w0.sketch().segment((-98,-17),(-61,-17)).segment((-61,-55)).segment((-81,-55)).arc((-14,-87),(59,-48)).segment((-11,-48)).segment((-11,87)).arc((-79,57),(-98,-17)).assemble().finalize().extrude(114))