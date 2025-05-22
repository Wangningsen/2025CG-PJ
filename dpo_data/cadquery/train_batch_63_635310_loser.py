import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-85))
w1=cq.Workplane('YZ',origin=(-76,0,0))
r=w0.sketch().segment((-65,-100),(-52,-100)).segment((-52,-17)).arc((-47,-24),(-41,-30)).arc((-13,-27),(13,-29)).arc((71,61),(-38,75)).arc((-46,69),(-54,64)).arc((-76,23),(-62,-22)).segment((-65,-22)).close().assemble().finalize().extrude(77).union(w1.workplane(offset=35/2).moveTo(-38.5,19).box(79,130,35))