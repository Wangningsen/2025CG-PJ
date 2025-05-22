import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
w1=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-74,-16),(-74,55)).arc((-100,19),(-74,-16)).assemble().reset().face(w0.sketch().arc((-51,-16),(-25,19),(-51,55)).close().assemble()).push([(-6.5,-83)]).rect(43,28).push([(46.5,95)]).rect(107,4).finalize().extrude(-101).union(w0.workplane(offset=65/2).moveTo(-57,82.5).box(30,15,65)).union(w1.sketch().arc((14,-40),(33,-40),(52,-46)).segment((58,-46)).segment((58,-55)).arc((58,-74),(57,-95)).arc((71,-41),(14,-40)).assemble().finalize().extrude(-47))