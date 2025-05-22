import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
w1=cq.Workplane('ZX',origin=(0,40,0))
r=w0.sketch().segment((-26,70),(14,35)).segment((40,65)).segment((2,100)).close().assemble().finalize().extrude(29).union(w0.sketch().arc((-53,-46),(-19,-59),(-27,-95)).arc((38,-27),(-53,-46)).assemble().push([(-6,-51)]).circle(6,mode='s').finalize().extrude(51)).union(w1.workplane(offset=13/2).moveTo(-60,-67.5).box(16,9,13))